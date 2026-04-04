<div align="center">

# 📰 Paper Claw

**2026-04-04**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-02 11:37:26 CST → 2026-04-04 11:27:06 CST |
| 📄 论文总数 | **3** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 1 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 3 篇新论文，主要分布在 ASR 1, Audio 2。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. Tracking the emergence of linguistic structure in self-supervised models learning from speech

👤 **作者**: Marianne de Heer Kloots, Martijn Bentum, Hosein Mohebbi, Charlotte Pouw, Gaofei Shen, Willem Zuidema
🔗 **来源**: [https://arxiv.org/abs/2604.02043v1](https://arxiv.org/abs/2604.02043v1)

**摘要**
> Self-supervised speech models learn effective representations of spoken language, which have been shown to reflect various aspects of linguistic structure. But when does such structure emerge in model training? We study the encoding of a wide range of linguistic structures, across layers and intermediate checkpoints of six Wav2Vec2 and HuBERT models trained on spoken Dutch. We find that different levels of linguistic structure show notably distinct layerwise patterns as well as learning trajectories, which can partially be explained by differences in their degree of abstraction from the acoustic signal and the timescale at which information from the input is integrated. Moreover, we find that the level at which pre-training objectives are defined strongly affects both the layerwise organization and the learning trajectories of linguistic structures, with greater parallelism induced by higher-order prediction tasks (i.e. iteratively refined pseudo-labels).

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Tracking the emergence of linguistic structure in self-supervised models learning from speech》所界定。 从摘要看，作者主要围绕 wav2vec、hubert 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Self-supervised speech models learn effective representations of spoken language, which have been shown to reflect various aspects of linguistic structure. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：wav2vec, hubert。 |

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

### 1. Woosh: A Sound Effects Foundation Model

👤 **作者**: Gaëtan Hadjeres, Marc Ferras, Khaled Koutini, Benno Weck, Alexandre Bittar, Thomas Hummel, Zineb Lahrici, Hakim Missoum, Joan Serrà, Yuki Mitsufuji
🔗 **来源**: [https://arxiv.org/abs/2604.01929v1](https://arxiv.org/abs/2604.01929v1)

**摘要**
> The audio research community depends on open generative models as foundational tools for building novel approaches and establishing baselines. In this report, we present Woosh, Sony AI's publicly released sound effect foundation model, detailing its architecture, training process, and an evaluation against other popular open models. Being optimized for sound effects, we provide (1) a high-quality audio encoder/decoder model and (2) a text-audio alignment model for conditioning, together with (3) text-to-audio and (4) video-to-audio generative models. Distilled text-to-audio and video-to-audio models are also included in the release, allowing for low-resource operation and fast inference. Our evaluation on both public and private data shows competitive or better performance for each module when compared to existing open alternatives like StableAudio-Open and TangoFlux. Inference code and model weights are available at https://github.com/SonyResearch/Woosh. Demo samples can be found at https://sonyresearch.github.io/Woosh/.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Woosh: A Sound Effects Foundation Model》所界定。 从摘要看，作者主要围绕 woosh、sound、effects 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our evaluation on both public and private data shows competitive or better performance for each module when compared to existing open alternatives like StableAudio-Open and TangoFlux. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：woosh, sound, effects。 |

---
### 2. Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations

👤 **作者**: Haitong Sun, Stephen McIntosh, Kwanghee Choi, Eunjung Yeo, Daisuke Saito, Nobuaki Minematsu
🔗 **来源**: [https://arxiv.org/abs/2604.02102v1](https://arxiv.org/abs/2604.02102v1)

**摘要**
> Speech representations from self-supervised speech models (S3Ms) are known to be sensitive to phonemic contrasts, but their sensitivity to prosodic contrasts has not been directly measured. The ABX discrimination task has been used to measure phonemic contrast in S3M representations via minimal pairs. We introduce prosodic ABX, an extension of this framework to evaluate prosodic contrast with only a handful of examples and no explicit labels. Also, we build and release a dataset of English and Japanese minimal pairs and use it along with a Mandarin dataset to evaluate contrast in English stress, Japanese pitch accent, and Mandarin tone. Finally, we show that model and layer rankings are often preserved across several experimental conditions, making it practical for low-resource settings.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations》所界定。 从摘要看，作者主要围绕 prosodic、language-agnostic、method 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Finally, we show that model and layer rankings are often preserved across several experimental conditions, making it practical for low-resource settings. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：prosodic, language-agnostic, method。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
