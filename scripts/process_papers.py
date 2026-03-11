"""
Paper processing module with multi-language and multi-provider LLM support.
"""

import json
import logging
import os
import re
from collections import Counter
from typing import Any

from llm_client import create_client


def build_classification_assets(config: dict[str, Any]) -> tuple[dict[str, list[str]], list[str], dict[str, dict[str, str]]]:
    """
    Build classification rules and labels from config.
    
    Returns:
        Tuple of (rules, priority, labels_by_language)
    """
    categories = config["classification"]["categories"]
    rules = {item["name"]: item["keywords"] for item in categories}
    priority = [item["name"] for item in categories]
    # Labels now support multiple languages
    labels = {item["name"]: item.get("labels", {"en": item["name"]}) for item in categories}
    return rules, priority, labels


def _normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().lower()


def extract_keywords(title: str, abstract: str, category_rules: dict[str, list[str]]) -> list[str]:
    haystack = _normalize_text(f"{title} {abstract}")
    matched: list[str] = []
    for keywords in category_rules.values():
        for keyword in keywords:
            if keyword in haystack and keyword not in matched:
                matched.append(keyword)
    if not matched:
        tokens = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", haystack)
        matched = list(dict.fromkeys(tokens[:6]))
    return matched[:8]


def classify_paper(
    title: str,
    abstract: str,
    keywords: list[str],
    category_rules: dict[str, list[str]],
    category_priority: list[str],
) -> str:
    haystack = _normalize_text(" ".join([title, abstract, " ".join(keywords)]))
    scores = Counter()
    for category, rules in category_rules.items():
        for keyword in rules:
            if keyword in haystack:
                scores[category] += max(1, len(keyword.split()))
    if not scores:
        return category_priority[-1]
    return sorted(scores.items(), key=lambda item: (-item[1], category_priority.index(item[0])))[0][0]


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
    return "摘要中的核心方法"


def build_summary_text(
    title: str,
    abstract: str,
    category_label: str,
    keywords: list[str],
    language: str = "zh"
) -> str:
    """Build summary text in specified language (fallback method)."""
    method_cue = _extract_method_cue(abstract, keywords)
    claim_sentence = _extract_claim_sentence(abstract)
    
    if language == "zh":
        summary_lines = [
            f"这篇工作归入「{category_label}」方向，核心任务由题目《{title}》所界定。",
            f"从摘要看，作者主要围绕 {method_cue} 展开方法设计、训练策略或系统建模。",
        ]
        if claim_sentence:
            summary_lines.append(f"结果部分最值得注意的是：{claim_sentence}")
        summary_lines.append("如果你想快速判断这篇论文是否值得细读，这份摘要已经能帮助你抓住问题、方法和结果主线。")
    elif language == "ja":
        summary_lines = [
            f"この研究は「{category_label}」カテゴリに分類され、タイトル「{title}」で示された核心課題に取り組んでいます。",
            f"要約から、著者は主に {method_cue} に関する方法設計、学習戦略、またはシステムモデリングに焦点を当てています。",
        ]
        if claim_sentence:
            summary_lines.append(f"結果の注目点：{claim_sentence}")
        summary_lines.append("この要約は、論文の価値を迅速に判断するのに役立ちます。")
    elif language == "ko":
        summary_lines = [
            f"이 연구는 「{category_label}」 범주로 분류되며, 제목《{title}》에서 제시된 핵심 과제를 다룹니다.",
            f"요약에 따른 저자는 주로 {method_cue}에 관한 방법 설계, 학습 전략, 또는 시스템 모델링에 중점을 두고 있습니다.",
        ]
        if claim_sentence:
            summary_lines.append(f"결과의 주목할 점: {claim_sentence}")
        summary_lines.append("이 요약은 논문의 가치를 신속하게 판단하는 데 도움이 됩니다.")
    else:  # Default to English
        summary_lines = [
            f"This work falls under the '{category_label}' category, addressing the core task outlined in the title '{title}'.",
            f"From the abstract, the authors focus on {method_cue} for method design, training strategies, or system modeling.",
        ]
        if claim_sentence:
            summary_lines.append(f"Notable result: {claim_sentence}")
        summary_lines.append("This summary helps you quickly assess whether the paper is worth reading in detail.")
    
    return " ".join(summary_lines[:4])


def build_readability_analysis(abstract: str, keywords: list[str], language: str = "zh") -> str:
    """Build readability analysis in specified language."""
    word_count = len(re.findall(r"\b\w+\b", abstract))
    acronym_count = len(re.findall(r"\b[A-Z]{2,}\b", abstract))
    has_metrics = bool(re.search(r"\b\d+(\.\d+)?%|\bWER\b|\bAUC\b|\bEER\b|\bF1\b", abstract))
    
    # Determine level
    if word_count < 140 and acronym_count <= 4:
        if language == "zh":
            level, reason = "高", "摘要结构较直白，问题、方法和结果都比较容易定位。"
        elif language == "ja":
            level, reason = "高い", "要約の構造が明確で、問題、方法、結果が比較的見つけやすいです。"
        elif language == "ko":
            level, reason = "높음", "요약 구조가 명확하고 문제, 방법, 결과가 비교적 찾기 쉽습니다."
        else:
            level, reason = "High", "The abstract structure is clear, making problem, method, and results easy to locate."
    elif word_count < 220 and acronym_count <= 8:
        if language == "zh":
            level, reason = "中", "需要一定领域背景，但主线仍然清楚。"
        elif language == "ja":
            level, reason = "中程度", "一定のドメイン知識が必要ですが、主線は依然として明確です。"
        elif language == "ko":
            level, reason = "중간", "일정한 분야 배경이 필요하지만 주선은 여전히 분명합니다."
        else:
            level, reason = "Medium", "Requires some domain background, but the main thread remains clear."
    else:
        if language == "zh":
            level, reason = "偏低", "缩写、设定或实验细节较多，首次浏览成本偏高。"
        elif language == "ja":
            level, reason = "やや低い", "略語、設定、または実験の詳細が多く、初回の閲覧コストが高めです。"
        elif language == "ko":
            level, reason = "다소 낮음", "약어, 설정 또는 실험 세부사항이 많아 초안 읽기 비용이 높습니다."
        else:
            level, reason = "Lower", "Many abbreviations, settings, or experimental details increase initial reading cost."
    
    # Build hints
    if language == "zh":
        metrics_hint = "摘要中给出了明确指标，适合快速判断效果。" if has_metrics else "摘要更偏方法描述，建议点开原文确认实验细节。"
        keyword_hint = f"优先看这些信号词：{', '.join(keywords[:3])}。" if keywords else "关键词信号较弱，建议结合题目与摘要一起判断。"
        return f"可读性{level}。{reason} {metrics_hint} {keyword_hint}"
    elif language == "ja":
        metrics_hint = "要約には明確な指標が示されており、効果を迅速に判断するのに適しています。" if has_metrics else "要約は方法の記述に偏っているため、原文を確認することをお勧めします。"
        keyword_hint = f"これらのシグナルワードに注意してください：{', '.join(keywords[:3])}。" if keywords else "キーワード信号が弱いため、タイトルと要約を組み合わせて判断することをお勧めします。"
        return f"可読性は{level}です。{reason} {metrics_hint} {keyword_hint}"
    elif language == "ko":
        metrics_hint = "요약에 명확한 지표가 제시되어 있어 효과를 신속하게 판단하기에 적합합니다." if has_metrics else "요약이 방법 설명에 치중되어 있어 원문을 확인하는 것이 좋습니다."
        keyword_hint = f"이러한 신호 단어에 주의하세요: {', '.join(keywords[:3])}." if keywords else "키워드 신호가 약하므로 제목과 요약을 함께 판단하는 것이 좋습니다."
        return f"가독성은 {level}입니다. {reason} {metrics_hint} {keyword_hint}"
    else:
        metrics_hint = "The abstract provides clear metrics, suitable for quick effectiveness assessment." if has_metrics else "The abstract focuses more on methodology; checking the original text is recommended."
        keyword_hint = f"Focus on these signal words: {', '.join(keywords[:3])}." if keywords else "Weak keyword signals; consider combining title and abstract for judgment."
        return f"Readability is {level}. {reason} {metrics_hint} {keyword_hint}"


def enrich_papers(
    papers: list[dict[str, Any]],
    config: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[str]]:
    """
    Enrich papers with classification, keywords, and AI-generated summaries.
    
    Args:
        papers: List of paper dictionaries
        config: Configuration dictionary
    
    Returns:
        Tuple of (enriched_papers, category_priority)
    """
    category_rules, category_priority, labels = build_classification_assets(config)
    
    # Get language setting
    language = config.get("language", {}).get("default", "zh")
    
    # Extract keywords and classify
    keywords_en = [extract_keywords(paper["title_en"], paper["abstract_en"], category_rules) for paper in papers]
    categories = [
        classify_paper(paper["title_en"], paper["abstract_en"], extracted, category_rules, category_priority)
        for paper, extracted in zip(papers, keywords_en)
    ]
    
    # Prepare LLM payload
    llm_payload = [
        {"title": paper["title_en"], "abstract": paper["abstract_en"], "category": category}
        for paper, category in zip(papers, categories)
    ]
    
    # Try LLM generation
    llm_reviews = None
    if "llm" in config:
        try:
            client = create_client(config["llm"])
            llm_reviews = client.generate_summaries(llm_payload, language=language)
            if llm_reviews:
                logging.info(f"LLM generated {len(llm_reviews)} summaries in {language}")
        except Exception as e:
            logging.warning(f"LLM generation failed: {e}")
    
    # Build enriched papers
    enriched: list[dict[str, Any]] = []
    for index, paper in enumerate(papers):
        paper_keywords_en = keywords_en[index]
        paper_category = categories[index]
        llm_review = llm_reviews[index] if llm_reviews and index < len(llm_reviews) else {}
        
        # Get label in target language
        category_labels = labels.get(paper_category, {"en": paper_category})
        category_label = category_labels.get(language, category_labels.get("en", paper_category))
        
        # Get LLM-generated or fallback summary
        if isinstance(llm_review, dict):
            summary_text = str(llm_review.get("summary", "")).strip()
            readability_text = str(llm_review.get("readability", "")).strip()
        else:
            summary_text = ""
            readability_text = ""
        
        # Fallback to rule-based if LLM fails
        if not summary_text:
            summary_text = build_summary_text(
                paper["title_en"],
                paper["abstract_en"],
                category_label,
                paper_keywords_en,
                language
            )
        if not readability_text:
            readability_text = build_readability_analysis(
                paper["abstract_en"],
                paper_keywords_en,
                language
            )
        
        enriched.append(
            {
                **paper,
                "keywords_en": paper_keywords_en,
                "digest_category": paper_category,
                "category_label": category_label,
                "language": language,
                "review": {
                    "summary": summary_text,
                    "readability": readability_text,
                },
            }
        )
    
    return enriched, category_priority


def build_summary(papers: list[dict[str, Any]], category_priority: list[str], language: str = "zh") -> dict[str, Any]:
    """Build summary statistics in specified language."""
    counts = {category: 0 for category in category_priority}
    for paper in papers:
        counts[paper["digest_category"]] += 1
    
    nonzero = [f"{category} {count}" for category, count in counts.items() if count]
    
    if language == "zh":
        if papers:
            headline = f"今日共收录 {len(papers)} 篇新论文，主要分布在 {', '.join(nonzero)}。"
            trend = "整体上以方法改进、跨模态建模和系统化评测为主，适合按分类快速筛选当天值得细读的论文。"
        else:
            headline = "今日时间窗口内未发现新的论文。"
            trend = "系统已完成抓取、归档与状态更新，可等待下一次定时运行。"
    elif language == "ja":
        if papers:
            headline = f"今日は {len(papers)} 件の新しい論文が収録されました。主な分布：{', '.join(nonzero)}。"
            trend = "全体的に方法の改善、クロスモーダルモデリング、および系統的な評価が中心で、分類別に当日の精読に値する論文を迅速に選別するのに適しています。"
        else:
            headline = "今日の時間枠内では新しい論文は見つかりませんでした。"
            trend = "システムはクロール、アーカイブ、および状態の更新を完了しました。次のスケジュールされた実行を待つことができます。"
    elif language == "ko":
        if papers:
            headline = f"오늘 총 {len(papers)}편의 새로운 논문이 수집되었습니다. 주요 분포: {', '.join(nonzero)}."
            trend = "전반적으로 방법 개선, 크로스 모달 모델링 및 체계적인 평가가 중심이며, 분류별로 당일 세밀하게 읽을 가치가 있는 논문을 빠르게 선별하는 데 적합합니다."
        else:
            headline = "오늘의 시간 창 내에서 새로운 논문을 찾을 수 없습니다."
            trend = "시스템이 크롤링, 아카이빙 및 상태 업데이트를 완료했습니다. 다음 예정된 실행을 기다릴 수 있습니다."
    else:
        if papers:
            headline = f"Today collected {len(papers)} new papers. Main distribution: {', '.join(nonzero)}."
            trend = "Overall focus on method improvements, cross-modal modeling, and systematic evaluation. Suitable for quickly filtering papers worth reading."
        else:
            headline = "No new papers found in today's time window."
            trend = "System has completed crawling, archiving, and state updates. Waiting for next scheduled run."
    
    return {
        "total": len(papers),
        "counts": counts,
        "headline": headline,
        "trend": trend,
        "language": language
    }
