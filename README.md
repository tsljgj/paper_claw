<div align="center">

# 📰 Article Claw

**Intelligent arXiv Paper Digest Generator**

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/daily_digest.yml)

*Automatically fetch, classify, and summarize arXiv papers in speech & audio daily*

[English](README.md) · [简体中文](README_CN.md) · [Quick Start](#quick-start) · [Configuration](#configuration) · [View Example](examples/sample_digest_excerpt.md)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Auto Fetch** | Daily scheduled fetching of latest papers from arXiv |
| 📊 **Smart Classification** | Automatically categorize papers into 7 domains |
| 📝 **Chinese Summary** | Generate concise Chinese abstracts and readability analysis |
| 📧 **Email Delivery** | Support HTML email digest delivery |
| ⚙️ **Config-Driven** | Customize domains and categories without code changes |
| 🔄 **State Persistence** | Automatic deduplication to avoid reprocessing |

## 🏗️ System Architecture

![System Architecture](assets/fig.png)

## 📂 Default Categories

- **🗣️ Speech LLM** - Speech Large Language Models
- **🎤 ASR** - Automatic Speech Recognition
- **🔊 TTS** - Text-to-Speech / Speech Synthesis
- **✨ Enhancement** - Speech Enhancement
- **🧠 SLU** - Spoken Language Understanding
- **😊 Paralinguistics** - Paralinguistics & Affective Computing
- **🎵 Audio** - General Audio Processing

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/article_claw.git
cd article_claw

# Create virtual environment
conda create -n article_claw python=3.11 -y
conda activate article_claw
pip install -r requirements.txt
```

### 2. Local Run

```bash
# Run today's digest
python scripts/main.py

# Run for specific date
python scripts/main.py --day 2026-03-10

# Custom date range
python scripts/main.py --start-date 2026-03-01 --end-date 2026-03-10
```

### 3. GitHub Actions Automation

The repository is configured to run automatically at UTC 01:00 (09:00 Beijing Time) daily.

**Required Secrets:**

| Secret | Description | Required |
|--------|-------------|----------|
| `SMTP_HOST` | SMTP server address | Optional |
| `SMTP_PORT` | SMTP port | Optional |
| `SMTP_USER` | SMTP username | Optional |
| `SMTP_PASS` | SMTP password | Optional |
| `EMAIL_TO` | Recipient email | Optional |
| `OPENAI_API_KEY` | OpenAI API key | Optional |

## ⚙️ Configuration

Edit `config/default.json` to customize your digest:

```json
{
  "sources": {
    "categories": ["cs.SD", "eess.AS"]
  },
  "classification": {
    "categories": [
      {
        "name": "ASR",
        "label_zh": "Speech Recognition",
        "keywords": ["asr", "speech recognition"]
      }
    ]
  }
}
```

## 📁 Project Structure

```
article_claw/
├── .github/workflows/      # GitHub Actions configuration
├── assets/                 # Assets (logos, figures)
├── config/                 # Configuration files
├── content/posts/          # Generated digests
├── data/
│   ├── raw/               # Raw data
│   └── processed/         # Processed data
├── scripts/               # Core scripts
├── templates/             # Output templates
└── examples/              # Example outputs
```

## 📖 Sample Output

Generated digests include:

- 📅 Time window and paper statistics
- 📊 Distribution across domains
- 📝 Detailed information for each paper:
  - English title
  - Author list
  - English abstract
  - Chinese summary
  - Readability analysis
  - arXiv link

[View Full Example →](examples/sample_digest_excerpt.md)

## 🌍 Language Support

Currently supports:
- 🇨🇳 **Chinese** - Full Chinese summaries and analysis
- 🇺🇸 **English** - Original English paper metadata

> **Note:** Chinese summaries are generated based on English abstracts using LLM or rule-based translation.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🗺️ Roadmap

- [ ] Multi-language support (Japanese, Korean, etc.)
- [ ] Web UI for configuration management
- [ ] RSS feed output
- [ ] More paper sources (ACL Anthology, etc.)
- [ ] Advanced classification using LLM

## 📄 License

[MIT License](LICENSE) © 2026 Article Claw Contributors

---

<div align="center">

**⭐ If you find this project helpful, please give us a star!**

</div>
