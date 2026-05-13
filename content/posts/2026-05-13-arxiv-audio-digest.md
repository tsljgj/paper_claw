<div align="center">

# 📰 Paper Claw

**2026-05-13**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-05-12 12:29:41 CST → 2026-05-13 12:36:31 CST |
| 📄 论文总数 | **5** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 2 篇
- **TTS**: 0 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 5 篇新论文，主要分布在 ASR 2, Enhancement 1, Audio 2。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. Too Good to Be True: A Study on Modern Automatic Speech Recognition for the Evaluation of Speech Enhancement

👤 **作者**: Danilo de Oliveira, Tal Peer, Timo Gerkmann
🔗 **来源**: [https://arxiv.org/abs/2605.12107v1](https://arxiv.org/abs/2605.12107v1)

**摘要**
> Speech enhancement (SE) systems are typically evaluated using a variety of instrumental metrics. The use of automatic speech recognition (ASR) systems to evaluate SE performance is common in literature, usually in terms of word error rate (WER). However, WER scores depend heavily on the choice of ASR system and text normalization pipeline. In this paper, we investigate how modern ASR models correlate with human recognition of enhanced speech. A listening experiment reveals that modern ASR models with large-scale noisy training and embedded language models correlate more with human WER than simpler ones, with a transducer model providing the most reliable transcriptions. Nevertheless, we also show that these models' robustness to noise and use of context can be uninformative to an acoustics-focused evaluation of enhancement performance.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Too Good to Be True: A Study on Modern Automatic Speech Recognition for the Evaluation of Speech Enhancement》所界定。 从摘要看，作者主要围绕 automatic speech recognition、asr system、speech enhancement 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Nevertheless, we also show that these models' robustness to noise and use of context can be uninformative to an acoustics-focused evaluation of enhancement performance. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：automatic speech recognition, asr system, speech enhancement。 |

---
### 2. A Semi-Supervised Framework for Speech Confidence Detection using Whisper

👤 **作者**: Adam Wynn, Jingyun Wang
🔗 **来源**: [https://arxiv.org/abs/2605.12387v1](https://arxiv.org/abs/2605.12387v1)

**摘要**
> Automatic detection of speaker confidence is critical for adaptive computing but remains constrained by limited labelled data and the subjectivity of paralinguistic annotations. This paper proposes a semi-supervised hybrid framework that fuses deep semantic embeddings from the Whisper encoder with an interpretable acoustic feature vector composed of eGeMAPS descriptors and auxiliary probability estimates of vocal stress and disfluency. To mitigate reliance on scarce ground truth data, we introduce an Uncertainty-Aware Pseudo-Labelling strategy where a model generates labels for unlabelled data, retaining only high-quality samples for training. Experimental results demonstrate that the proposed approach achieves a Macro-F1 score of 0.751, outperforming self-supervised baselines, including WavLM, HuBERT, and Wav2Vec 2.0. The hybrid architecture also surpasses the unimodal Whisper baseline, yielding a 3\% improvement in the minority class, confirming that explicit prosodic and auxiliary features provide necessary corrective signals which are otherwise lost in deep semantic representations. Ablation studies further show that a curated set of high confidence pseudo-labels outperforms indiscriminate large scale augmentation, confirming that data quality outweighs quantity for perceived confidence detection.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《A Semi-Supervised Framework for Speech Confidence Detection using Whisper》所界定。 从摘要看，作者主要围绕 wav2vec、hubert、whisper 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experimental results demonstrate that the proposed approach achieves a Macro-F1 score of 0.751, outperforming self-supervised baselines, including WavLM, HuBERT, and Wav2Vec 2.0. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：wav2vec, hubert, whisper。 |

---
## 🏷️ TTS

> 📭 今日该分类暂无新论文。

---
## 🏷️ Enhancement

### 1. STRUM: A Spectral Transcription and Rhythm Understanding Model for End-to-End Generation of Playable Rhythm-Game Charts

👤 **作者**: Joshua Opria
🔗 **来源**: [https://arxiv.org/abs/2605.12135v1](https://arxiv.org/abs/2605.12135v1)

**摘要**
> We present STRUM (Spectral Transcription and Rhythm Understanding Model), an audio-to-chart pipeline that converts raw recordings into playable Clone Hero / YARG charts for drums, guitar, bass, vocals, and keys without any oracle metadata. STRUM is a multi-stage hybrid: a two-stage CRNN onset detector and a six-model ensemble classifier for drums; neural onset detectors with monophonic pitch tracking for guitar and bass; word-aligned ASR for vocals; and spectral keyboard detection for keys. We evaluate on a 30-song in-envelope benchmark constructed by screening candidate songs on a single audio-quality criterion -- the median 1-second drum-stem RMS after htdemucs_6s source separation. On this benchmark STRUM achieves drums onset F1 = 0.838, bass F1 = 0.694, guitar F1 = 0.651, and vocals F1 = 0.539 at a +/- 100 ms tolerance with per-song global offset search. We report a complete ablation of seven drum-pipeline components with paired per-song Wilcoxon tests, an analysis of ground-truth-to-audio timing distributions in community Clone Hero charts, and a per-class confusion matrix for the drum classifier. Code, model weights, and the full benchmark manifest are released.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《STRUM: A Spectral Transcription and Rhythm Understanding Model for End-to-End Generation of Playable Rhythm-Game Charts》所界定。 从摘要看，作者主要围绕 source separation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：On this benchmark STRUM achieves drums onset F1 = 0.838, bass F1 = 0.694, guitar F1 = 0.651, and vocals F1 = 0.539 at a +/- 100 ms tolerance with per-song global offset search. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：source separation。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. The SMC Blind Spot: A Failure Mode Analysis of State-of-the-Art Beat Tracking

👤 **作者**: Jaehoon Ahn, Tae Gum Hwang, Moon-Ryul Jung
🔗 **来源**: [https://arxiv.org/abs/2605.12287v1](https://arxiv.org/abs/2605.12287v1)

**摘要**
> Over the past two decades, the task of musical beat tracking has transitioned from heuristic onset detection algorithms to highly capable deep neural networks (DNN). Although DNN-based beat tracking models achieve near-perfect performance on mainstream, percussive datasets, the SMC dataset has stubbornly yielded low F-measure scores. By testing how well state-of-the-art models detect beats on individual tracks in the SMC dataset, we identify three distinct failure modes: octave errors, continuity errors, and complete tracking failure where all metrics fall below 0.3. We reveal that state-of-the-art models tend to generate "confident-but-wrong" activations. Furthermore, we show that the standard DBN's default minimum tempo of 55 BPM prevents it from inferring the correct tempo for 21\% of SMC tracks, forcing double-tempo predictions on slow music. By exposing such fundamental oversights, we provide concrete directions for improving beat and downbeat detection, specifically emphasizing training data diversification and multi-hypothesis tempo estimation.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《The SMC Blind Spot: A Failure Mode Analysis of State-of-the-Art Beat Tracking》所界定。 从摘要看，作者主要围绕 blind、spot、failure 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Although DNN-based beat tracking models achieve near-perfect performance on mainstream, percussive datasets, the SMC dataset has stubbornly yielded low F-measure scores. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：blind, spot, failure。 |

---
### 2. Poly-SVC: Polyphony-Aware Singing Voice Conversion with Harmonic Modeling

👤 **作者**: Chen Geng, Meng Chen, Ruohua Zhou, Ruolan Liu, Weifeng Zhao
🔗 **来源**: [https://arxiv.org/abs/2605.12310v1](https://arxiv.org/abs/2605.12310v1)

**摘要**
> Singing Voice Conversion (SVC) aims to transform a source singing voice into a target singer while preserving lyrics and melody. Most existing SVC methods depend on F0 extractors to capture the lead melody from clean vocals. However, no existing method can reliably extract clean vocals from accompanied recordings without leaving residual harmonies behind. In this paper, we innovatively propose Poly-SVC, a zero-shot, cross-lingual singing voice conversion system designed to process residual harmonies. Poly-SVC is composed of three key components: a Constant-Q Transform (CQT)-based pitch extractor to preserve both the lead melody and residual harmony, a random sampler to reduce interference information from the CQT and a diffusion decoder based on Conditional Flow Matching (CFM) that fuses pitch, content, and timbre features into natural-sounding polyphonic outputs. Experiments demonstrate that Poly-SVC surpasses the baseline models in naturalness, timbre similarity and harmony reconstruction across both harmony-rich and single-melody recordings.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Poly-SVC: Polyphony-Aware Singing Voice Conversion with Harmonic Modeling》所界定。 从摘要看，作者主要围绕 poly-svc、polyphony-aware、singing 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments demonstrate that Poly-SVC surpasses the baseline models in naturalness, timbre similarity and harmony reconstruction across both harmony-rich and single-melody recordings. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：poly-svc, polyphony-aware, singing。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
