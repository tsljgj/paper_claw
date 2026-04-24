<div align="center">

# 📰 Paper Claw

**2026-04-24**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-23 11:59:20 CST → 2026-04-24 12:12:07 CST |
| 📄 论文总数 | **4** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 1 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 3 篇

> 💡 今日共收录 4 篇新论文，主要分布在 ASR 1, Audio 3。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. Time vs. Layer: Locating Predictive Cues for Dysarthric Speech Descriptors in wav2vec 2.0

👤 **作者**: Natalie Engert, Dominik Wagner, Korbinian Riedhammer, Tobias Bocklet
🔗 **来源**: [https://arxiv.org/abs/2604.21628v1](https://arxiv.org/abs/2604.21628v1)

**摘要**
> Wav2vec 2.0 (W2V2) has shown strong performance in pathological speech analysis by effectively capturing the characteristics of atypical speech. Despite its success, it remains unclear which components of its learned representations are most informative for specific downstream tasks. In this study, we address this question by investigating the regression of dysarthric speech descriptors using annotations from the Speech Accessibility Project dataset. We focus on five descriptors, each addressing a different aspect of speech or voice production: intelligibility, imprecise consonants, inappropriate silences, harsh voice and monoloudness. Speech representations are derived from a W2V2-based feature extractor, and we systematically compare layer-wise and time-wise aggregation strategies using attentive statistics pooling. Our results show that intelligibility is best captured through layer-wise representations, whereas imprecise consonants, harsh voice and monoloudness benefit from time-wise modeling. For inappropriate silences, no clear advantage could be observed for either approach.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Time vs. Layer: Locating Predictive Cues for Dysarthric Speech Descriptors in wav2vec 2.0》所界定。 从摘要看，作者主要围绕 wav2vec 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Wav2vec 2.0 (W2V2) has shown strong performance in pathological speech analysis by effectively capturing the characteristics of atypical speech. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：wav2vec。 |

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

### 1. Dilated CNNs for Periodic Signal Processing: A Low-Complexity Approach

👤 **作者**: Eli Gildish, Michael Grebshtein, Igor Makienko
🔗 **来源**: [https://arxiv.org/abs/2604.21651v1](https://arxiv.org/abs/2604.21651v1)

**摘要**
> Denoising of periodic signals and accurate waveform estimation are core tasks across many signal processing domains, including speech, music, medical diagnostics, radio, and sonar. Although deep learning methods have recently shown performance improvements over classical approaches, they require substantial computational resources and are usually trained separately for each signal observation. This study proposes a computationally efficient method based on DCNN and Re-sampling, termed R-DCNN, designed for operation under strict power and resource constraints. The approach targets signals with varying fundamental frequencies and requires only a single observation for training. It generalizes to additional signals via a lightweight resampling step that aligns time scales in signals with different frequencies to re-use the same network weights. Despite its low computational complexity, R-DCNN achieves performance comparable to state-of-the-art classical methods, such as autoregressive (AR)-based techniques, as well as conventional DCNNs trained individually for each observation. This combination of efficiency and performance makes the proposed method particularly well suited for deployment in resource-constrained environments without sacrificing denoising or estimation accuracy.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Dilated CNNs for Periodic Signal Processing: A Low-Complexity Approach》所界定。 从摘要看，作者主要围绕 dilated、cnns、periodic 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Although deep learning methods have recently shown performance improvements over classical approaches, they require substantial computational resources and are usually trained separately for each signal observation. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：dilated, cnns, periodic。 |

---
### 2. PHOTON: Non-Invasive Optical Tracking of Key-Lever Motion in Historical Keyboard Instruments

👤 **作者**: Noah Jaffe, John Ashley Burgoyne
🔗 **来源**: [https://arxiv.org/abs/2604.21682v1](https://arxiv.org/abs/2604.21682v1)

**摘要**
> This paper introduces PHOTON (PHysical Optical Tracking of Notes), a non-invasive optical sensing system for measuring key-lever motion in historical keyboard instruments. PHOTON tracks the vertical displacement of the key lever itself, capturing motion shaped by both performer input and the instrument's mechanically imposed, time-varying load. Reflective optical sensors mounted beneath the distal end of each lever provide continuous displacement, timing, and articulation data without interfering with the action. Unlike existing optical systems designed for modern pianos, PHOTON accommodates the diverse geometries, limited clearances, and non-standard layouts of harpsichords, clavichords, and early fortepianos. Its modular, low-profile architecture enables high-resolution, low-latency sensing across multiple manuals and variable key counts. Beyond performance capture, PHOTON provides real-time MIDI output and supports empirical study of expressive gesture, human-instrument interaction, and the construction of instrument-specific MIDI corpora using real historical mechanisms. The complete system is released as open-source hardware and software, from schematics and PCB layouts developed in KiCad to firmware written in CircuitPython, lowering the barrier to adoption, replication, and extension.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《PHOTON: Non-Invasive Optical Tracking of Key-Lever Motion in Historical Keyboard Instruments》所界定。 从摘要看，作者主要围绕 photon、non-invasive、optical 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：PHOTON tracks the vertical displacement of the key lever itself, capturing motion shaped by both performer input and the instrument's mechanically imposed, time-varying load. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：photon, non-invasive, optical。 |

---
### 3. Beyond Rules: Towards Basso Continuo Personal Style Identification

👤 **作者**: Adam Štefunko, Jan Hajič
🔗 **来源**: [https://arxiv.org/abs/2604.21822v1](https://arxiv.org/abs/2604.21822v1)

**摘要**
> A central part of the contemporary Historically Informed Practice movement is basso continuo, an improvised accompaniment genre with its traditions originating in the baroque era and actively practiced by many keyboard players nowadays. Although computational musicology has studied the theoretical foundations of basso continuo expressed by harmonic and voice-leading rules and constraints, characteristics of basso continuo as an active performing art have been largely overlooked mostly due to a lack of suitable performance data that could be empirically analyzed. This has changed with the introduction of The Aligned Continuo Realization Dataset (ACoRD) and the basso continuo realization-to-score alignment. Basso continuo playing is shaped by stylistic traditions coming from historical treatises, but it also may provide space for showcasing individual performance styles of its practitioners. In this paper, we attempt to explore the question of the presence of personal styles in the basso continuo realizations of players in the ACoRD dataset. We use a historically informed structured representation of basso continuo performance pitch content called griffs and Support Vector Machines to see whether it is possible to classify players based on their performances. The results show that we can identify players from their performances. In addition to the player classification problem, we discuss the elements that make up the individual styles of the players.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Beyond Rules: Towards Basso Continuo Personal Style Identification》所界定。 从摘要看，作者主要围绕 beyond、rules、towards 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：A central part of the contemporary Historically Informed Practice movement is basso continuo, an improvised accompaniment genre with its traditions originating in the baroque era and actively practiced by many keyboard players nowadays. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：beyond, rules, towards。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
