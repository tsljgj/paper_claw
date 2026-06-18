import json
import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable
from urllib.parse import urlencode

import feedparser
import requests


ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_RSS_URL = "https://rss.arxiv.org/rss/"
REQUEST_DELAY_SECONDS = 3.5
MAX_RETRIES = 5
DEFAULT_USER_AGENT = "paper-claw/1.0"

# Announcement types in the arXiv RSS feed: "new" = brand-new submission,
# "cross" = newly cross-listed into this category, "replace"/"replace-cross" =
# revision of an existing paper. We want freshly announced papers.
RSS_KEEP_ANNOUNCE_TYPES = {"new", "cross"}


@dataclass
class FetchWindow:
    start: datetime
    end: datetime


def _format_arxiv_timestamp(dt: datetime) -> str:
    return dt.strftime("%Y%m%d%H%M%S")


def _build_query(category: str, window: FetchWindow, start_index: int, max_results: int) -> str:
    submitted = (
        f"submittedDate:[{_format_arxiv_timestamp(window.start)} TO "
        f"{_format_arxiv_timestamp(window.end)}]"
    )
    params = {
        "search_query": f"cat:{category} AND {submitted}",
        "sortBy": "submittedDate",
        "sortOrder": "ascending",
        "start": start_index,
        "max_results": max_results,
    }
    return f"{ARXIV_API_URL}?{urlencode(params)}"


def _extract_affiliations(entry: feedparser.FeedParserDict) -> list[str]:
    affiliations: list[str] = []
    for author in entry.get("authors", []):
        aff = author.get("arxiv_affiliation")
        if aff and aff not in affiliations:
            affiliations.append(aff.strip())
    return affiliations


def _normalize_entry(entry: feedparser.FeedParserDict, source_category: str) -> dict:
    raw_id = entry.get("id", "").rstrip("/")
    arxiv_id = raw_id.split("/")[-1]
    authors = [author.get("name", "").strip() for author in entry.get("authors", []) if author.get("name")]
    affiliations = _extract_affiliations(entry)
    categories = [tag["term"] for tag in entry.get("tags", []) if tag.get("term")]
    primary_category = entry.get("arxiv_primary_category", {}).get("term") or source_category
    return {
        "arxiv_id": arxiv_id,
        "title_en": " ".join(entry.get("title", "").split()),
        "abstract_en": " ".join(entry.get("summary", "").split()),
        "authors": authors,
        "affiliations": affiliations,
        "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}",
        "primary_category": primary_category,
        "source_categories": sorted(set([source_category, *categories])),
        "published": entry.get("published"),
        "updated": entry.get("updated"),
    }


def _user_agent() -> str:
    contact = os.getenv("ARXIV_CONTACT_EMAIL")
    if contact:
        return f"{DEFAULT_USER_AGENT} (mailto:{contact})"
    return DEFAULT_USER_AGENT


def _retry_delay(response: requests.Response | None, attempt: int) -> float:
    if response is not None:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return max(float(retry_after), REQUEST_DELAY_SECONDS)
            except ValueError:
                pass
    return REQUEST_DELAY_SECONDS * (2 ** attempt)


def _get_with_backoff(session: requests.Session, url: str) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES):
        if attempt > 0:
            delay = REQUEST_DELAY_SECONDS * attempt
            logging.info("Retrying arXiv request after %.1f seconds", delay)
            time.sleep(delay)

        try:
            response = session.get(
                url,
                timeout=30,
                headers={"User-Agent": _user_agent()},
            )
        except requests.RequestException as exc:
            last_error = exc
            if attempt == MAX_RETRIES - 1:
                raise
            continue

        if response.status_code in {429, 500, 502, 503, 504}:
            if attempt == MAX_RETRIES - 1:
                response.raise_for_status()
            delay = _retry_delay(response, attempt)
            logging.warning(
                "arXiv returned status=%s, backing off for %.1f seconds before retry",
                response.status_code,
                delay,
            )
            time.sleep(delay)
            continue

        response.raise_for_status()
        return response

    if last_error is not None:
        raise last_error
    raise RuntimeError("arXiv request failed without a captured exception")


def fetch_category(category: str, window: FetchWindow, session: requests.Session | None = None) -> list[dict]:
    session = session or requests.Session()
    papers: list[dict] = []
    start_index = 0
    page_size = 50

    while True:
        url = _build_query(category, window, start_index, page_size)
        logging.info("Fetching arXiv category=%s start=%s", category, start_index)
        response = _get_with_backoff(session, url)
        feed = feedparser.parse(response.text)
        entries = feed.entries
        if not entries:
            break
        papers.extend(_normalize_entry(entry, category) for entry in entries)
        if len(entries) < page_size:
            break
        start_index += page_size
        logging.info("Sleeping %.1f seconds to respect arXiv API rate limits", REQUEST_DELAY_SECONDS)
        time.sleep(REQUEST_DELAY_SECONDS)

    return papers


def _clean_rss_abstract(summary: str) -> str:
    """Strip the 'arXiv:ID Announce Type: X \\nAbstract: ' prefix from an RSS summary."""
    text = summary or ""
    marker = "Abstract:"
    idx = text.find(marker)
    if idx != -1:
        text = text[idx + len(marker):]
    return " ".join(text.split())


def _split_rss_authors(entry: feedparser.FeedParserDict) -> list[str]:
    """RSS packs all authors into one comma-separated string; split them out."""
    raw = entry.get("author", "")
    if not raw:
        return [a.get("name", "").strip() for a in entry.get("authors", []) if a.get("name")]
    return [name.strip() for name in raw.split(",") if name.strip()]


def _normalize_rss_entry(entry: feedparser.FeedParserDict, requested_categories: list[str]) -> dict:
    raw_id = entry.get("id", "")
    # RSS id looks like "oai:arXiv.org:2606.18271v1"; take the trailing id.
    arxiv_id = raw_id.split(":")[-1] if raw_id else entry.get("link", "").rstrip("/").split("/")[-1]
    categories = [tag["term"] for tag in entry.get("tags", []) if tag.get("term")]
    primary_category = categories[0] if categories else (requested_categories[0] if requested_categories else "")
    # Which of our requested categories this paper actually belongs to.
    matched = sorted(set(categories) & set(requested_categories)) or [primary_category]
    return {
        "arxiv_id": arxiv_id,
        "title_en": " ".join(entry.get("title", "").split()),
        "abstract_en": _clean_rss_abstract(entry.get("summary", "")),
        "authors": _split_rss_authors(entry),
        "affiliations": [],  # RSS feed does not carry affiliations
        "arxiv_url": f"https://arxiv.org/abs/{arxiv_id.split('v')[0]}",
        "primary_category": primary_category,
        "source_categories": sorted(set([*matched, *categories])),
        "published": entry.get("published"),
        "updated": entry.get("updated"),
        "announce_type": entry.get("arxiv_announce_type", ""),
    }


def fetch_via_rss(
    categories: list[str],
    session: requests.Session | None = None,
    keep_types: set[str] | None = None,
) -> list[dict]:
    """
    Fetch today's freshly *announced* papers via the arXiv RSS feed.

    Unlike the search API (which windows on submittedDate and silently misses
    Thursday/Friday and QA-held papers), the RSS feed is keyed on the actual
    announcement, so it reflects exactly what's new today. All categories are
    fetched in a single request (joined with '+').
    """
    session = session or requests.Session()
    keep_types = keep_types if keep_types is not None else RSS_KEEP_ANNOUNCE_TYPES
    url = ARXIV_RSS_URL + "+".join(categories)
    logging.info("Fetching arXiv RSS for categories=%s", categories)
    response = _get_with_backoff(session, url)
    feed = feedparser.parse(response.text)

    papers: list[dict] = []
    skipped = 0
    for entry in feed.entries:
        announce = entry.get("arxiv_announce_type", "")
        if announce and announce not in keep_types:
            skipped += 1
            continue
        papers.append(_normalize_rss_entry(entry, categories))
    logging.info(
        "RSS feed: %s entries, kept %s (types=%s), skipped %s revisions/other",
        len(feed.entries), len(papers), sorted(keep_types), skipped,
    )
    return papers


HF_DAILY_URL = "https://huggingface.co/api/daily_papers"


def fetch_huggingface_daily(
    dates: list[str],
    session: requests.Session | None = None,
) -> dict[str, dict]:
    """
    Fetch Hugging Face "Daily Papers" for the given YYYY-MM-DD dates.

    Returns a dict keyed by bare arXiv id (no version) → {upvotes, ai_keywords,
    title}. HF Daily Papers is a community-curated, cross-domain list (~30-50/day);
    we use it both as a popularity signal (upvotes) and as an extra source for
    papers the RSS feed missed. This endpoint is unofficial — failures are
    swallowed so they never break the digest.
    """
    session = session or requests.Session()
    by_id: dict[str, dict] = {}
    for date in dates:
        try:
            resp = session.get(
                HF_DAILY_URL,
                params={"date": date},
                headers={"User-Agent": _user_agent()},
                timeout=20,
            )
            resp.raise_for_status()
            items = resp.json()
        except Exception as exc:  # network / JSON / HTTP — non-fatal
            logging.warning("Hugging Face daily papers fetch failed for %s: %s", date, exc)
            continue
        for item in items if isinstance(items, list) else []:
            paper = item.get("paper", {}) if isinstance(item, dict) else {}
            raw_id = str(paper.get("id", "")).strip()
            if not raw_id:
                continue
            bare_id = raw_id.split("v")[0]
            upvotes = int(paper.get("upvotes", item.get("upvotes", 0)) or 0)
            # Keep the highest upvote count if the paper appears on multiple days.
            prev = by_id.get(bare_id)
            if prev and prev["upvotes"] >= upvotes:
                continue
            by_id[bare_id] = {
                "upvotes": upvotes,
                "ai_keywords": paper.get("ai_keywords", []) or [],
                "title": paper.get("title", "") or "",
                "arxiv_id": raw_id,
            }
    logging.info("Hugging Face daily papers: %s unique papers across %s date(s)", len(by_id), len(dates))
    return by_id


def fetch_abstracts_by_id(arxiv_ids: list[str], session: requests.Session | None = None) -> dict[str, dict]:
    """
    Batch-fetch title/abstract/authors for a list of arXiv ids in one query
    (arXiv's id_list supports many ids per request). Returns {bare_id: fields}.
    Used to backfill abstracts for HF papers that the RSS feed didn't carry.
    """
    if not arxiv_ids:
        return {}
    session = session or requests.Session()
    out: dict[str, dict] = {}
    # arXiv recommends ≤ a few hundred ids per call; chunk to be safe.
    for i in range(0, len(arxiv_ids), 100):
        chunk = arxiv_ids[i:i + 100]
        url = f"{ARXIV_API_URL}?{urlencode({'id_list': ','.join(chunk), 'max_results': len(chunk)})}"
        try:
            response = _get_with_backoff(session, url)
            feed = feedparser.parse(response.text)
        except Exception as exc:
            logging.warning("arXiv id_list backfill failed: %s", exc)
            continue
        for entry in feed.entries:
            raw_id = entry.get("id", "").rstrip("/").split("/")[-1]
            bare = raw_id.split("v")[0]
            out[bare] = {
                "abstract_en": " ".join(entry.get("summary", "").split()),
                "authors": [a.get("name", "").strip() for a in entry.get("authors", []) if a.get("name")],
                "primary_category": entry.get("arxiv_primary_category", {}).get("term", ""),
                "source_categories": sorted({t["term"] for t in entry.get("tags", []) if t.get("term")}),
            }
        if i + 100 < len(arxiv_ids):
            time.sleep(REQUEST_DELAY_SECONDS)
    logging.info("Backfilled abstracts for %s/%s HF papers from arXiv", len(out), len(arxiv_ids))
    return out


def backfill_abstracts(papers: list[dict], session: requests.Session | None = None) -> list[dict]:
    """Fill in missing abstracts (HF-sourced papers) via a batch arXiv id query."""
    missing = [p for p in papers if not p.get("abstract_en") and p.get("arxiv_id")]
    if not missing:
        return papers
    ids = [p["arxiv_id"].split("v")[0] for p in missing]
    fetched = fetch_abstracts_by_id(ids, session=session)
    for p in missing:
        bare = p["arxiv_id"].split("v")[0]
        info = fetched.get(bare)
        if info:
            p["abstract_en"] = info["abstract_en"]
            if not p.get("authors"):
                p["authors"] = info["authors"]
            if not p.get("primary_category"):
                p["primary_category"] = info["primary_category"]
            if not p.get("source_categories"):
                p["source_categories"] = info["source_categories"]
    return papers


def merge_huggingface(papers: list[dict], hf_by_id: dict[str, dict]) -> list[dict]:
    """
    Annotate papers that appear on HF Daily with hf_upvotes, and append HF papers
    that the RSS feed missed (as extra candidates) so they get scored too.
    """
    existing_ids = {p["arxiv_id"].split("v")[0] for p in papers}
    for paper in papers:
        bare = paper["arxiv_id"].split("v")[0]
        if bare in hf_by_id:
            paper["hf_upvotes"] = hf_by_id[bare]["upvotes"]

    added = 0
    for bare_id, hf in hf_by_id.items():
        if bare_id in existing_ids:
            continue
        # Reconstruct a minimal paper record from the HF entry so it can be scored.
        papers.append({
            "arxiv_id": hf["arxiv_id"],
            "title_en": " ".join(hf["title"].split()),
            "abstract_en": "",  # HF doesn't give the full abstract; scorer uses title + keywords
            "authors": [],
            "affiliations": [],
            "arxiv_url": f"https://arxiv.org/abs/{bare_id}",
            "primary_category": "",
            "source_categories": [],
            "published": None,
            "updated": None,
            "announce_type": "hf",
            "hf_upvotes": hf["upvotes"],
            "hf_keywords": hf["ai_keywords"],
        })
        added += 1
    if added:
        logging.info("Added %s extra paper(s) from Hugging Face not in the RSS feed", added)
    return papers


def deduplicate_papers(papers: Iterable[dict]) -> list[dict]:
    deduped: dict[str, dict] = {}
    for paper in papers:
        arxiv_id = paper["arxiv_id"]
        if arxiv_id not in deduped:
            deduped[arxiv_id] = paper
            continue
        merged_categories = sorted(
            set(deduped[arxiv_id].get("source_categories", [])) | set(paper.get("source_categories", []))
        )
        deduped[arxiv_id]["source_categories"] = merged_categories
        if not deduped[arxiv_id].get("affiliations") and paper.get("affiliations"):
            deduped[arxiv_id]["affiliations"] = paper["affiliations"]
    return sorted(deduped.values(), key=lambda item: item.get("published") or "")


def save_raw_payload(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
