---
name: paper_claw
description: Fetch, classify, and summarize papers from multiple sources (arXiv, etc.) with AI-powered multi-language summaries and email delivery.
homepage: https://github.com/PigeonDan1/paper_claw
metadata: {"clawdbot":{"emoji":"📰","requires":{"bins":["python3"],"env":["SMTP_HOST","SMTP_PORT","SMTP_USER","SMTP_PASS"],"optional_env":["MOONSHOT_API_KEY","OPENAI_API_KEY","ANTHROPIC_API_KEY","GOOGLE_API_KEY","DEEPSEEK_API_KEY"]}}}
---

# Paper Claw Skill

Intelligent multi-source paper digest generator. Automatically fetch, classify, and summarize papers with AI-powered translations in 7 languages.

## Features

- 🌐 **Multi-Source Support** — arXiv (170+ categories), extensible for CNKI, Web of Science
- 🗣️ **Multi-Language** — Chinese, English, Japanese, Korean, German, French, Spanish
- 🤖 **Multi-Provider LLM** — Kimi, OpenAI, Claude, Gemini, DeepSeek with auto-fallback
- 📧 **Email Delivery** — HTML digests with full Markdown attachment
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

Optional for AI summaries (multiple providers supported):

```bash
# Primary: Kimi AI (recommended for Chinese)
export MOONSHOT_API_KEY="sk-your-kimi-key"

# Alternatives (auto-fallback)
export OPENAI_API_KEY="sk-your-openai-key"
export ANTHROPIC_API_KEY="sk-your-claude-key"
export GOOGLE_API_KEY="your-gemini-key"
export DEEPSEEK_API_KEY="sk-your-deepseek-key"
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

### 3. Source & Category Configuration

Edit `config/default.json` to customize sources:

```json
{
  "sources": {
    "arxiv": {
      "enabled": true,
      "categories": [
        {"id": "cs.CL", "name": "NLP", "url": "https://arxiv.org/list/cs.CL/recent"},
        {"id": "cs.CV", "name": "Computer Vision", "url": "https://arxiv.org/list/cs.CV/recent"}
      ]
    }
  }
}
```

See `config/arxiv_categories.json` for all 170+ available categories.

### 4. Language Configuration

```json
{
  "language": {
    "default": "zh",
    "supported": ["zh", "en", "ja", "ko", "de", "fr", "es"]
  }
}
```

## Usage

### Fetch Papers

```bash
# Fetch today's papers (default language from config)
python scripts/main.py

# Fetch with specific language
python scripts/main.py --day 2026-03-10 --language en
python scripts/main.py --day 2026-03-10 --language ja  # Japanese

# Fetch date range
python scripts/main.py --start-date 2026-03-01 --end-date 2026-03-10
```

### Generated Outputs

- **Markdown digest:** `content/posts/YYYY-MM-DD-arxiv-audio-digest.md`
- **JSON data:** `data/processed/YYYY-MM-DD.json`
- **Raw data:** `data/raw/YYYY-MM-DD.json`

### Email Delivery

Email is automatically sent with:
- **HTML preview** — Shows first 3 papers with logo and GitHub link
- **Full Markdown attachment** — Complete digest with all papers

### Schedule Daily Runs

**GitHub Actions:**
Already configured in `.github/workflows/daily_digest.yml`

**Linux/Mac Cron:**
```bash
0 1 * * * cd /path/to/paper_claw && python scripts/main.py
```

**Windows Task Scheduler:**
```powershell
$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "scripts/main.py"
$Trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
Register-ScheduledTask -TaskName "PaperClaw" -Action $Action -Trigger $Trigger
```

## AI Summary Chain

The system uses intelligent fallback across providers:

```
Kimi → OpenAI → Claude → DeepSeek → Gemini → Rule-based
```

Even without API keys, summaries are generated using rule-based methods.

## Agent Tools

### fetch_papers

Fetch papers from configured sources.

**Parameters:**
- `day` (string, optional): Date in YYYY-MM-DD format
- `start_date` + `end_date` (string, optional): Date range
- `language` (string, optional): Output language (zh/en/ja/ko/de/fr/es)

**Example:**
```python
from skill.example import fetch_papers
result = fetch_papers(day="2026-03-10", language="en")
```

### configure_sources

Update data sources and categories.

**Parameters:**
- `sources` (object): Source configuration with categories

**Example:**
```python
from skill.example import configure_sources
configure_sources({
    "arxiv": {
        "enabled": True,
        "categories": [
            {"id": "cs.AI", "name": "AI"},
            {"id": "cs.LG", "name": "ML"}
        ]
    }
})
```

### configure_language

Set output language for summaries.

**Parameters:**
- `language` (string): One of zh/en/ja/ko/de/fr/es

**Example:**
```python
from skill.example import configure_language
configure_language("ja")  # Japanese output
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
    {"email": "user@example.com", "name": "User", "enabled": True}
])
```

## Default Categories

Categories support multi-language labels:

| Category | English | Chinese | Japanese |
|----------|---------|---------|----------|
| Speech LLM | Speech LLM | 语音大模型 | 音声大規模言語モデル |
| ASR | Speech Recognition | 语音识别 | 音声認識 |
| TTS | Speech Synthesis | 语音合成 | 音声合成 |
| Enhancement | Enhancement | 语音增强 | 音声強調 |
| SLU | Spoken Language Understanding | 口语理解 | 音声言語理解 |
| Paralinguistics | Paralinguistics | 副语言学 | 副言語学 |
| Audio | General Audio | 通用音频 | 一般音声 |

## SMTP Providers

| Service | Host | Port | Note |
|---------|------|------|------|
| QQ Mail | smtp.qq.com | 465 | Use authorization code |
| 163 Mail | smtp.163.com | 465 | Use authorization code |
| Gmail | smtp.gmail.com | 465 | Use app password |

## Notes

- All configurations are in `config/` directory
- `.env` and `config/recipients.json` are git-ignored for security
- API rate limits: System auto-retries with fallback providers
- State is tracked in `data/state.json` to avoid duplicate processing
- Email includes both HTML preview and full Markdown attachment
- Logo displayed in emails from GitHub raw URL

## Examples

```bash
# Quick start - fetch and send email
python scripts/main.py --day 2026-03-10

# Multi-language examples
python scripts/main.py --day 2026-03-10 --language zh  # Chinese
python scripts/main.py --day 2026-03-10 --language en  # English
python scripts/main.py --day 2026-03-10 --language ja  # Japanese

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
- `config/default.json` — Source and language configuration
- `config/arxiv_categories.json` — Complete arXiv category list
- `config/recipients.example.json` — Recipient template
