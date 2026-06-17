# paper_claw — Personal Setup

Daily arXiv digest, filtered to *your* interests by an LLM relevance scorer,
emailed to your inbox. Runs automatically on GitHub Actions.

## How the daily job works

`.github/workflows/daily_digest.yml` runs `python scripts/main.py` on GitHub's
servers every day at **12:00 UTC = 8 AM America/New_York**. Each run:

1. Fetches recent papers from arXiv (cs.AI, cs.CL, cs.HC, cs.LG).
2. **Scores every paper 0–10** against your interest profile (`config/default.json` → `relevance.profile`).
3. Keeps papers scoring `>= min_score` (default 6), capped at `max_papers` (default 18).
4. **Force-keeps** any paper by a followed author (see below), pinned at the top.
5. Summarizes only the survivors (Chinese summaries) and emails you a clean digest
   with the full list attached as Markdown.
6. Emails the digest (the generated files stay on the runner only — nothing is
   committed back to the repo; `data/` artifacts are gitignored).

Your laptop does not need to be on.

## One-time GitHub Actions setup

1. **Push this fork** to GitHub (`git push`).
2. **Add repository secrets**: fork → Settings → Secrets and variables → Actions →
   *New repository secret*. Add:

   | Secret | Value |
   |---|---|
   | `SMTP_HOST` | `smtp.gmail.com` |
   | `SMTP_PORT` | `465` |
   | `SMTP_USER` | your Gmail address (the send-from account) |
   | `SMTP_PASS` | your Gmail **app password** |
   | `OPENAI_API_KEY` | your OpenAI key |
   | `EMAIL_TO` | recipient address, e.g. `zhihaoyu@andrew.cmu.edu` |

   Note: `config/recipients.json` is **gitignored** (it holds a personal address),
   so it is NOT on GitHub — the runner has no recipients file and falls back to the
   `EMAIL_TO` secret. That is why `EMAIL_TO` is required for the GitHub Actions run.
   For multiple recipients, comma-separate them in `EMAIL_TO`. Locally,
   `config/recipients.json` still works and takes priority when present.
3. **Enable Actions**: Actions tab → "I understand my workflows, enable them".
4. **Test it**: Actions → *📰 Daily arXiv Digest* → *Run workflow*. Watch the log,
   check your inbox + Spam.

## Tuning your recommendations

All in `config/default.json`:

- **`relevance.profile`** — plain-English description of what you want. Edit freely;
  this is the single biggest lever on quality.
- **`relevance.min_score`** — raise to 7–8 for a stricter/shorter digest, lower to 5 for more.
- **`relevance.max_papers`** — hard cap on digest size.
- **`watched_authors.authors`** — people/groups you always want to see. Each entry:
  ```json
  {"name": "Graham Neubig", "aliases": ["Graham Neubig", "G. Neubig"]}
  ```
  `name` is the canonical label shown in the email; `aliases` lists every spelling to
  match against arXiv (case-insensitive). Their papers are always included and pinned,
  even if off-topic. Set `watched_authors.enabled` to `false` to turn the feature off.
- **`sources.arxiv.categories`** — which arXiv sections to pull from.

## Local manual run

```bash
cd ~/paper_claw
source .venv/bin/activate
python scripts/main.py --day 2026-05-15          # specific day
python scripts/main.py --day 2026-05-15 --no-email   # generate only, no send
```
