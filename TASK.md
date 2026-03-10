Build a minimal production-ready GitHub Actions project called `arxiv-audio-digest` that publishes a daily Chinese digest of new arXiv papers in speech and audio.

Goal
- Every day at 09:00 Beijing time, fetch newly appeared papers from:
  - cs.SD (Computer Science / Sound)
  - eess.AS (Audio and Speech Processing)
- Time window:
  - First run: previous day 09:00 Beijing -> current day 09:00 Beijing
  - Later runs: last successful run time -> current run time
- Generate:
  1) a structured JSON archive for the day
  2) a Markdown blog post grouped by category
  3) an optional HTML email summary

Core requirements
1. Data collection
- Use the arXiv API or official arXiv feeds.
- Only include papers newly submitted in the time window.
- Deduplicate papers that appear in both categories.
- Persist state so repeated runs do not resend the same paper.

2. Paper fields
For each paper, collect:
- arXiv id
- English title
- Chinese title
- authors
- affiliations if clearly available; otherwise omit affiliations
- English abstract
- Chinese abstract
- English keywords
- Chinese keywords
- arXiv abstract URL
- primary category / matched source category
- final digest category tag

3. Classification
Classify every paper into exactly one of these 6 categories:
- ASR
- TTS
- Enhancement
- SLU
- Paralinguistics
- Audio

Use title + abstract + keywords for classification.
Implement a deterministic keyword-rule baseline first.
If an LLM key is available, allow optional refinement, but the rule-based path must still work.

Suggested category coverage
- ASR: speech recognition, streaming ASR, multilingual ASR, LLM+ASR
- TTS: speech synthesis, neural vocoder, controllable TTS, voice conversion, singing synthesis
- Enhancement: denoising, dereverberation, AEC, separation, target speaker extraction
- SLU: speaker verification/identification, language identification, keyword spotting, spoken language understanding
- Paralinguistics: emotion, depression/cognitive detection, age/gender, deepfake/spoof detection
- Audio: acoustic event detection, music/audio analysis, sound scene analysis, bioacoustics, general audio

4. Blog output
Create one Markdown file per day:
- path: `content/posts/YYYY-MM-DD-arxiv-audio-digest.md`
- language: Chinese
- grouped by the 6 categories above
- for each paper include:
  - English title
  - Chinese title
  - authors
  - affiliations only if available
  - Chinese keywords
  - Chinese abstract
  - arXiv link
- add a short “today at a glance” section summarizing the daily distribution and notable trends

5. Email output
Create an optional HTML email summary that includes:
- total number of papers
- count per category
- 1–3 highlighted papers per category
- link or path to the full Markdown digest

6. Deployment
Implement as a GitHub Actions workflow:
- run daily at 01:00 UTC (= 09:00 Beijing time)
- support manual trigger
- commit generated JSON and Markdown back to the repo
- if email secrets are present, send the email; otherwise skip email cleanly

7. Secrets and security
Use GitHub Secrets only:
- SMTP_HOST
- SMTP_PORT
- SMTP_USER
- SMTP_PASS
- EMAIL_TO
- OPENAI_API_KEY (optional)
Never hardcode secrets.
Do not print secrets in logs.

8. Project structure
Create:
- `.github/workflows/daily_digest.yml`
- `scripts/main.py`
- `scripts/fetch_arxiv.py`
- `scripts/process_papers.py`
- `scripts/build_markdown.py`
- `scripts/send_email.py`
- `data/state.json`
- `data/raw/`
- `data/processed/`
- `content/posts/`
- `templates/blog_template.md.j2`
- `templates/email_template.html.j2`
- `requirements.txt`
- `README.md`

9. Implementation details
- Python 3.11
- Use requests/feedparser/python-dateutil/jinja2
- Use Asia/Shanghai timezone consistently
- Handle empty-day cases gracefully and still produce a digest saying no new papers were found
- Log clearly
- Make code modular and readable

10. Acceptance criteria
- A manual run produces:
  - one JSON file in `data/processed/`
  - one Markdown digest in `content/posts/`
  - updated `data/state.json`
- If SMTP secrets are configured, an email is sent successfully
- A second run does not duplicate previously processed papers
- README explains setup, GitHub Secrets, timezone logic, and local testing

Important behavior
- If affiliations cannot be confidently extracted, omit them instead of guessing.
- Keep Chinese summaries concise and faithful.
- Prefer stable deterministic behavior over clever but brittle parsing.
- If the LLM path is unavailable, the whole pipeline must still function.
