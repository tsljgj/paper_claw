# arxiv-audio-digest

Daily Chinese digest for newly submitted arXiv papers in speech and audio, built for unattended GitHub Actions runs and readable human review.

This project fetches new papers from `cs.SD` and `eess.AS`, deduplicates them, classifies them into curated research buckets, and publishes:

- a structured JSON archive
- a Markdown daily digest
- an optional HTML email summary

The output is designed for researchers who want a fast daily scan first, then the original English metadata when they decide what to read in depth.

## Why this exists

arXiv moves quickly in speech and audio. The raw feed is noisy, category boundaries are imperfect, and most daily update workflows are either too manual or too generic.

This repository packages a narrow workflow:

- fetch only new papers in a time window
- group them into speech/audio categories that are useful in practice
- keep the original English title and abstract intact
- add a short Chinese review block for each paper
- persist state so repeated runs do not resend the same papers

## What the digest looks like

Each paper entry includes:

- original English title
- authors
- affiliations when confidently available
- original English abstract
- arXiv link
- a Chinese review block:
  - `总结`: a short 2-4 sentence Chinese summary
  - `可读性分析`: a concise reading-difficulty note

## Categories

The current rule-based classifier assigns each paper to exactly one category:

- `Speech LLM`
- `ASR`
- `TTS`
- `Enhancement`
- `SLU`
- `Paralinguistics`
- `Audio`

This baseline is deterministic. If `OPENAI_API_KEY` is available, the review text becomes more natural, but the pipeline still works without any LLM dependency.

## End-to-end flow

```text
GitHub Actions / local run
  -> resolve time window
  -> query arXiv for cs.SD and eess.AS
  -> deduplicate overlapping papers
  -> filter already processed IDs
  -> classify each paper
  -> generate Chinese review block
  -> write raw JSON
  -> write processed JSON
  -> render Markdown digest
  -> optionally send HTML email
  -> update state.json
```

## Time window logic

Default scheduled behavior:

- workflow runs daily at `01:00 UTC`
- this corresponds to `09:00` in Beijing time

Window rules:

- first run:
  - previous day `09:00` Beijing time -> current day `09:00` Beijing time
- later runs:
  - `last_successful_run` -> current run time
- manual override:
  - pass `--start`
  - optionally pass `--end`

Timezone is consistently `Asia/Shanghai`.

## Repository structure

```text
.github/workflows/daily_digest.yml
scripts/main.py
scripts/fetch_arxiv.py
scripts/process_papers.py
scripts/build_markdown.py
scripts/send_email.py
scripts/reset_state.py
data/state.json
data/raw/
data/processed/
content/posts/
templates/blog_template.md.j2
templates/email_template.html.j2
```

## Quick start

### 1. Create an environment

```bash
conda create -n article_claw python=3.11 -y
conda activate article_claw
python -m pip install -r requirements.txt
```

### 2. Run locally

Default run:

```bash
python scripts/main.py
```

Use a fixed reference time for testing:

```bash
python scripts/main.py --now 2026-03-10T09:00:00+08:00
```

Manually specify a window:

```bash
python scripts/main.py --start 2026-03-09T09:00:00+08:00 --end 2026-03-10T09:00:00+08:00
```

Reset state and generated outputs:

```bash
python scripts/reset_state.py
```

## Configuration

### Required Python packages

Install with:

```bash
python -m pip install -r requirements.txt
```

Note:

- the correct package name is `python-dateutil`, not `dateutil`

### Optional environment variables

- `OPENAI_API_KEY`
- `ARXIV_CONTACT_EMAIL`

`ARXIV_CONTACT_EMAIL` is used in the arXiv request `User-Agent` so the crawler is better behaved operationally.

## GitHub Actions setup

The workflow file is `.github/workflows/daily_digest.yml`.

It:

- runs daily at `01:00 UTC`
- supports manual trigger
- installs dependencies
- runs the digest generator
- commits generated JSON and Markdown back to the repository
- sends email only when SMTP secrets are configured

### GitHub Secrets

Configure these secrets in the repository:

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASS`
- `EMAIL_TO`
- `OPENAI_API_KEY`

If SMTP secrets are absent, email is skipped cleanly.

## Output files

- `data/raw/YYYY-MM-DD.json`
  - fetched and deduplicated raw paper records
- `data/processed/YYYY-MM-DD.json`
  - processed paper records with category and review metadata
- `content/posts/YYYY-MM-DD-arxiv-audio-digest.md`
  - human-facing daily digest

## Design choices

### Why keep English titles and abstracts

Academic metadata is easy to mistranslate in subtle ways. This project keeps the original English title and abstract intact, then adds a separate Chinese review layer instead of replacing the source text.

### Why the classifier is rule-based first

Daily tooling needs repeatability. A deterministic rule baseline is easier to debug, easier to improve incrementally, and still useful when no LLM key is available.

### Why not guess affiliations

Affiliations are omitted unless clearly extractable. Wrong affiliations are worse than missing affiliations in a research digest.

## Current limitations

- category assignment is still heuristic
- review quality is much better with an LLM key than without one
- arXiv rate limiting can still happen under hostile network conditions
- the blog/email templates are intentionally simple and not yet heavily branded

## Good first PRs

- improve `Speech LLM` vs `ASR` routing with stronger keyword rules
- add fallback to official arXiv RSS feeds when API throttling is severe
- upgrade the email template with richer highlighting and stronger typography
- add a small evaluation set for classifier regression testing
- add paper highlighting heuristics beyond category counts
- support multiple digest styles, for example terse vs editorial
- add unit tests for window logic, classification, and state transitions
- improve readability scoring with more robust signals

## Suggested roadmap

### Near term

- harden retry and fallback behavior around arXiv rate limiting
- improve deterministic Chinese summary generation
- add tests

### Medium term

- support multiple source categories
- allow category-specific highlight selection
- expose a lightweight config file for custom deployments

### Longer term

- ship as a reusable template repository
- add a tiny review UI for correcting categories and exporting curated selections

## Open-sourcing checklist

Before publishing this repository:

1. remove any generated artifacts you do not want tracked
2. confirm no secrets exist in tracked files
3. choose a license
4. initialize git if needed
5. create the GitHub repository
6. push the code
7. configure secrets
8. run the workflow manually once

## Publishing this repo to GitHub

This directory is not yet a git repository. I can prepare it for publishing in either of these two ways:

1. local-only packaging:
   - initialize git
   - make the repo ready
   - leave actual GitHub creation to you
2. full publishing:
   - initialize git
   - create the GitHub repo
   - add remote
   - push the initial branch

If you want the second path, I can do it next. If `gh` needs re-authentication, you can help at that step.
