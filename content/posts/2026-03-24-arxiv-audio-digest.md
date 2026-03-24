<div align="center">

# 📰 Paper Claw

**2026-03-24**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-23 11:37:41 CST → 2026-03-24 11:28:25 CST |
| 📄 论文总数 | **8** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 0 篇
- **TTS**: 1 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 5 篇

> 💡 今日共收录 8 篇新论文，主要分布在 Speech LLM 1, TTS 1, Enhancement 1, Audio 5。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. TiCo: Time-Controllable Training for Spoken Dialogue Models

👤 **作者**: Kai-Wei Chang, Wei-Chih Chen, En-Pei Hu, Hung-yi Lee, James Glass
🔗 **来源**: [https://arxiv.org/abs/2603.22267v1](https://arxiv.org/abs/2603.22267v1)

**摘要**
> We propose TiCo, a simple post-training method for enabling spoken dialogue models (SDMs) to follow time-constrained instructions and generate responses with controllable duration. This capability is valuable for real-world spoken language systems such as voice assistants and interactive agents, where controlling response duration can improve interaction quality. However, despite their strong ability to generate natural spoken responses, existing models lack time awareness and struggle to follow duration-related instructions (e.g., "Please generate a response lasting about 15 seconds"). Through an empirical evaluation of both open-source and commercial SDMs, we show that they frequently fail to satisfy such time-control requirements. TiCo addresses this limitation by enabling models to estimate elapsed speaking time during generation through Spoken Time Markers (STM) (e.g., <10.6 seconds>). These markers help the model maintain awareness of time and adjust the remaining content to meet the target duration. TiCo is simple and efficient: it requires only a small amount of data and no additional question-answer pairs, relying instead on self-generation and reinforcement learning. Experimental results show that TiCo significantly improves adherence to duration constraints while preserving response quality.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《TiCo: Time-Controllable Training for Spoken Dialogue Models》所界定。 从摘要看，作者主要围绕 spoken dialogue 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：This capability is valuable for real-world spoken language systems such as voice assistants and interactive agents, where controlling response duration can improve interaction quality. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：spoken dialogue。 |

---
## 🏷️ ASR

> 📭 今日该分类暂无新论文。

---
## 🏷️ TTS

### 1. SelfTTS: cross-speaker style transfer through explicit embedding disentanglement and self-refinement using self-augmentation

👤 **作者**: Lucas H. Ueda, João G. T. Lima, Pedro R. Corrêa, Flávio O. Simões, Mário U. Neto, Paula D. P. Costa
🔗 **来源**: [https://arxiv.org/abs/2603.22252v1](https://arxiv.org/abs/2603.22252v1)

**摘要**
> This paper presents SelfTTS, a text-to-speech (TTS) model designed for cross-speaker style transfer that eliminates the need for external pre-trained speaker or emotion encoders. The architecture achieves emotional expressivity in neutral speakers through an explicit disentanglement strategy utilizing Gradient Reversal Layers (GRL) combined with cosine similarity loss to decouple speaker and emotion information. We introduce Multi Positive Contrastive Learning (MPCL) to induce clustered representations of speaker and emotion embeddings based on their respective labels. Furthermore, SelfTTS employs a self-refinement strategy via Self-Augmentation, exploiting the model's voice conversion capabilities to enhance the naturalness of synthesized speech. Experimental results demonstrate that SelfTTS achieves superior emotional naturalness (eMOS) and robust stability in target timbre and emotion compared to state-of-the-art baselines.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《SelfTTS: cross-speaker style transfer through explicit embedding disentanglement and self-refinement using self-augmentation》所界定。 从摘要看，作者主要围绕 text-to-speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The architecture achieves emotional expressivity in neutral speakers through an explicit disentanglement strategy utilizing Gradient Reversal Layers (GRL) combined with cosine similarity loss to decouple speaker and emotion information. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：text-to-speech。 |

---
## 🏷️ Enhancement

### 1. Semi-Blind Channel Estimation and Hybrid Receiver Beamforming in the Tera-Hertz Multi-User Massive MIMO Uplink

👤 **作者**: Abhisha Garg, Suraj Srivastava, Varsha Dubey, Aditya Jagannatham, Lajos Hanzo
🔗 **来源**: [https://arxiv.org/abs/2603.22258v1](https://arxiv.org/abs/2603.22258v1)

**摘要**
> We develop a pragmatic multi-user (MU) massive multiple-input multiple-output (MIMO) channel model tailored to the THz band, encompassing factors such as molecular absorption, reflection losses and multipath diffused ray components. Next, we propose a novel semi-blind based channel state information (CSI) acquisition technique i.e. MU whitening decorrelation semi-blind (MU-WD-SB) that exploits the second order statistics corresponding to the unknown data symbols along with pilot vectors. A constrained Cramer-Rao Lower Bound (C-CRLB) is derived to bound the normalized mean square error (NMSE) performance of the proposed semi-blind learning technique. Our proposed scheme efficiently reduces the training overheads while enhancing the overall accuracy of the channel learning process. Furthermore, a novel hybrid receiver combiner framework is devised for MU THz massive MIMO systems, leveraging multiple measurement vector based sparse Bayesian learning (MMV-SBL) that relies on the estimated CSI acquired through our proposed semi-blind technique relying on low resolution analog-to-digital converters (ADCs). Finally, we propose an optimal hybrid combiner based on MMV-SBL, which directly reduces the MU interference. Extensive simulations are conducted to evaluate the performance gain of the proposed MU-WD-SB scheme over conventional training-based and other semi-blind learning techniques for a practical THz channel obtained from the high-resolution transmission (HITRAN) database. The metrics considered for quantifying the improvements include the NMSE, bit error rate (BER) and spectral-efficiency (SE).

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《Semi-Blind Channel Estimation and Hybrid Receiver Beamforming in the Tera-Hertz Multi-User Massive MIMO Uplink》所界定。 从摘要看，作者主要围绕 beamforming 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The metrics considered for quantifying the improvements include the NMSE, bit error rate (BER) and spectral-efficiency (SE). 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：beamforming。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning

👤 **作者**: Xi Xuan, Wenxin Zhang, Zhiyu Li, Jennifer Williams, Ville Hautamäki, Tomi H. Kinnunen
🔗 **来源**: [https://arxiv.org/abs/2603.21875v1](https://arxiv.org/abs/2603.21875v1)

**摘要**
> Speech deepfake source verification systems aims to determine whether two synthetic speech utterances originate from the same source generator, often assuming that the resulting source embeddings are independent of speaker traits. However, this assumption remains unverified. In this paper, we first investigate the impact of speaker factors on source verification. We propose a speaker-disentangled metric learning (SDML) framework incorporating two novel loss functions. The first leverages Chebyshev polynomial to mitigate gradient instability during disentanglement optimization. The second projects source and speaker embeddings into hyperbolic space, leveraging Riemannian metric distances to reduce speaker information and learn more discriminative source features. Experimental results on MLAAD benchmark, evaluated under four newly proposed protocols designed for source-speaker disentanglement scenarios, demonstrate the effectiveness of SDML framework. The code, evaluation protocols and demo website are available at https://github.com/xxuan-acoustics/RiemannSD-Net.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning》所界定。 从摘要看，作者主要围绕 disentangling、speaker、traits 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experimental results on MLAAD benchmark, evaluated under four newly proposed protocols designed for source-speaker disentanglement scenarios, demonstrate the effectiveness of SDML framework. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：disentangling, speaker, traits。 |

---
### 2. Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations

👤 **作者**: Xin Guo, Chunrui Zhao, Hong Jia, Ting Dang, Gongping Huang, Xianrui Zheng, Yan Gao
🔗 **来源**: [https://arxiv.org/abs/2603.21888v1](https://arxiv.org/abs/2603.21888v1)

**摘要**
> Integrating Federated Learning (FL) with self-supervised learning (SSL) enables privacy-preserving fine-tuning for speech tasks. However, federated environments exhibit significant heterogeneity: clients differ in computational capacity, causing straggler effects under unified fine-tuning, while diverse downstream tasks require different representation depths, making full-model updates inefficient. To address these challenges, we propose an adaptive federated fine-tuning framework with early exits. Lightweight prediction heads are inserted at intermediate layers of the SSL backbone, allowing clients to terminate computation based on local constraints and task requirements. We further introduce a layer-wise, depth-aware partial aggregation strategy to better utilize representations from different network depths. Experiments show that the framework reduces edge overhead, supports heterogeneous hardware, and maintains competitive performance in resource-constrained federated environments.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations》所界定。 从摘要看，作者主要围绕 adaptive、federated、fine-tuning 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments show that the framework reduces edge overhead, supports heterogeneous hardware, and maintains competitive performance in resource-constrained federated environments. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：adaptive, federated, fine-tuning。 |

---
### 3. AnimalCLAP: Taxonomy-Aware Language-Audio Pretraining for Species Recognition and Trait Inference

👤 **作者**: Risa Shinoda, Kaede Shiohara, Nakamasa Inoue, Hiroaki Santo, Fumio Okura
🔗 **来源**: [https://arxiv.org/abs/2603.22053v1](https://arxiv.org/abs/2603.22053v1)

**摘要**
> Animal vocalizations provide crucial insights for wildlife assessment, particularly in complex environments such as forests, aiding species identification and ecological monitoring. Recent advances in deep learning have enabled automatic species classification from their vocalizations. However, classifying species unseen during training remains challenging. To address this limitation, we introduce AnimalCLAP, a taxonomy-aware language-audio framework comprising a new dataset and model that incorporate hierarchical biological information. Specifically, our vocalization dataset consists of 4,225 hours of recordings covering 6,823 species, annotated with 22 ecological traits. The AnimalCLAP model is trained on this dataset to align audio and textual representations using taxonomic structures, improving the recognition of unseen species. We demonstrate that our proposed model effectively infers ecological and biological attributes of species directly from their vocalizations, achieving superior performance compared to CLAP. Our dataset, code, and models will be publicly available at https://dahlian00.github.io/AnimalCLAP_Page/.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《AnimalCLAP: Taxonomy-Aware Language-Audio Pretraining for Species Recognition and Trait Inference》所界定。 从摘要看，作者主要围绕 animalclap、taxonomy-aware、language-audio 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The AnimalCLAP model is trained on this dataset to align audio and textual representations using taxonomic structures, improving the recognition of unseen species. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：animalclap, taxonomy-aware, language-audio。 |

---
### 4. WiRD-Gest: Gesture Recognition In The Real World Using Range-Doppler Wi-Fi Sensing on COTS Hardware

👤 **作者**: Jessica Sanson, Rahul C. Shah, Yazhou Zhu, Rafael Rosales, Valerio Frascolla
🔗 **来源**: [https://arxiv.org/abs/2603.22131v1](https://arxiv.org/abs/2603.22131v1)

**摘要**
> Wi-Fi sensing has emerged as a promising technique for gesture recognition, yet its practical deployment is hindered by environmental sensitivity and device placement challenges. To overcome these limitations we propose Wi-Fi Range and Doppler (WiRD)-Gest, a novel system that performs gesture recognition using a single, unmodified Wi-Fi transceiver on a commercial off-the-shelf (COTS) laptop. The system leverages an monostatic full duplex sensing pipeline capable of extracting Range-Doppler (RD) information. Utilizing this, we present the first benchmark of deep learning models for gesture recognition based on monostatic sensing. The key innovation lies in how monostatic sensing and spatial (range) information fundamentally transforms accuracy, robustness and generalization compared to prior approaches. We demonstrate excellent performance in crowded, unseen public spaces with dynamic interference and additional moving targets even when trained on data from controlled environments only. These are scenarios where prior Wi-Fi sensing approaches often fail, however, our system suffers minor degradation. The WiRD-Gest benchmark and dataset will also be released as open source.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《WiRD-Gest: Gesture Recognition In The Real World Using Range-Doppler Wi-Fi Sensing on COTS Hardware》所界定。 从摘要看，作者主要围绕 wird-gest、gesture、recognition 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We demonstrate excellent performance in crowded, unseen public spaces with dynamic interference and additional moving targets even when trained on data from controlled environments only. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：wird-gest, gesture, recognition。 |

---
### 5. Adapting Self-Supervised Speech Representations for Cross-lingual Dysarthria Detection in Parkinson's Disease

👤 **作者**: Abner Hernandez, Eunjung Yeo, Kwanghee Choi, Chin-Jou Li, Zhengjun Yue, Rohan Kumar Das, Jan Rusz, Mathew Magimai Doss, Juan Rafael Orozco-Arroyave, Tomás Arias-Vergara, Andreas Maier, Elmar Nöth, David R. Mortensen, David Harwath, Paula Andrea Perez-Toro
🔗 **来源**: [https://arxiv.org/abs/2603.22225v1](https://arxiv.org/abs/2603.22225v1)

**摘要**
> The limited availability of dysarthric speech data makes cross-lingual detection an important but challenging problem. A key difficulty is that speech representations often encode language-dependent structure that can confound dysarthria detection. We propose a representation-level language shift (LS) that aligns source-language self-supervised speech representations with the target-language distribution using centroid-based vector adaptation estimated from healthy-control speech. We evaluate the approach on oral DDK recordings from Parkinson's disease speech datasets in Czech, German, and Spanish under both cross-lingual and multilingual settings. LS substantially improves sensitivity and F1 in cross-lingual settings, while yielding smaller but consistent gains in multilingual settings. Representation analysis further shows that LS reduces language identity in the embedding space, supporting the interpretation that LS removes language-dependent structure.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Adapting Self-Supervised Speech Representations for Cross-lingual Dysarthria Detection in Parkinson's Disease》所界定。 从摘要看，作者主要围绕 adapting、self-supervised、speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：LS substantially improves sensitivity and F1 in cross-lingual settings, while yielding smaller but consistent gains in multilingual settings. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：adapting, self-supervised, speech。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
