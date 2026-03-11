<div align="center">

# 📰 Article Claw

**Intelligent Multi-Source Paper Digest Generator**

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/daily_digest.yml)
[![Multi-LLM](https://img.shields.io/badge/LLM-Kimi%20%7C%20OpenAI%20%7C%20Claude%20%7C%20Gemini-blue)](https://github.com/yourusername/article_claw)

*Fetch, classify, and summarize papers from multiple sources in multiple languages*

[English](README.md) · [简体中文](README_CN.md) · [Quick Start](#-quick-start) · [Features](#-features) · [Agent Skill](#-agent-skill)

</div>

---

## ✨ Features

<table>
<tr>
<td width="60%">

🌐 **Multi-Source Support**
- arXiv (cs.SD, eess.AS, customizable)
- CNKI (知网) - planned
- Web of Science - planned
- Extensible architecture for new sources

🗣️ **Multi-Language Summaries**
- 🇨🇳 Chinese (中文)
- 🇺🇸 English
- 🇯🇵 Japanese (日本語)
- 🇰🇷 Korean (한국어)
- 🇩🇪 German (Deutsch)
- 🇫🇷 French (Français)
- 🇪🇸 Spanish (Español)

🤖 **Multi-Provider LLM**
- Kimi AI (Moonshot) - recommended
- OpenAI (GPT-4)
- Anthropic Claude
- Google Gemini
- DeepSeek
- Auto-fallback chain

</td>
<td width="40%">

<img src="assets/fig.png" width="100%" alt="System Architecture">

</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# 1. Clone & Setup
git clone https://github.com/yourusername/article_claw.git
cd article_claw && pip install -r requirements.txt

# 2. Configure
cp .env.example .env
cp config/recipients.example.json config/recipients.json

# 3. Run with different languages
python scripts/main.py --day 2026-03-10 --language zh  # Chinese
python scripts/main.py --day 2026-03-10 --language en  # English
python scripts/main.py --day 2026-03-10 --language ja  # Japanese
```

---

## 📂 Configuration

<details>
<summary><b>🌐 Sources Configuration</b> — Click to expand</summary><br>

Edit `config/default.json` to configure data sources:

```json
{
  "sources": {
    "arxiv": {
      "enabled": true,
      "name": "arXiv",
      "url": "https://arxiv.org",
      "categories": [
        {"id": "cs.SD", "name": "Sound", "url": "https://arxiv.org/list/cs.SD/recent"},
        {"id": "eess.AS", "name": "Audio and Speech", "url": "https://arxiv.org/list/eess.AS/recent"}
      ]
    },
    "cnki": {
      "enabled": false,
      "name": "中国知网",
      "url": "https://www.cnki.net"
    }
  }
}
```

Each source includes:
- `enabled`: Whether to fetch from this source
- `name`: Display name
- `url`: Source URL
- `categories`: List of categories with IDs and URLs

</details>

<details>
<summary><b>🗣️ Language Settings</b> — Click to expand</summary><br>

Edit `config/default.json`:

```json
{
  "language": {
    "default": "zh",
    "supported": ["zh", "en", "ja", "ko", "de", "fr", "es"]
  }
}
```

Or use command line:
```bash
python scripts/main.py --language ja  # Japanese output
```

Category labels are also multilingual:
```json
{
  "name": "ASR",
  "labels": {
    "zh": "语音识别",
    "en": "Speech Recognition",
    "ja": "音声認識",
    "ko": "음성 인식"
  }
}
```

</details>

<details>
<summary><b>🤖 LLM Provider Configuration</b> — Click to expand</summary><br>

Configure multiple LLM providers in `config/default.json`:

```json
{
  "llm": {
    "default_provider": "kimi",
    "providers": {
      "kimi": {
        "name": "Kimi AI (Moonshot)",
        "api_base": "https://api.moonshot.cn/v1",
        "model": "moonshot-v1-8k",
        "env_key": "MOONSHOT_API_KEY"
      },
      "openai": {
        "name": "OpenAI",
        "api_base": "https://api.openai.com/v1",
        "model": "gpt-4.1-mini",
        "env_key": "OPENAI_API_KEY"
      },
      "claude": {
        "name": "Anthropic Claude",
        "api_base": "https://api.anthropic.com",
        "model": "claude-3-haiku-20240307",
        "env_key": "ANTHROPIC_API_KEY"
      },
      "gemini": {
        "name": "Google Gemini",
        "api_base": "https://generativelanguage.googleapis.com/v1beta",
        "model": "gemini-pro",
        "env_key": "GOOGLE_API_KEY"
      },
      "deepseek": {
        "name": "DeepSeek",
        "api_base": "https://api.deepseek.com/v1",
        "model": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY"
      }
    },
    "fallback_chain": ["kimi", "openai", "claude", "deepseek", "gemini", "rule_based"]
  }
}
```

Set API keys in `.env`:
```bash
MOONSHOT_API_KEY=sk-your-key
OPENAI_API_KEY=sk-your-key
ANTHROPIC_API_KEY=sk-your-key
GOOGLE_API_KEY=your-key
DEEPSEEK_API_KEY=sk-your-key
```

The system automatically tries providers in the fallback chain.

</details>

<details>
<summary><b>📧 Email & Recipients</b> — Click to expand</summary><br>

**SMTP Settings** (`.env`):
```bash
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=your-email@qq.com
SMTP_PASS=your-auth-code
```

**Recipients** (`config/recipients.json`):
```json
{
  "recipients": [
    {"email": "prof@university.edu.cn", "name": "Professor", "enabled": true}
  ]
}
```

</details>

---

## 🚀 Deployment

<details>
<summary><b>☁️ GitHub Actions</b></summary><br>

1. Fork repository
2. Add secrets: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`
3. Add LLM API keys (optional): `MOONSHOT_API_KEY`, `OPENAI_API_KEY`, etc.
4. Runs daily at UTC 01:00

</details>

<details>
<summary><b>🖥️ Local / Server</b></summary><br>

```bash
# Linux/Mac Cron (daily at 9 AM)
0 1 * * * cd /path/to/article_claw && python scripts/main.py

# Windows Task Scheduler
schtasks /create /tn "ArticleClaw" /tr "python scripts/main.py" /sc daily /st 09:00
```

</details>

---

## 🤖 Agent Skill

<details>
<summary><b>🔧 Using the Skill</b> — Click to expand</summary><br>

```python
from skill.example import fetch_papers, get_digest_content

# Fetch with language
result = fetch_papers(day="2026-03-10", language="ja")

# Get content
content = get_digest_content("2026-03-10", format="summary")
```

**Available Tools:**
- `fetch_papers` — Fetch from configured sources
- `configure_sources` — Add/modify sources
- `configure_llm` — Switch LLM providers
- `configure_language` — Set output language
- `get_digest_content` — Retrieve generated content

See [skill/SKILL.md](skill/SKILL.md) for complete documentation.

</details>

---

## 📁 Project Structure

```
article_claw/
├── config/
│   ├── default.json           # Sources, languages, LLM config
│   ├── recipients.json        # Email recipients
│   └── recipients.example.json
├── scripts/
│   ├── main.py                # Main entry
│   ├── llm_client.py          # Multi-provider LLM client ⭐ NEW
│   ├── process_papers.py      # Multi-language processing
│   └── ...
├── skill/                     # Agent Skill interface
├── content/posts/             # Generated digests
└── ...
```

---

## 🗺️ Roadmap

- [x] Multi-provider LLM support (Kimi, OpenAI, Claude, Gemini, DeepSeek)
- [x] Multi-language output (7 languages)
- [x] Extensible source architecture
- [ ] CNKI (知网) integration
- [ ] Web of Science integration
- [ ] Web UI for configuration

---

## 📄 License

[MIT License](LICENSE) © 2026 Article Claw Contributors

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

</div>
