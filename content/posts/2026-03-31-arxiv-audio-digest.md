<div align="center">

# 📰 Paper Claw

**2026-03-31**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-28 11:29:38 CST → 2026-03-31 11:44:33 CST |
| 📄 论文总数 | **20** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 3 篇
- **TTS**: 1 篇
- **Enhancement**: 3 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 12 篇

> 💡 今日共收录 20 篇新论文，主要分布在 Speech LLM 1, ASR 3, TTS 1, Enhancement 3, Audio 12。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. HumMusQA: A Human-written Music Understanding QA Benchmark Dataset

👤 **作者**: Benno Weck, Pablo Puentes, Andrea Poltronieri, Satyajeet Prabhu, Dmitry Bogdanov
🔗 **来源**: [https://arxiv.org/abs/2603.27877v1](https://arxiv.org/abs/2603.27877v1)

**摘要**
> The evaluation of music understanding in Large Audio-Language Models (LALMs) requires a rigorously defined benchmark that truly tests whether models can perceive and interpret music, a standard that current data methodologies frequently fail to meet. This paper introduces a meticulously structured approach to music evaluation, proposing a new dataset of 320 hand-written questions curated and validated by experts with musical training, arguing that such focused, manual curation is superior for probing complex audio comprehension. To demonstrate the use of the dataset, we benchmark six state-of-the-art LALMs and additionally test their robustness to uni-modal shortcuts.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《HumMusQA: A Human-written Music Understanding QA Benchmark Dataset》所界定。 从摘要看，作者主要围绕 audio-language model 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：To demonstrate the use of the dataset, we benchmark six state-of-the-art LALMs and additionally test their robustness to uni-modal shortcuts. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio-language model。 |

---
## 🏷️ ASR

### 1. Investigation on the Robustness of Acoustic Foundation Models on Post Exercise Speech

👤 **作者**: Xiangyuan Xue, Yuyu Wang, Ruijie Yao, Xiaoyue Ni, Xiaofan Jiang, Jingping Nie
🔗 **来源**: [https://arxiv.org/abs/2603.27508v1](https://arxiv.org/abs/2603.27508v1)

**摘要**
> Automatic speech recognition (ASR) has been extensively studied on neutral and stationary speech, yet its robustness under post-exercise physiological shift remains underexplored. Compared with resting speech, post-exercise speech often contains micro-breaths, non-semantic pauses, unstable phonation, and repetitions caused by reduced breath support, making transcription more difficult. In this work, we benchmark acoustic foundation models on post-exercise speech under a unified evaluation protocol. We compare sequence-to-sequence models (Whisper and FunASR/Paraformer) and self-supervised encoders with CTC decoding (Wav2Vec2, HuBERT, and WavLM), under both off-the-shelf inference and post-exercise in-domain fine-tuning. Across the Static/Post-All benchmark, most models degrade on post-exercise speech, while FunASR shows the strongest baseline robustness at 14.57% WER and 8.21% CER on Post-All. Fine-tuning substantially improves several CTC-based models, whereas Whisper shows unstable adaptation. As an exploratory case study, we further stratify results by fluent and non-fluent speakers; although the non-fluent subset is small, it is consistently more challenging than the fluent subset. Overall, our findings show that post-exercise ASR robustness is strongly model-dependent, that in-domain adaptation can be highly effective but not uniformly stable, and that future post-exercise ASR studies should explicitly separate fluency-related effects from exercise-induced speech variation.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Investigation on the Robustness of Acoustic Foundation Models on Post Exercise Speech》所界定。 从摘要看，作者主要围绕 automatic speech recognition、wav2vec、hubert 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Across the Static/Post-All benchmark, most models degrade on post-exercise speech, while FunASR shows the strongest baseline robustness at 14.57% WER and 8.21% CER on Post-All. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：automatic speech recognition, wav2vec, hubert。 |

---
### 2. On the Role of Encoder Depth: Pruning Whisper and LoRA Fine-Tuning in SLAM-ASR

👤 **作者**: Ganesh Pavan Kartikeya Bharadwaj Kolluri, Michael Kampouridis, Ravi Shekhar
🔗 **来源**: [https://arxiv.org/abs/2603.27981v1](https://arxiv.org/abs/2603.27981v1)

**摘要**
> Automatic speech recognition (ASR) has advanced rapidly in recent years, driven by large-scale pretrained models and end-to-end architectures such as SLAM-ASR. A key component of SLAM-ASR systems is the Whisper speech encoder, which provides robust acoustic representations. While model pruning has been explored for the full Whisper encoder-decoder architecture, its impact within the SLAM-ASR setting remains under-investigated. In this work, we analyze the effects of layer pruning in the Whisper encoder when used as the acoustic backbone of SLAM-ASR. We further examine the extent to which LoRA-based fine-tuning can recover performance degradation caused by pruning. Experiments conducted across three Whisper variants (Small, Medium, Large-v2), three languages representing distinct resource levels (Danish, Dutch, English), and over 200 training runs demonstrate that pruning two encoder layers causes only 2-4% WER degradation, and that combining this pruning with LoRA adaptation consistently outperforms the unpruned baseline while reducing total parameters by 7-14%. Moreover, our error analysis reveals that LoRA primarily compensates through the language model's linguistic priors, reducing total word errors by 11-21% for Dutch and English, with substitutions and deletions showing the largest reductions. However, for low-resource Danish, the reduction is smaller (4-7%), and LoRA introduces increased insertion errors, indicating that compensation effectiveness depends on the LLM's pre-existing language proficiency and available training data.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《On the Role of Encoder Depth: Pruning Whisper and LoRA Fine-Tuning in SLAM-ASR》所界定。 从摘要看，作者主要围绕 automatic speech recognition、asr system、whisper 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments conducted across three Whisper variants (Small, Medium, Large-v2), three languages representing distinct resource levels (Danish, Dutch, English), and over 200 training runs demonstrate that pruning two encoder layers causes only 2-4% WER degradation, and that combining this pruning with LoRA adaptation consistently outperforms the unpruned baseline while reducing total parameters by 7-14%. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：automatic speech recognition, asr system, whisper。 |

---
### 3. Acoustic-to-articulatory Inversion of the Complete Vocal Tract from RT-MRI with Various Audio Embeddings and Dataset Sizes

👤 **作者**: Sofiane Azzouz, Pierre-André Vuissoz, Yves Laprie
🔗 **来源**: [https://arxiv.org/abs/2603.28723v1](https://arxiv.org/abs/2603.28723v1)

**摘要**
> Articulatory-to-acoustic inversion strongly depends on the type of data used. While most previous studies rely on EMA, which is limited by the number of sensors and restricted to accessible articulators, we propose an approach aiming at a complete inversion of the vocal tract, from the glottis to the lips. To this end, we used approximately 3.5 hours of RT-MRI data from a single speaker. The innovation of our approach lies in the use of articulator contours automatically extracted from MRI images, rather than relying on the raw images themselves. By focusing on these contours, the model prioritizes the essential geometric dynamics of the vocal tract while discarding redundant pixel-level information. These contours, alongside denoised audio, were then processed using a Bi-LSTM architecture. Two experiments were conducted: (1) the analysis of the impact of the audio embedding, for which three types of embeddings were evaluated as input to the model (MFCCs, LCCs, and HuBERT), and (2) the study of the influence of the dataset size, which we varied from 10 minutes to 3.5 hours. Evaluation was performed on the test data using RMSE, median error, as well as Tract Variables, to which we added an additional measurement: the larynx height. The average RMSE obtained is 1.48\,mm, compared with the pixel size (1.62\,mm). These results confirm the feasibility of a complete vocal-tract inversion using RT-MRI data.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Acoustic-to-articulatory Inversion of the Complete Vocal Tract from RT-MRI with Various Audio Embeddings and Dataset Sizes》所界定。 从摘要看，作者主要围绕 hubert 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：While most previous studies rely on EMA, which is limited by the number of sensors and restricted to accessible articulators, we propose an approach aiming at a complete inversion of the vocal tract, from the glottis to the lips. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：hubert。 |

---
## 🏷️ TTS

### 1. MOSS-VoiceGenerator: Create Realistic Voices with Natural Language Descriptions

👤 **作者**: Kexin Huang, Liwei Fan, Botian Jiang, Yaozhou Jiang, Qian Tu, Jie Zhu, Yuqian Zhang, Yiwei Zhao, Chenchen Yang, Zhaoye Fei, Shimin Li, Xiaogui Yang, Qinyuan Cheng, Xipeng Qiu
🔗 **来源**: [https://arxiv.org/abs/2603.28086v1](https://arxiv.org/abs/2603.28086v1)

**摘要**
> Voice design from natural language aims to generate speaker timbres directly from free-form textual descriptions, allowing users to create voices tailored to specific roles, personalities, and emotions. Such controllable voice creation benefits a wide range of downstream applications-including storytelling, game dubbing, role-play agents, and conversational assistants, making it a significant task for modern Text-to-Speech models. However, existing models are largely trained on carefully recorded studio data, which produces speech that is clean and well-articulated, yet lacks the lived-in qualities of real human voices. To address these limitations, we present MOSS-VoiceGenerator, an open-source instruction-driven voice generation model that creates new timbres directly from natural language prompts. Motivated by the hypothesis that exposure to real-world acoustic variation produces more perceptually natural voices, we train on large-scale expressive speech data sourced from cinematic content. Subjective preference studies demonstrate its superiority in overall performance, instruction-following, and naturalness compared to other voice design models.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《MOSS-VoiceGenerator: Create Realistic Voices with Natural Language Descriptions》所界定。 从摘要看，作者主要围绕 text-to-speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Subjective preference studies demonstrate its superiority in overall performance, instruction-following, and naturalness compared to other voice design models. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：text-to-speech。 |

---
## 🏷️ Enhancement

### 1. On the Usefulness of Diffusion-Based Room Impulse Response Interpolation to Microphone Array Processing

👤 **作者**: Sagi Della Torre, Mirco Pezzoli, Fabio Antonacci, Sharon Gannot
🔗 **来源**: [https://arxiv.org/abs/2603.28209v1](https://arxiv.org/abs/2603.28209v1)

**摘要**
> Room Impulse Responses estimation is a fundamental problem in spatial audio processing and speech enhancement. In this paper, we build upon our previously introduced diffusion-based inpainting framework for Room Impulse Response interpolation and demonstrate its applicability to enhancing the performance of practical multi-microphone array processing tasks. Furthermore, we validate the robustness of this method in interpolating real-world Room Impulse Responses.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《On the Usefulness of Diffusion-Based Room Impulse Response Interpolation to Microphone Array Processing》所界定。 从摘要看，作者主要围绕 speech enhancement 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：In this paper, we build upon our previously introduced diffusion-based inpainting framework for Room Impulse Response interpolation and demonstrate its applicability to enhancing the performance of practical multi-microphone array processing tasks. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech enhancement。 |

---
### 2. A Probabilistic Generative Model for Spectral Speech Enhancement

👤 **作者**: Marco Hidalgo-Araya, Raphaël Trésor, Bart Van Erp, Wouter W. L. Nuijten, Thijs Van De Laar, Bert De Vries
🔗 **来源**: [https://arxiv.org/abs/2603.28436v1](https://arxiv.org/abs/2603.28436v1)

**摘要**
> Speech enhancement in hearing aids remains a difficult task in nonstationary acoustic environments, mainly because current signal processing algorithms rely on fixed, manually tuned parameters that cannot adapt in situ to different users or listening contexts. This paper introduces a unified modular framework that formulates signal processing, learning, and personalization as Bayesian inference with explicit uncertainty tracking. The proposed framework replaces ad hoc algorithm design with a single probabilistic generative model that continuously adapts to changing acoustic conditions and user preferences. It extends spectral subtraction with principled mechanisms for in-situ personalization and adaptation to acoustic context. The system is implemented as an interconnected probabilistic state-space model, and inference is performed via variational message passing in the \texttt{RxInfer.jl} probabilistic programming environment, enabling real-time Bayesian processing under hearing-aid constraints. Proof-of-concept experiments on the \emph{VoiceBank+DEMAND} corpus show competitive speech quality and noise reduction with 85 effective parameters. The framework provides an interpretable, data-efficient foundation for uncertainty-aware, adaptive hearing-aid processing and points toward devices that learn continuously through probabilistic inference.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《A Probabilistic Generative Model for Spectral Speech Enhancement》所界定。 从摘要看，作者主要围绕 speech enhancement、noise reduction 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Proof-of-concept experiments on the \emph{VoiceBank+DEMAND} corpus show competitive speech quality and noise reduction with 85 effective parameters. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech enhancement, noise reduction。 |

---
### 3. SonoWorld: From One Image to a 3D Audio-Visual Scene

👤 **作者**: Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao
🔗 **来源**: [https://arxiv.org/abs/2603.28757v1](https://arxiv.org/abs/2603.28757v1)

**摘要**
> Tremendous progress in visual scene generation now turns a single image into an explorable 3D world, yet immersion remains incomplete without sound. We introduce Image2AVScene, the task of generating a 3D audio-visual scene from a single image, and present SonoWorld, the first framework to tackle this challenge. From one image, our pipeline outpaints a 360° panorama, lifts it into a navigable 3D scene, places language-guided sound anchors, and renders ambisonics for point, areal, and ambient sources, yielding spatial audio aligned with scene geometry and semantics. Quantitative evaluations on a newly curated real-world dataset and a controlled user study confirm the effectiveness of our approach. Beyond free-viewpoint audio-visual rendering, we also demonstrate applications to one-shot acoustic learning and audio-visual spatial source separation. Project website: https://humathe.github.io/sonoworld/

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《SonoWorld: From One Image to a 3D Audio-Visual Scene》所界定。 从摘要看，作者主要围绕 source separation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Beyond free-viewpoint audio-visual rendering, we also demonstrate applications to one-shot acoustic learning and audio-visual spatial source separation. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：source separation。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. TokenDance: Token-to-Token Music-to-Dance Generation with Bidirectional Mamba

👤 **作者**: Ziyue Yang, Kaixing Yang, Xulong Tang
🔗 **来源**: [https://arxiv.org/abs/2603.27314v1](https://arxiv.org/abs/2603.27314v1)

**摘要**
> Music-to-dance generation has broad applications in virtual reality, dance education, and digital character animation. However, the limited coverage of existing 3D dance datasets confines current models to a narrow subset of music styles and choreographic patterns, resulting in poor generalization to real-world music. Consequently, generated dances often become overly simplistic and repetitive, substantially degrading expressiveness and realism. To tackle this problem, we present TokenDance, a two-stage music-to-dance generation framework that explicitly addresses this limitation through dual-modality tokenization and efficient token-level generation. In the first stage, we discretize both dance and music using Finite Scalar Quantization, where dance motions are factorized into upper and lower-body components with kinematic-dynamic constraints, and music is decomposed into semantic and acoustic features with dedicated codebooks to capture choreography-specific structures. In the second stage, we introduce a Local-Global-Local token-to-token generator built on a Bidirectional Mamba backbone, enabling coherent motion synthesis, strong music-dance alignment, and efficient non-autoregressive inference. Extensive experiments demonstrate that TokenDance achieves overall state-of-the-art (SOTA) performance in both generation quality and inference speed, highlighting its effectiveness and practical value for real-world music-to-dance applications.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《TokenDance: Token-to-Token Music-to-Dance Generation with Bidirectional Mamba》所界定。 从摘要看，作者主要围绕 tokendance、token-to-token、music-to-dance 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Extensive experiments demonstrate that TokenDance achieves overall state-of-the-art (SOTA) performance in both generation quality and inference speed, highlighting its effectiveness and practical value for real-world music-to-dance applications. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：tokendance, token-to-token, music-to-dance。 |

---
### 2. SHroom: A Python Framework for Ambisonics Room Acoustics Simulation and Binaural Rendering

👤 **作者**: Yhonatan Gayer
🔗 **来源**: [https://arxiv.org/abs/2603.27342v1](https://arxiv.org/abs/2603.27342v1)

**摘要**
> Spherical Harmonics ROOM), an open-source Python library for room acoustics simulation using Ambisonics, available at https://github.com/Yhonatangayer/shroom and installable via \texttt{pip install pyshroom}. \textbf{shroom} projects image-source contributions onto a Spherical Harmonics (SH) basis, yielding a composable pipeline for binaural decoding, spherical array simulation, and real-time head rotation. Benchmarked against \texttt{pyroomacoustics} with an $N=30$ reference, \textbf{shroom} with Magnitude Least Squares (MagLS) achieves perceptual transparency (2.02~dB Log Spectral Distance (LSD) at $N=5$, within the 1--2~dB Just Noticeable Difference (JND)) while its fixed-once decode amortises over multiple sources ($K=1$-to-$8$: slowdown narrows from $7\times$ to $3.1\times$). For dynamic head rotation, \textbf{shroom} applies a Wigner-D multiply at $<1$~ms/frame, making it the only architecturally viable real-time choice.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《SHroom: A Python Framework for Ambisonics Room Acoustics Simulation and Binaural Rendering》所界定。 从摘要看，作者主要围绕 shroom、python、framework 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Benchmarked against \texttt{pyroomacoustics} with an $N=30$ reference, \textbf{shroom} with Magnitude Least Squares (MagLS) achieves perceptual transparency (2.02~dB Log Spectral Distance (LSD) at $N=5$, within the 1--2~dB Just Noticeable Difference (JND)) while its fixed-once decode amortises over multiple sources ($K=1$-to-$8$: slowdown narrows from $7\times$ to $3.1\times$). 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：shroom, python, framework。 |

---
### 3. Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge

👤 **作者**: Ojas Chaturvedi, Kayshav Bhardwaj, Tanay Gondil, Benjamin Shiue-Hal Chou, Kristen Yeon-Ji Yun, Yung-Hsiang Lu, Yujia Yan, Sungkyun Chang
🔗 **来源**: [https://arxiv.org/abs/2603.27528v1](https://arxiv.org/abs/2603.27528v1)

**摘要**
> This paper presents the results of the 2025 Automatic Music Transcription (AMT) Challenge, an online competition to benchmark progress in multi-instrument transcription. Eight teams submitted valid solutions; two outperformed the baseline MT3 model. The results highlight both advances in transcription accuracy and the remaining difficulties in handling polyphony and timbre variation. We conclude with directions for future challenges: broader genre coverage and stronger emphasis on instrument detection.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge》所界定。 从摘要看，作者主要围绕 advancing、multi-instrument、music 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Eight teams submitted valid solutions; two outperformed the baseline MT3 model. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：advancing, multi-instrument, music。 |

---
### 4. A General Model for Deepfake Speech Detection: Diverse Bonafide Resources or Diverse AI-Based Generators

👤 **作者**: Lam Pham, Khoi Vu, Dat Tran, David Fischinger, Simon Freitter, Marcel Hasenbalg, Davide Antonutti, Alexander Schindler, Martin Boyer, Ian McLoughlin
🔗 **来源**: [https://arxiv.org/abs/2603.27557v1](https://arxiv.org/abs/2603.27557v1)

**摘要**
> In this paper, we analyze two main factors of Bonafide Resource (BR) or AI-based Generator (AG) which affect the performance and the generality of a Deepfake Speech Detection (DSD) model. To this end, we first propose a deep-learning based model, referred to as the baseline. Then, we conducted experiments on the baseline by which we indicate how Bonafide Resource (BR) and AI-based Generator (AG) factors affect the threshold score used to detect fake or bonafide input audio in the inference process. Given the experimental results, a dataset, which re-uses public Deepfake Speech Detection (DSD) datasets and shows a balance between Bonafide Resource (BR) or AI-based Generator (AG), is proposed. We then train various deep-learning based models on the proposed dataset and conduct cross-dataset evaluation on different benchmark datasets. The cross-dataset evaluation results prove that the balance of Bonafide Resources (BR) and AI-based Generators (AG) is the key factor to train and achieve a general Deepfake Speech Detection (DSD) model.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《A General Model for Deepfake Speech Detection: Diverse Bonafide Resources or Diverse AI-Based Generators》所界定。 从摘要看，作者主要围绕 general、model、deepfake 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Given the experimental results, a dataset, which re-uses public Deepfake Speech Detection (DSD) datasets and shows a balance between Bonafide Resource (BR) or AI-based Generator (AG), is proposed. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：general, model, deepfake。 |

---
### 5. EvA: An Evidence-First Audio Understanding Paradigm for LALMs

👤 **作者**: Xinyuan Xie, Shunian Chen, Zhiheng Liu, Yuhao Zhang, Zhiqiang Lv, Liyin Liang, Benyou Wang
🔗 **来源**: [https://arxiv.org/abs/2603.27667v1](https://arxiv.org/abs/2603.27667v1)

**摘要**
> Large Audio Language Models (LALMs) still struggle in complex acoustic scenes because they often fail to preserve task-relevant acoustic evidence before reasoning begins. We call this failure the evidence bottleneck: state-of-the-art systems show larger deficits in evidence extraction than in downstream reasoning, suggesting that the main limitation lies in upstream perception rather than reasoning policy. To address this problem, we propose EvA (Evidence-First Audio), a dual-path architecture that combines Whisper and CED-Base through non-compressive, time-aligned fusion. EvA first aggregates intermediate CED layers to preserve multi-scale acoustic cues, then aligns the aggregated CED features to the Whisper timeline and adds the two streams without changing sequence length. We also build EvA-Perception, a large-scale open-source training set with about 54K event-ordered captions (150 h) and about 500K QA pairs. Under a unified zero-shot protocol, EvA achieves the best open-source Perception scores on MMAU, MMAR, and MMSU, and improves over Kimi-Audio-7B on all reported metrics, with the largest gains on perception-heavy splits. These results support the evidence-first hypothesis: stronger audio understanding depends on preserving acoustic evidence before reasoning.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《EvA: An Evidence-First Audio Understanding Paradigm for LALMs》所界定。 从摘要看，作者主要围绕 whisper、acoustic scene 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We call this failure the evidence bottleneck: state-of-the-art systems show larger deficits in evidence extraction than in downstream reasoning, suggesting that the main limitation lies in upstream perception rather than reasoning policy. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：whisper, acoustic scene。 |

---
### 6. BiFormer3D: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer

👤 **作者**: Shaoheng Xu, Chunyi Sun, Jihui Zhang, Amy Bastine, Prasanga N. Samarasinghe, Thushara D. Abhayapala, Hongdong Li
🔗 **来源**: [https://arxiv.org/abs/2603.27998v1](https://arxiv.org/abs/2603.27998v1)

**摘要**
> Individualized head-related impulse responses (HRIRs) enable binaural rendering, but dense per-listener measurements are costly. We address HRIR spatial up-sampling from sparse per-listener measurements: given a few measured HRIRs for a listener, predict HRIRs at unmeasured target directions. Prior learning methods often work in the frequency domain, rely on minimum-phase assumptions or separate timing models, and use a fixed direction grid, which can degrade temporal fidelity and spatial continuity. We propose BiFormer3D, a time-domain, grid-free binaural Transformer for reconstructing HRIRs at arbitrary directions from sparse inputs. It uses sinusoidal spatial features, a Conv1D refinement module, and auxiliary interaural time difference (ITD) and interaural level difference (ILD) heads. On SONICOM, it improves normalized mean squared error (NMSE), cosine distance, and ITD/ILD errors over prior methods; ablations validate modules and show minimum-phase pre-processing is unnecessary.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《BiFormer3D: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer》所界定。 从摘要看，作者主要围绕 biformer、grid-free、time-domain 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：On SONICOM, it improves normalized mean squared error (NMSE), cosine distance, and ITD/ILD errors over prior methods; ablations validate modules and show minimum-phase pre-processing is unnecessary. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：biformer, grid-free, time-domain。 |

---
### 7. Audio Language Model for Deepfake Detection Grounded in Acoustic Chain-of-Thought

👤 **作者**: Runkun Chen, Yixiong Fang, Pengyu Chang, Yuante Li, Massa Baali, Bhiksha Ramakrishnan
🔗 **来源**: [https://arxiv.org/abs/2603.28021v1](https://arxiv.org/abs/2603.28021v1)

**摘要**
> Deepfake speech detection systems are often limited to binary classification tasks and struggle to generate interpretable reasoning or provide context-rich explanations for their decisions. These models primarily extract latent embeddings for authenticity detection but fail to leverage structured acoustic evidence such as prosodic, spectral, and physiological attributes in a meaningful manner. This paper introduces CoLMbo-DF, a Feature-Guided Audio Language Model that addresses these limitations by integrating robust deepfake detection with explicit acoustic chain-of-thought reasoning. By injecting structured textual representations of low-level acoustic features directly into the model prompt, our approach grounds the model's reasoning in interpretable evidence and improves detection accuracy. To support this framework, we introduce a novel dataset of audio pairs paired with chain-of-thought annotations. Experiments show that our method, trained on a lightweight open-source language model, significantly outperforms existing audio language model baselines despite its smaller scale, marking a significant advancement in explainable deepfake speech detection.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Audio Language Model for Deepfake Detection Grounded in Acoustic Chain-of-Thought》所界定。 从摘要看，作者主要围绕 audio、language、model 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：By injecting structured textual representations of low-level acoustic features directly into the model prompt, our approach grounds the model's reasoning in interpretable evidence and improves detection accuracy. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio, language, model。 |

---
### 8. Membership Inference Attacks against Large Audio Language Models

👤 **作者**: Jia-Kai Dong, Yu-Xiang Lin, Hung-Yi Lee
🔗 **来源**: [https://arxiv.org/abs/2603.28378v1](https://arxiv.org/abs/2603.28378v1)

**摘要**
> We present the first systematic Membership Inference Attack (MIA) evaluation of Large Audio Language Models (LALMs). As audio encodes non-semantic information, it induces severe train and test distribution shifts and can lead to spurious MIA performance. Using a multi-modal blind baseline based on textual, spectral, and prosodic features, we demonstrate that common speech datasets exhibit near-perfect train/test separability (AUC approximately 1.0) even without model inference, and the standard MIA scores strongly correlate with these blind acoustic artifacts (correlation greater than 0.7). Using this blind baseline, we identify that distribution-matched datasets enable reliable MIA evaluation without distribution shift confounds. We benchmark multiple MIA methods and conduct modality disentanglement experiments on these datasets. The results reveal that LALM memorization is cross-modal, arising only from binding a speaker's vocal identity with its text. These findings establish a principled standard for auditing LALMs beyond spurious correlations.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Membership Inference Attacks against Large Audio Language Models》所界定。 从摘要看，作者主要围绕 membership、inference、attacks 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Using a multi-modal blind baseline based on textual, spectral, and prosodic features, we demonstrate that common speech datasets exhibit near-perfect train/test separability (AUC approximately 1.0) even without model inference, and the standard MIA scores strongly correlate with these blind acoustic artifacts (correlation greater than 0.7). 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：membership, inference, attacks。 |

---
### 9. Constructing Composite Features for Interpretable Music-Tagging

👤 **作者**: Chenhao Xue, Weitao Hu, Joyraj Chakraborty, Zhijin Guo, Kang Li, Tianyu Shi, Martin Reed, Nikolaos Thomos
🔗 **来源**: [https://arxiv.org/abs/2603.28644v1](https://arxiv.org/abs/2603.28644v1)

**摘要**
> Combining multiple audio features can improve the performance of music tagging, but common deep learning-based feature fusion methods often lack interpretability. To address this problem, we propose a Genetic Programming (GP) pipeline that automatically evolves composite features by mathematically combining base music features, thereby capturing synergistic interactions while preserving interpretability. This approach provides representational benefits similar to deep feature fusion without sacrificing interpretability. Experiments on the MTG-Jamendo and GTZAN datasets demonstrate consistent improvements compared to state-of-the-art systems across base feature sets at different abstraction levels. It should be noted that most of the performance gains are noticed within the first few hundred GP evaluations, indicating that effective feature combinations can be identified under modest search budgets. The top evolved expressions include linear, nonlinear, and conditional forms, with various low-complexity solutions at top performance aligned with parsimony pressure to prefer simpler expressions. Analyzing these composite features further reveals which interactions and transformations tend to be beneficial for tagging, offering insights that remain opaque in black-box deep models.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Constructing Composite Features for Interpretable Music-Tagging》所界定。 从摘要看，作者主要围绕 constructing、composite、features 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Combining multiple audio features can improve the performance of music tagging, but common deep learning-based feature fusion methods often lack interpretability. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：constructing, composite, features。 |

---
### 10. VAANI: Capturing the language landscape for an inclusive digital India

👤 **作者**: Sujith Pulikodan, Abhayjeet Singh, Agneedh Basu, Lokesh Rady, Nihar Desai, Pavan Kumar J, Prajjwal Srivastav, Pranav D Bhat, Raghu Dharmaraju, Ritika Gupta, Sathvik Udupa, Saurabh Kumar, Sumit Sharma, Vaibhav Vishwakarma, Visruth Sanka, Dinesh Tewari, Harsh Dhand, Amrita Kamat, Sukhwinder Singh, Shikhar Vashishth, Partha Talukdar, Raj Acharya, Prasanta Kumar Ghosh
🔗 **来源**: [https://arxiv.org/abs/2603.28714v1](https://arxiv.org/abs/2603.28714v1)

**摘要**
> Project VAANI is an initiative to create an India-representative multi-modal dataset that comprehensively maps India's linguistic diversity, starting with 165 districts across the country in its first two phases. Speech data is collected through a carefully structured process that uses image-based prompts to encourage spontaneous responses. Images are captured through a separate process that encompasses a broad range of topics, gathered from both within and across districts. The collected data undergoes a rigorous multi-stage quality evaluation, including both automated and manual checks to ensure highest possible standards in audio quality and transcription accuracy. Following this thorough validation, we have open-sourced around 289K images, approximately 31,270 hours of audio recordings, and around 2,067 hours of transcribed speech, encompassing 112 languages from 165 districts from 31 States and Union territories. Notably, significant of these languages are being represented for the first time in a dataset of this scale, making the VAANI project a groundbreaking effort in preserving and promoting linguistic inclusivity. This data can be instrumental in building inclusive speech models for India, and in advancing research and development across speech, image, and multimodal applications.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《VAANI: Capturing the language landscape for an inclusive digital India》所界定。 从摘要看，作者主要围绕 vaani、capturing、language 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Speech data is collected through a carefully structured process that uses image-based prompts to encourage spontaneous responses. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：vaani, capturing, language。 |

---
### 11. Can Hierarchical Cross-Modal Fusion Predict Human Perception of AI Dubbed Content?

👤 **作者**: Ashwini Dasare, Nirmesh Shah, Ashishkumar Gudmalwar, Pankaj Wasnik
🔗 **来源**: [https://arxiv.org/abs/2603.28717v1](https://arxiv.org/abs/2603.28717v1)

**摘要**
> Evaluating AI generated dubbed content is inherently multi-dimensional, shaped by synchronization, intelligibility, speaker consistency, emotional alignment, and semantic context. Human Mean Opinion Scores (MOS) remain the gold standard but are costly and impractical at scale. We present a hierarchical multimodal architecture for perceptually meaningful dubbing evaluation, integrating complementary cues from audio, video, and text. The model captures fine-grained features such as speaker identity, prosody, and content from audio, facial expressions and scene-level cues from video and semantic context from text, which are progressively fused through intra and inter-modal layers. Lightweight LoRA adapters enable parameter-efficient fine-tuning across modalities. To overcome limited subjective labels, we derive proxy MOS by aggregating objective metrics with weights optimized via active learning. The proposed architecture was trained on 12k Hindi-English bidirectional dubbed clips, followed by fine-tuning with human MOS. Our approach achieves strong perceptual alignment (PCC > 0.75), providing a scalable solution for automatic evaluation of AI-dubbed content.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Can Hierarchical Cross-Modal Fusion Predict Human Perception of AI Dubbed Content?》所界定。 从摘要看，作者主要围绕 hierarchical、cross-modal、fusion 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our approach achieves strong perceptual alignment (PCC > 0.75), providing a scalable solution for automatic evaluation of AI-dubbed content. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：hierarchical, cross-modal, fusion。 |

---
### 12. ParaSpeechCLAP: A Dual-Encoder Speech-Text Model for Rich Stylistic Language-Audio Pretraining

👤 **作者**: Anuj Diwan, Eunsol Choi, David Harwath
🔗 **来源**: [https://arxiv.org/abs/2603.28737v1](https://arxiv.org/abs/2603.28737v1)

**摘要**
> We introduce ParaSpeechCLAP, a dual-encoder contrastive model that maps speech and text style captions into a common embedding space, supporting a wide range of intrinsic (speaker-level) and situational (utterance-level) descriptors (such as pitch, texture and emotion) far beyond the narrow set handled by existing models. We train specialized ParaSpeechCLAP-Intrinsic and ParaSpeechCLAP-Situational models alongside a unified ParaSpeechCLAP-Combined model, finding that specialization yields stronger performance on individual style dimensions while the unified model excels on compositional evaluation. We further show that ParaSpeechCLAP-Intrinsic benefits from an additional classification loss and class-balanced training. We demonstrate our models' performance on style caption retrieval, speech attribute classification and as an inference-time reward model that improves style-prompted TTS without additional training. ParaSpeechCLAP outperforms baselines on most metrics across all three applications. Our models and code are released at https://github.com/ajd12342/paraspeechclap .

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《ParaSpeechCLAP: A Dual-Encoder Speech-Text Model for Rich Stylistic Language-Audio Pretraining》所界定。 从摘要看，作者主要围绕 paraspeechclap、dual-encoder、speech-text 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We further show that ParaSpeechCLAP-Intrinsic benefits from an additional classification loss and class-balanced training. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：paraspeechclap, dual-encoder, speech-text。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
