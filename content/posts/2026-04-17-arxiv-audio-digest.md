<div align="center">

# 📰 Paper Claw

**2026-04-17**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-16 12:00:42 CST → 2026-04-17 11:57:45 CST |
| 📄 论文总数 | **4** 篇 |

### 分类统计

- **Speech LLM**: 0 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 4 篇

> 💡 今日共收录 4 篇新论文，主要分布在 Audio 4。
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

### 1. From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench

👤 **作者**: Ke Xu, Yuhao Wang, Yu Wang
🔗 **来源**: [https://arxiv.org/abs/2604.15037v1](https://arxiv.org/abs/2604.15037v1)

**摘要**
> Recent advancements in LLM agents are gradually shifting from reactive, text-based paradigms toward proactive, multimodal interaction. However, existing benchmarks primarily focus on reactive responses, overlooking the complexities of proactive intervention and monitoring. To bridge this gap, we introduce ProVoice-Bench, the first evaluation framework specifically designed for proactive voice agents, featuring four novel tasks. By leveraging a multi-stage data synthesis pipeline, we curate 1,182 high-quality samples for rigorous testing. Our evaluation of state-of-the-art Multimodal LLMs reveals a significant performance gap, particularly regarding over-triggering and reasoning capabilities. These findings highlight the limitations of current models and offer a roadmap for developing more natural, context-aware proactive agents.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench》所界定。 从摘要看，作者主要围绕 from、reactive、proactive 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our evaluation of state-of-the-art Multimodal LLMs reveals a significant performance gap, particularly regarding over-triggering and reasoning capabilities. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：from, reactive, proactive。 |

---
### 2. Enhancing time-frequency resolution with optimal transport and barycentric fusion of multiple spectrogram

👤 **作者**: David Valdivia, Elsa Cazelles, Cédric Févotte
🔗 **来源**: [https://arxiv.org/abs/2604.15055v1](https://arxiv.org/abs/2604.15055v1)

**摘要**
> Time-frequency representations, such as the short-time Fourier transform (STFT), are fundamental tools for analyzing non-stationary signals. However, their ability to achieve sharp localization in both time and frequency is inherently limited by the Gabor-Heisenberg uncertainty principle. In this paper, we address this limitation by introducing a method to generate super-resolution spectrograms through the fusion of two or more spectrograms with varying resolutions. Specifically, we compute the super-resolution spectrogram as the barycenter of input spectrograms using optimal transport (OT) divergences. Unlike existing fusion approaches, our method does not require the input spectrograms to share the same time-frequency grid. Instead, the input spectrograms can be computed using any STFT parameters, and the resulting super-resolution spectrogram can be defined on an arbitrary user-specified grid. We explore various OT divergences based on different transportation costs. Notably, we introduce a novel transportation cost that preserves time-frequency geometry while significantly reducing computational complexity compared to standard Wasserstein barycenters. We adopt the unbalanced OT framework and derive a new block majorization-minimization algorithm for efficient barycenter computation. We validate the proposed method on controlled synthetic signals and recorded speech using both quantitative and qualitative evaluations. The results show that our approach combines the best localization properties of the input spectrograms and outperforms an unsupervised state-of-the-art fusion method.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Enhancing time-frequency resolution with optimal transport and barycentric fusion of multiple spectrogram》所界定。 从摘要看，作者主要围绕 enhancing、time-frequency、resolution 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：However, their ability to achieve sharp localization in both time and frequency is inherently limited by the Gabor-Heisenberg uncertainty principle. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：enhancing, time-frequency, resolution。 |

---
### 3. ControlFoley: Unified and Controllable Video-to-Audio Generation with Cross-Modal Conflict Handling

👤 **作者**: Jianxuan Yang, Xinyue Guo, Zhi Cheng, Kai Wang, Lipan Zhang, Jinjie Hu, Qiang Ji, Yihua Cao, Yihao Meng, Zhaoyue Cui, Mengmei Liu, Meng Meng, Jian Luan
🔗 **来源**: [https://arxiv.org/abs/2604.15086v1](https://arxiv.org/abs/2604.15086v1)

**摘要**
> Recent advances in video-to-audio (V2A) generation enable high-quality audio synthesis from visual content, yet achieving robust and fine-grained controllability remains challenging. Existing methods suffer from weak textual controllability under visual-text conflict and imprecise stylistic control due to entangled temporal and timbre information in reference audio. Moreover, the lack of standardized benchmarks limits systematic evaluation. We propose ControlFoley, a unified multimodal V2A framework that enables precise control over video, text, and reference audio. We introduce a joint visual encoding paradigm that integrates CLIP with a spatio-temporal audio-visual encoder to improve alignment and textual controllability. We further propose temporal-timbre decoupling to suppress redundant temporal cues while preserving discriminative timbre features. In addition, we design a modality-robust training scheme with unified multimodal representation alignment (REPA) and random modality dropout. We also present VGGSound-TVC, a benchmark for evaluating textual controllability under varying degrees of visual-text conflict. Extensive experiments demonstrate state-of-the-art performance across multiple V2A tasks, including text-guided, text-controlled, and audio-controlled generation. ControlFoley achieves superior controllability under cross-modal conflict while maintaining strong synchronization and audio quality, and shows competitive or better performance compared to an industrial V2A system. Code, models, datasets, and demos are available at: https://yjx-research.github.io/ControlFoley/.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《ControlFoley: Unified and Controllable Video-to-Audio Generation with Cross-Modal Conflict Handling》所界定。 从摘要看，作者主要围绕 audio generation 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Recent advances in video-to-audio (V2A) generation enable high-quality audio synthesis from visual content, yet achieving robust and fine-grained controllability remains challenging. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：audio generation。 |

---
### 4. A Manual Bar-by-Bar Tempo Measurement Protocol for Polyphonic Chamber Music Recordings: Design, Validation, and Application to Beethoven's Piano and Cello Sonatas

👤 **作者**: Ignasi Sole
🔗 **来源**: [https://arxiv.org/abs/2604.15278v1](https://arxiv.org/abs/2604.15278v1)

**摘要**
> Empirical performance analysis depends on the accurate extraction of tempo data from recordings, yet standard computational tools, designed for monophonic audio or modern studio conditions, fail systematically when applied to historical polyphonic chamber music. This paper documents the failure of automated beat-detection software on duo recordings of Beethoven's five piano and cello sonatas (Op.~5 Nos.~1 and~2; Op.~69; Op.~102 Nos.~1 and~2), and presents a formalised manual alternative: a cumulative lap-timer protocol that yields bar-level beats-per-minute data with millisecond resolution. The protocol, developed in cross-disciplinary collaboration with an engineer specialising in VLSI design, rests on a cumulative timestamp architecture that prevents error accumulation, permits internal self-validation, and captures expressive timing phenomena (rubato, fermatas, accelerandi, ritardandi) that automated tools systematically suppress or misread. The mathematical derivation of the BPM formula, the spreadsheet data structure, and the error characterisation are presented in full. Applied to over one hundred movement-level recordings spanning 1930--2012, the protocol generated a dataset subsequently visualised through tempographs, histograms with spline-smoothed probability density functions, ridgeline plots, and combination charts. The paper argues that manual annotation is not a methodological retreat but a principled response to the intrinsic limitations of computational tools when faced with the specific challenges of polyphonic historical recordings. The complete dataset and analysis code are publicly available.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《A Manual Bar-by-Bar Tempo Measurement Protocol for Polyphonic Chamber Music Recordings: Design, Validation, and Application to Beethoven's Piano and Cello Sonatas》所界定。 从摘要看，作者主要围绕 manual、bar-by-bar、tempo 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：This paper documents the failure of automated beat-detection software on duo recordings of Beethoven's five piano and cello sonatas (Op.~5 Nos.~1 and~2; Op.~69; Op.~102 Nos.~1 and~2), and presents a formalised manual alternative: a cumulative lap-timer protocol that yields bar-level beats-per-minute data with millisecond resolution. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：manual, bar-by-bar, tempo。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
