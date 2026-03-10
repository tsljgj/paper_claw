import json
import logging
import os
import re
from collections import Counter
from typing import Any

import requests


CATEGORY_RULES = {
    "Speech LLM": [
        "speech llm",
        "spoken llm",
        "speech language model",
        "speech large language model",
        "audio language model",
        "audio large language model",
        "speechgpt",
        "audiollm",
        "speech instruction",
        "spoken dialogue model",
        "speech question answering",
        "speech-to-llm",
        "audio-to-llm",
        "llm-based speech",
        "multimodal llm for speech",
    ],
    "ASR": [
        "asr",
        "automatic speech recognition",
        "speech recognition",
        "streaming asr",
        "streaming recognition",
        "transducer",
        "ctc",
        "rnnt",
        "multilingual asr",
        "audiovisual speech recognition",
        "avsr",
    ],
    "TTS": [
        "tts",
        "text-to-speech",
        "speech synthesis",
        "neural vocoder",
        "vocoder",
        "voice conversion",
        "singing synthesis",
        "controllable tts",
    ],
    "Enhancement": [
        "speech enhancement",
        "denois",
        "dereverb",
        "dereverberation",
        "aec",
        "acoustic echo cancellation",
        "source separation",
        "speech separation",
        "target speaker extraction",
        "beamforming",
    ],
    "SLU": [
        "spoken language understanding",
        "speaker verification",
        "speaker identification",
        "language identification",
        "keyword spotting",
        "slot filling",
        "intent detection",
        "diarization",
    ],
    "Paralinguistics": [
        "emotion",
        "affective",
        "depression",
        "cognitive",
        "age estimation",
        "gender",
        "deepfake",
        "spoof",
        "anti-spoofing",
        "pathological speech",
        "paralinguistic",
    ],
    "Audio": [
        "audio",
        "acoustic event",
        "sound event",
        "sound scene",
        "music",
        "bioacoustic",
        "environmental sound",
        "sonification",
        "compression",
    ],
}

CATEGORY_PRIORITY = [
    "Speech LLM",
    "ASR",
    "TTS",
    "Enhancement",
    "SLU",
    "Paralinguistics",
    "Audio",
]

CATEGORY_LABELS_ZH = {
    "Speech LLM": "语音大模型",
    "ASR": "语音识别",
    "TTS": "语音合成",
    "Enhancement": "语音增强",
    "SLU": "口语理解",
    "Paralinguistics": "副语言学",
    "Audio": "通用音频",
}


def _normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().lower()


def extract_keywords(title: str, abstract: str) -> list[str]:
    haystack = _normalize_text(f"{title} {abstract}")
    matched: list[str] = []
    for keywords in CATEGORY_RULES.values():
        for keyword in keywords:
            if keyword in haystack and keyword not in matched:
                matched.append(keyword)
    if not matched:
        tokens = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", haystack)
        matched = list(dict.fromkeys(tokens[:6]))
    return matched[:8]


def classify_paper(title: str, abstract: str, keywords: list[str]) -> str:
    haystack = _normalize_text(" ".join([title, abstract, " ".join(keywords)]))
    scores = Counter()
    for category, rules in CATEGORY_RULES.items():
        for keyword in rules:
            if keyword in haystack:
                scores[category] += max(1, len(keyword.split()))
    if not scores:
        return "Audio"
    return sorted(scores.items(), key=lambda item: (-item[1], CATEGORY_PRIORITY.index(item[0])))[0][0]


def maybe_openai_json(prompt_text: str, payload: list[dict[str, Any]]) -> list[dict[str, Any]] | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not payload:
        return None

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": "gpt-4.1-mini",
            "temperature": 0.2,
            "input": [
                {
                    "role": "system",
                    "content": prompt_text,
                },
                {
                    "role": "user",
                    "content": json.dumps(payload, ensure_ascii=False),
                },
            ],
        },
        timeout=90,
    )
    response.raise_for_status()
    data = response.json()
    chunks: list[str] = []
    for item in data.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                chunks.append(content.get("text", ""))
    if not chunks:
        return None
    try:
        parsed = json.loads("".join(chunks))
    except json.JSONDecodeError:
        logging.warning("OpenAI response was not valid JSON; falling back to deterministic summaries.")
        return None
    if isinstance(parsed, list):
        return parsed
    return None


def _extract_claim_sentence(abstract: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", abstract.strip())
    if not sentences:
        return ""
    for sentence in sentences:
        lowered = sentence.lower()
        if any(token in lowered for token in ["outperform", "improv", "achiev", "show", "demonstrat", "state-of-the-art"]):
            return sentence.strip()
    return sentences[min(1, len(sentences) - 1)].strip()


def _extract_method_cue(abstract: str, keywords: list[str]) -> str:
    if keywords:
        return "、".join(keywords[:3])
    tokens = re.findall(r"[A-Z][A-Za-z0-9\-]{2,}", abstract)
    if tokens:
        return "、".join(tokens[:3])
    return "论文摘要中的核心方法"


def build_chinese_summary(title: str, abstract: str, category: str, keywords: list[str]) -> str:
    label = CATEGORY_LABELS_ZH.get(category, category)
    method_cue = _extract_method_cue(abstract, keywords)
    claim_sentence = _extract_claim_sentence(abstract)
    summary_lines = [
        f"这篇工作归类为{label}，重点关注 {title} 所对应的问题设定。",
        f"从摘要看，作者主要围绕 {method_cue} 展开方法设计或系统建模。",
    ]
    if claim_sentence:
        summary_lines.append(f"实验与结论部分强调：{claim_sentence}")
    summary_lines.append(f"整体上，这篇论文更适合用来快速了解该方向当天的新方法和评测结论。")
    return " ".join(summary_lines[:4])


def build_readability_analysis(title: str, abstract: str, keywords: list[str]) -> str:
    word_count = len(re.findall(r"\b\w+\b", abstract))
    acronym_count = len(re.findall(r"\b[A-Z]{2,}\b", abstract))
    has_metrics = bool(re.search(r"\b\d+(\.\d+)?%|\bWER\b|\bAUC\b|\bEER\b|\bF1\b", abstract))

    if word_count < 140 and acronym_count <= 4:
        level = "高"
        reason = "摘要结构较直白，问题、方法和结果基本都能快速定位。"
    elif word_count < 220 and acronym_count <= 8:
        level = "中"
        reason = "需要一定领域背景，但主线仍然清楚。"
    else:
        level = "偏低"
        reason = "缩写、设定或实验细节较多，首次浏览成本偏高。"

    supplement = "摘要里给出了明确指标，便于快速判断效果。" if has_metrics else "摘要更偏方法描述，需要点开原文确认实验细节。"
    keyword_hint = f"优先关注关键词：{', '.join(keywords[:3])}。" if keywords else "关键词信号较弱，建议结合题目和原文摘要判断。"
    return f"可读性{level}。{reason} {supplement} {keyword_hint}"


def enrich_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    keywords_en = [extract_keywords(paper["title_en"], paper["abstract_en"]) for paper in papers]
    categories = [
        classify_paper(paper["title_en"], paper["abstract_en"], extracted)
        for paper, extracted in zip(papers, keywords_en)
    ]

    llm_payload = [
        {
            "title": paper["title_en"],
            "abstract": paper["abstract_en"],
            "category": category,
        }
        for paper, category in zip(papers, categories)
    ]
    llm_reviews = maybe_openai_json(
        (
            "For each paper, return a JSON array where each item has keys "
            "`summary_zh` and `readability_zh`. "
            "`summary_zh` must be a faithful 2-4 sentence Simplified Chinese summary. "
            "`readability_zh` must be one concise Simplified Chinese sentence analyzing readability. "
            "Do not invent results or claims not present in the abstract."
        ),
        llm_payload,
    )

    enriched: list[dict[str, Any]] = []
    for index, paper in enumerate(papers):
        paper_keywords_en = keywords_en[index]
        paper_category = categories[index]
        llm_review = llm_reviews[index] if llm_reviews and index < len(llm_reviews) else {}
        summary_zh = str(llm_review.get("summary_zh", "")).strip() if isinstance(llm_review, dict) else ""
        readability_zh = str(llm_review.get("readability_zh", "")).strip() if isinstance(llm_review, dict) else ""
        if not summary_zh:
            summary_zh = build_chinese_summary(
                paper["title_en"],
                paper["abstract_en"],
                paper_category,
                paper_keywords_en,
            )
        if not readability_zh:
            readability_zh = build_readability_analysis(
                paper["title_en"],
                paper["abstract_en"],
                paper_keywords_en,
            )
        enriched.append(
            {
                **paper,
                "keywords_en": paper_keywords_en,
                "digest_category": paper_category,
                "review": {
                    "summary_zh": summary_zh,
                    "readability_zh": readability_zh,
                },
            }
        )
    return enriched


def build_summary(papers: list[dict[str, Any]]) -> dict[str, Any]:
    counts = {category: 0 for category in CATEGORY_PRIORITY}
    for paper in papers:
        counts[paper["digest_category"]] += 1

    nonzero = [f"{category} {count} 篇" for category, count in counts.items() if count]
    if papers:
        headline = "今日共收录 {} 篇新论文，主要分布在 {}。".format(
            len(papers),
            "、".join(nonzero) if nonzero else "各类别",
        )
        trend = "整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。"
    else:
        headline = "今日时间窗口内未发现新的语音与音频 arXiv 论文。"
        trend = "系统仍已完成抓取、归档与状态更新，可等待下一次北京时间 09:00 的定时运行。"
    return {
        "total": len(papers),
        "counts": counts,
        "headline": headline,
        "trend": trend,
    }
