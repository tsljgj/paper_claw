<div align="center">

# 📰 Paper Claw

**2026-05-14**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-05-13 12:36:31 CST → 2026-05-14 12:35:01 CST |
| 📄 论文总数 | **2** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 2 篇新论文，主要分布在 Audio 2。
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

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating

👤 **作者**: Zhongju Yuan, Geraint Wiggins, Dick Botteldooren
🔗 **来源**: [https://arxiv.org/abs/2605.13651v1](https://arxiv.org/abs/2605.13651v1)

**摘要**
> Audio provides critical situational cues, yet current Audio Language Models (ALMs) face an attention bottleneck in long-form recordings where dominant background patterns can dilute rare, salient events. We introduce NAACA, a training-free NeuroAuditory Attentive Cognitive Architecture that reframes attention allocation as an auditory salience filtering problem. At its core is OWM, a neuro-inspired Oscillatory Working Memory that maintains stable attractor-like states and triggers higher-cognition ALM processing only when adaptive energy fluctuations signal perceptual salience, triggering higher-level reasoning. On XD-Violence, NAACA improves AudioQwen's average precision (AP) from 53.50% to 70.60% while reducing unnecessary ALM invocations. Furthermore, qualitative case studies on the Urban Soundscapes of the World (USoW) dataset show that OWM captures novel events and subcategory shifts while remaining robust to transient pauses and ambient urban noise.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating》所界定。 从摘要看，作者主要围绕 naaca、training-free、neuroauditory 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：On XD-Violence, NAACA improves AudioQwen's average precision (AP) from 53.50% to 70.60% while reducing unnecessary ALM invocations. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：naaca, training-free, neuroauditory。 |

---
### 2. EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents

👤 **作者**: Tara Bogavelli, Gabrielle Gauthier Melançon, Katrina Stankiewicz, Oluwanifemi Bamgbose, Fanny Riols, Hoang H. Nguyen, Raghav Mehndiratta, Lindsay Devon Brin, Joseph Marinier, Hari Subramani, Anil Madamala, Sridhar Krishna Nemala, Srinivas Sunkara
🔗 **来源**: [https://arxiv.org/abs/2605.13841v1](https://arxiv.org/abs/2605.13841v1)

**摘要**
> Voice agents, artificial intelligence systems that conduct spoken conversations to complete tasks, are increasingly deployed across enterprise applications. However, no existing benchmark jointly addresses two core evaluation challenges: generating realistic simulated conversations, and measuring quality across the full scope of voice-specific failure modes. We present EVA-Bench, an end-to-end evaluation framework that addresses both. On the simulation side, EVA-Bench orchestrates bot-to-bot audio conversations over dynamic multi-turn dialogues, with automatic simulation validation that detects user simulator error and appropriately regenerates conversations before scoring. On the measurement side, EVA-Bench introduces two composite metrics: EVA-A (Accuracy), capturing task completion, faithfulness, and audio-level speech fidelity; and EVA-X (Experience), capturing conversation progression, spoken conciseness, and turn-taking timing. Both metrics apply to different agent architectures, enabling direct cross-architecture comparison. EVA-Bench includes 213 scenarios across three enterprise domains, a controlled perturbation suite for accent and noise robustness, and pass@1, pass@k, pass^k measurements that distinguish peak from reliable capability. Across 12 systems spanning all three architectures, we find: (1) no system simultaneously exceeds 0.5 on both EVA-A pass@1 and EVA-X pass@1; (2) peak and reliable performance diverge substantially (median pass@k - pass^k gap of 0.44 on EVA-A); and (3) accent and noise perturbations expose substantial robustness gaps, with effects varying across architectures, systems, and metrics (mean up to 0.314). We release the full framework, evaluation suite, and benchmark data under an open-source license.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents》所界定。 从摘要看，作者主要围绕 eva-bench、end-to-end、framework 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：However, no existing benchmark jointly addresses two core evaluation challenges: generating realistic simulated conversations, and measuring quality across the full scope of voice-specific failure modes. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：eva-bench, end-to-end, framework。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
