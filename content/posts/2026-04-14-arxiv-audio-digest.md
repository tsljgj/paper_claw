<div align="center">

# 📰 Paper Claw

**2026-04-14**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-13 12:14:22 CST → 2026-04-14 11:55:37 CST |
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

### 1. MimicLM: Zero-Shot Voice Imitation through Autoregressive Modeling of Pseudo-Parallel Speech Corpora

👤 **作者**: Tao Feng, Yuxiang Wang, Yuancheng Wang, Xueyao Zhang, Dekun Chen, Chaoren Wang, Xun Guan, Zhizheng Wu
🔗 **来源**: [https://arxiv.org/abs/2604.11552v1](https://arxiv.org/abs/2604.11552v1)

**摘要**
> Voice imitation aims to transform source speech to match a reference speaker's timbre and speaking style while preserving linguistic content. A straightforward approach is to train on triplets of (source, reference, target), where source and target share the same content but target matches the reference's voice characteristics, yet such data is extremely scarce. Existing approaches either employ carefully designed disentanglement architectures to bypass this data scarcity or leverage external systems to synthesize pseudo-parallel training data. However, the former requires intricate model design, and the latter faces a quality ceiling when synthetic speech is used as training targets. To address these limitations, we propose MimicLM, which takes a novel approach by using synthetic speech as training sources while retaining real recordings as targets. This design enables the model to learn directly from real speech distributions, breaking the synthetic quality ceiling. Building on this data construction approach, we incorporate interleaved text-audio modeling to guide the generation of content-accurate speech and apply post-training with preference alignment to mitigate the inherent distributional mismatch when training on synthetic data. Experiments demonstrate that MimicLM achieves superior voice imitation quality with a simple yet effective architecture, significantly outperforming existing methods in naturalness while maintaining competitive similarity scores across speaker identity, accent, and emotion dimensions.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《MimicLM: Zero-Shot Voice Imitation through Autoregressive Modeling of Pseudo-Parallel Speech Corpora》所界定。 从摘要看，作者主要围绕 mimiclm、zero-shot、voice 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments demonstrate that MimicLM achieves superior voice imitation quality with a simple yet effective architecture, significantly outperforming existing methods in naturalness while maintaining competitive similarity scores across speaker identity, accent, and emotion dimensions. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：mimiclm, zero-shot, voice。 |

---
### 2. HumDial-EIBench: A Human-Recorded Multi-Turn Emotional Intelligence Benchmark for Audio Language Models

👤 **作者**: Shuiyuan Wang, Zhixian Zhao, Hongfei Yue, Chengyou Wang, Shuai Wang, Hui Bu, Xin Xu, Lei Xie
🔗 **来源**: [https://arxiv.org/abs/2604.11594v1](https://arxiv.org/abs/2604.11594v1)

**摘要**
> Evaluating the emotional intelligence (EI) of audio language models (ALMs) is critical. However, existing benchmarks mostly rely on synthesized speech, are limited to single-turn interactions, and depend heavily on open-ended scoring. This paper proposes HumDial-EIBench, a comprehensive benchmark for evaluating ALMs' EI. Using real-recorded human dialogues from the ICASSP 2026 HumDial Challenge, it reformulates emotional tracking and causal reasoning into multiple-choice questions with adversarial distractors, mitigating subjective scoring bias for cognitive tasks. It retains the generation of empathetic responses and introduces an acoustic-semantic conflict task to assess robustness against contradictory multimodal signals. Evaluations of eight ALMs reveal that most models struggle with multi-turn emotional tracking and implicit causal reasoning. Furthermore, all models exhibit decoupled textual and acoustic empathy, alongside a severe text-dominance bias during cross-modal conflicts.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《HumDial-EIBench: A Human-Recorded Multi-Turn Emotional Intelligence Benchmark for Audio Language Models》所界定。 从摘要看，作者主要围绕 humdial-eibench、human-recorded、multi-turn 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：However, existing benchmarks mostly rely on synthesized speech, are limited to single-turn interactions, and depend heavily on open-ended scoring. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：humdial-eibench, human-recorded, multi-turn。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
