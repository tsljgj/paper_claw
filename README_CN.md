<div align="center">

# 📰 Article Claw

**智能 arXiv 论文日报生成器**

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/daily_digest.yml)
[![Kimi AI](https://img.shields.io/badge/Kimi-AI-blueviolet)](https://www.moonshot.cn/)

*每日自动抓取、分类、总结 arXiv 语音与音频领域论文*

[English](README.md) · [简体中文](README_CN.md) · [快速开始](#快速开始) · [配置说明](#配置说明) · [查看示例](examples/sample_digest_excerpt.md)

</div>

---

## ✨ 功能特性

| 特性 | 说明 |
|------|------|
| 🤖 **自动抓取** | 每日定时从 arXiv 获取最新论文 |
| 📊 **智能分类** | 自动将论文归类到 7 大领域 |
| 📝 **AI 中文总结** | 通过 **Kimi AI** 或 **OpenAI** 生成高质量中文摘要 |
| 📧 **邮件推送** | 支持多收件人 HTML 邮件推送 |
| 👥 **收件人管理** | 通过 JSON 文件灵活配置收件人列表 |
| ⚙️ **配置驱动** | 零代码修改即可自定义领域和分类 |
| 🔄 **状态持久** | 自动去重，避免重复处理 |
| 🤖 **智能降级** | API 不可用时自动回退到规则生成 |

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

### 2. 本地配置

创建 `.env` 文件进行本地配置（程序会自动加载）：

```bash
# 从模板复制
cp .env.example .env

# 编辑 .env 填入你的配置
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=你的邮箱@qq.com
SMTP_PASS=你的授权码
MOONSHOT_API_KEY=sk-你的kimi密钥
```

### 3. 配置收件人

创建 `config/recipients.json` 管理邮件收件人：

```bash
# 从模板复制
cp config/recipients.example.json config/recipients.json
```

编辑 `config/recipients.json`：

```json
{
  "recipients": [
    {
      "email": "professor@university.edu.cn",
      "name": "教授",
      "enabled": true
    },
    {
      "email": "student@university.edu.cn",
      "name": "学生",
      "enabled": true
    }
  ]
}
```

### 4. 运行

```bash
# 运行今日日报
python scripts/main.py

# 指定日期运行
python scripts/main.py --day 2026-03-10

# 自定义日期范围
python scripts/main.py --start-date 2026-03-01 --end-date 2026-03-10
```

---

## 🤖 AI 中文总结

Article Claw 支持 **Kimi AI**（推荐）和 **OpenAI** 生成高质量中文摘要。

### Kimi AI（推荐）

Kimi（月之暗面）对中文理解能力更强，生成更流畅的中文摘要。

**配置方法：**
```bash
# 在 .env 中添加
MOONSHOT_API_KEY=sk-你的kimi密钥
```

**特点：**
- 原生中文语言理解
- 更好的上下文理解能力
- 限流时自动降级

### OpenAI

```bash
# 在 .env 中添加
OPENAI_API_KEY=sk-你的openai密钥
```

### 智能降级策略

系统采用智能降级机制：

```
Kimi API → OpenAI API → 规则生成
```

即使没有 API 密钥，系统也会使用规则方法生成中文摘要。

---

## 📧 邮件配置

### SMTP 设置（在 `.env` 中配置）

| 邮箱服务 | SMTP_HOST | SMTP_PORT | 说明 |
|---------|-----------|-----------|------|
| QQ 邮箱 | smtp.qq.com | 465 | 使用授权码 |
| 163 邮箱 | smtp.163.com | 465 | 使用授权码 |
| Gmail | smtp.gmail.com | 465 | 使用应用密码 |

### 多收件人配置

在 `config/recipients.json` 中配置：
- 支持任意数量的收件人
- 可单独启用/禁用
- 修改即时生效

---

## ⚙️ 配置说明

### 分类配置

编辑 `config/default.json` 自定义论文分类：

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

---

## 📁 项目结构

```
article_claw/
├── .github/workflows/      # GitHub Actions 配置
├── assets/                 # 资源文件（Logo、架构图）
├── config/
│   ├── default.json        # 分类配置
│   ├── recipients.json     # 收件人列表（隐私）
│   └── recipients.example.json  # 收件人模板
├── content/posts/          # 生成的日报
├── data/
│   ├── raw/               # 原始数据
│   └── processed/         # 处理后数据
├── scripts/               # 核心脚本
├── templates/             # 输出模板
├── .env                   # 本地密钥（隐私）
├── .env.example           # 环境变量模板
└── examples/              # 示例输出
```

---

## 🚀 部署方式

### 方式 1：GitHub Actions（推荐）

1. Fork 本仓库
2. 在 Settings → Secrets 中添加密钥：
   - `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`
   - `MOONSHOT_API_KEY` 或 `OPENAI_API_KEY`（可选）
3. 启用 Actions
4. 每日 UTC 01:00（北京时间 09:00）自动运行

### 方式 2：Linux/Mac 定时任务

```bash
# 编辑定时任务
crontab -e

# 每天 9:00 运行
0 1 * * * cd /path/to/article_claw && python scripts/main.py >> /var/log/article_claw.log 2>&1
```

### 方式 3：Windows 任务计划

```powershell
$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "D:\article_claw\scripts\main.py"
$Trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
Register-ScheduledTask -TaskName "ArticleClaw-Daily" -Action $Action -Trigger $Trigger
```

---

## 📖 示例输出

生成的日报包含：

- 📅 时间窗口和论文统计
- 📊 各领域论文分布
- 📝 每篇论文详细信息：
  - 英文标题和完整摘要
  - 作者列表和机构
  - **AI 生成中文总结**（通过 Kimi/OpenAI）
  - 可读性分析
  - arXiv 链接

[查看完整示例 →](examples/sample_digest_excerpt.md)

---

## 🌍 语言支持

- 🇨🇳 **中文** - 通过 Kimi AI 或规则生成完整中文摘要
- 🇺🇸 **英文** - 保留原始英文论文元数据

---

## 🤝 贡献

欢迎提交 Issue 和 PR！请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 🗺️ 路线图

- [x] Kimi AI 集成生成中文摘要
- [x] 多收件人管理
- [x] 完整内容邮件推送
- [ ] Web 配置界面
- [ ] RSS 订阅输出
- [ ] 多语言支持（日语、韩语）

---

## 📄 许可证

[MIT License](LICENSE) © 2026 Article Claw Contributors

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！**

</div>
