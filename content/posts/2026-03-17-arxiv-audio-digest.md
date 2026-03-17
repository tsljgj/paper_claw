<div align="center">

# 📰 Paper Claw

**2026-03-17**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-16 11:48:42 CST → 2026-03-17 11:27:30 CST |
| 📄 论文总数 | **6** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 1 篇
- **TTS**: 1 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 3 篇

> 💡 今日共收录 6 篇新论文，主要分布在 ASR 1, TTS 1, Enhancement 1, Audio 3。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. Two-Stage Adaptation for Non-Normative Speech Recognition: Revisiting Speaker-Independent Initialization for Personalization

👤 **作者**: Shan Jiang, Jiawen Qi, Chuanbing Huo, Yingqiang Gao, Qinyu Chen
🔗 **来源**: [https://arxiv.org/abs/2603.15261v1](https://arxiv.org/abs/2603.15261v1)

**摘要**
> Personalizing automatic speech recognition (ASR) systems for non-normative speech, such as dysarthric and aphasic speech, is challenging. While speaker-specific fine-tuning (SS-FT) is widely used, it is typically initialized directly from a generic pre-trained model. Whether speaker-independent adaptation provides a stronger initialization prior under such mismatch remains unclear. In this work, we propose a two-stage adaptation framework consisting of speaker-independent fine-tuning (SI-FT) on multi-speaker non-normative data followed by SS-FT, and evaluate it through a controlled comparison with direct SS-FT under identical per-speaker conditions. Experiments on AphasiaBank and UA-Speech with Whisper-Large-v3 and Qwen3-ASR, alongside evaluation on typical-speech datasets TED-LIUM v3 and FLEURS, show that two-stage adaptation consistently improves personalization while maintaining manageable out-of-domain (OOD) trade-offs.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《Two-Stage Adaptation for Non-Normative Speech Recognition: Revisiting Speaker-Independent Initialization for Personalization》所界定。 从摘要看，作者主要围绕 automatic speech recognition、whisper 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experiments on AphasiaBank and UA-Speech with Whisper-Large-v3 and Qwen3-ASR, alongside evaluation on typical-speech datasets TED-LIUM v3 and FLEURS, show that two-stage adaptation consistently improves personalization while maintaining manageable out-of-domain (OOD) trade-offs. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：automatic speech recognition, whisper。 |

---
## 🏷️ TTS

### 1. NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation

👤 **作者**: Qinke Ni, Huan Liao, Dekun Chen, Yuxiang Wang, Zhizheng Wu
🔗 **来源**: [https://arxiv.org/abs/2603.15352v1](https://arxiv.org/abs/2603.15352v1)

**摘要**
> While recent text-to-speech (TTS) systems increasingly integrate nonverbal vocalizations (NVs), their evaluations lack standardized metrics and reliable ground-truth references. To bridge this gap, we propose NV-Bench, the first benchmark grounded in a functional taxonomy that treats NVs as communicative acts rather than acoustic artifacts. NV-Bench comprises 1,651 multi-lingual, in-the-wild utterances with paired human reference audio, balanced across 14 NV categories. We introduce a dual-dimensional evaluation protocol: (1) Instruction Alignment, utilizing the proposed paralinguistic character error rate (PCER) to assess controllability, (2) Acoustic Fidelity, measuring the distributional gap to real recordings to assess acoustic realism. We evaluate diverse TTS models and develop two baselines. Experimental results demonstrate a strong correlation between our objective metrics and human perception, establishing NV-Bench as a standardized evaluation framework.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音合成」方向，核心任务由题目《NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation》所界定。 从摘要看，作者主要围绕 text-to-speech 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experimental results demonstrate a strong correlation between our objective metrics and human perception, establishing NV-Bench as a standardized evaluation framework. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：text-to-speech。 |

---
## 🏷️ Enhancement

### 1. Neural Network-Based Time-Frequency-Bin-Wise Linear Combination of Beamformers for Underdetermined Target Source Extraction

👤 **作者**: Changda Chen, Yichen Yang, Wei Liu, Shoji Makino
🔗 **来源**: [https://arxiv.org/abs/2603.15288v1](https://arxiv.org/abs/2603.15288v1)

**摘要**
> Extracting a target source from underdetermined mixtures is challenging for beamforming approaches. Recently proposed time-frequency-bin-wise switching (TFS) and linear combination (TFLC) strategies mitigate this by combining multiple beamformers in each time-frequency (TF) bin and choosing combination weights that minimize the output power. However, making this decision independently for each TF bin can weaken temporal-spectral coherence, causing discontinuities and consequently degrading extraction performance. In this paper, we propose a novel neural network-based time-frequency-bin-wise linear combination (NN-TFLC) framework that constructs minimum power distortionless response (MPDR) beamformers without explicit noise covariance estimation. The network encodes the mixture and beamformer outputs, and predicts temporally and spectrally coherent linear combination weights via a cross-attention mechanism. On dual-microphone mixtures with multiple interferers, NN-TFLC-MPDR consistently outperforms TFS/TFLC-MPDR and achieves competitive performance with TFS/TFLC built on the minimum variance distortionless response (MVDR) beamformers that require noise priors.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《Neural Network-Based Time-Frequency-Bin-Wise Linear Combination of Beamformers for Underdetermined Target Source Extraction》所界定。 从摘要看，作者主要围绕 beamforming 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：On dual-microphone mixtures with multiple interferers, NN-TFLC-MPDR consistently outperforms TFS/TFLC-MPDR and achieves competitive performance with TFS/TFLC built on the minimum variance distortionless response (MVDR) beamformers that require noise priors. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：beamforming。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. Music Genre Classification: A Comparative Analysis of Classical Machine Learning and Deep Learning Approaches

👤 **作者**: Sachin Prajuli, Abhishek Karna, OmPrakash Dhakl
🔗 **来源**: [https://arxiv.org/abs/2603.15440v1](https://arxiv.org/abs/2603.15440v1)

**摘要**
> Automatic music genre classification is a long-standing challenge in Music Information Retrieval (MIR); work on non-Western music traditions remains scarce. Nepali music encompasses culturally rich and acoustically diverse genres--from the call-and-response duets of Lok Dohori to the rhythmic poetry of Deuda and the distinctive melodies of Tamang Selo--that have not been addressed by existing classification systems. In this paper, we construct a novel dataset of approximately 8,000 labeled 30-second audio clips spanning eight Nepali music genres and conduct a systematic comparison of nine classification models across two paradigms. Five classical machine learning classifiers (Logistic Regression, SVM, KNN, Random Forest, and XGBoost) are trained on 51 hand-crafted audio features extracted via Librosa, while four deep learning architectures (CNN, RNN, parallel CNN-RNN, and sequential CNN followed by RNN) operate on Mel spectrograms of dimension 640 x 128. Our experiments reveal that the sequential Convolutional Recurrent Neural Network (CRNN)--in which convolutional layers feed into an LSTM--achieves the highest accuracy of 84%, substantially outperforming both the best classical models (Logistic Regression and XGBoost, both at 71%) and all other deep architectures. We provide per-class precision, recall, F1-score, confusion matrices, and ROC analysis for every model, and offer a culturally grounded interpretation of misclassification patterns that reflects genuine overlaps in Nepal's musical traditions.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Music Genre Classification: A Comparative Analysis of Classical Machine Learning and Deep Learning Approaches》所界定。 从摘要看，作者主要围绕 music information retrieval 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our experiments reveal that the sequential Convolutional Recurrent Neural Network (CRNN)--in which convolutional layers feed into an LSTM--achieves the highest accuracy of 84%, substantially outperforming both the best classical models (Logistic Regression and XGBoost, both at 71%) and all other deep architectures. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：music information retrieval。 |

---
### 2. spINAch: A Diachronic Corpus of French Broadcast Speech Controlled for Speakers' Age and Gender

👤 **作者**: Simon Devauchelle, David Doukhan, Rémi Uro, Lucas Ondel Yang, Valentin Pelloin, Olympia Imbert-Brégégère, Véronique Lefort, Kévin Picard, Emeline Seignobos, Albert Rilliard
🔗 **来源**: [https://arxiv.org/abs/2603.15516v1](https://arxiv.org/abs/2603.15516v1)

**摘要**
> We present spINAch, a large diachronic corpus of French speech from radio and television archives, balanced by speakers' gender, age (20-95 years old), and spanning 60 years from 1955 to 2015. The dataset includes over 320 hours of recordings from more than two thousand speakers. The methodology for building the corpus is described, focusing on the quality of collected samples in acoustic terms. The data were automatically transcribed and phonetically aligned to allow studies at a phonemic level. More than 3 million oral vowels have been analyzed to propose their fundamental frequency and formants. The corpus, available to the community for research purposes, is valuable for describing the evolution of Parisian French through the representation of gender and age. The presented analyses also demonstrate that the diachronic nature of the corpus allows the observation of various phonetic phenomena, such as the evolution of voice pitch over time (which does not differ by gender in our data) and the neutralization of the /a/-/$a$/ opposition in Parisian French during this period.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《spINAch: A Diachronic Corpus of French Broadcast Speech Controlled for Speakers' Age and Gender》所界定。 从摘要看，作者主要围绕 spinach、diachronic、corpus 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The presented analyses also demonstrate that the diachronic nature of the corpus allows the observation of various phonetic phenomena, such as the evolution of voice pitch over time (which does not differ by gender in our data) and the neutralization of the /a/-/$a$/ opposition in Parisian French during this period. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：spinach, diachronic, corpus。 |

---
### 3. AC-Foley: Reference-Audio-Guided Video-to-Audio Synthesis with Acoustic Transfer

👤 **作者**: Pengjun Fang, Yingqing He, Yazhou Xing, Qifeng Chen, Ser-Nam Lim, Harry Yang
🔗 **来源**: [https://arxiv.org/abs/2603.15597v1](https://arxiv.org/abs/2603.15597v1)

**摘要**
> Existing video-to-audio (V2A) generation methods predominantly rely on text prompts alongside visual information to synthesize audio. However, two critical bottlenecks persist: semantic granularity gaps in training data, such as conflating acoustically distinct sounds under coarse labels, and textual ambiguity in describing micro-acoustic features. These bottlenecks make it difficult to perform fine-grained sound synthesis using text-controlled modes. To address these limitations, we propose AC-Foley, an audio-conditioned V2A model that directly leverages reference audio to achieve precise and fine-grained control over generated sounds. This approach enables fine-grained sound synthesis, timbre transfer, zero-shot sound generation, and improved audio quality. By directly conditioning on audio signals, our approach bypasses the semantic ambiguities of text descriptions while enabling precise manipulation of acoustic attributes. Empirically, AC-Foley achieves state-of-the-art performance for Foley generation when conditioned on reference audio, while remaining competitive with state-of-the-art video-to-audio methods even without audio conditioning.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《AC-Foley: Reference-Audio-Guided Video-to-Audio Synthesis with Acoustic Transfer》所界定。 从摘要看，作者主要围绕 sound synthesis 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：To address these limitations, we propose AC-Foley, an audio-conditioned V2A model that directly leverages reference audio to achieve precise and fine-grained control over generated sounds. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：sound synthesis。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
