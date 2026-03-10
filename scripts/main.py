import argparse
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from dateutil.parser import isoparse

from build_markdown import render_email, render_markdown
from config_loader import load_config
from fetch_arxiv import FetchWindow, deduplicate_papers, fetch_category, save_raw_payload
from process_papers import build_summary, enrich_papers
from send_email import send_html_email


ASIA_SHANGHAI = ZoneInfo("Asia/Shanghai")
ROOT = Path(__file__).resolve().parents[1]
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


def resolve_window(args: argparse.Namespace, state: dict, now: datetime) -> FetchWindow:
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
    parser = argparse.ArgumentParser(description="Build a daily arXiv audio digest.")
    parser.add_argument("--now", help="Override current time in ISO 8601 format.")
    parser.add_argument("--start", help="Explicit window start time in ISO 8601 format.")
    parser.add_argument("--end", help="Explicit window end time in ISO 8601 format.")
    parser.add_argument("--config", help="Path to a JSON config file.")
    return parser.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()
    config = load_config(args.config)
    now = ensure_timezone(isoparse(args.now)) if args.now else datetime.now(tz=ASIA_SHANGHAI)

    state = load_state()
    window = resolve_window(args, state, now)
    logging.info("Using time window %s -> %s", window.start.isoformat(), window.end.isoformat())
    source_categories = config["sources"]["categories"]

    with requests.Session() as session:
        papers = []
        for category in source_categories:
            papers.extend(fetch_category(category, window, session=session))

    deduped = deduplicate_papers(papers)
    filtered = filter_already_processed(deduped, state)
    enriched, category_priority = enrich_papers(filtered, config)
    summary = build_summary(enriched, category_priority)

    run_date = window.end.strftime("%Y-%m-%d")
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
    subject = f"arXiv Audio Digest {run_date}"
    send_html_email(subject, email_html)

    update_state(state, window, enriched)
    logging.info("Processed JSON written to %s", processed_path)
    logging.info("Markdown digest written to %s", markdown_path)


if __name__ == "__main__":
    main()
