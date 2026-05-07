<div align="center">

# 📰 Paper Claw

**2026-05-07**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-05-06 12:27:39 CST → 2026-05-07 12:27:47 CST |
| 📄 论文总数 | **2** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 2 篇新论文，主要分布在 Audio 2。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

> 📭 今日该分类暂无新论文。

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

### 1. Hearing the Ocean: Bio-inspired Gammatone-CNN framework for Robust Underwater Acoustic Target Classification

👤 **作者**: Rajeshwar Tripathi, Sandeep Kumar, Monika Aggarwal, Neel Kanth Kundu
🔗 **来源**: [https://arxiv.org/abs/2605.04839v1](https://arxiv.org/abs/2605.04839v1)

**摘要**
> This study presents a bio inspired signal processing framework for robust Underwater Acoustic Target Recognition (UATR). The latest state of the art methods often fail to resolve dense low frequency harmonic structures in vessel propulsion signals under high noise conditions, which is addressed by the proposed framework using a biologically inspired Gammatone filter bank that emulates the cochlea nonlinear frequency selectivity. By distributing filters according to the Equivalent Rectangular Bandwidth (ERB) scale, the framework achieves a high fidelity representation of engine radiated tonals while effectively suppressing isotropic ambient interference. The resulting Cochleagram features are processed by a lightweight, custom designed Convolutional Neural Network (CNN) that leverages large receptive fields to integrate spectral-temporal continuities. Experimental results on the VTUAD dataset demonstrate a state of the art classification accuracy of 98.41%, outperforming Continuous Wavelet Transform and Mel Frequency Cepstral Coefficients baselines by 3.5% and 7.7% respectively. Furthermore, the framework achieves an inference latency of only 0.77 ms and a 0.971 Cohen Kappa score, validating its efficacy for real time deployment on autonomous, low-power sonar hardware.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Hearing the Ocean: Bio-inspired Gammatone-CNN framework for Robust Underwater Acoustic Target Classification》所界定。 从摘要看，作者主要围绕 hearing、ocean、bio-inspired 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：By distributing filters according to the Equivalent Rectangular Bandwidth (ERB) scale, the framework achieves a high fidelity representation of engine radiated tonals while effectively suppressing isotropic ambient interference. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：hearing, ocean, bio-inspired。 |

---
### 2. Empirical Study of Pop and Jazz Mix Ratios for Genre-Adaptive Chord Generation

👤 **作者**: Jinju Lee
🔗 **来源**: [https://arxiv.org/abs/2605.04998v1](https://arxiv.org/abs/2605.04998v1)

**摘要**
> Chord progression generation is practically important but understudied. Most large-scale symbolic music systems target melody, multi-track arrangement, or audio synthesis, and chord-only models tend to be relegated to conditioning components inside larger pipelines. This paper treats chord generation as a standalone task and addresses a question that arises whenever such a model is adapted across genres: how much old-domain data must be retained during fine-tuning to acquire a new domain without forgetting the old? I study jazz fine-tuning starting from a pop-pretrained 25M-parameter Music Transformer (84.24% top-1 chord accuracy on a held-out pop test set). The available jazz corpus is an order of magnitude smaller than the pop corpus, so every fine-tune run uses all 1,513 jazz training sequences. The swept variable is the volume of pop "rehearsal" data mixed alongside, taking values in {0, 1K, 2.5K, 5K, 10K}. Every fine-tuned model gains 7 to 9 points of jazz top-1. Pop accuracy collapses by 2.14 points under jazz-only fine-tuning, recovers to baseline at approximately 2.5K rehearsal samples (1.65x the jazz volume), and saturates beyond that point. A complementary observation: the metric-best run (F3, 2.5K mix) is not always the perceptually preferred one. The pop-leaning (10K) and jazz-leaning (1K) endpoints carry more committed stylistic identities that the author more often selects as finished output in informal listening. I discuss what this suggests for music co-creation tools but make no perceptual claim, since no formal listening study has been conducted. All six checkpoints are released on the HuggingFace Hub at https://huggingface.co/PearlLeeStudio.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Empirical Study of Pop and Jazz Mix Ratios for Genre-Adaptive Chord Generation》所界定。 从摘要看，作者主要围绕 empirical、study、jazz 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Most large-scale symbolic music systems target melody, multi-track arrangement, or audio synthesis, and chord-only models tend to be relegated to conditioning components inside larger pipelines. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：empirical, study, jazz。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
