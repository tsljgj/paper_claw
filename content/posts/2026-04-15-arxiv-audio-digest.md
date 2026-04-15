<div align="center">

# 📰 Paper Claw

**2026-04-15**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-14 11:55:37 CST → 2026-04-15 11:54:16 CST |
| 📄 论文总数 | **5** 篇 |

### 分类统计

- **Speech LLM**: 2 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 3 篇

> 💡 今日共收录 5 篇新论文，主要分布在 Speech LLM 2, Audio 3。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models

👤 **作者**: Chung-Ming Chien, Manu Orsini, Eugene Kharitonov, Neil Zeghidour, Karen Livescu, Alexandre Défossez
🔗 **来源**: [https://arxiv.org/abs/2604.12928v1](https://arxiv.org/abs/2604.12928v1)

**摘要**
> Speech-to-speech language models have recently emerged to enhance the naturalness of conversational AI. In particular, full-duplex models are distinguished by their real-time interactivity, including handling of pauses, interruptions, and backchannels. However, improving their factuality remains an open challenge. While scaling the model size could address this gap, it would make real-time inference prohibitively expensive. In this work, we propose MoshiRAG, a modular approach that combines a compact full-duplex interface with selective retrieval to access more powerful knowledge sources. Our asynchronous framework enables the model to identify knowledge-demanding queries and ground its responses in external information. By leveraging the natural temporal gap between response onset and the delivery of core information, the retrieval process can be completed while maintaining a natural conversation flow. With this approach, MoshiRAG achieves factuality comparable to the best publicly released non-duplex speech language models while preserving the interactivity inherent to full-duplex systems. Moreover, our flexible design supports plug-and-play retrieval methods without retraining and demonstrates strong performance on out-of-domain mathematical reasoning tasks.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models》所界定。 从摘要看，作者主要围绕 speech language model 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：However, improving their factuality remains an open challenge. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech language model。 |

---
### 2. SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding

👤 **作者**: Luoyi Sun, Xiao Zhou, Zeqian Li, Ya Zhang, Yanfeng Wang, Weidi Xie
🔗 **来源**: [https://arxiv.org/abs/2604.13023v1](https://arxiv.org/abs/2604.13023v1)

**摘要**
> Large Audio-Language Models (ALMs) have recently demonstrated remarkable capabilities in holistic audio understanding, yet they remain unreliable for temporal grounding, i.e., the task of pinpointing exactly when an event occurs within long-form audio. This limitation stems from two factors: training data dominated by clip-level supervision lacking precise timestamps, and benchmarks that fail to simulate real-world scenarios where short events are obscured by dense background sounds. In this paper, we introduce SpotSound, an audio language model designed for grounding audio events. SpotSound incorporates a novel training objective, specifically designed to suppress hallucinated timestamps for events absent from the input. Additionally, we present SpotSound-Bench, a challenging temporal grounding benchmark where target events occupy less than ~10\% of each clip, creating a rigorous `needle-in-a-haystack' evaluation. Experiments demonstrate that SpotSound achieves state-of-the-art results on temporal grounding benchmarks while maintaining robust performance across general downstream audio-language tasks. Code, models and benchmark are released on https://loiesun.github.io/spotsound/

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding》所界定。 从摘要看，作者主要围绕 audio-language model 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Large Audio-Language Models (ALMs) have recently demonstrated remarkable capabilities in holistic audio understanding, yet they remain unreliable for temporal grounding, i.e., the task of pinpointing exactly when an event occurs within long-form audio. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio-language model。 |

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

### 1. Adaptive Test-Time Scaling for Zero-Shot Respiratory Audio Classification

👤 **作者**: Tsai-Ning Wang, Herman Teun den Dekker, Lin-Lin Chen, Neil Zeghidour, Aaqib Saeed
🔗 **来源**: [https://arxiv.org/abs/2604.12647v1](https://arxiv.org/abs/2604.12647v1)

**摘要**
> Automated respiratory audio analysis promises scalable, non-invasive disease screening, yet progress is limited by scarce labeled data and costly expert annotation. Zero-shot inference eliminates task-specific supervision, but existing methods apply uniform computation to every input regardless of difficulty. We introduce TRIAGE, a tiered zero-shot framework that adaptively scales test-time compute by routing each audio sample through progressively richer reasoning stages: fast label-cosine scoring in a joint audio-text embedding space (Tier-L), structured matching with clinician-style descriptors (Tier-M), and retrieval-augmented large language model reasoning (Tier-H). A confidence-based router finalizes easy predictions early while allocating additional computation to ambiguous inputs, enabling nearly half of all samples to exit at the cheapest tier. Across nine respiratory classification tasks without task-specific training, TRIAGE achieves a mean AUROC of 0.744, outperforming prior zero-shot methods and matching or exceeding supervised baselines on multiple tasks. Our analysis show that test-time scaling concentrates gains where they matter: uncertain cases see up to 19% relative improvement while confident predictions remain unchanged at minimal cost.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Adaptive Test-Time Scaling for Zero-Shot Respiratory Audio Classification》所界定。 从摘要看，作者主要围绕 audio classification 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Across nine respiratory classification tasks without task-specific training, TRIAGE achieves a mean AUROC of 0.744, outperforming prior zero-shot methods and matching or exceeding supervised baselines on multiple tasks. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：audio classification。 |

---
### 2. Transformer Based Machine Fault Detection From Audio Input

👤 **作者**: Kiran Voderhobli Holla
🔗 **来源**: [https://arxiv.org/abs/2604.12733v1](https://arxiv.org/abs/2604.12733v1)

**摘要**
> In recent years, Sound AI is being increasingly used to predict machine failures. By attaching a microphone to the machine of interest, one can get real time data on machine behavior from the field. Traditionally, Convolutional Neural Net (CNN) architectures have been used to analyze spectrogram images generated from the sounds captured and predict if the machine is functioning as expected. CNN architectures seem to work well empirically even though they have biases like locality and parameter-sharing which may not be completely relevant for spectrogram analysis. With the successful application of transformer-based models in the field of image processing starting with Vision Transformer (ViT) in 2020, there has been significant interest in leveraging these in the field of Sound AI. Since transformer-based architectures have significantly lower inductive biases, they are expected to perform better than CNNs at spectrogram analysis given enough data. This paper demonstrates the effectiveness of transformer-driven architectures in analyzing Sound data and compares the embeddings they generate with CNNs on the specific task of machine fault detection.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Transformer Based Machine Fault Detection From Audio Input》所界定。 从摘要看，作者主要围绕 transformer、based、machine 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：This paper demonstrates the effectiveness of transformer-driven architectures in analyzing Sound data and compares the embeddings they generate with CNNs on the specific task of machine fault detection. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：transformer, based, machine。 |

---
### 3. Four Decades of Digital Waveguides

👤 **作者**: Pablo Tablas de Paula, Julius O. Smith, Vesa Välimäki, Joshua D. Reiss
🔗 **来源**: [https://arxiv.org/abs/2604.12878v1](https://arxiv.org/abs/2604.12878v1)

**摘要**
> Digital waveguide physical modeling offers efficient simulation of acoustic wave propagation as compared to general finite-difference schemes commonly used in computational physics. This efficiency has enabled the real-time implementation of physically modeled musical instruments and sound effects, as well as real-time vocal models and artificial reverberation. This paper provides an overview of the historical evolution and applications of digital waveguide modeling and highlights recent advances in the field. Parametric optimization using classical, evolutionary and neural approaches are also discussed and compared. Digital waveguides provide physically accurate simulations with reduced computational cost, and can now be optimized with modern machine learning and differentiable digital signal processing techniques.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Four Decades of Digital Waveguides》所界定。 从摘要看，作者主要围绕 four、decades、digital 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：This efficiency has enabled the real-time implementation of physically modeled musical instruments and sound effects, as well as real-time vocal models and artificial reverberation. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：four, decades, digital。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
