<div align="center">

# 📰 Paper Claw

**智能 arXiv 论文日报生成器**

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/daily_digest.yml)
[![Kimi AI](https://img.shields.io/badge/Kimi-AI-blueviolet)](https://www.moonshot.cn/)

*每日自动抓取、分类、总结 arXiv 语音与音频领域论文*

[English](README.md) · [简体中文](README_CN.md) · [快速开始](#-快速开始) · [Agent Skill](#-agent-skill)

</div>

---

## ✨ 功能特性

<table>
<tr>
<td width="50%">

- 🤖 **自动抓取** — 每日自动获取 arXiv 论文
- 📊 **智能分类** — 7 大领域自动归类
- 📝 **AI 总结** — Kimi/OpenAI 生成中文摘要
- 📧 **邮件推送** — 多收件人 HTML 邮件
- 👥 **收件人管理** — JSON 配置管理
- ⚙️ **配置驱动** — 零代码自定义
- 🔄 **状态持久** — 自动去重
- 🤖 **智能降级** — API 不可用时自动回退

</td>
<td width="50%">

<img src="assets/fig.png" width="100%" alt="系统架构图">

</td>
</tr>
</table>

---

## 🚀 快速开始

```bash
# 1. 克隆并安装
git clone https://github.com/yourusername/paper_claw.git
cd paper_claw && pip install -r requirements.txt

# 2. 配置
cp .env.example .env
cp config/recipients.example.json config/recipients.json
# 编辑 .env 和 config/recipients.json

# 3. 运行
python scripts/main.py --day 2026-03-10

# 其他常用命令
python scripts/main.py --day 2026-03-10 --no-email  # 只生成本地日报，不发送邮件
python scripts/main.py --day 2026-03-10 --preview    # 预览收件人列表
```

---

## 📂 配置说明

<details>
<summary><b>📁 分类和数据源</b> — 点击展开</summary><br>

编辑 `config/default.json`：

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

**默认分类：**
- 🗣️ Speech LLM — 语音大模型
- 🎤 ASR — 语音识别
- 🔊 TTS — 语音合成
- ✨ Enhancement — 语音增强
- 🧠 SLU — 口语理解
- 😊 Paralinguistics — 副语言学
- 🎵 Audio — 通用音频

</details>

<details>
<summary><b>📧 邮件收件人</b> — 点击展开</summary><br>

编辑 `config/recipients.json`：

```json
{
  "recipients": [
    {"email": "prof@university.edu.cn", "name": "教授", "enabled": true},
    {"email": "student@university.edu.cn", "name": "学生", "enabled": true}
  ]
}
```

可单独启用或禁用每个收件人。

**个性化问候：** 每封邮件将显示个性化问候语：
> 👋 *教授，你好！这是PJ的论文助手为你整理的每日学术日报～*
>
> `name` 字段用于显示问候语，请填写收件人的称呼。

</details>

<details>
<summary><b>🔐 环境变量</b> — 点击展开</summary><br>

创建 `.env` 文件：

```bash
# SMTP 配置（发送邮件必需）
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=你的邮箱@qq.com
SMTP_PASS=你的授权码

# AI API 密钥（可选，用于更好的摘要）
MOONSHOT_API_KEY=sk-你的kimi密钥
OPENAI_API_KEY=sk-你的openai密钥
```

**SMTP 服务商：**

| 邮箱 | 服务器 | 端口 | 说明 |
|------|--------|------|------|
| QQ | smtp.qq.com | 465 | 使用授权码 |
| 163 | smtp.163.com | 465 | 使用授权码 |
| Gmail | smtp.gmail.com | 465 | 使用应用密码 |

</details>

---

## 🤖 AI 中文总结

<details>
<summary><b>🎨 工作原理</b> — 点击展开</summary><br>

**优先级链：** Kimi AI → OpenAI → 规则生成

**Kimi AI**（推荐）：
```bash
MOONSHOT_API_KEY=sk-你的密钥
```
- 原生中文理解能力
- 更好的上下文理解
- 限流时自动重试

**OpenAI**（备选）：
```bash
OPENAI_API_KEY=sk-你的密钥
```

**降级：** 无需 API 密钥，自动使用规则生成中文摘要。

</details>

---

## 🚀 部署方式

<details>
<summary><b>☁️ GitHub Actions（推荐）</b></summary><br>

1. Fork 本仓库
2. 在 Settings → Secrets 中添加：
   - `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`
   - `MOONSHOT_API_KEY` 或 `OPENAI_API_KEY`（可选）
3. 启用 Actions
4. 每日 UTC 01:00（北京时间 09:00）自动运行

</details>

<details>
<summary><b>🖥️ 本地部署</b></summary><br>

**Linux/Mac 定时任务：**
```bash
0 1 * * * cd /path/to/paper_claw && python scripts/main.py
```

**Windows 任务计划：**
```powershell
$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "scripts/main.py"
$Trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
Register-ScheduledTask -TaskName "ArticleClaw" -Action $Action -Trigger $Trigger
```

</details>

---

## 🤖 Agent Skill

<details>
<summary><b>🔧 Skill 接口</b> — 点击展开</summary><br>

**位置：** `skill/` 目录

```python
from skill.example import fetch_papers, get_digest_content

# 抓取论文
result = fetch_papers(day="2026-03-10")

# 获取摘要
content = get_digest_content("2026-03-10", format="summary")
```

**可用工具：**

| 工具 | 说明 |
|------|------|
| `fetch_papers` | 抓取 arXiv 论文 |
| `send_digest` | 发送邮件推送 |
| `configure_categories` | 更新分类配置 |
| `configure_recipients` | 更新收件人 |
| `get_digest_content` | 获取日报内容 |
| `schedule_digest` | 设置定时任务 |

详见 [skill/SKILL.md](skill/SKILL.md) 和 [skill/tools.json](skill/tools.json)。

</details>

---

## 📁 项目结构

```
paper_claw/
├── .github/workflows/      # CI/CD 配置
├── assets/                 # Logo 和图片
├── config/                 # 配置文件
├── content/posts/          # 生成的日报
├── data/                   # 原始和处理后数据
├── scripts/                # 核心脚本
├── skill/                  # Agent Skill 接口
├── templates/              # 邮件模板
├── .env.example            # 环境变量模板
└── examples/               # 示例输出
```

---

## 📖 文档

- [查看示例输出](examples/sample_digest_excerpt.md)
- [Agent Skill 指南](skill/SKILL.md)
- [贡献指南](CONTRIBUTING.md)

---

## 📝 更新日志

### v2.1.0 (2026-03-17)

**新功能：**
- `--no-email` 参数：只生成本地日报，不发送邮件
- `--preview` 参数：发送前预览收件人列表
- 邮件个性化问候语，使用收件人姓名

**Bug 修复：**
- 修复了 LLM 批处理返回值错误，可能导致空结果的问题
- 改进了 API 错误处理和日志记录

---

## 🗺️ 路线图

- [x] Kimi AI 集成
- [x] 多收件人支持
- [x] Agent Skill 接口
- [ ] Web 界面
- [ ] RSS 订阅
- [ ] 多语言支持

---

## 📄 许可证

[MIT License](LICENSE) © 2026 Paper Claw Contributors

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！**

</div>
