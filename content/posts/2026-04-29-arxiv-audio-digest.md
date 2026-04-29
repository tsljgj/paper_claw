<div align="center">

# 📰 Paper Claw

**2026-04-29**

</div>

---

## 📊 今日速览

| 指标 | 数值 |
|:---|:---|
| ⏰ 时间窗口 | 2026-04-28 12:27:52 CST → 2026-04-29 12:23:11 CST |
| 📄 论文总数 | **5** 篇 |

### 分类统计

- **Speech LLM**: 1 篇
- **ASR**: 1 篇
- **TTS**: 0 篇
- **Enhancement**: 1 篇
- **SLU**: 0 篇
- **Paralinguistics**: 0 篇
- **Audio**: 2 篇

> 💡 今日共收录 5 篇新论文，主要分布在 Speech LLM 1, ASR 1, Enhancement 1, Audio 2。
> 📈 整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。

---

## 🏷️ Speech LLM

### 1. Step-Audio-R1.5 Technical Report

👤 **作者**: Yuxin Zhang, Xiangyu Tony Zhang, Daijiao Liu, Fei Tian, Yayue Deng, Jun Chen, Qingjian Lin, Haoyang Zhang, Yuxin Li, Jinglan Gong, Yechang Huang, Liang Zhao, Chengyuan Yao, Hexin Liu, Eng Siong Chng, Xuerui Yang, Gang Yu, Xiangyu Zhang, Daxin Jiang
🔗 **来源**: [https://arxiv.org/abs/2604.25719v1](https://arxiv.org/abs/2604.25719v1)

**摘要**
> Recent advancements in large audio language models have extended Chain-of-Thought (CoT) reasoning into the auditory domain, enabling models to tackle increasingly complex acoustic and spoken tasks. To elicit and sustain these extended reasoning chains, the prevailing paradigm -- driven by the success of text-based reasoning models -- overwhelmingly relies on Reinforcement Learning with Verified Rewards (RLVR). However, as models are strictly optimized to distill rich, continuous auditory contexts into isolated, verifiable text labels, a fundamental question arises: are we fostering true audio intelligence, or merely reducing a continuous sensory medium into a discrete puzzle? We identify this as the "verifiable reward trap." While RLVR yields remarkable scores on standardized objective benchmarks, it systematically degrades the real-world conversational feel of audio models. By prioritizing isolated correctness over acoustic nuance, RLVR reduces dynamic interactions to mechanical "answering machines," severely compromising prosodic naturalness, emotional continuity, and user immersion, particularly in long-turn dialogues. To bridge the gap between mechanical objective verification and genuine sensory empathy, we introduce Step-Audio-R1.5, marking a paradigm shift toward Reinforcement Learning from Human Feedback (RLHF) in audio reasoning. Comprehensive evaluations demonstrate that Step-Audio-R1.5 not only maintains robust analytical reasoning but profoundly transforms the interactive experience, redefining the boundaries of deeply immersive long-turn spoken dialogue.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音大模型」方向，核心任务由题目《Step-Audio-R1.5 Technical Report》所界定。 从摘要看，作者主要围绕 spoken dialogue 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Comprehensive evaluations demonstrate that Step-Audio-R1.5 not only maintains robust analytical reasoning but profoundly transforms the interactive experience, redefining the boundaries of deeply immersive long-turn spoken dialogue. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：spoken dialogue。 |

---
## 🏷️ ASR

### 1. WhisperPipe: A Resource-Efficient Streaming Architecture for Real-Time Automatic Speech Recognition

👤 **作者**: Erfan Ramezani, Mohammad Mahdi Giahi, Mohammad Erfan Zarabadipour, Amir Reza Yosefian, Hamid Ghadiri
🔗 **来源**: [https://arxiv.org/abs/2604.25611v1](https://arxiv.org/abs/2604.25611v1)

**摘要**
> Real-time automatic speech recognition (ASR) systems face a fundamental trade-off between transcription accuracy and computational efficiency, particularly when deploying large-scale transformer models like Whisper. Existing streaming approaches either sacrifice accuracy through aggressive chunking or incur prohibitive memory costs through unbounded context accumulation. We present WhisperPipe, a novel streaming architecture that achieves bounded memory consumption while maintaining transcription quality through three key innovations a hybrid Voice Activity Detection (VAD) pipeline combining Silero VAD with energy-based filtering to reduce false activations by 34%, a dynamic buffering mechanism with overlapping context windows that prevents information loss at segment boundaries, and an adaptive processing strategy that balances latency and accuracy based on speech characteristics. Evaluated on 2.5 hours of diverse audio data, WhisperPipe demonstrates a median end-to-end latency of 89ms (90th percentile: 142ms) while consuming 48% less peak GPU memory and 80.9% lower average GPU utilization compared to baseline Whisper implementations. The system maintains stable memory usage over extended sessions, with zero growth rate across 150-minute continuous operation. Comparative analysis against related work shows that WhisperPipe achieves competitive accuracy (WER within 2% of offline Whisper) while operating at 3-5x lower latency than existing streaming solutions. The architecture's modular design enables deployment across resource-constrained environments, from edge devices to cloud infrastructure. Our results demonstrate that careful architectural design can reconcile the competing demands of real-time responsiveness and model sophistication in production ASR systems.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音识别」方向，核心任务由题目《WhisperPipe: A Resource-Efficient Streaming Architecture for Real-Time Automatic Speech Recognition》所界定。 从摘要看，作者主要围绕 automatic speech recognition、asr system、whisper 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：We present WhisperPipe, a novel streaming architecture that achieves bounded memory consumption while maintaining transcription quality through three key innovations a hybrid Voice Activity Detection (VAD) pipeline combining Silero VAD with energy-based filtering to reduce false activations by 34%, a dynamic buffering mechanism with overlapping context windows that prevents information loss at segment boundaries, and an adaptive processing strategy that balances latency and accuracy based on speech characteristics. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要中给出了明确指标，适合快速判断效果。 优先看这些信号词：automatic speech recognition, asr system, whisper。 |

---
## 🏷️ TTS

> 📭 今日该分类暂无新论文。

---
## 🏷️ Enhancement

### 1. UNet-Based Fusion and Exponential Moving Average Adaptation for Noise-Robust Speaker Recognition

👤 **作者**: Chong-Xin Gan, Peter Bell, Man-Wai Mak, Zhe Li, Zezhong Jin, Zilong Huang, Kong Aik Lee
🔗 **来源**: [https://arxiv.org/abs/2604.25624v1](https://arxiv.org/abs/2604.25624v1)

**摘要**
> The joint training of speech enhancement and speaker embedding networks for speaker recognition is widely adopted under noisy acoustic environments. While effective, this paradigm often fails to leverage the generalization and robustness benefits inherent in large-scale speech enhancement pre-training. Moreover, maintaining the speaker information in the denoised speech is not an explicit objective of the speech enhancement process. To address these limitations, we proposed a scalable \textbf{U}Net-based \textbf{F}usion framework (UF-EMA) that considers the noisy and enhanced speech as a multi-channel input, thereby enabling the speaker encoder to exploit speaker information effectively. In addition, an \textbf{E}xponential \textbf{M}oving \textbf{A}verage strategy is applied to a speaker encoder pre-trained on clean speech to mitigate overfitting and facilitate a smooth transition from clean to noisy conditions. Experimental results on multiple noise-contaminated test sets showcase the superiority of the proposed approach.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「语音增强」方向，核心任务由题目《UNet-Based Fusion and Exponential Moving Average Adaptation for Noise-Robust Speaker Recognition》所界定。 从摘要看，作者主要围绕 speech enhancement、speaker recognition 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Experimental results on multiple noise-contaminated test sets showcase the superiority of the proposed approach. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：speech enhancement, speaker recognition。 |

---
## 🏷️ SLU

> 📭 今日该分类暂无新论文。

---
## 🏷️ Paralinguistics

> 📭 今日该分类暂无新论文。

---
## 🏷️ Audio

### 1. Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models

👤 **作者**: Chun-Yi Kuan, Wei-Ping Huang, Hung-yi Lee
🔗 **来源**: [https://arxiv.org/abs/2604.25591v1](https://arxiv.org/abs/2604.25591v1)

**摘要**
> Recent audio-aware large language models (ALLMs) have demonstrated strong capabilities across diverse audio understanding and reasoning tasks, but they still frequently produce hallucinated or overly confident outputs. While uncertainty estimation has been extensively studied in text-only LLMs, it remains largely unexplored for ALLMs, where audio-conditioned generation introduces additional challenges such as perceptual ambiguity and cross-modal grounding. In this work, we present the first systematic empirical study of uncertainty estimation in ALLMs. We benchmark five representative methods, including predictive entropy, length-normalized entropy, semantic entropy, discrete semantic entropy, and P(True), across multiple models and diverse evaluation settings spanning general audio understanding, reasoning, hallucination detection, and unanswerable question answering. Our results reveal two key findings. First, semantic-level and verification-based methods consistently outperform token-level baselines on general audio reasoning benchmarks. Second, on trustworthiness-oriented benchmarks, the relative effectiveness of uncertainty methods becomes notably more model- and benchmark-dependent, indicating that conclusions drawn from general reasoning settings do not straightforwardly transfer to hallucination and unanswerable-question scenarios. We further explore uncertainty-based adaptive inference as a potential downstream application. We hope this study provides a foundation for future research on reliable, uncertainty-aware audio-language systems.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models》所界定。 从摘要看，作者主要围绕 walking、through、uncertainty 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Recent audio-aware large language models (ALLMs) have demonstrated strong capabilities across diverse audio understanding and reasoning tasks, but they still frequently produce hallucinated or overly confident outputs. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性中。需要一定领域背景，但主线仍然清楚。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：walking, through, uncertainty。 |

---
### 2. Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation

👤 **作者**: Yupeng Zhou, Lianghua Huang, Zhifan Wu, Jiabao Wang, Yupeng Shi, Biao Jiang, Daquan Zhou, Yu Liu, Ming-Ming Cheng, Qibin Hou
🔗 **来源**: [https://arxiv.org/abs/2604.25819v1](https://arxiv.org/abs/2604.25819v1)

**摘要**
> In this work, we propose Mutual Forcing, a framework for fast autoregressive audio-video generation with long-horizon audio-video synchronization. Our approach addresses two key challenges: joint audio-video modeling and fast autoregressive generation. To ease joint audio-video optimization, we adopt a two-stage training strategy: we first train uni-modal generators and then couple them into a unified audio-video model for joint training on paired data. For streaming generation, we ask whether a native fast causal audio-video model can be trained directly, instead of following existing streaming distillation pipelines that typically train a bidirectional model first and then convert it into a causal generator through multiple distillation stages. Our answer is Mutual Forcing, which builds directly on native autoregressive model and integrates few-step and multi-step generation within a single weight-shared model, enabling self-distillation and improved training-inference consistency. The multi-step mode improves the few-step mode via self-distillation, while the few-step mode generates historical context during training to improve training-inference consistency; because the two modes share parameters, these two effects reinforce each other within a single model. Compared with prior approaches such as Self-Forcing, Mutual Forcing removes the need for an additional bidirectional teacher model, supports more flexible training sequence lengths, reduces training overhead, and allows the model to improve directly from real paired data rather than a fixed teacher. Experiments show that Mutual Forcing matches or surpasses strong baselines that require around 50 sampling steps while using only 4 to 8 steps, demonstrating substantial advantages in both efficiency and quality. The project page is available at https://mutualforcing.github.io.

**综合评价**
| 项目 | 内容 |
|:---|:---|
| 📝 总结 | 这篇工作归入「通用音频」方向，核心任务由题目《Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation》所界定。 从摘要看，作者主要围绕 mutual、forcing、dual-mode 展开方法设计、训练策略或系统建模。 结果部分最值得注意的是：Our answer is Mutual Forcing, which builds directly on native autoregressive model and integrates few-step and multi-step generation within a single weight-shared model, enabling self-distillation and improved training-inference consistency. 如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。 |
| 📖 可读性 | 可读性偏低。缩写、设定或实验细节较多，首次浏览成本偏高。 摘要更偏方法描述，建议点开原文确认实验细节。 优先看这些信号词：mutual, forcing, dual-mode。 |

---

<div align="center">

*Generated by [Paper Claw](https://github.com/yourusername/paper_claw)*

</div>
