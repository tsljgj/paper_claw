<div align="center">

# 📰 Paper Claw

**2026-03-12**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-11 09:00:00 CST → 2026-03-12 11:26:05 CST |
| 📄 论文总数 | **12** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 2 篇
- **TTS**: 2 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 1 篇
- **Audio**: 6 篇

> 💡 今日共收录 12 篇新论文，主要分布在 Speech LLM 1, ASR 2, TTS 2, Paralinguistics 1, Audio 6。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. OSUM-Pangu: An Open-Source Multidimension Speech Understanding Foundation Model Built upon OpenPangu on Ascend NPUs

👤 **作者**: Yujie Liao, Xuelong Geng, Hongfei Xue, Shuiyuan Wang, Lei Xie
🔗 **来源**: [https://arxiv.org/abs/2603.10862v1](https://arxiv.org/abs/2603.10862v1)

**摘要**
> Recent advancements in Speech Large Language Models have significantly enhanced multi-dimensional speech understanding. However, the majority of high-performance frameworks are predominantly optimized for GPU centric ecosystems and proprietary backbones, creating a significant gap for deployment on non-CUDA computing infrastructures. In this paper, we present OSUM-Pangu, a fully open-source speech understanding foundation model developed on a completely non-CUDA software and hardware stack. By integrating an audio encoder with the openPangu-7B LLM backbone, we successfully implement the entire training and inference pipeline on the Ascend NPU platform. To facilitate efficient task alignment under non-CUDA resource constraints, we adopt a practical training process that sequentially bridges speech perception and user intent recognition. Experimental results demonstrate that OSUM-Pangu achieves task accuracy comparable to mainstream GPU-based models while maintaining robust natural language interaction capabilities. Our work provides a reproducible, non-CUDA baseline for the open-source speech community, promoting the independent evolution of multimodal intelligence.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《OSUM-Pangu: An Open-Source Multidimension Speech Understanding Foundation Model Built upon OpenPangu on Ascend NPUs》所界定。 从摘要看，作者主要围绕 speech understanding、intent recognition 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experimental results demonstrate that OSUM-Pangu achieves task accuracy comparable to mainstream GPU-based models while maintaining robust natural language interaction capabilities. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech understanding, intent recognition。 |

---
## 🏷️ ASR

### 1. Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing

👤 **作者**: Hao Shi, Yusuke Fujita, Roman Koshkin, Mengjie Zhao, Yuan Gao, Lianbo Liu, Yui Sudo
🔗 **来源**: [https://arxiv.org/abs/2603.10587v1](https://arxiv.org/abs/2603.10587v1)

**摘要**
> Large language models (LLMs) provide strong semantic priors that can improve multi-talker automatic speech recognition (MT-ASR), but using an LLM as an autoregressive decoder is computationally expensive and remains fragile under heavy overlap. In this paper, we propose an encoder-only MT-ASR framework that adapts an LLM to multi-talker conditioning and distills its semantic guidance into the encoder during training, while retaining fast CTC-style decoding at inference. Our model employs a post-encoder separator with serialized CTC to produce talker-ordered transcripts, and leverages an adapted LLM-based SOT objective as a multi-talker-aware teacher signal to explicitly regularize mixed-speech representations. To further support variable numbers of talkers, we introduce a Talker-Count Head that predicts the talker count and dynamically selects the appropriate decoding branch. Experiments on LibriMix show that the proposed encoder-only model achieves comparable performance to LLM-based systems in the two-talker condition, while delivering significant improvements in the three-talker condition with significant small RTF.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing》所界定。 从摘要看，作者主要围绕 automatic speech recognition 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Large language models (LLMs) provide strong semantic priors that can improve multi-talker automatic speech recognition (MT-ASR), but using an LLM as an autoregressive decoder is computationally expensive and remains fragile under heavy overlap. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：automatic speech recognition。 |

---
### 2. AlphaFlowTSE: One-Step Generative Target Speaker Extraction via Conditional AlphaFlow

👤 **作者**: Duojia Li, Shuhan Zhang, Zihan Qian, Wenxuan Wu, Shuai Wang, Qingyang Hong, Lin Li, Haizhou Li
🔗 **来源**: [https://arxiv.org/abs/2603.10701v1](https://arxiv.org/abs/2603.10701v1)

**摘要**
> In target speaker extraction (TSE), we aim to recover target speech from a multi-talker mixture using a short enrollment utterance as reference. Recent studies on diffusion and flow-matching generators have improved target-speech fidelity. However, multi-step sampling increases latency, and one-step solutions often rely on a mixture-dependent time coordinate that can be unreliable for real-world conversations. We present AlphaFlowTSE, a one-step conditional generative model trained with a Jacobian-vector product (JVP)-free AlphaFlow objective. AlphaFlowTSE learns mean-velocity transport along a mixture-to-target trajectory starting from the observed mixture, eliminating auxiliary mixing-ratio prediction, and stabilizes training by combining flow matching with an interval-consistency teacher-student target. Experiments on Libri2Mix and REAL-T confirm that AlphaFlowTSE improves target-speaker similarity and real-mixture generalization for downstream automatic speech recognition (ASR).

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《AlphaFlowTSE: One-Step Generative Target Speaker Extraction via Conditional AlphaFlow》所界定。 从摘要看，作者主要围绕 automatic speech recognition 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Recent studies on diffusion and flow-matching generators have improved target-speech fidelity. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：automatic speech recognition。 |

---
## 🏷️ TTS

### 1. Probabilistic Verification of Voice Anti-Spoofing Models

👤 **作者**: Evgeny Kushnir, Alexandr Kozodaev, Dmitrii Korzh, Mikhail Pautov, Oleg Kiriukhin, Oleg Y. Rogov
🔗 **来源**: [https://arxiv.org/abs/2603.10713v1](https://arxiv.org/abs/2603.10713v1)

**摘要**
> Recent advances in generative models have amplified the risk of malicious misuse of speech synthesis technologies, enabling adversaries to impersonate target speakers and access sensitive resources. Although speech deepfake detection has progressed rapidly, most existing countermeasures lack formal robustness guarantees or fail to generalize to unseen generation techniques. We propose PV-VASM, a probabilistic framework for verifying the robustness of voice anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-speech (TTS), voice cloning (VC), and parametric signal transformations. The approach is model-agnostic and enables robustness verification against unseen speech synthesis techniques and input perturbations. We derive a theoretical upper bound on the error probability and validate the method across diverse experimental settings, demonstrating its effectiveness as a practical robustness verification tool.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《Probabilistic Verification of Voice Anti-Spoofing Models》所界定。 从摘要看，作者主要围绕 text-to-speech、speech synthesis 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We derive a theoretical upper bound on the error probability and validate the method across diverse experimental settings, demonstrating its effectiveness as a practical robustness verification tool. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：text-to-speech, speech synthesis。 |

---
### 2. When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS

👤 **作者**: Anupam Purwar, Aditya Choudhary
🔗 **来源**: [https://arxiv.org/abs/2603.10904v1](https://arxiv.org/abs/2603.10904v1)

**摘要**
> Large language models are increasingly adopted as semantic backbones for neural text-to-speech systems. However, frozen LLM representations are insufficient for modeling speaker specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language Model backbone of TTS show promise in improving the voice consistency and Signal to Noise ratio SNR in voice cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base Qwen-0.5B model across three complementary dimensions of speech quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose training data exhibits sufficient acoustic variability. Second, speaker fidelity improves for all evaluated speakers with consistent increases in voice similarity indicating that LoRA effectively adapts speaker identity representations without degrading linguistic modeling. Third, signal level quality improves in most cases with signal to noise ratio increasing by as much as 34 percent. Crucially these improvements are strongly governed by the characteristics of the training data. Speakers with high variability in acoustic energy and perceptual quality achieve simultaneous gains in DNS-MOS voice similarity and SNR. Overall this work establishes that LoRA finetuning is not merely a parameter efficient optimization technique but an effective mechanism for better speaker level adaptation in compact LLM-based TTS systems. When supported by sufficiently diverse training data LoRA adapted Qwen-0.5B consistently surpasses its frozen base model in perceptual quality speaker similarity with low latency using GGUF model hosted in quantized form.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS》所界定。 从摘要看，作者主要围绕 text-to-speech、tts system 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our experiments involving fine tuning of the Language Model backbone of TTS show promise in improving the voice consistency and Signal to Noise ratio SNR in voice cloning task. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：text-to-speech, tts system。 |

---
## 🏷️ Enhancement

> 📭 今日该分类暂无新论文。

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

### 1. Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation

👤 **作者**: Thomas Thebaud, Yuzhe Wang, Laureano Moro-Velazquez, Jesus Villalba-Lopez, Najim Dehak
🔗 **来源**: [https://arxiv.org/abs/2603.10827v1](https://arxiv.org/abs/2603.10827v1)

**摘要**
> Speech-aware large language models (LLMs) can accept speech inputs, yet their training objectives largely emphasize linguistic content or specific fields such as emotions or the speaker's gender, leaving it unclear whether they encode speaker identity. First, we propose a model-agnostic scoring protocol that produces continuous verification scores for both API-only and open-weight models, using confidence scores or log-likelihood ratios from the Yes/No token probabilities. Using this protocol, we benchmark recent speech-aware LLMs and observe weak speaker discrimination (EERs above 20% on VoxCeleb1). Second, we introduce a lightweight augmentation that equips an LLM with ASV capability by injecting frozen ECAPA-TDNN speaker embeddings through a learned projection and training only LoRA adapters. On TinyLLaMA-1.1B, the resulting ECAPA-LLM achieves 1.03% EER on VoxCeleb1-E, approaching a dedicated speaker verification system while preserving a natural-language interface.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「副语言学」方向，核心任务由题目《Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation》所界定。 从摘要看，作者主要围绕 speaker verification 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：On TinyLLaMA-1.1B, the resulting ECAPA-LLM achieves 1.03% EER on VoxCeleb1-E, approaching a dedicated speaker verification system while preserving a natural-language interface. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：speaker verification。 |

---
## 🏷️ Audio

### 1. Geo-ATBench: A Benchmark for Geospatial Audio Tagging with Geospatial Semantic Context

👤 **作者**: Yuanbo Hou, Yanru Wu, Qiaoqiao Ren, Shengchen Li, Stephen Roberts, Dick Botteldooren
🔗 **来源**: [https://arxiv.org/abs/2603.10623v1](https://arxiv.org/abs/2603.10623v1)

**摘要**
> Environmental sound understanding in computational auditory scene analysis (CASA) is often formulated as an audio-only recognition problem. This formulation leaves a persistent drawback in multi-label audio tagging (AT): acoustic similarity can make certain events difficult to separate from waveforms alone. In such cases, disambiguating cues often lie outside the waveform. Geospatial semantic context (GSC), derived from geographic information system data, e.g., points of interest (POI), provides location-tied environmental priors that can help reduce this ambiguity. A systematic study of this direction is enabled through the proposed geospatial audio tagging (Geo-AT) task, which conditions multi-label sound event tagging on GSC alongside audio. To benchmark Geo-AT, Geo-ATBench is introduced as a polyphonic audio benchmark with geographical annotations, containing 10.71 hours of audio across 28 event categories; each clip is paired with a GSC representation from 11 semantic context categories. GeoFusion-AT is proposed as a unified geo-audio fusion framework that evaluates feature-, representation-, and decision-level fusion on representative audio backbones, with audio- and GSC-only baselines. Results show that incorporating GSC improves AT performance, especially on acoustically confounded labels, indicating geospatial semantics provide effective priors beyond audio alone. A crowdsourced listening study with 10 participants on 579 samples shows that there is no significant difference in performance between models on Geo-ATBench labels and aggregated human labels, supporting Geo-ATBench as a human-aligned benchmark. The Geo-AT task, benchmark Geo-ATBench, and reproducible geo-audio fusion framework GeoFusion-AT provide a foundation for studying AT with geospatial semantic context within the CASA community. Dataset, code, models are on homepage (https://github.com/WuYanru2002/Geo-ATBench).

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Geo-ATBench: A Benchmark for Geospatial Audio Tagging with Geospatial Semantic Context》所界定。 从摘要看，作者主要围绕 audio tagging 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Results show that incorporating GSC improves AT performance, especially on acoustically confounded labels, indicating geospatial semantics provide effective priors beyond audio alone. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio tagging。 |

---
### 2. MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment

👤 **作者**: Wenze Ren, Yi-Cheng Lin, Wen-Chin Huang, Erica Cooper, Ryandhimas E. Zezario, Hsin-Min Wang, Hung-yi Lee, Yu Tsao
🔗 **来源**: [https://arxiv.org/abs/2603.10723v1](https://arxiv.org/abs/2603.10723v1)

**摘要**
> The Mean Opinion Score (MOS) serves as the standard metric for speech quality assessment, yet biases in human annotations remain underexplored. We conduct the first systematic analysis of gender bias in MOS, revealing that male listeners consistently assign higher scores than female listeners--a gap that is most pronounced in low-quality speech and gradually diminishes as quality improves. This quality-dependent structure proves difficult to eliminate through simple calibration. We further demonstrate that automated MOS models trained on aggregated labels exhibit predictions skewed toward male standards of perception. To address this, we propose a gender-aware model that learns gender-specific scoring patterns through abstracting binary group embeddings, thereby improving overall and gender-specific prediction accuracy. This study establishes that gender bias in MOS constitutes a systematic, learnable pattern demanding attention in equitable speech evaluation.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment》所界定。 从摘要看，作者主要围绕 mos-bias、from、hidden 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We conduct the first systematic analysis of gender bias in MOS, revealing that male listeners consistently assign higher scores than female listeners--a gap that is most pronounced in low-quality speech and gradually diminishes as quality improves. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：mos-bias, from, hidden。 |

---
### 3. Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning

👤 **作者**: Artem Dvirniak, Evgeny Kushnir, Dmitrii Tarasov, Artem Iudin, Oleg Kiriukhin, Mikhail Pautov, Dmitrii Korzh, Oleg Y. Rogov
🔗 **来源**: [https://arxiv.org/abs/2603.10725v1](https://arxiv.org/abs/2603.10725v1)

**摘要**
> The modern generative audio models can be used by an adversary in an unlawful manner, specifically, to impersonate other people to gain access to private information. To mitigate this issue, speech deepfake detection (SDD) methods started to evolve. Unfortunately, current SDD methods generally suffer from the lack of generalization to new audio domains and generators. More than that, they lack interpretability, especially human-like reasoning that would naturally explain the attribution of a given audio to the bona fide or spoof class and provide human-perceptible cues. In this paper, we propose HIR-SDD, a novel SDD framework that combines the strengths of Large Audio Language Models (LALMs) with the chain-of-thought reasoning derived from the novel proposed human-annotated dataset. Experimental evaluation demonstrates both the effectiveness of the proposed method and its ability to provide reasonable justifications for predictions.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning》所界定。 从摘要看，作者主要围绕 towards、robust、speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experimental evaluation demonstrates both the effectiveness of the proposed method and its ability to provide reasonable justifications for predictions. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：towards, robust, speech。 |

---
### 4. VoxCare: Studying Natural Communication Behaviors of Hospital Caregivers through Wearable Sensing of Egocentric Audio

👤 **作者**: Tiantian Feng, Kleanthis Avramidis, Anfeng Xu, Deqi Wang, Brandon M Booth, Shrikanth Narayanan
🔗 **来源**: [https://arxiv.org/abs/2603.10888v1](https://arxiv.org/abs/2603.10888v1)

**摘要**
> Healthcare professionals work in complex, high-stakes environments where effective communication is critical for care delivery, team coordination, and individual well-being. However, communication activity in everyday clinical settings remains challenging to measure and largely unexplored in human behavioral research. We present VoxCare, a scalable egocentric wearable audio sensing and computing system that captures natural communication behaviors of hospital professionals in real-world settings without storing raw audio. VoxCare performs real-time, on-device acoustic feature extraction and applies a speech foundation model-guided teacher-student framework to identify foreground speech activity. From these features, VoxCare derives interpretable behavioral measures of communication frequency, duration, and vocal arousal. Our analyses reveal how, when, and how often clinicians communicate across different shifts and working units, and suggest that communication activity reflects underlying workload and stress. By enabling continuous assessment of communication patterns in everyday contexts, this study provides data-driven approaches to understand the behaviors of healthcare providers and ultimately improve healthcare delivery.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《VoxCare: Studying Natural Communication Behaviors of Hospital Caregivers through Wearable Sensing of Egocentric Audio》所界定。 从摘要看，作者主要围绕 voxcare、studying、natural 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：By enabling continuous assessment of communication patterns in everyday contexts, this study provides data-driven approaches to understand the behaviors of healthcare providers and ultimately improve healthcare delivery. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：voxcare, studying, natural。 |

---
### 5. Training-Free Multi-Step Inference for Target Speaker Extraction

👤 **作者**: Zhenghai You, Ying Shi, Lantian Li, Dong Wang
🔗 **来源**: [https://arxiv.org/abs/2603.10921v1](https://arxiv.org/abs/2603.10921v1)

**摘要**
> Target speaker extraction (TSE) aims to recover a target speaker's speech from a mixture using a reference utterance as a cue. Most TSE systems adopt conditional auto-encoder architectures with one-step inference. Inspired by test-time scaling, we propose a training-free multi-step inference method that enables iterative refinement with a frozen pretrained model. At each step, new candidates are generated by interpolating the original mixture and the previous estimate, and the best candidate is selected for further refinement until convergence. Experiments show that, when ground-truth target speech is available, optimizing an intrusive metric (SI-SDRi) yields consistent gains across multiple evaluation metrics. Without ground truth, optimizing non-intrusive metrics (UTMOS or SpkSim) improves the corresponding metric but may hurt others. We therefore introduce joint metric optimization to balance these objectives, enabling controllable extraction preferences for practical deployment.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Training-Free Multi-Step Inference for Target Speaker Extraction》所界定。 从摘要看，作者主要围绕 training-free、multi-step、inference 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments show that, when ground-truth target speech is available, optimizing an intrusive metric (SI-SDRi) yields consistent gains across multiple evaluation metrics. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：training-free, multi-step, inference。 |

---
### 6. V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation

👤 **作者**: Yan-Bo Lin, Jonah Casebeer, Long Mai, Aniruddha Mahapatra, Gedas Bertasius, Nicholas J. Bryan
🔗 **来源**: [https://arxiv.org/abs/2603.11042v1](https://arxiv.org/abs/2603.11042v1)

**摘要**
> Generating music that temporally aligns with video events is challenging for existing text-to-music models, which lack fine-grained temporal control. We introduce V2M-Zero, a zero-pair video-to-music generation approach that outputs time-aligned music for video. Our method is motivated by a key observation: temporal synchronization requires matching when and how much change occurs, not what changes. While musical and visual events differ semantically, they exhibit shared temporal structure that can be captured independently within each modality. We capture this structure through event curves computed from intra-modal similarity using pretrained music and video encoders. By measuring temporal change within each modality independently, these curves provide comparable representations across modalities. This enables a simple training strategy: fine-tune a text-to-music model on music-event curves, then substitute video-event curves at inference without cross-modal training or paired data. Across OES-Pub, MovieGenBench-Music, and AIST++, V2M-Zero achieves substantial gains over paired-data baselines: 5-21% higher audio quality, 13-15% better semantic alignment, 21-52% improved temporal synchronization, and 28% higher beat alignment on dance videos. We find similar results via a large crowd-source subjective listening test. Overall, our results validate that temporal alignment through within-modality features, rather than paired cross-modal supervision, is effective for video-to-music generation. Results are available at https://genjib.github.io/v2m_zero/

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation》所界定。 从摘要看，作者主要围绕 m-zero、zero-pair、time-aligned 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Across OES-Pub, MovieGenBench-Music, and AIST++, V2M-Zero achieves substantial gains over paired-data baselines: 5-21% higher audio quality, 13-15% better semantic alignment, 21-52% improved temporal synchronization, and 28% higher beat alignment on dance videos. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：m-zero, zero-pair, time-aligned。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
