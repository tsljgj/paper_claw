import argparse
import json
import logging
import os
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from dateutil.parser import isoparse

# Auto-load .env file if exists
ROOT = Path(__file__).resolve().parents[1]
env_path = ROOT / ".env"
if env_path.exists():
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key not in os.environ:
                    os.environ[key] = value

from build_markdown import render_email, render_markdown
from config_loader import load_config
from fetch_arxiv import FetchWindow, deduplicate_papers, fetch_category, save_raw_payload
from process_papers import build_summary, enrich_papers
from send_email import send_html_email


ASIA_SHANGHAI = ZoneInfo("Asia/Shanghai")
STATE_PATH = ROOT / "data" / "state.json"
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
POSTS_DIR = ROOT / "content" / "posts"
TEMPLATE_DIR = ROOT / "templates"

def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"last_successful_run": None, "processed_ids": []}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def default_window(now: datetime, state: dict) -> FetchWindow:
    if state.get("last_successful_run"):
        return FetchWindow(start=isoparse(state["last_successful_run"]).astimezone(ASIA_SHANGHAI), end=now)

    anchor = now.replace(hour=9, minute=0, second=0, microsecond=0)
    if now < anchor:
        anchor -= timedelta(days=1)
    return FetchWindow(start=anchor - timedelta(days=1), end=anchor)


def ensure_timezone(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=ASIA_SHANGHAI)
    return dt.astimezone(ASIA_SHANGHAI)


def format_datetime(dt: datetime) -> str:
    return dt.astimezone(ASIA_SHANGHAI).strftime("%Y-%m-%d %H:%M:%S %Z")


def parse_date_only(value: str) -> date:
    return date.fromisoformat(value)


def at_beijing_nine(day_value: date) -> datetime:
    return datetime(day_value.year, day_value.month, day_value.day, 9, 0, 0, tzinfo=ASIA_SHANGHAI)


def resolve_window(args: argparse.Namespace, state: dict, now: datetime) -> FetchWindow:
    if args.day and (args.start or args.end or args.start_date or args.end_date):
        raise ValueError("--day cannot be combined with other manual window arguments")

    if args.day:
        end_day = parse_date_only(args.day)
        return FetchWindow(start=at_beijing_nine(end_day - timedelta(days=1)), end=at_beijing_nine(end_day))

    if args.start_date or args.end_date:
        start_day = parse_date_only(args.start_date) if args.start_date else None
        end_day = parse_date_only(args.end_date) if args.end_date else None

        if start_day and end_day and end_day <= start_day:
            raise ValueError("end date must be later than start date")

        if start_day:
            start_dt = at_beijing_nine(start_day)
            end_dt = at_beijing_nine(end_day) if end_day else now
            if end_dt <= start_dt:
                raise ValueError("resolved end time must be later than start time")
            return FetchWindow(start=start_dt, end=end_dt)

    start_arg = ensure_timezone(isoparse(args.start)) if args.start else None
    end_arg = ensure_timezone(isoparse(args.end)) if args.end else now

    if start_arg and end_arg <= start_arg:
        raise ValueError("end time must be later than start time")

    if start_arg:
        return FetchWindow(start=start_arg, end=end_arg)

    return default_window(end_arg, state)


def filter_already_processed(papers: list[dict], state: dict) -> list[dict]:
    processed_ids = set(state.get("processed_ids", []))
    return [paper for paper in papers if paper["arxiv_id"] not in processed_ids]


def build_payload(window: FetchWindow, papers: list[dict], summary: dict, markdown_path: Path, category_priority: list[str], config: dict) -> dict:
    grouped = {
        category: [paper for paper in papers if paper["digest_category"] == category]
        for category in category_priority
    }
    return {
        "generated_at": datetime.now(tz=ASIA_SHANGHAI).isoformat(),
        "project": config["project"],
        "window": {
            "start": window.start.isoformat(),
            "end": window.end.isoformat(),
            "start_display": format_datetime(window.start),
            "end_display": format_datetime(window.end),
        },
        "summary": summary,
        "markdown_path": str(markdown_path.relative_to(ROOT)),
        "papers": papers,
        "grouped": grouped,
    }


def persist_outputs(payload: dict, run_date: str) -> tuple[Path, Path]:
    processed_path = PROCESSED_DIR / f"{run_date}.json"
    markdown_path = POSTS_DIR / f"{run_date}-arxiv-audio-digest.md"
    save_raw_payload(processed_path, payload)

    markdown = render_markdown(TEMPLATE_DIR, payload)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(markdown, encoding="utf-8")
    return processed_path, markdown_path


def update_state(state: dict, window: FetchWindow, papers: list[dict]) -> None:
    processed_ids = state.get("processed_ids", [])
    processed_ids.extend(paper["arxiv_id"] for paper in papers)
    state["processed_ids"] = processed_ids[-5000:]
    state["last_successful_run"] = window.end.isoformat()
    save_state(state)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a daily paper digest from multiple sources.")
    parser.add_argument("--now", help="Override current time in ISO 8601 format.")
    parser.add_argument("--start", help="Explicit window start time in ISO 8601 format.")
    parser.add_argument("--end", help="Explicit window end time in ISO 8601 format.")
    parser.add_argument("--day", help="Run a daily window for YYYY-MM-DD.")
    parser.add_argument("--start-date", help="Window start day in YYYY-MM-DD.")
    parser.add_argument("--end-date", help="Window end day in YYYY-MM-DD.")
    parser.add_argument("--config", help="Path to a JSON config file.")
    parser.add_argument("--language", choices=["zh", "en", "ja", "ko", "de", "fr", "es"],
                        help="Output language for summaries.")
    return parser.parse_args()


def get_source_categories(config: dict) -> list[str]:
    """Extract category IDs from enabled sources."""
    sources = config.get("sources", {})
    categories = []
    
    # Handle new format with multiple sources
    if isinstance(sources, dict):
        for source_name, source_config in sources.items():
            if source_config.get("enabled", True):
                for cat in source_config.get("categories", []):
                    if isinstance(cat, dict):
                        categories.append(cat["id"])
                    else:
                        categories.append(cat)
    # Handle old format (backward compatibility)
    elif isinstance(sources, list):
        categories = sources
    
    return categories


def load_existing_digest(run_date: str) -> dict | None:
    """Load existing processed data if available."""
    processed_path = PROCESSED_DIR / f"{run_date}.json"
    if processed_path.exists():
        try:
            data = json.loads(processed_path.read_text(encoding="utf-8"))
            logging.info("Found existing digest for %s with %s papers", run_date, data.get("summary", {}).get("total", 0))
            return data
        except Exception as e:
            logging.warning("Failed to load existing digest: %s", e)
    return None


def main() -> None:
    configure_logging()
    args = parse_args()
    config = load_config(args.config)
    now = ensure_timezone(isoparse(args.now)) if args.now else datetime.now(tz=ASIA_SHANGHAI)
    
    # Get language from args or config
    language = args.language or config.get("language", {}).get("default", "zh")
    logging.info("Using language: %s", language)
    
    # Override config language for this run
    if "language" not in config:
        config["language"] = {}
    config["language"]["default"] = language

    # Determine run date
    state = load_state()
    window = resolve_window(args, state, now)
    run_date = window.end.strftime("%Y-%m-%d")
    
    # Check if we already have processed data for this date
    existing_data = load_existing_digest(run_date)
    if existing_data:
        logging.info("Using existing digest for %s", run_date)
        
        # Reconstruct payload from existing data
        from process_papers import build_classification_assets
        _, category_priority, _ = build_classification_assets(config)
        
        # Build window from existing data or use current
        window_start = window.start
        window_end = window.end
        if "window" in existing_data:
            try:
                window_start = isoparse(existing_data["window"].get("start", window.start.isoformat()))
                window_end = isoparse(existing_data["window"].get("end", window.end.isoformat()))
            except:
                pass
        
        window = FetchWindow(start=window_start, end=window_end)
        
        provisional_markdown = POSTS_DIR / f"{run_date}-arxiv-audio-digest.md"
        payload = build_payload(
            window,
            existing_data.get("papers", []),
            existing_data.get("summary", {}),
            provisional_markdown,
            category_priority,
            config
        )
        
        # Check if markdown exists
        markdown_path = POSTS_DIR / f"{run_date}-arxiv-audio-digest.md"
        if not markdown_path.exists():
            # Save markdown if missing
            markdown_content = render_markdown(TEMPLATE_DIR, payload)
            markdown_path.parent.mkdir(parents=True, exist_ok=True)
            markdown_path.write_text(markdown_content, encoding="utf-8")
            logging.info("Recreated missing markdown: %s", markdown_path)
        
        # Send email with existing data
        email_html = render_email(TEMPLATE_DIR, payload)
        subject = f"📰 Paper Claw Digest - {run_date}"
        send_html_email(subject, email_html, markdown_path)
        logging.info("Email sent using existing digest for %s", run_date)
        return

    # No existing data, fetch and process normally
    logging.info("Using time window %s -> %s", window.start.isoformat(), window.end.isoformat())
    
    source_categories = get_source_categories(config)
    logging.info("Fetching from categories: %s", source_categories)

    with requests.Session() as session:
        papers = []
        for category in source_categories:
            papers.extend(fetch_category(category, window, session=session))

    deduped = deduplicate_papers(papers)
    filtered = filter_already_processed(deduped, state)
    enriched, category_priority = enrich_papers(filtered, config)
    summary = build_summary(enriched, category_priority, language)

    provisional_markdown = POSTS_DIR / f"{run_date}-arxiv-audio-digest.md"
    payload = build_payload(window, enriched, summary, provisional_markdown, category_priority, config)
    raw_path = RAW_DIR / f"{run_date}.json"
    save_raw_payload(
        raw_path,
        {
            "window": {"start": window.start.isoformat(), "end": window.end.isoformat()},
            "fetched_count": len(papers),
            "deduplicated_count": len(deduped),
            "new_count": len(filtered),
            "papers": deduped,
        },
    )
    processed_path, markdown_path = persist_outputs(payload, run_date)

    email_html = render_email(TEMPLATE_DIR, payload)
    subject = f"📰 Paper Claw Digest - {run_date}"
    send_html_email(subject, email_html, markdown_path)

    update_state(state, window, enriched)
    logging.info("Processed JSON written to %s", processed_path)
    logging.info("Markdown digest written to %s", markdown_path)


if __name__ == "__main__":
    main()
