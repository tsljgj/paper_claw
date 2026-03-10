# arxiv-audio-digest

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions](https://img.shields.io/badge/workflow-daily%20digest-2ea44f)](.github/workflows/daily_digest.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)
[![Config Driven](https://img.shields.io/badge/config-driven-orange.svg)](config/default.json)

Config-driven arXiv digest generator for speech, audio, and adjacent research domains.

The default setup ships with a speech/audio preset, but the repository is designed to be repurposed:

- choose your own arXiv source categories
- choose your own classification buckets
- keep the same fetch -> classify -> digest -> email pipeline

## What this repo does

On each run, the project:

1. resolves a time window
2. fetches new arXiv papers from configured categories
3. deduplicates overlapping papers
4. filters already processed IDs
5. classifies each paper into one configured bucket
6. renders a Markdown digest
7. optionally sends an HTML email summary
8. persists state for the next run

Default domain:

- `cs.SD`
- `eess.AS`

Default buckets:

- `Speech LLM`
- `ASR`
- `TTS`
- `Enhancement`
- `SLU`
- `Paralinguistics`
- `Audio`

## Why this is more than a one-off script

This repository is intended to be a reusable research-digest template:

- the source domain is configurable
- the classification schema is configurable
- the daily output is human-readable
- the state machine supports repeated unattended runs
- the workflow works locally and in GitHub Actions

## Example output

Each paper entry includes:

- original English title
- authors
- affiliations when available
- original English abstract
- arXiv link
- `综合评价`
  - `总结`: a short 2-4 sentence Chinese summary
  - `可读性分析`: a concise note on whether the paper is easy to scan quickly

This keeps the source metadata intact while adding an editorial layer for fast reading.

A tiny example excerpt lives at:

- `examples/sample_digest_excerpt.md`

## Architecture

```text
config/default.json
  -> scripts/main.py
     -> scripts/fetch_arxiv.py
     -> scripts/process_papers.py
     -> scripts/build_markdown.py
     -> scripts/send_email.py
  -> data/raw/
  -> data/processed/
  -> content/posts/
```

## Configuration

The repository is now config-driven.

Default config lives at:

```text
config/default.json
```

It controls:

- project metadata
- source arXiv categories
- classification categories
- category labels
- keyword rules

### Example: change the source domain

You can replace the default speech/audio source list:

```json
{
  "sources": {
    "categories": ["cs.CL", "cs.LG"]
  }
}
```

### Example: define your own buckets

You can replace the built-in buckets entirely:

```json
{
  "classification": {
    "categories": [
      {
        "name": "Foundation Models",
        "label_zh": "基础模型",
        "keywords": ["foundation model", "large language model", "pretraining"]
      },
      {
        "name": "Applications",
        "label_zh": "应用",
        "keywords": ["dialogue", "agent", "retrieval", "evaluation"]
      }
    ]
  }
}
```

### Run with a custom config

```bash
python scripts/main.py --config config/default.json
```

## Time window behavior

Default scheduled behavior:

- workflow runs daily at `01:00 UTC`
- this is `09:00` in Beijing time

Window rules:

- first run:
  - previous day `09:00` Beijing time -> current day `09:00` Beijing time
- later runs:
  - `last_successful_run` -> current run time
- manual override:
  - `--start`
  - optional `--end`

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

Use a fixed test time:

```bash
python scripts/main.py --now 2026-03-10T09:00:00+08:00
```

Use a custom window:

```bash
python scripts/main.py --start 2026-03-09T09:00:00+08:00 --end 2026-03-10T09:00:00+08:00
```

Use a custom config:

```bash
python scripts/main.py --config config/default.json
```

Reset all state and generated outputs:

```bash
python scripts/reset_state.py
```

## Interactive and extensible points

This is still a repository-first tool, but it already has useful interaction points:

- CLI time-window overrides with `--start`, `--end`, `--now`
- CLI config override with `--config`
- reset script for restarting the pipeline cleanly
- issue templates and PR template for external collaboration

Natural next interaction layers for future PRs:

- a tiny web UI to edit config
- a review page to correct categories before publish
- a highlight selector for “editor’s picks”
- a setup wizard that creates a new domain config interactively

## GitHub Actions

Workflow:

- `.github/workflows/daily_digest.yml`

It:

- runs daily
- supports manual trigger
- installs dependencies
- generates JSON and Markdown
- commits generated artifacts back to the repo
- optionally sends email

## Secrets

Optional or required secrets depending on your deployment:

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASS`
- `EMAIL_TO`
- `OPENAI_API_KEY`

Optional environment variable:

- `ARXIV_CONTACT_EMAIL`

`ARXIV_CONTACT_EMAIL` is included in the HTTP `User-Agent` for better operational hygiene when talking to arXiv.

## Repository structure

```text
.github/
config/
content/posts/
data/raw/
data/processed/
examples/
scripts/
templates/
README.md
CONTRIBUTING.md
LICENSE
requirements.txt
```

## Example use cases

- daily speech/audio reading group digest
- personalized arXiv scan for a lab
- domain-specific newsletter for a niche category mix
- internal team alerting with email summaries
- a base repo for custom arXiv editorial workflows

## Good first PRs

- add a setup wizard that generates a new config from prompts
- add a small front-end preview for a generated digest
- support multiple output themes
- add RSS fallback when API throttling is severe
- add classifier regression tests
- add configurable highlight heuristics
- add per-domain example configs under `config/examples/`

## Current limitations

- classification remains heuristic
- LLM-free summaries are still weaker than LLM-assisted summaries
- templates are intentionally simple
- there is not yet a true interactive UI

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
