---
name: article_claw
description: Fetch, classify, and summarize arXiv papers in speech & audio domains with AI-powered Chinese summaries and email delivery.
homepage: https://github.com/yourusername/article_claw
metadata: {"clawdbot":{"emoji":"📰","requires":{"bins":["python3"],"env":["SMTP_HOST","SMTP_PORT","SMTP_USER","SMTP_PASS"],"optional_env":["MOONSHOT_API_KEY","OPENAI_API_KEY"]}}}
---

# Article Claw Skill

Intelligent arXiv paper digest generator for speech & audio research. Automatically fetch, classify, and summarize papers with AI-powered Chinese translations.

## Features

- 🤖 **Auto Fetch** — Daily arXiv paper retrieval (cs.SD, eess.AS)
- 📊 **Smart Classification** — Auto-categorize into 7 domains
- 📝 **AI Summaries** — Kimi/OpenAI Chinese summaries with fallback
- 📧 **Email Delivery** — HTML digests to multiple recipients
- 👥 **Recipient Management** — JSON-based configuration
- ⚙️ **Config-Driven** — Zero-code customization
- 🔄 **State Persistence** — Auto-deduplication

## Setup

### 1. Environment Variables

Required for email delivery:

```bash
export SMTP_HOST="smtp.qq.com"
export SMTP_PORT="465"
export SMTP_USER="your-email@qq.com"
export SMTP_PASS="your-auth-code"
```

Optional for AI summaries:

```bash
export MOONSHOT_API_KEY="sk-your-kimi-key"  # Recommended
export OPENAI_API_KEY="sk-your-openai-key"  # Alternative
```

### 2. Recipient Configuration

Create `config/recipients.json`:

```json
{
  "recipients": [
    {"email": "prof@university.edu.cn", "name": "Professor", "enabled": true},
    {"email": "student@university.edu.cn", "name": "Student", "enabled": true}
  ]
}
```

### 3. Category Configuration

Edit `config/default.json` to customize domains:

```json
{
  "classification": {
    "categories": [
      {"name": "ASR", "label_zh": "语音识别", "keywords": ["asr", "speech recognition"]}
    ]
  }
}
```

## Usage

### Fetch Papers

```bash
# Fetch today's papers
python scripts/main.py

# Fetch specific date
python scripts/main.py --day 2026-03-10

# Fetch date range
python scripts/main.py --start-date 2026-03-01 --end-date 2026-03-10
```

### Generated Outputs

- **Markdown digest:** `content/posts/YYYY-MM-DD-arxiv-audio-digest.md`
- **JSON data:** `data/processed/YYYY-MM-DD.json`
- **Raw data:** `data/raw/YYYY-MM-DD.json`

### View Digest Content

```bash
# View markdown
cat content/posts/2026-03-10-arxiv-audio-digest.md

# View JSON summary
jq '.summary' data/processed/2026-03-10.json
```

### Schedule Daily Runs

**GitHub Actions:**
Already configured in `.github/workflows/daily_digest.yml`

**Linux/Mac Cron:**
```bash
0 1 * * * cd /path/to/article_claw && python scripts/main.py
```

**Windows Task Scheduler:**
```powershell
$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "scripts/main.py"
$Trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
Register-ScheduledTask -TaskName "ArticleClaw" -Action $Action -Trigger $Trigger
```

## AI Summary Chain

The system uses intelligent fallback:

```
Kimi API → OpenAI API → Rule-based Generation
```

Even without API keys, Chinese summaries are generated using rule-based methods.

## Agent Tools

### fetch_papers

Fetch papers from arXiv.

**Parameters:**
- `day` (string, optional): Date in YYYY-MM-DD format
- `start_date` + `end_date` (string, optional): Date range

**Example:**
```python
from skill.example import fetch_papers
result = fetch_papers(day="2026-03-10")
```

### get_digest_content

Retrieve generated digest.

**Parameters:**
- `date` (string): Date in YYYY-MM-DD format
- `format` (string): "markdown", "json", or "summary"

**Example:**
```python
from skill.example import get_digest_content
content = get_digest_content("2026-03-10", format="summary")
```

### configure_recipients

Update email recipients.

**Parameters:**
- `recipients` (array): List of {email, name, enabled}

**Example:**
```python
from skill.example import configure_recipients
configure_recipients([
    {"email": "user@example.com", "name": "User", "enabled": true}
])
```

## Default Categories

| Category | Description | Chinese |
|----------|-------------|---------|
| Speech LLM | Speech Large Language Models | 语音大模型 |
| ASR | Automatic Speech Recognition | 语音识别 |
| TTS | Text-to-Speech / Speech Synthesis | 语音合成 |
| Enhancement | Speech Enhancement | 语音增强 |
| SLU | Spoken Language Understanding | 口语理解 |
| Paralinguistics | Paralinguistics & Affective Computing | 副语言学 |
| Audio | General Audio Processing | 通用音频 |

## SMTP Providers

| Service | Host | Port | Note |
|---------|------|------|------|
| QQ Mail | smtp.qq.com | 465 | Use authorization code |
| 163 Mail | smtp.163.com | 465 | Use authorization code |
| Gmail | smtp.gmail.com | 465 | Use app password |

## Notes

- All configurations are in `config/` directory
- `.env` and `config/recipients.json` are git-ignored for security
- API rate limits: Kimi/OpenAI may have rate limits; system auto-retries
- State is tracked in `data/state.json` to avoid duplicate processing
- Email is sent automatically if SMTP is configured

## Examples

```bash
# Quick start - fetch and send email
python scripts/main.py --day 2026-03-10

# View paper count
cat data/processed/2026-03-10.json | jq '.summary.total'

# View papers by category
cat data/processed/2026-03-10.json | jq '.grouped.ASR'

# Reset state and re-fetch
python scripts/reset_state.py
python scripts/main.py --day 2026-03-10
```

## Files

- `skill/tools.json` — Tool definitions for agent frameworks
- `skill/example.py` — Python usage examples
- `config/default.json` — Category configuration
- `config/recipients.example.json` — Recipient template
