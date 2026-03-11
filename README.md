<div align="center">

# 📰 Article Claw

**Intelligent arXiv Paper Digest Generator**

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/daily_digest.yml)
[![Kimi AI](https://img.shields.io/badge/Kimi-AI-blueviolet)](https://www.moonshot.cn/)

*Automatically fetch, classify, and summarize arXiv papers in speech & audio daily*

[English](README.md) · [简体中文](README_CN.md) · [Quick Start](#-quick-start) · [Agent Skill](#-agent-skill)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

- 🤖 **Auto Fetch** — Daily arXiv paper retrieval
- 📊 **Smart Classification** — 7-domain auto-categorization
- 📝 **AI Summaries** — Kimi/OpenAI Chinese summaries
- 📧 **Email Delivery** — Multi-recipient HTML digests
- 👥 **Recipient Management** — JSON-based configuration
- ⚙️ **Config-Driven** — Zero-code customization
- 🔄 **State Persistence** — Auto-deduplication
- 🤖 **LLM Fallback** — Graceful degradation

</td>
<td width="50%">

<img src="assets/fig.png" width="100%" alt="System Architecture">

</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# 1. Clone and Setup
git clone https://github.com/yourusername/article_claw.git
cd article_claw && pip install -r requirements.txt

# 2. Configure
cp .env.example .env
cp config/recipients.example.json config/recipients.json
# Edit .env and config/recipients.json with your settings

# 3. Run
python scripts/main.py --day 2026-03-10
```

---

## 📂 Configuration

<details>
<summary><b>📁 Categories and Sources</b> — Click to expand</summary><br>

Edit `config/default.json`:

```json
{
  "sources": {"categories": ["cs.SD", "eess.AS"]},
  "classification": {
    "categories": [
      {"name": "ASR", "label_zh": "语音识别", "keywords": ["asr", "speech recognition"]}
    ]
  }
}
```

**Default Categories:**
- 🗣️ Speech LLM — Speech Large Language Models
- 🎤 ASR — Automatic Speech Recognition
- 🔊 TTS — Text-to-Speech / Speech Synthesis
- ✨ Enhancement — Speech Enhancement
- 🧠 SLU — Spoken Language Understanding
- 😊 Paralinguistics — Paralinguistics and Affective Computing
- 🎵 Audio — General Audio Processing

</details>

<details>
<summary><b>📧 Email Recipients</b> — Click to expand</summary><br>

Edit `config/recipients.json`:

```json
{
  "recipients": [
    {"email": "prof@university.edu.cn", "name": "Professor", "enabled": true},
    {"email": "student@university.edu.cn", "name": "Student", "enabled": true}
  ]
}
```

Enable or disable recipients individually.

</details>

<details>
<summary><b>🔐 Environment Variables</b> — Click to expand</summary><br>

Create `.env` file:

```bash
# SMTP Configuration (Required for email)
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=your-email@qq.com
SMTP_PASS=your-auth-code

# AI API Keys (Optional, for better summaries)
MOONSHOT_API_KEY=sk-your-kimi-key
OPENAI_API_KEY=sk-your-openai-key
```

**SMTP Providers:**

| Service | Host | Port | Note |
|---------|------|------|------|
| QQ Mail | smtp.qq.com | 465 | Use authorization code |
| 163 Mail | smtp.163.com | 465 | Use authorization code |
| Gmail | smtp.gmail.com | 465 | Use app password |

</details>

---

## 🤖 AI Summaries

<details>
<summary><b>🎨 How It Works</b> — Click to expand</summary><br>

**Priority Chain:** Kimi AI → OpenAI → Rule-based

**Kimi AI** (Recommended for Chinese):
```bash
MOONSHOT_API_KEY=sk-your-key
```
- Native Chinese language understanding
- Better context comprehension
- Automatic retry on rate limit

**OpenAI** (Alternative):
```bash
OPENAI_API_KEY=sk-your-key
```

**Fallback:** Works without API keys using rule-based generation.

</details>

---

## 🚀 Deployment

<details>
<summary><b>☁️ GitHub Actions (Recommended)</b></summary><br>

1. Fork this repository
2. Add secrets in Settings → Secrets:
   - `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`
   - `MOONSHOT_API_KEY` or `OPENAI_API_KEY` (optional)
3. Enable Actions
4. Runs daily at UTC 01:00 (09:00 Beijing Time)

</details>

<details>
<summary><b>🖥️ Local Deployment</b></summary><br>

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

</details>

---

## 🤖 Agent Skill

<details>
<summary><b>🔧 Skill Interface</b> — Click to expand</summary><br>

**Location:** `skill/` directory

```python
from skill.example import fetch_papers, get_digest_content

# Fetch papers
result = fetch_papers(day="2026-03-10")

# Get summary
content = get_digest_content("2026-03-10", format="summary")
```

**Available Tools:**

| Tool | Description |
|------|-------------|
| `fetch_papers` | Fetch arXiv papers |
| `send_digest` | Send email digest |
| `configure_categories` | Update categories |
| `configure_recipients` | Update recipients |
| `get_digest_content` | Retrieve content |
| `schedule_digest` | Schedule runs |

See [skill/SKILL.md](skill/SKILL.md) and [skill/tools.json](skill/tools.json) for details.

</details>

---

## 📁 Project Structure

```
article_claw/
├── .github/workflows/      # CI/CD configuration
├── assets/                 # Logos and figures
├── config/                 # Configuration files
├── content/posts/          # Generated digests
├── data/                   # Raw and processed data
├── scripts/                # Core scripts
├── skill/                  # Agent Skill interface
├── templates/              # Email templates
├── .env.example            # Environment template
└── examples/               # Example outputs
```

---

## 📖 Documentation

- [View Example Output](examples/sample_digest_excerpt.md)
- [Agent Skill Guide](skill/SKILL.md)
- [Contributing Guide](CONTRIBUTING.md)

---

## 🗺️ Roadmap

- [x] Kimi AI integration
- [x] Multi-recipient support
- [x] Agent Skill interface
- [ ] Web UI
- [ ] RSS feed
- [ ] Multi-language support

---

## 📄 License

[MIT License](LICENSE) © 2026 Article Claw Contributors

---

<div align="center">

**⭐ If you find this project helpful, please give us a star!**

</div>
