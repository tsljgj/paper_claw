<div align="center">

# 📰 Paper Claw

**2026-05-15**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-05-14 12:35:01 CST → 2026-05-15 12:41:09 CST |
| 📄 论文总数 | **3** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 2 篇
- **Audio**: 1 篇

> 💡 今日共收录 3 篇新论文，主要分布在 Paralinguistics 2, Audio 1。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

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

### 1. Text-Dependent Speaker Verification (TdSV) Challenge 2024: Team Naive System Report

👤 **作者**: Amir Mohammad Rostami, Pourya Jafarzadeh
🔗 **来源**: [https://arxiv.org/abs/2605.14896v1](https://arxiv.org/abs/2605.14896v1)

**摘要**
> This paper presents a system for the 2024 Text-Dependent Speaker Verification (TdSV) Challenge. The system achieved a Minimum Detection Cost Function (MinDCF) of 0.0461 and an Equal Error Rate (EER) of 1.3\%. Our approach focused on adapting existing state-of-the-art neural networks, ResNet-TDNN and NeXt-TDNN, originally trained on the VoxCeleb dataset. This strategy was chosen because of the limited challenge duration and the available resources at the time. In addition, we designed a lightweight and resource-efficient model, EfficientNet-A0, trained specifically on the challenge dataset to improve adaptation and strengthen the ensemble approach. Our system combines advanced neural architectures, extensive data augmentation, and optimised hyperparameters. These components helped achieve strong performance in text-dependent speaker verification. The results also demonstrate the effectiveness of multi-model ensemble learning for both speaker and phrase verification.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「副语言学」方向，核心任务由题目《Text-Dependent Speaker Verification (TdSV) Challenge 2024: Team Naive System Report》所界定。 从摘要看，作者主要围绕 speaker verification 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The system achieved a Minimum Detection Cost Function (MinDCF) of 0.0461 and an Equal Error Rate (EER) of 1.3\%. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：speaker verification。 |

---
### 2. SpeakerLLM: A Speaker-Specialized Audio-LLM for Speaker Understanding and Verification Reasoning

👤 **作者**: KiHyun Nam, Jungwoo Heo, Siu Bae, Ha-Jin Yu, Joon Son Chung
🔗 **来源**: [https://arxiv.org/abs/2605.15044v1](https://arxiv.org/abs/2605.15044v1)

**摘要**
> As audio-first agents become increasingly common in physical AI, conversational robots, and screenless wearables, audio large language models (audio-LLMs) must integrate speaker-specific understanding to support user authorization, personalization, and context-aware interaction. This requires modeling who is speaking, how the voice sounds, and how recording conditions affect speaker cues. Conventional speaker verification systems provide strong scalar scores but little linguistic evidence, while current audio-LLMs and speaker-aware language models have limited ability to organize speaker information beyond binary labels or descriptive profiles. We present SpeakerLLM, a speaker-specialized audio-LLM framework that unifies single-utterance speaker profiling, recording-condition understanding, utterance-pair speaker comparison, and evidence-organized verification reasoning within a natural-language interface. We construct verification-reasoning targets and a decision-composition policy that separate profile-level evidence from the final same-or-different decision and organize recording condition, profile evidence, and the decision into a structured trace. At its core, SpeakerLLM uses a hierarchical speaker tokenizer designed to capture multiple granularities of speaker evidence. Utterance-level speaker embeddings summarize identity and profile-level cues, whereas frame-level speaker features preserve fine-grained acoustic descriptors. Experiments show that SpeakerLLM-Base improves speaker-profile and recording-condition understanding over general audio-LLMs, while SpeakerLLM-VR preserves strong generated-verdict accuracy and produces decision traces grounded in the supervised verification reasoning schema. We will release the metadata-enriched supervision dataset and target-construction code for reproducibility.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「副语言学」方向，核心任务由题目《SpeakerLLM: A Speaker-Specialized Audio-LLM for Speaker Understanding and Verification Reasoning》所界定。 从摘要看，作者主要围绕 speaker verification 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments show that SpeakerLLM-Base improves speaker-profile and recording-condition understanding over general audio-LLMs, while SpeakerLLM-VR preserves strong generated-verdict accuracy and produces decision traces grounded in the supervised verification reasoning schema. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speaker verification。 |

---
## 🏷️ Audio

### 1. PROCESS-2: A Benchmark Speech Corpus for Early Cognitive Impairment Detection

👤 **作者**: Madhurananda Pahar, Caitlin H. Illingworth, Bahman Mirheidari, Hend Elghazaly, Fritz Peters, Sophie Young, Wing-Zin Leung, Labhpreet Kaur, Daniel Blackburn, Heidi Christensen
🔗 **来源**: [https://arxiv.org/abs/2605.14888v1](https://arxiv.org/abs/2605.14888v1)

**摘要**
> Speech-based analysis offers a scalable and non-invasive approach for detecting cognitive decline, yet progress has been constrained by the limited availability of clinically validated datasets collected under realistic conditions. We introduce PROCESS-2, a large-scale speech dataset designed to support research on automatic assessment of cognitive impairment from spontaneous and task-oriented speech. The dataset comprises recordings from 200 healthy controls, 150 mild cognitive impairment, and 50 dementia diagnoses collected using the CognoMemory digital assessment platform. Each participant completed a single assessment session, including picture description and verbal fluency tasks, accompanied by manually verified transcripts and participant-level metadata. PROCESS-2 contains approximately 21 hours of speech audio with predefined train/test partitions. Comprehensive technical validation evaluated demographic balance, clinical consistency, recording stability, embedding-space structure, and reproducible baseline modelling performance, demonstrating clinically meaningful group separation and stable performance across modelling approaches while preserving real-world conversational variability. PROCESS-2 is released under controlled access via Hugging Face to enable responsible reuse while protecting participant privacy, providing a reproducible benchmark resource for speech-based cognitive assessment research.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《PROCESS-2: A Benchmark Speech Corpus for Early Cognitive Impairment Detection》所界定。 从摘要看，作者主要围绕 process-、benchmark、speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Comprehensive technical validation evaluated demographic balance, clinical consistency, recording stability, embedding-space structure, and reproducible baseline modelling performance, demonstrating clinically meaningful group separation and stable performance across modelling approaches while preserving real-world conversational variability. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：process-, benchmark, speech。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
