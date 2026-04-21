<div align="center">

# 📰 Paper Claw

**2026-04-21**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-20 12:14:15 CST → 2026-04-21 11:58:11 CST |
| 📄 论文总数 | **4** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 0 篇
- **TTS**: 0 篇
- **Enhancement**: 0 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 3 篇

> 💡 今日共收录 4 篇新论文，主要分布在 Speech LLM 1, Audio 3。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. Audio-DeepThinker: Progressive Reasoning-Aware Reinforcement Learning for High-Quality Chain-of-Thought Emergence in Audio Language Models

👤 **作者**: Xiang He, Chenxing Li, Jinting Wang, Yan Rong, Tianxin Xie, Wenfu Wang, Li Liu, Dong Yu
🔗 **来源**: [https://arxiv.org/abs/2604.18187v1](https://arxiv.org/abs/2604.18187v1)

**摘要**
> Large Audio-Language Models (LALMs) have made significant progress in audio understanding, yet they primarily operate as perception-and-answer systems without explicit reasoning processes. Existing methods for enhancing audio reasoning rely either on supervised chain-of-thought (CoT) fine-tuning, which is limited by training data quality, or on reinforcement learning (RL) with coarse rewards that do not directly evaluate reasoning quality. As a result, the generated reasoning chains often appear well-structured yet lack specific acoustic grounding. We propose Audio-DeepThinker, a framework built on two core ideas. First, we introduce a hybrid reasoning similarity reward that directly supervises the quality of generated reasoning chains by combining an LLM evaluator assessing logical path alignment, key step coverage, and analytical depth with an embedding similarity component enforcing semantic alignment with reference reasoning chains. Second, we propose a progressive two-stage curriculum that enables high-quality CoT reasoning to emerge through pure RL exploration, without any supervised reasoning fine-tuning, from an instruction-tuned model that possesses no prior chain-of-thought capability. Stage 1 trains on foundational audio QA with the hybrid reward to foster basic reasoning patterns, while Stage 2 shifts to acoustically challenging boundary cases with an LLM-only reward for greater reasoning diversity. Audio-DeepThinker achieves state-of-the-art results on MMAR (74.0%), MMAU-test-mini (78.5%), and MMSU (77.26%), winning 1st Place in the Interspeech 2026 Audio Reasoning Challenge (Single Model Track). Interpretability analyses further reveal that RL training primarily reshapes upper-layer MoE gating mechanisms and that reasoning tokens crystallize progressively in the upper transformer layers, offering mechanistic insights into how audio reasoning emerges through exploration.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《Audio-DeepThinker: Progressive Reasoning-Aware Reinforcement Learning for High-Quality Chain-of-Thought Emergence in Audio Language Models》所界定。 从摘要看，作者主要围绕 audio-language model 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Audio-DeepThinker achieves state-of-the-art results on MMAR (74.0%), MMAU-test-mini (78.5%), and MMSU (77.26%), winning 1st Place in the Interspeech 2026 Audio Reasoning Challenge (Single Model Track). 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：audio-language model。 |

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

### 1. Incremental learning for audio classification with Hebbian Deep Neural Networks

👤 **作者**: Riccardo Casciotti, Francesco De Santis, Alberto Antonietti, Annamaria Mesaros
🔗 **来源**: [https://arxiv.org/abs/2604.18270v1](https://arxiv.org/abs/2604.18270v1)

**摘要**
> The ability of humans for lifelong learning is an inspiration for deep learning methods and in particular for continual learning. In this work, we apply Hebbian learning, a biologically inspired learning process, to sound classification. We propose a kernel plasticity approach that selectively modulates network kernels during incremental learning, acting on selected kernels to learn new information and on others to retain previous knowledge. Using the ESC-50 dataset, the proposed method achieves 76.3% overall accuracy over five incremental steps, outperforming a baseline without kernel plasticity (68.7%) and demonstrating significantly greater stability across tasks.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Incremental learning for audio classification with Hebbian Deep Neural Networks》所界定。 从摘要看，作者主要围绕 audio classification 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Using the ESC-50 dataset, the proposed method achieves 76.3% overall accuracy over five incremental steps, outperforming a baseline without kernel plasticity (68.7%) and demonstrating significantly greater stability across tasks. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性高。摘要结构较直白，问题、方法和结果都比较容易定位。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：audio classification。 |

---
### 2. Omni-Embed-Audio: Leveraging Multimodal LLMs for Robust Audio-Text Retrieval

👤 **作者**: HaeJun Yoo, Yongseop Shin, Insung Lee, Myoung-Wan Koo, Du-Seong Chang
🔗 **来源**: [https://arxiv.org/abs/2604.18360v1](https://arxiv.org/abs/2604.18360v1)

**摘要**
> Audio-text retrieval systems based on Contrastive Language-Audio Pretraining (CLAP) achieve strong performance on traditional benchmarks; however, these benchmarks rely on caption-style queries that differ substantially from real-world search behavior, limiting their assessment of practical retrieval robustness. We present Omni-Embed-Audio (OEA), a retrieval-oriented encoder leveraging multimodal LLMs with native audio understanding. To systematically evaluate robustness beyond caption-style queries, we introduce User-Intent Queries (UIQs) - five formulations reflecting natural search behaviors: questions, commands, keyword tags, paraphrases, and exclusion-based negative queries. For negative queries, we develop a hard negative mining pipeline and propose discrimination metrics (HNSR, TFR) assessing models' ability to suppress acoustically similar distractors. Experiments on AudioCaps, Clotho, and MECAT show that OEA achieves comparable text-to-audio retrieval performance to state-of-the-art M2D-CLAP, while demonstrating clear advantages in two critical areas: (1) dominant text-to-text retrieval (+22% relative improvement), and (2) substantially superior hard negative discrimination (+4.3%p HNSR@10, +34.7% relative TFR@10), revealing that LLM backbones provide superior semantic understanding of complex queries.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Omni-Embed-Audio: Leveraging Multimodal LLMs for Robust Audio-Text Retrieval》所界定。 从摘要看，作者主要围绕 omni-embed-audio、leveraging、multimodal 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Audio-text retrieval systems based on Contrastive Language-Audio Pretraining (CLAP) achieve strong performance on traditional benchmarks; however, these benchmarks rely on caption-style queries that differ substantially from real-world search behavior, limiting their assessment of practical retrieval robustness. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：omni-embed-audio, leveraging, multimodal。 |

---
### 3. Aligning Language Models for Lyric-to-Melody Generation with Rule-Based Musical Constraints

👤 **作者**: Hao Meng, Siyuan Zheng, Shuran Zhou, Qiangqiang Wang, Yang Song
🔗 **来源**: [https://arxiv.org/abs/2604.18489v1](https://arxiv.org/abs/2604.18489v1)

**摘要**
> Large Language Models (LLMs) show promise in lyric-to-melody generation, but models trained with Supervised Fine-Tuning (SFT) often produce musically implausible melodies with issues like poor rhythm and unsuitable vocal ranges, a phenomenon we term "constraint violation". To address this, we propose a novel alignment framework that instills musical knowledge without human annotation. We define rule-based musical constraints to automatically generate a preference dataset from an SFT model's outputs. The model is then aligned through a sequential process, first using Direct Preference Optimization (DPO) on paired preference data, followed by Kahneman-Tversky Optimization (KTO) on unpaired negative samples. Experimental results demonstrate that our aligned model substantially reduces rule violations and outperforms strong baselines in both objective and subjective evaluations, generating melodies with substantially improved musicality and coherence. An interactive demo with audio comparisons is available at https://arain233.github.io/AligningMelody-demo.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Aligning Language Models for Lyric-to-Melody Generation with Rule-Based Musical Constraints》所界定。 从摘要看，作者主要围绕 aligning、language、models 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Large Language Models (LLMs) show promise in lyric-to-melody generation, but models trained with Supervised Fine-Tuning (SFT) often produce musically implausible melodies with issues like poor rhythm and unsuitable vocal ranges, a phenomenon we term "constraint violation". 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：aligning, language, models。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
