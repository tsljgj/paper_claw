<div align="center">

# 📰 Paper Claw

**2026-03-26**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-25 11:31:58 CST → 2026-03-26 11:41:57 CST |
| 📄 论文总数 | **7** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 2 篇
- **TTS**: 2 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 1 篇
- **Audio**: 1 篇

> 💡 今日共收录 7 篇新论文，主要分布在 ASR 2, TTS 2, Enhancement 1, Paralinguistics 1, Audio 1。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. Enhancing Efficiency and Performance in Deepfake Audio Detection through Neuron-level dropin & Neuroplasticity Mechanisms

👤 **作者**: Yupei Li, Shuaijie Shao, Manuel Milling, Björn Schuller
🔗 **来源**: [https://arxiv.org/abs/2603.24343v1](https://arxiv.org/abs/2603.24343v1)

**摘要**
> Current audio deepfake detection has achieved remarkable performance using diverse deep learning architectures such as ResNet, and has seen further improvements with the introduction of large models (LMs) like Wav2Vec. The success of large language models (LLMs) further demonstrates the benefits of scaling model parameters, but also highlights one bottleneck where performance gains are constrained by parameter counts. Simply stacking additional layers, as done in current LLMs, is computationally expensive and requires full retraining. Furthermore, existing low-rank adaptation methods are primarily applied to attention-based architectures, which limits their scope. Inspired by the neuronal plasticity observed in mammalian brains, we propose novel algorithms, dropin and further plasticity, that dynamically adjust the number of neurons in certain layers to flexibly modulate model parameters. We evaluate these algorithms on multiple architectures, including ResNet, Gated Recurrent Neural Networks, and Wav2Vec. Experimental results using the widely recognised ASVSpoof2019 LA, PA, and FakeorReal dataset demonstrate consistent improvements in computational efficiency with the dropin approach and a maximum of around 39% and 66% relative reduction in Equal Error Rate with the dropin and plasticity approach among these dataset, respectively. The code and supplementary material are available at Github link.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Enhancing Efficiency and Performance in Deepfake Audio Detection through Neuron-level dropin & Neuroplasticity Mechanisms》所界定。 从摘要看，作者主要围绕 wav2vec 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Current audio deepfake detection has achieved remarkable performance using diverse deep learning architectures such as ResNet, and has seen further improvements with the introduction of large models (LMs) like Wav2Vec. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：wav2vec。 |

---
### 2. A Sociolinguistic Analysis of Automatic Speech Recognition Bias in Newcastle English

👤 **作者**: Dana Serditova, Kevin Tang
🔗 **来源**: [https://arxiv.org/abs/2603.24549v1](https://arxiv.org/abs/2603.24549v1)

**摘要**
> Automatic Speech Recognition (ASR) systems are widely used in everyday communication, education, healthcare, and industry, yet their performance remains uneven across speakers, particularly when dialectal variation diverges from the mainstream accents represented in training data. This study investigates ASR bias through a sociolinguistic analysis of Newcastle English, a regional variety of North-East England that has been shown to challenge current speech recognition technologies. Using spontaneous speech from the Diachronic Electronic Corpus of Tyneside English (DECTE), we evaluate the output of a state-of-the-art commercial ASR system and conduct a fine-grained analysis of more than 3,000 transcription errors. Errors are classified by linguistic domain and examined in relation to social variables including gender, age, and socioeconomic status. In addition, an acoustic case study of selected vowel features demonstrates how gradient phonetic variation contributes directly to misrecognition. The results show that phonological variation accounts for the majority of errors, with recurrent failures linked to dialect-specific features like vowel quality and glottalisation, as well as local vocabulary and non-standard grammatical forms. Error rates also vary across social groups, with higher error frequencies observed for men and for speakers at the extremes of the age spectrum. These findings indicate that ASR errors are not random but socially patterned and can be explained from a sociolinguistic perspective. Thus, the study demonstrates the importance of incorporating sociolinguistic expertise into the evaluation and development of speech technologies and argues that more equitable ASR systems require explicit attention to dialectal variation and community-based speech data.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《A Sociolinguistic Analysis of Automatic Speech Recognition Bias in Newcastle English》所界定。 从摘要看，作者主要围绕 automatic speech recognition、asr system 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：This study investigates ASR bias through a sociolinguistic analysis of Newcastle English, a regional variety of North-East England that has been shown to challenge current speech recognition technologies. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：automatic speech recognition, asr system。 |

---
## 🏷️ TTS

### 1. Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation

👤 **作者**: Shengfan Shen, Di Wu, Xingchen Song, Dinghao Zhou, Liumeng Xue, Meng Meng, Jian Luan, Shuai Wang
🔗 **来源**: [https://arxiv.org/abs/2603.24430v1](https://arxiv.org/abs/2603.24430v1)

**摘要**
> Reliable evaluation of modern zero-shot text-to-speech (TTS) models remains challenging. Subjective tests are costly and hard to reproduce, while objective metrics often saturate, failing to distinguish SOTA systems. To address this, we propose Iterate to Differentiate (I2D), an evaluation framework that recursively synthesizes speech using the model's own outputs as references. Higher-quality models exhibit greater resilience to the distributional shift induced by iterative synthesis, resulting in slower performance degradation. I2D exploits this differential degradation to amplify performance gaps and reveal robustness. By aggregating objective metrics across iterations, I2D improves discriminability and alignment with human judgments, increasing system-level SRCC from 0.118 to 0.464 for UTMOSv2. Experiments on 11 models across Chinese, English, and emotion datasets demonstrate that I2D enables more reliable automated evaluation for zero-shot TTS.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation》所界定。 从摘要看，作者主要围绕 text-to-speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：By aggregating objective metrics across iterations, I2D improves discriminability and alignment with human judgments, increasing system-level SRCC from 0.118 to 0.464 for UTMOSv2. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：text-to-speech。 |

---
### 2. YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance

👤 **作者**: Chunbo Hao, Junjie Zheng, Guobin Ma, Yuepeng Jiang, Huakang Chen, Wenjie Tian, Gongyu Chen, Zihao Chen, Lei Xie
🔗 **来源**: [https://arxiv.org/abs/2603.24589v1](https://arxiv.org/abs/2603.24589v1)

**摘要**
> Regenerating singing voices with altered lyrics while preserving melody consistency remains challenging, as existing methods either offer limited controllability or require laborious manual alignment. We propose YingMusic-Singer, a fully diffusion-based model enabling melody-controllable singing voice synthesis with flexible lyric manipulation. The model takes three inputs: an optional timbre reference, a melody-providing singing clip, and modified lyrics, without manual alignment. Trained with curriculum learning and Group Relative Policy Optimization, YingMusic-Singer achieves stronger melody preservation and lyric adherence than Vevo2, the most comparable baseline supporting melody control without manual alignment. We also introduce LyricEditBench, the first benchmark for melody-preserving lyric modification evaluation. The code, weights, benchmark, and demos are publicly available at https://github.com/ASLP-lab/YingMusic-Singer.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance》所界定。 从摘要看，作者主要围绕 voice synthesis 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Trained with curriculum learning and Group Relative Policy Optimization, YingMusic-Singer achieves stronger melody preservation and lyric adherence than Vevo2, the most comparable baseline supporting melody control without manual alignment. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：voice synthesis。 |

---
## 🏷️ Enhancement

### 1. ArrayDPS-Refine: Generative Refinement of Discriminative Multi-Channel Speech Enhancement

👤 **作者**: Zhongweiyang Xu, Ashutosh Pandey, Juan Azcarreta, Zhaoheng Ni, Sanjeel Parekh, Buye Xu
🔗 **来源**: [https://arxiv.org/abs/2603.24385v1](https://arxiv.org/abs/2603.24385v1)

**摘要**
> Multi-channel speech enhancement aims to recover clean speech from noisy multi-channel recordings. Most deep learning methods employ discriminative training, which can lead to non-linear distortions from regression-based objectives, especially under challenging environmental noise conditions. Inspired by ArrayDPS for unsupervised multi-channel source separation, we introduce ArrayDPS-Refine, a method designed to enhance the outputs of discriminative models using a clean speech diffusion prior. ArrayDPS-Refine is training-free, generative, and array-agnostic. It first estimates the noise spatial covariance matrix (SCM) from the enhanced speech produced by a discriminative model, then uses this estimated noise SCM for diffusion posterior sampling. This approach allows direct refinement of any discriminative model's output without retraining. Our results show that ArrayDPS-Refine consistently improves the performance of various discriminative models, including state-of-the-art waveform and STFT domain models. Audio demos are provided at https://xzwy.github.io/ArrayDPSRefineDemo/.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《ArrayDPS-Refine: Generative Refinement of Discriminative Multi-Channel Speech Enhancement》所界定。 从摘要看，作者主要围绕 speech enhancement、source separation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our results show that ArrayDPS-Refine consistently improves the performance of various discriminative models, including state-of-the-art waveform and STFT domain models. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech enhancement, source separation。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

### 1. What and When to Learn: CURriculum Ranking Loss for Large-Scale Speaker Verification

👤 **作者**: Massa Baali, Sarthak Bisht, Rita Singh, Bhiksha Raj
🔗 **来源**: [https://arxiv.org/abs/2603.24432v1](https://arxiv.org/abs/2603.24432v1)

**摘要**
> Speaker verification at large scale remains an open challenge as fixed-margin losses treat all samples equally regardless of quality. We hypothesize that mislabeled or degraded samples introduce noisy gradients that disrupt compact speaker manifolds. We propose Curry (CURriculum Ranking), an adaptive loss that estimates sample difficulty online via Sub-center ArcFace: confidence scores from dominant sub-center cosine similarity rank samples into easy, medium, and hard tiers using running batch statistics, without auxiliary annotations. Learnable weights guide the model from stable identity foundations through manifold refinement to boundary sharpening. To our knowledge, this is the largest-scale speaker verification system trained to date. Evaluated on VoxCeleb1-O, and SITW, Curry reduces EER by 86.8\% and 60.0\% over the Sub-center ArcFace baseline, establishing a new paradigm for robust speaker verification on imperfect large-scale data.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「副语言学」方向，核心任务由题目《What and When to Learn: CURriculum Ranking Loss for Large-Scale Speaker Verification》所界定。 从摘要看，作者主要围绕 speaker verification 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We hypothesize that mislabeled or degraded samples introduce noisy gradients that disrupt compact speaker manifolds. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：speaker verification。 |

---
## 🏷️ Audio

### 1. Bridging Biological Hearing and Neuromorphic Computing: End-to-End Time-Domain Audio Signal Processing with Reservoir Computing

👤 **作者**: Rinku Sebastian, Simon O'Keefe, Martin Trefzer
🔗 **来源**: [https://arxiv.org/abs/2603.24283v1](https://arxiv.org/abs/2603.24283v1)

**摘要**
> Despite the advancements in cutting-edge technologies, audio signal processing continues to pose challenges and lacks the precision of a human speech processing system. To address these challenges, we propose a novel approach to simplify audio signal processing by leveraging time-domain techniques and reservoir computing. Through our research, we have developed a real-time audio signal processing system by simplifying audio signal processing through the utilization of reservoir computers, which are significantly easier to train. Feature extraction is a fundamental step in speech signal processing, with Mel Frequency Cepstral Coefficients (MFCCs) being a dominant choice due to their perceptual relevance to human hearing. However, conventional MFCC extraction relies on computationally intensive time-frequency transformations, limiting efficiency in real-time applications. To address this, we propose a novel approach that leverages reservoir computing to streamline MFCC extraction. By replacing traditional frequency-domain conversions with convolution operations, we eliminate the need for complex transformations while maintaining feature discriminability. We present an end-to-end audio processing framework that integrates this method, demonstrating its potential for efficient and real-time speech analysis. Our results contribute to the advancement of energy-efficient audio processing technologies, enabling seamless deployment in embedded systems and voice-driven applications. This work bridges the gap between biologically inspired feature extraction and modern neuromorphic computing, offering a scalable solution for next-generation speech recognition systems.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Bridging Biological Hearing and Neuromorphic Computing: End-to-End Time-Domain Audio Signal Processing with Reservoir Computing》所界定。 从摘要看，作者主要围绕 bridging、biological、hearing 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We present an end-to-end audio processing framework that integrates this method, demonstrating its potential for efficient and real-time speech analysis. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：bridging, biological, hearing。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
