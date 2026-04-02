<div align="center">

# 📰 Paper Claw

**2026-04-02**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-01 11:56:03 CST → 2026-04-02 11:37:26 CST |
| 📄 论文总数 | **4** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 1 篇
- **TTS**: 0 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 4 篇新论文，主要分布在 ASR 1, Enhancement 1, Audio 2。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. VisG AV-HuBERT: Viseme-Guided AV-HuBERT

👤 **作者**: Aristeidis Papadopoulos, Rishabh Jain, Naomi Harte
🔗 **来源**: [https://arxiv.org/abs/2604.00982v1](https://arxiv.org/abs/2604.00982v1)

**摘要**
> Audio-Visual Speech Recognition (AVSR) systems nowadays integrate Large Language Model (LLM) decoders with transformer-based encoders, achieving state-of-the-art results. However, the relative contributions of improved language modelling versus enhanced audiovisual encoding remain unclear. We propose Viseme-Guided AV-HuBERT (VisG AV-HuBERT), a multi-task fine-tuning framework that incorporates auxiliary viseme classification to strengthen the model's reliance on visual articulatory features. By extending AV-HuBERT with a lightweight viseme prediction sub-network, this method explicitly guides the encoder to preserve visual speech information. Evaluated on LRS3, VisG AV-HuBERT achieves comparable or improved performance over the baseline AV-HuBERT, with notable gains under heavy noise conditions. WER reduces from 13.59% to 6.60% (51.4% relative improvement) at -10 dB Signal-to-Noise Ratio (SNR) for Speech noise. Deeper analysis reveals substantial reductions in substitution errors across noise types, demonstrating improved speech unit discrimination. Evaluation on LRS2 confirms generalization capability. Our results demonstrate that explicit viseme modelling enhances encoder representations, and provides a foundation for enhancing noise-robust AVSR through encoder-level improvements.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《VisG AV-HuBERT: Viseme-Guided AV-HuBERT》所界定。 从摘要看，作者主要围绕 hubert 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Audio-Visual Speech Recognition (AVSR) systems nowadays integrate Large Language Model (LLM) decoders with transformer-based encoders, achieving state-of-the-art results. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：hubert。 |

---
## 🏷️ TTS

> 📭 今日该分类暂无新论文。

---
## 🏷️ Enhancement

### 1. Diff-VS: Efficient Audio-Aware Diffusion U-Net for Vocals Separation

👤 **作者**: Yun-Ning, Hung, Richard Vogl, Filip Korzeniowski, Igor Pereira
🔗 **来源**: [https://arxiv.org/abs/2604.01120v1](https://arxiv.org/abs/2604.01120v1)

**摘要**
> While diffusion models are best known for their performance in generative tasks, they have also been successfully applied to many other tasks, including audio source separation. However, current generative approaches to music source separation often underperform on standard objective metrics. In this paper, we address this issue by introducing a novel generative vocal separation model based on the Elucidated Diffusion Model (EDM) framework. Our model processes complex short-time Fourier transform spectrograms and employs an improved U-Net architecture based on music-informed design choices. Our approach matches discriminative baselines on objective metrics and achieves perceptual quality comparable to state-of-the-art systems, as assessed by proxy subjective metrics. We hope these results encourage broader exploration of generative methods for music source separation

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《Diff-VS: Efficient Audio-Aware Diffusion U-Net for Vocals Separation》所界定。 从摘要看，作者主要围绕 source separation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our model processes complex short-time Fourier transform spectrograms and employs an improved U-Net architecture based on music-informed design choices. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：source separation。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. TRACE: Training-Free Partial Audio Deepfake Detection via Embedding Trajectory Analysis of Speech Foundation Models

👤 **作者**: Awais Khan, Muhammad Umar Farooq, Kutub Uddin, Khalid Malik
🔗 **来源**: [https://arxiv.org/abs/2604.01083v1](https://arxiv.org/abs/2604.01083v1)

**摘要**
> Partial audio deepfakes, where synthesized segments are spliced into genuine recordings, are particularly deceptive because most of the audio remains authentic. Existing detectors are supervised: they require frame-level annotations, overfit to specific synthesis pipelines, and must be retrained as new generative models emerge. We argue that this supervision is unnecessary. We hypothesize that speech foundation models implicitly encode a forensic signal: genuine speech forms smooth, slowly varying embedding trajectories, while splice boundaries introduce abrupt disruptions in frame-level transitions. Building on this, we propose TRACE (Training-free Representation-based Audio Countermeasure via Embedding dynamics), a training-free framework that detects partial audio deepfakes by analyzing the first-order dynamics of frozen speech foundation model representations without any training, labeled data, or architectural modification. We evaluate TRACE on four benchmarks that span two languages using six speech foundation models. In PartialSpoof, TRACE achieves 8.08% EER, competitive with fine-tuned supervised baselines. In LlamaPartialSpoof, the most challenging benchmark featuring LLM-driven commercial synthesis, TRACE surpasses a supervised baseline outright (24.12% vs. 24.49% EER) without any target-domain data. These results show that temporal dynamics in speech foundation models provide an effective, generalize signal for training-free audio forensics.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《TRACE: Training-Free Partial Audio Deepfake Detection via Embedding Trajectory Analysis of Speech Foundation Models》所界定。 从摘要看，作者主要围绕 trace、training-free、partial 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：In PartialSpoof, TRACE achieves 8.08% EER, competitive with fine-tuned supervised baselines. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：trace, training-free, partial。 |

---
### 2. FineLAP: Taming Heterogeneous Supervision for Fine-grained Language-Audio Pretraining

👤 **作者**: Xiquan Li, Xuenan Xu, Ziyang Ma, Wenxi Chen, Haolin He, Qiuqiang Kong, Xie Chen
🔗 **来源**: [https://arxiv.org/abs/2604.01155v1](https://arxiv.org/abs/2604.01155v1)

**摘要**
> Contrastively pretrained audio-language models (e.g., CLAP) excel at clip-level understanding but struggle with frame-level tasks. Existing extensions fail to exploit the varying granularity of real-world audio-text data, where massive clip-level textual descriptions coexist with limited frame-level annotations. This paper proposes Fine-grained Language-Audio Pretraining (FineLAP), a novel training paradigm that advances both clip- and frame-level alignment in CLAP with heterogeneous data. FineLAP introduces a dual-stream sigmoid loss with a cluster-based sampling strategy to jointly learn from clip- and frame-level supervision. To capture both global semantics and local details, FineLAP uses a decoupled audio projector on top of a self-supervised encoder. To alleviate the scarcity of temporally annotated data, we present FineLAP-100k, a large-scale synthetic SED dataset constructed through a scalable curation pipeline. Extensive experiments demonstrate that FineLAP achieves SOTA performance across multiple audio understanding tasks, including retrieval, classification, sound event detection, and text-to-audio grounding. Ablation studies further show that coarse- and fine-grained alignment are mutually beneficial, providing insights for building better audio-language models (ALMs).

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《FineLAP: Taming Heterogeneous Supervision for Fine-grained Language-Audio Pretraining》所界定。 从摘要看，作者主要围绕 audio-language model、sound event detection 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Extensive experiments demonstrate that FineLAP achieves SOTA performance across multiple audio understanding tasks, including retrieval, classification, sound event detection, and text-to-audio grounding. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio-language model, sound event detection。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
