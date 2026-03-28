<div align="center">

# 📰 Paper Claw

**2026-03-28**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-26 11:41:57 CST → 2026-03-28 11:29:38 CST |
| 📄 论文总数 | **3** 篇 |

### 分类统计

- **Speech LLM**: 3 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 0 篇

> 💡 今日共收录 3 篇新论文，主要分布在 Speech LLM 3。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. Joint Learning Global-Local Speaker Classification to Enhance End-to-End Speaker Diarization and Recognition

👤 **作者**: Yuhang Dai, Haopeng Lin, Jiale Qian, Ruiqi Yan, Hao Meng, Hanke Xie, Hanlin Wen, Shunshun Yin, Ming Tao, Xie Chen, Lei Xie, Xinsheng Wang
🔗 **来源**: [https://arxiv.org/abs/2603.25377v1](https://arxiv.org/abs/2603.25377v1)

**摘要**
> Large Audio-Language Models (LALMs) have demonstrated remarkable performance in end-to-end speaker diarization and recognition. However, their speaker discriminability remains limited due to the scarcity of large-scale conversational data and the absence of explicit speaker representation optimization. To address this, we propose GLSC-SDR, a paradigm that jointly trains speaker classification with diarization and recognition. We further introduce a Global-Local Speaker Classification strategy, which uses clustered speakers as global labels and re-encoded intra-cluster speakers as local labels. This hierarchical design enhances fine-grained speaker discrimination while preserving semantic transcription accuracy. Experiments on AliMeeting, AISHELL-4, and AMI-SDM demonstrate that GLSC-SDR achieves competitive or superior performance compared to simulation-based and multi-encoder approaches, without relying on large-scale real conversational data.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《Joint Learning Global-Local Speaker Classification to Enhance End-to-End Speaker Diarization and Recognition》所界定。 从摘要看，作者主要围绕 audio-language model 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Large Audio-Language Models (LALMs) have demonstrated remarkable performance in end-to-end speaker diarization and recognition. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio-language model。 |

---
### 2. CoDeTT: A Context-Aware Decision Benchmark for Turn-Taking Evaluation

👤 **作者**: Huan Shen, Yingao Wang, Shangkun Huang, Wei Zou, Yunzhang Chen
🔗 **来源**: [https://arxiv.org/abs/2603.25434v1](https://arxiv.org/abs/2603.25434v1)

**摘要**
> Turn-taking modeling is fundamental to spoken dialogue systems, yet its evaluation remains fragmented and often limited to binary boundary detection under narrow interaction settings. Such protocols hinder systematic comparison and obscure model weaknesses across conversational conditions. We present CoDeTT, a context-aware decision benchmark for turn-taking evaluation. CoDeTT formulates turn-taking as a structured decision problem and constructs a multi-scenario dataset with fine-grained decision categories and controlled context variations. Under a unified evaluation protocol, we assess representative existing models and observe substantial performance disparities across decision types and interaction scenarios. CoDeTT provides a standardized benchmark for systematic and context-aware evaluation of turn-taking systems. The benchmark dataset and evaluation toolkit are available at https://github.com/YingaoWang-casia/CoDeTT.github.io.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《CoDeTT: A Context-Aware Decision Benchmark for Turn-Taking Evaluation》所界定。 从摘要看，作者主要围绕 spoken dialogue、dialogue system 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Such protocols hinder systematic comparison and obscure model weaknesses across conversational conditions. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：spoken dialogue, dialogue system。 |

---
### 3. CLAR: CIF-Localized Alignment for Retrieval-Augmented Speech LLM-Based Contextual ASR

👤 **作者**: Shangkun Huang, Huan Shen, Wei Zou, Yunzhang Chen
🔗 **来源**: [https://arxiv.org/abs/2603.25460v1](https://arxiv.org/abs/2603.25460v1)

**摘要**
> Speech LLM-based ASR often struggles with named entities and long-tail words due to strong internal language-model priors. Retrieval-augmented biasing can help, but its effectiveness depends on accurate hotword localization in full-utterance speech under weak supervision. We propose CLAR, a dual-encoder speech-text retriever that uses Continuous Integrate-and-Fire (CIF) to learn monotonic token-level alignments without timestamps. With length-aware localized matching, CLAR anchors short-entity acoustic cues and reduces representation dilution and attention drift. The retriever is trained with a multi-granularity objective combining global and local segment-level contrastive losses and a CIF quantity constraint. At inference, top-ranked hotwords are injected as contextual prompts for the Speech LLM, improving recognition without shallow fusion. Experiments show that CLAR significantly improves hotword retrieval and reduces both CER and B-WER against strong contextual ASR baselines.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《CLAR: CIF-Localized Alignment for Retrieval-Augmented Speech LLM-Based Contextual ASR》所界定。 从摘要看，作者主要围绕 speech llm 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：At inference, top-ranked hotwords are injected as contextual prompts for the Speech LLM, improving recognition without shallow fusion. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：speech llm。 |

---
## 🏷️ ASR

> 📭 今日该分类暂无新论文。

---
## 🏷️ TTS

> 📭 今日该分类暂无新论文。

---
## 🏷️ Enhancement

> 📭 今日该分类暂无新论文。

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

> 📭 今日该分类暂无新论文。

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
