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
REQUEST_DELAY_SECONDS = 3.5
MAX_RETRIES = 5
DEFAULT_USER_AGENT = "arxiv-audio-digest/1.0"


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
