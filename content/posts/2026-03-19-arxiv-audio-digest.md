<div align="center">

# 📰 Paper Claw

**2026-03-19**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-18 11:34:28 CST → 2026-03-19 11:34:27 CST |
| 📄 论文总数 | **3** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 3 篇新论文，主要分布在 Speech LLM 1, Audio 2。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning

👤 **作者**: Donghang Wu, Tianyu Zhang, Yuxin Li, Hexin Liu, Chen Chen, Eng Siong Chng, Yoshua Bengio
🔗 **来源**: [https://arxiv.org/abs/2603.17837v1](https://arxiv.org/abs/2603.17837v1)

**摘要**
> During conversational interactions, humans subconsciously engage in concurrent thinking while listening to a speaker. Although this internal cognitive processing may not always manifest as explicit linguistic structures, it is instrumental in formulating high-quality responses. Inspired by this cognitive phenomenon, we propose a novel Full-duplex LAtent and Internal Reasoning method named FLAIR that conducts latent thinking simultaneously with speech perception. Unlike conventional "thinking" mechanisms in NLP, which require post-hoc generation, our approach aligns seamlessly with spoken dialogue systems: during the user's speaking phase, it recursively feeds the latent embedding output from the previous step into the next step, enabling continuous reasoning that strictly adheres to causality without introducing additional latency. To enable this latent reasoning, we design an Evidence Lower Bound-based objective that supports efficient supervised finetuning via teacher forcing, circumventing the need for explicit reasoning annotations. Experiments demonstrate the effectiveness of this think-while-listening design, which achieves competitive results on a range of speech benchmarks. Furthermore, FLAIR robustly handles conversational dynamics and attains competitive performance on full-duplex interaction metrics.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning》所界定。 从摘要看，作者主要围绕 spoken dialogue、dialogue system 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments demonstrate the effectiveness of this think-while-listening design, which achieves competitive results on a range of speech benchmarks. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：spoken dialogue, dialogue system。 |

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

### 1. Modeling Overlapped Speech with Shuffles

👤 **作者**: Matthew Wiesner, Samuele Cornell, Alexander Polok, Lucas Ondel Yang, Lukáš Burget, Sanjeev Khudanpur
🔗 **来源**: [https://arxiv.org/abs/2603.17769v1](https://arxiv.org/abs/2603.17769v1)

**摘要**
> We propose to model parallel streams of data, such as overlapped speech, using shuffles. Specifically, this paper shows how the shuffle product and partial order finite-state automata (FSAs) can be used for alignment and speaker-attributed transcription of overlapped speech. We train using the total score on these FSAs as a loss function, marginalizing over all possible serializations of overlapping sequences at subword, word, and phrase levels. To reduce graph size, we impose temporal constraints by constructing partial order FSAs. We address speaker attribution by modeling (token, speaker) tuples directly. Viterbi alignment through the shuffle product FSA directly enables one-pass alignment. We evaluate performance on synthetic LibriSpeech overlaps. To our knowledge, this is the first algorithm that enables single-pass alignment of multi-talker recordings. All algorithms are implemented using k2 / Icefall.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Modeling Overlapped Speech with Shuffles》所界定。 从摘要看，作者主要围绕 modeling、overlapped、speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Specifically, this paper shows how the shuffle product and partial order finite-state automata (FSAs) can be used for alignment and speaker-attributed transcription of overlapped speech. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：modeling, overlapped, speech。 |

---
### 2. Multi-Source Evidence Fusion for Audio Question Answering

👤 **作者**: Aivo Olev, Tanel Alumäe
🔗 **来源**: [https://arxiv.org/abs/2603.17822v1](https://arxiv.org/abs/2603.17822v1)

**摘要**
> Large audio language models (LALMs) can answer questions about speech, music, and environmental sounds, yet their internal reasoning is largely opaque and difficult to validate. We describe TalTech's solution to the Agent Track of the Interspeech 2026 Audio Reasoning Challenge, in which systems are evaluated on reasoning process quality, specifically the factual accuracy, logical soundness, and completeness of their reasoning chains. Our multi-source ensemble pipeline uses two LALMs that generate independent observations, while a separate text-only reasoning model cross-checks these against outputs from 25 acoustic tools organized into reliability tiers. By grounding every inference step in explicit, reliability-tagged evidence, the system produces dense, verifiable reasoning chains. Our system ranked first in the challenge, outperforming all competing systems by a wide margin in challenge's reasoning quality metric.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Multi-Source Evidence Fusion for Audio Question Answering》所界定。 从摘要看，作者主要围绕 multi-source、evidence、fusion 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our system ranked first in the challenge, outperforming all competing systems by a wide margin in challenge's reasoning quality metric. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：multi-source, evidence, fusion。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
