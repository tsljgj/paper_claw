<div align="center">

# 📰 Paper Claw

**2026-03-18**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-03-17 11:27:30 CST → 2026-03-18 11:34:28 CST |
| 📄 论文总数 | **5** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 1 篇
- **TTS**: 0 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 3 篇

> 💡 今日共收录 5 篇新论文，主要分布在 ASR 1, Enhancement 1, Audio 3。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

---
## 🏷️ ASR

### 1. RECOVER: Robust Entity Correction via agentic Orchestration of hypothesis Variants for Evidence-based Recovery

👤 **作者**: Abhishek Kumar, Aashraya Sachdeva
🔗 **来源**: [https://arxiv.org/abs/2603.16411v1](https://arxiv.org/abs/2603.16411v1)

**摘要**
> Entity recognition in Automatic Speech Recognition (ASR) is challenging for rare and domain-specific terms. In domains such as finance, medicine, and air traffic control, these errors are costly. If the entities are entirely absent from the ASR output, post-ASR correction becomes difficult. To address this, we introduce RECOVER, an agentic correction framework that serves as a tool-using agent. It leverages multiple hypotheses as evidence from ASR, retrieves relevant entities, and applies Large Language Model (LLM) correction under constraints. The hypotheses are used using different strategies, namely, 1-Best, Entity-Aware Select, Recognizer Output Voting Error Reduction (ROVER) Ensemble, and LLM-Select. Evaluated across five diverse datasets, it achieves 8-46% relative reductions in entity-phrase word error rate (E-WER) and increases recall by up to 22 percentage points. The LLM-Select achieves the best overall performance in entity correction while maintaining overall WER.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《RECOVER: Robust Entity Correction via agentic Orchestration of hypothesis Variants for Evidence-based Recovery》所界定。 从摘要看，作者主要围绕 automatic speech recognition 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Evaluated across five diverse datasets, it achieves 8-46% relative reductions in entity-phrase word error rate (E-WER) and increases recall by up to 22 percentage points. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：automatic speech recognition。 |

---
## 🏷️ TTS

> 📭 今日该分类暂无新论文。

---
## 🏷️ Enhancement

### 1. HRTF-guided Binaural Target Speaker Extraction with Real-World Validation

👤 **作者**: Yoav Ellinson, Sharon Gannot
🔗 **来源**: [https://arxiv.org/abs/2603.16668v1](https://arxiv.org/abs/2603.16668v1)

**摘要**
> This paper presents a Head-Related Transfer Function (HRTF)-guided framework for binaural Target Speaker Extraction (TSE) from mixtures of concurrent sources. Unlike conventional TSE methods based on Direction of Arrival (DOA) estimation or enrollment signals, which often distort perceived spatial location, the proposed approach leverages the listener's HRTF as an explicit spatial prior. The proposed framework is built upon a multi-channel deep blind source separation backbone, adapted to the binaural TSE setting. It is trained on measured HRTFs from a diverse population, enabling cross-listener generalization rather than subject-specific tuning. By conditioning the extraction on HRTF-derived spatial information, the method preserves binaural cues while enhancing speech quality and intelligibility. The performance of the proposed framework is validated through simulations and real recordings obtained from a head and torso simulator (HATS).

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《HRTF-guided Binaural Target Speaker Extraction with Real-World Validation》所界定。 从摘要看，作者主要围绕 source separation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Unlike conventional TSE methods based on Direction of Arrival (DOA) estimation or enrollment signals, which often distort perceived spatial location, the proposed approach leverages the listener's HRTF as an explicit spatial prior. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：source separation。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. A Semantic Timbre Dataset for the Electric Guitar

👤 **作者**: Joseph Cameron, Alan Blackwell
🔗 **来源**: [https://arxiv.org/abs/2603.16682v1](https://arxiv.org/abs/2603.16682v1)

**摘要**
> Understanding and manipulating timbre is central to audio synthesis, yet this remains under-explored in machine learning due to a lack of annotated datasets linking perceptual timbre dimensions to semantic descriptors. We present the Semantic Timbre Dataset, a curated collection of monophonic electric guitar sounds, each labeled with one of 19 semantic timbre descriptors and corresponding magnitudes. These descriptors were derived from a qualitative analysis of physical and virtual guitar effect units and applied systematically to clean guitar tones. The dataset bridges perceptual timbre and machine learning representations, supporting learning for timbre control and semantic audio generation. We validate the dataset by training a variational autoencoder (VAE) on its latent space and evaluating it using human perceptual judgments and descriptor classifiers. Results show that the VAE captures timbral structure and enables smooth interpolation across descriptors. We release the dataset, code, and evaluation protocols to support timbre-aware generative AI research.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《A Semantic Timbre Dataset for the Electric Guitar》所界定。 从摘要看，作者主要围绕 audio generation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Results show that the VAE captures timbral structure and enables smooth interpolation across descriptors. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio generation。 |

---
### 2. Evaluating Latent Space Structure in Timbre VAEs: A Comparative Study of Unsupervised, Descriptor-Conditioned, and Perceptual Feature-Conditioned Models

👤 **作者**: Joseph Cameron, Alan Blackwell
🔗 **来源**: [https://arxiv.org/abs/2603.16713v1](https://arxiv.org/abs/2603.16713v1)

**摘要**
> We present a comparative evaluation of latent space organization in three Variational Autoencoders (VAEs) for musical timbre generation: an unsupervised VAE, a descriptor-conditioned VAE, and a VAE conditioned on continuous perceptual features from the AudioCommons timbral models. Using a curated dataset of electric guitar sounds labeled with 19 semantic descriptors across four intensity levels, we assess each model's latent structure with a suite of clustering and interpretability metrics. These include silhouette scores, timbre descriptor compactness, pitch-conditional separation, trajectory linearity, and cross-pitch consistency. Our findings show that conditioning on perceptual features yields a more compact, discriminative, and pitch-invariant latent space, outperforming both the unsupervised and discrete descriptor-conditioned models. This work highlights the limitations of one-hot semantic conditioning and provides methodological tools for evaluating timbre latent spaces, contributing to the development of more controllable and interpretable generative audio models.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Evaluating Latent Space Structure in Timbre VAEs: A Comparative Study of Unsupervised, Descriptor-Conditioned, and Perceptual Feature-Conditioned Models》所界定。 从摘要看，作者主要围绕 evaluating、latent、space 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our findings show that conditioning on perceptual features yields a more compact, discriminative, and pitch-invariant latent space, outperforming both the unsupervised and discrete descriptor-conditioned models. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：evaluating, latent, space。 |

---
### 3. Making Separation-First Multi-Stream Audio Watermarking Feasible via Joint Training

👤 **作者**: Houmin Sun, Zi Hu, Linxi Li, Yechen Wang, Liwei Jin, Ming Li
🔗 **来源**: [https://arxiv.org/abs/2603.16805v1](https://arxiv.org/abs/2603.16805v1)

**摘要**
> Modern audio is created by mixing stems from different sources, raising the question: can we independently watermark each stem and recover all watermarks after separation? We study a separation-first, multi-stream watermarking framework-embedding distinct information into stems using unique keys but a shared structure, mixing, separating, and decoding from each output. A naive pipeline (robust watermarking + off-the-shelf separation) yields poor bit recovery, showing robustness to generic distortions does not ensure robustness to separation artifacts. To enable this, we jointly train the watermark system and the separator in an end-to-end manner, encouraging the separator to preserve watermark cues while adapting embedding to separation-specific distortions. Experiments on speech+music and vocal+accompaniment mixtures show substantial gains in post-separation recovery while maintaining perceptual quality.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Making Separation-First Multi-Stream Audio Watermarking Feasible via Joint Training》所界定。 从摘要看，作者主要围绕 making、separation-first、multi-stream 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：A naive pipeline (robust watermarking + off-the-shelf separation) yields poor bit recovery, showing robustness to generic distortions does not ensure robustness to separation artifacts. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：making, separation-first, multi-stream。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
