# Article Claw Skill

A powerful Skill for agents to fetch, classify, and summarize arXiv papers in speech & audio domains.

## Overview

This Skill enables agents to:
- 🔍 Fetch latest papers from arXiv (cs.SD, eess.AS categories)
- 📊 Automatically classify papers into 7 domains
- 📝 Generate Chinese summaries via Kimi AI or OpenAI
- 📧 Send HTML email digests to multiple recipients
- ⏰ Schedule daily automated runs

## Quick Start

### 1. Configuration

All configurations are centralized in `config/` directory:

```
config/
├── default.json           # Paper categories and sources
├── recipients.json        # Email recipients (create from example)
└── recipients.example.json # Template for recipients
```

**Setup recipients:**
```bash
cp config/recipients.example.json config/recipients.json
# Edit config/recipients.json to add your recipients
```

**Environment variables (in .env):**
```bash
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=your-email@qq.com
SMTP_PASS=your-auth-code
MOONSHOT_API_KEY=sk-your-kimi-key  # Optional, for AI summaries
```

### 2. Usage

#### Fetch Papers

```bash
# Fetch today's papers
python scripts/main.py

# Fetch specific date
python scripts/main.py --day 2026-03-10

# Fetch date range
python scripts/main.py --start-date 2026-03-01 --end-date 2026-03-10
```

#### Send Email Digest

Email is automatically sent if SMTP is configured in `.env` and recipients are defined in `config/recipients.json`.

#### Schedule Daily Runs

**GitHub Actions:**
- Already configured in `.github/workflows/daily_digest.yml`
- Runs daily at UTC 01:00 (09:00 Beijing Time)
- Add secrets in repository settings

**Local Cron:**
```bash
0 1 * * * cd /path/to/article_claw && python scripts/main.py
```

## Configuration Reference

### config/default.json

```json
{
  "project": {
    "name": "arxiv-audio-digest",
    "title": "arXiv Speech & Audio Digest",
    "timezone": "Asia/Shanghai"
  },
  "sources": {
    "categories": ["cs.SD", "eess.AS"]
  },
  "classification": {
    "categories": [
      {
        "name": "ASR",
        "label_zh": "语音识别",
        "keywords": ["asr", "speech recognition"]
      }
    ]
  }
}
```

### config/recipients.json

```json
{
  "recipients": [
    {
      "email": "professor@university.edu.cn",
      "name": "Professor",
      "enabled": true
    },
    {
      "email": "student@university.edu.cn",
      "name": "Student",
      "enabled": true
    }
  ],
  "settings": {
    "display_mode": "full",
    "papers_per_category": 999,
    "show_full_abstract": true
  }
}
```

## Agent Integration

### For OpenClaw/Kimi Agents

Agents can use this Skill by:

1. **Reading the configuration:**
   ```python
   # Load category configuration
   config = load_config("config/default.json")
   
   # Load recipients
   with open("config/recipients.json") as f:
       recipients = json.load(f)
   ```

2. **Running the pipeline:**
   ```python
   # Execute main script
   python scripts/main.py --day 2026-03-10
   ```

3. **Accessing outputs:**
   - Markdown digest: `content/posts/YYYY-MM-DD-arxiv-audio-digest.md`
   - JSON data: `data/processed/YYYY-MM-DD.json`
   - Raw data: `data/raw/YYYY-MM-DD.json`

### Tool Definitions

#### fetch_papers

Fetch papers from arXiv for a specific time window.

**Parameters:**
- `day` (string, optional): Specific date in YYYY-MM-DD format
- `start_date` (string, optional): Start date for range
- `end_date` (string, optional): End date for range

**Example:**
```json
{
  "tool": "fetch_papers",
  "parameters": {
    "day": "2026-03-10"
  }
}
```

#### send_digest

Send email digest to configured recipients.

**Parameters:**
- `date` (string, optional): Date of digest to send

**Example:**
```json
{
  "tool": "send_digest",
  "parameters": {
    "date": "2026-03-10"
  }
}
```

#### configure_skill

Update Skill configuration.

**Parameters:**
- `config_type` (string): "categories" or "recipients"
- `config_data` (object): Configuration data

**Example:**
```json
{
  "tool": "configure_skill",
  "parameters": {
    "config_type": "recipients",
    "config_data": {
      "recipients": [
        {"email": "new@example.com", "name": "New User", "enabled": true}
      ]
    }
  }
}
```

## Output Structure

### Markdown Digest

Location: `content/posts/YYYY-MM-DD-arxiv-audio-digest.md`

Contains:
- Daily statistics
- Papers grouped by category
- Full abstracts
- Chinese summaries
- Readability analysis
- arXiv links

### JSON Data

Location: `data/processed/YYYY-MM-DD.json`

Structure:
```json
{
  "generated_at": "2026-03-10T09:00:00+08:00",
  "window": {
    "start": "2026-03-09T09:00:00+08:00",
    "end": "2026-03-10T09:00:00+08:00"
  },
  "summary": {
    "total": 15,
    "counts": {...}
  },
  "papers": [...],
  "grouped": {...}
}
```

## Advanced Usage

### Custom Categories

Edit `config/default.json` to customize classification:

```json
{
  "classification": {
    "categories": [
      {
        "name": "Your Category",
        "label_zh": "你的分类",
        "keywords": ["keyword1", "keyword2"]
      }
    ]
  }
}
```

### AI Summaries

Configure API keys in `.env`:
- `MOONSHOT_API_KEY`: Kimi AI (recommended for Chinese)
- `OPENAI_API_KEY`: OpenAI (alternative)

Fallback chain: Kimi → OpenAI → Rule-based

### Multiple arXiv Categories

Edit `config/default.json`:
```json
{
  "sources": {
    "categories": ["cs.SD", "eess.AS", "cs.CL", "cs.LG"]
  }
}
```

## Troubleshooting

### SMTP Issues
- Verify SMTP settings in `.env`
- Use authorization code (not login password) for QQ/163
- Check firewall settings

### API Rate Limits
- Kimi/OpenAI may have rate limits
- Skill automatically falls back to rule-based generation
- Increase delays in `scripts/process_papers.py` if needed

### No Papers Found
- Check date range
- Verify arXiv categories in config
- Check internet connection

## License

MIT License - See repository LICENSE file

## Repository

https://github.com/yourusername/article_claw
