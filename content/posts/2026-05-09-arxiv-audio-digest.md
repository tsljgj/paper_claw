<div align="center">

# 📰 Paper Claw

**2026-05-09**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-05-07 12:27:47 CST → 2026-05-09 12:16:50 CST |
| 📄 论文总数 | **7** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 5 篇

> 💡 今日共收录 7 篇新论文，主要分布在 Speech LLM 1, Enhancement 1, Audio 5。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. WavCube: Unifying Speech Representation for Understanding and Generation via Semantic-Acoustic Joint Modeling

👤 **作者**: Guanrou Yang, Tian Tan, Qian Chen, Zhikang Niu, Yakun Song, Ziyang Ma, Yushen Chen, Zeyu Xie, Tianrui Wang, Yifan Yang, Wenxi Chen, Qi Chen, Wenrui Liu, Shan Yang, Xie Chen
🔗 **来源**: [https://arxiv.org/abs/2605.06407v1](https://arxiv.org/abs/2605.06407v1)

**摘要**
> Integrating speech understanding and generation is a pivotal step toward building unified speech models. However, the different representations required for these two tasks currently pose significant compatibility challenges. Typically, semantics-oriented features are learned from self-supervised learning (SSL), and acoustic-oriented features from reconstruction. Such fragmented representations hinder the realization of truly unified speech systems. We present WavCube, a compact continuous latent derived from an SSL speech encoder that simultaneously supports speech understanding, reconstruction, and generation. WavCube employs a two-stage training scheme. Stage 1 trains a semantic bottleneck to filter off-manifold redundancy that makes raw SSL features intractable for diffusion. Stage 2 injects fine-grained acoustic details via end-to-end reconstruction, while a semantic anchoring loss ensures the representation remains grounded within its original semantic manifold. Comprehensive experiments show that WavCube closely approaches WavLM performance on SUPERB despite an 8x dimensional compression, attains reconstruction quality on par with existing acoustic representations, delivers state-of-the-art zero-shot TTS performance with markedly faster training convergence, and excels in speech enhancement, separation, and voice conversion tasks on the SUPERB-SG benchmark. Systematic ablations reveal that WavCube's two-stage recipe resolves two intrinsic flaws of SSL features for generative modeling, paving the way for future unified speech systems. Codes and checkpoints are available at https://github.com/yanghaha0908/WavCube.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《WavCube: Unifying Speech Representation for Understanding and Generation via Semantic-Acoustic Joint Modeling》所界定。 从摘要看，作者主要围绕 speech understanding、speech enhancement 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Comprehensive experiments show that WavCube closely approaches WavLM performance on SUPERB despite an 8x dimensional compression, attains reconstruction quality on par with existing acoustic representations, delivers state-of-the-art zero-shot TTS performance with markedly faster training convergence, and excels in speech enhancement, separation, and voice conversion tasks on the SUPERB-SG benchmark. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech understanding, speech enhancement。 |

---
## 🏷️ ASR

> 📭 今日该分类暂无新论文。

---
## 🏷️ TTS

> 📭 今日该分类暂无新论文。

---
## 🏷️ Enhancement

### 1. Predictive-Generative Drift Decomposition for Speech Enhancement and Separation

👤 **作者**: Julius Richter, Yoshiki Masuyama, Christoph Boeddeker, Takahiro Edo, Gordon Wichern, Jonathan Le Roux
🔗 **来源**: [https://arxiv.org/abs/2605.06189v1](https://arxiv.org/abs/2605.06189v1)

**摘要**
> We propose a plug-and-play framework for speech enhancement and separation that augments predictive methods with a generative speech prior. Our approach, termed Stochastic Interpolant Prior for Speech (SIPS), builds on stochastic interpolants and leverages their flexibility to bridge predictive and generative modeling. Specifically, we decompose the interpolation dynamics into a task-specific drift and a stochastic denoising component, allowing a predictive estimate to be integrated directly into the generative sampling process. This results in a mathematically grounded framework for combining strong pretrained predictors with the expressive power of generative models. To this end, we train a score model using only clean speech, yielding a degradation-agnostic prior that can be reused across tasks. During inference, the predictor provides a deterministic drift that steers the sampling process toward a task-consistent estimate, while the score model preserves perceptual naturalness. Unlike prior hybrid approaches, which typically rely on architecture-specific conditioning and are tied to particular predictors or degradation settings, SIPS provides a unified framework that generalizes across predictors and additive degradation tasks. We demonstrate its effectiveness for both speech enhancement and speech separation using recent predictors such as SEMamba and FlexIO. The proposed method consistently improves perceptual quality, achieving gains up +1.0 NISQA for speech separation.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《Predictive-Generative Drift Decomposition for Speech Enhancement and Separation》所界定。 从摘要看，作者主要围绕 speech enhancement、speech separation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We demonstrate its effectiveness for both speech enhancement and speech separation using recent predictors such as SEMamba and FlexIO. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech enhancement, speech separation。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization

👤 **作者**: Adhiraj Banerjee, Vipul Arora
🔗 **来源**: [https://arxiv.org/abs/2605.06582v1](https://arxiv.org/abs/2605.06582v1)

**摘要**
> Many operations on sensory data -- comparison, memory, retrieval, and reasoning -- are naturally expressed over discrete symbolic structures. In language this interface is given by tokens; in audio, it must be learned. Existing audio tokenizers rely on quantization, clustering, or codec reconstruction, assigning tokens locally, so sequence consistency, compactness, length control, termination, and edit similarity are rarely optimized directly. We introduce PairAlign, a framework for compact audio tokenization through sequence-level self-alignment. PairAlign treats tokenization as conditional sequence generation: an encoder maps speech to a continuous condition, and an autoregressive decoder generates tokens from BOS, learning token identity, order, length, and EOS placement. Given two content-preserving views, each view's sequence is trained to be likely under the other's representation, while unrelated examples provide competing sequences. This gives a scalable surrogate for edit-distance preservation while discouraging many-to-one collapse. PairAlign starts from VQ-style tokenization and refines it with EMA-teacher targets, cross-paired teacher forcing, prefix corruption, likelihood contrast, and length control. On 3-second speech, PairAlign learns compact, non-degenerate sequences with broad vocabulary usage and strong cross-view consistency. On TIMIT retrieval, it preserves edit-distance search while reducing archive token count by 55%. A continuous-sweep probe shows lower local overlap than a dense geometric tokenizer, but stronger length control and bounded edit trajectories under 100 ms shifts. PairAlign is a sequence-symbolic predictive learner: like JEPA-style objectives, it predicts an abstract target from another view as a learned variable-length symbolic sequence, not a continuous latent.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization》所界定。 从摘要看，作者主要围绕 pairalign、framework、sequence 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：A continuous-sweep probe shows lower local overlap than a dense geometric tokenizer, but stronger length control and bounded edit trajectories under 100 ms shifts. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：pairalign, framework, sequence。 |

---
### 2. Weight-Decay Turns Transformer Loss Landscapes Villani: Functional-Analytic Foundations for Optimization and Generalization

👤 **作者**: Abhijit Das, Sayantan Dutta
🔗 **来源**: [https://arxiv.org/abs/2605.06599v1](https://arxiv.org/abs/2605.06599v1)

**摘要**
> Weight decay is widely used as a regularizer in large language models, yet its precise role in shaping Transformer loss landscapes remains theoretically underexplored. This paper provides the first rigorous functional-analytic characterization of the standard Transformer objective--cross-entropy loss with $L^2$ regularization--by proving it satisfies Villani's criteria for coercive energy functions. Specifically, we show that the regularized loss $\mathcal{F}$ is infinitely differentiable, grows at least quadratically, has Gaussian-integrable tails, and satisfies the differential growth condition $-Δ\mathcal{F} + \tfrac{1}{s}\|\nabla\mathcal{F}\|^{2} \to \infty$ as $\|θ\| \to \infty$ for all $s>0$. From this structure, we derive explicit log-Sobolev and Poincaré constants $C_{\mathrm{LS}} \leq λ^{-1} + d/λ^{2}$, linking the regularization strength $λ$ and model dimension $d$ to finite-time convergence guarantees for noisy stochastic gradient descent and PAC-Bayesian generalization bounds that tighten with increasing $λ$. To validate our theory, we introduce a scalable Villani diagnostic $Ψ_s(θ) = -Δ\mathcal{F} + s^{-1}\|\nabla \mathcal{F}\|^2$ and estimate it efficiently using Hutchinson trace probes in models with over 100M parameters. Experiments on GPT-Neo-125M across Penn Treebank and WikiText-103 confirm the predicted quadratic growth of $Ψ_s$, spectral inflation of the Hessian, and exponential convergence behavior consistent with our log-Sobolev analysis. These results demonstrate that weight decay not only improves generalization empirically but also establishes the mathematical conditions required for fast Langevin mixing and theoretically grounded curvature-aware optimization in deep learning.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Weight-Decay Turns Transformer Loss Landscapes Villani: Functional-Analytic Foundations for Optimization and Generalization》所界定。 从摘要看，作者主要围绕 weight-decay、turns、transformer 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Specifically, we show that the regularized loss $\mathcal{F}$ is infinitely differentiable, grows at least quadratically, has Gaussian-integrable tails, and satisfies the differential growth condition $-Δ\mathcal{F} + \tfrac{1}{s}\|\nabla\mathcal{F}\|^{2} \to \infty$ as $\|θ\| \to \infty$ for all $s>0$. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：weight-decay, turns, transformer。 |

---
### 3. PianoCoRe: Combined and Refined Piano MIDI Dataset

👤 **作者**: Ilya Borovik
🔗 **来源**: [https://arxiv.org/abs/2605.06627v1](https://arxiv.org/abs/2605.06627v1)

**摘要**
> Symbolic music datasets with matched scores and performances are essential for many music information retrieval (MIR) tasks. Yet, existing resources often cover a narrow range of composers, lack performance variety, omit note-level alignments, or use inconsistent naming formats. This work presents PianoCoRe, a large-scale piano MIDI dataset that unifies and refines major open-source piano corpora. The dataset contains 250,046 performances of 5,625 pieces written by 483 composers, totaling 21,763 h of performed music. PianoCoRe is released in tiered subsets to support different applications: from large-scale analysis and pre-training (PianoCoRe-C and deduplicated PianoCoRe-B) to expressive performance modeling with note-level score alignment (PianoCoRe-A/A*). The note-aligned subset, PianoCoRe-A, provides the largest open-source collection of 157,207 performances aligned to 1,591 scores to date. In addition to the dataset, the contributions are: (1) a MIDI quality classifier for detecting corrupted and score-like transcriptions and (2) RAScoP, an alignment refinement pipeline that cleans temporal alignment errors and interpolates missing notes. The analysis shows that the refinement reduces temporal noise and eliminates tempo outliers. Moreover, an expressive performance rendering model trained on PianoCoRe demonstrates improved robustness to unseen pieces compared to models trained on raw or smaller datasets. PianoCoRe provides a ready-to-use foundation for the next generation of expressive piano performance research.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《PianoCoRe: Combined and Refined Piano MIDI Dataset》所界定。 从摘要看，作者主要围绕 music information retrieval 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The analysis shows that the refinement reduces temporal noise and eliminates tempo outliers. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：music information retrieval。 |

---
### 4. LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation

👤 **作者**: Dan Jacobellis, Neeraja J. Yadwadkar
🔗 **来源**: [https://arxiv.org/abs/2605.06628v1](https://arxiv.org/abs/2605.06628v1)

**摘要**
> Modern sensors generate rich, high-fidelity data, yet applications operating on wearable or remote sensing devices remain constrained by bandwidth and power budgets. Standardized codecs such as JPEG and MPEG achieve efficient trade-offs between bitrate and perceptual quality but are designed for human perception, limiting their applicability to machine-perception tasks and non-traditional modalities such as spatial audio arrays, hyperspectral images, and 3D medical images. General-purpose compression schemes based on scalar quantization or resolution reduction are broadly applicable but fail to exploit inherent signal redundancies, resulting in suboptimal rate-distortion performance. Recent generative neural codecs, or tokenizers, model complex signal dependencies but are often over-parameterized, data-hungry, and modality-specific, making them impractical for resource-constrained environments. We introduce a Lightweight, Versatile, and Asymmetric neural codec architecture (LiVeAction), that addresses these limitations through two key ideas. (1) To reduce the complexity of the encoder to meet the resource constraints of the execution environments, we impose an FFT-like structure and reduce the overall size and depth of the neural-network-based analysis transform. (2) To allow arbitrary signal modalities and simplify training, we replace adversarial and perceptual losses with a variance-based rate penalty. Our design produces codecs that deliver superior rate-distortion performance compared to state-of-the-art generative tokenizers, while remaining practical for deployment on low-power sensors. We release our code, experiments, and python library at https://github.com/UT-SysML/liveaction .

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation》所界定。 从摘要看，作者主要围绕 liveaction、lightweight、versatile 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Standardized codecs such as JPEG and MPEG achieve efficient trade-offs between bitrate and perceptual quality but are designed for human perception, limiting their applicability to machine-perception tasks and non-traditional modalities such as spatial audio arrays, hyperspectral images, and 3D medical images. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：liveaction, lightweight, versatile。 |

---
### 5. Task-Aware Answer Preservation under Audio Compression for Large Audio Language Models

👤 **作者**: Amir Ivry
🔗 **来源**: [https://arxiv.org/abs/2605.06631v1](https://arxiv.org/abs/2605.06631v1)

**摘要**
> Large audio language models (LALMs) are increasingly used to reason over long audio clips, yet deployment often compresses audio before inference to reduce memory and latency. The risk is that compression can leave aggregate accuracy acceptable while sharply degrading answers for a deployment-critical query family. We study answer-preserving audio compression, judging a compressor by the excess answer-error it induces, especially for the worst-affected family. We formulate this theoretically as a compressor acceptance-rejection criterion, derive a practical sign-off protocol that returns compression budgets satisfying worst-family checks with statistical confidence, and evaluate it on five multiple-choice audio question-answering benchmarks with two Qwen-based backbones. The protocol exposes hidden family-level damage, shows that the chosen query-family partition can change the approved budget, and identifies regimes where query-conditioned compression helps maintain answer preservation.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Task-Aware Answer Preservation under Audio Compression for Large Audio Language Models》所界定。 从摘要看，作者主要围绕 task-aware、answer、preservation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：The protocol exposes hidden family-level damage, shows that the chosen query-family partition can change the approved budget, and identifies regimes where query-conditioned compression helps maintain answer preservation. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：task-aware, answer, preservation。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
