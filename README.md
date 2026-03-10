<div align="center">

# 📰 Article Claw

**智能 arXiv 论文日报生成器**

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/daily_digest.yml)

*每日自动抓取、分类、总结 arXiv 语音与音频领域论文*

[简体中文](README.md) · [English](README_EN.md) · [开始使用](#快速开始) · [配置说明](#配置) · [查看示例](examples/sample_digest_excerpt.md)

</div>

---

## ✨ 功能特性

| 特性 | 说明 |
|------|------|
| 🤖 **自动抓取** | 每日定时从 arXiv 获取最新论文 |
| 📊 **智能分类** | 自动将论文归类到 7 大领域 |
| 📝 **中文总结** | 生成简洁的中文摘要和可读性分析 |
| 📧 **邮件推送** | 支持 HTML 邮件摘要推送 |
| ⚙️ **配置驱动** | 零代码修改即可自定义领域和分类 |
| 🔄 **状态持久** | 自动去重，避免重复处理 |

## 🏗️ 系统架构

![系统架构](assets/fig.png)

## 📂 默认分类

- **🗣️ Speech LLM** - 语音大模型
- **🎤 ASR** - 语音识别
- **🔊 TTS** - 语音合成
- **✨ Enhancement** - 语音增强
- **🧠 SLU** - 口语理解
- **😊 Paralinguistics** - 副语言学
- **🎵 Audio** - 通用音频

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆仓库
git clone https://github.com/yourusername/article_claw.git
cd article_claw

# 创建虚拟环境
conda create -n article_claw python=3.11 -y
conda activate article_claw
pip install -r requirements.txt
```

### 2. 本地运行

```bash
# 运行今日日报
python scripts/main.py

# 指定日期运行
python scripts/main.py --day 2026-03-10

# 自定义日期范围
python scripts/main.py --start-date 2026-03-01 --end-date 2026-03-10
```

### 3. GitHub Actions 自动运行

仓库已配置每日 UTC 01:00 (北京时间 09:00) 自动运行。

**所需 Secrets：**

| Secret | 说明 | 必需 |
|--------|------|------|
| `SMTP_HOST` | SMTP 服务器地址 | 可选 |
| `SMTP_PORT` | SMTP 端口 | 可选 |
| `SMTP_USER` | SMTP 用户名 | 可选 |
| `SMTP_PASS` | SMTP 密码 | 可选 |
| `EMAIL_TO` | 接收邮箱 | 可选 |
| `OPENAI_API_KEY` | OpenAI API 密钥 | 可选 |

## ⚙️ 配置

编辑 `config/default.json` 自定义你的日报：

```json
{
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

## 📁 项目结构

```
article_claw/
├── .github/workflows/      # GitHub Actions 配置
├── config/                 # 配置文件
├── content/posts/          # 生成的日报
├── data/
│   ├── raw/               # 原始数据
│   └── processed/         # 处理后数据
├── scripts/               # 核心脚本
├── templates/             # 输出模板
└── examples/              # 示例输出
```

## 📖 示例输出

生成的日报包含：

- 📅 时间窗口和论文统计
- 📊 各领域论文分布
- 📝 每篇论文的详细信息：
  - 英文标题
  - 作者列表
  - 英文摘要
  - 中文总结
  - 可读性分析
  - arXiv 链接

[查看完整示例 →](examples/sample_digest_excerpt.md)

## 🤝 贡献

欢迎提交 Issue 和 PR！请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

[MIT License](LICENSE) © 2026 Article Claw Contributors

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！**

</div>
