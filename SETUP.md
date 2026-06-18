# paper_claw — Personal Setup

Daily arXiv digest, filtered to *your* interests by an LLM relevance scorer,
emailed to your inbox. Runs automatically on GitHub Actions.

## How the daily job works

`.github/workflows/daily_digest.yml` runs in **two phases** each day so the email
lands as close to 08:00 ET as possible despite GitHub cron's drift:

- **PREPARE — ~07:30 ET (11:30 UTC).** Fetch from arXiv → score every paper 0–10
  against your interest profile → keep the top ones (and force-keep followed
  authors) → summarize. Commits the prepared digest to the repo. This is the slow
  part (the LLM work).
- **SEND — 08:00 ET (12:00 UTC).** Reuses the prepared digest and just emails it —
  takes a few seconds, so even if this cron fires a little late the email is still
  near 8:00. If PREPARE hasn't finished yet, SEND falls back to building from
  scratch (slower, but still sends).

Each pipeline run:

1. Fetches recent papers from arXiv (cs.AI, cs.CL, cs.HC, cs.LG).
2. **Scores every paper 0–10** against your interest profile (`config/default.json` → `relevance.profile`).
3. Keeps papers scoring `>= min_score` (default 6), capped at `max_papers` (default 18).
4. **Force-keeps** any paper by a followed author, pinned at the top.
5. Summarizes survivors (the top 5 get a deeper read with a stronger model) and
   emails you a clean digest with the full list attached as Markdown.

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
   | `EMAIL_FROM_NAME` | *(optional)* sender display name, e.g. `Zhihao's Paper Assistant`. Defaults to that if unset. |

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
