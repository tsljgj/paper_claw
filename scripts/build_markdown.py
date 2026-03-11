"""
Template rendering with multi-language support.
"""
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape


# Multi-language labels
LABELS = {
    "zh": {
        "overview": "今日速览",
        "metric": "指标",
        "value": "数值",
        "time_window": "时间窗口",
        "total_papers": "论文总数",
        "papers_unit": "篇",
        "category_stats": "分类统计",
        "authors": "作者",
        "affiliations": "机构",
        "source": "来源",
        "abstract": "摘要",
        "assessment": "综合评价",
        "item": "项目",
        "content": "内容",
        "summary": "总结",
        "readability": "可读性",
        "no_papers": "今日该分类暂无新论文。",
    },
    "en": {
        "overview": "Overview",
        "metric": "Metric",
        "value": "Value",
        "time_window": "Time Window",
        "total_papers": "Total Papers",
        "papers_unit": "papers",
        "category_stats": "Category Statistics",
        "authors": "Authors",
        "affiliations": "Affiliations",
        "source": "Source",
        "abstract": "Abstract",
        "assessment": "Assessment",
        "item": "Item",
        "content": "Content",
        "summary": "Summary",
        "readability": "Readability",
        "no_papers": "No papers in this category today.",
    },
    "ja": {
        "overview": "今日の概要",
        "metric": "指標",
        "value": "数値",
        "time_window": "時間枠",
        "total_papers": "論文総数",
        "papers_unit": "件",
        "category_stats": "カテゴリ統計",
        "authors": "著者",
        "affiliations": "所属機関",
        "source": "ソース",
        "abstract": "要約",
        "assessment": "評価",
        "item": "項目",
        "content": "内容",
        "summary": "概要",
        "readability": "可読性",
        "no_papers": "今日、このカテゴリには論文がありません。",
    },
    "ko": {
        "overview": "오늘의 개요",
        "metric": "지표",
        "value": "수치",
        "time_window": "시간 창",
        "total_papers": "논문 총수",
        "papers_unit": "편",
        "category_stats": "범주 통계",
        "authors": "저자",
        "affiliations": "소속 기관",
        "source": "출처",
        "abstract": "요약",
        "assessment": "평가",
        "item": "항목",
        "content": "내용",
        "summary": "요약",
        "readability": "가독성",
        "no_papers": "오늘 이 범주에는 논문이 없습니다.",
    },
    "de": {
        "overview": "Überblick",
        "metric": "Metrik",
        "value": "Wert",
        "time_window": "Zeitfenster",
        "total_papers": "Gesamtzahl",
        "papers_unit": "Papiere",
        "category_stats": "Kategoriestatistik",
        "authors": "Autoren",
        "affiliations": "Zugehörigkeiten",
        "source": "Quelle",
        "abstract": "Zusammenfassung",
        "assessment": "Bewertung",
        "item": "Element",
        "content": "Inhalt",
        "summary": "Zusammenfassung",
        "readability": "Lesbarkeit",
        "no_papers": "Heute keine Papiere in dieser Kategorie.",
    },
    "fr": {
        "overview": "Aperçu",
        "metric": "Métrique",
        "value": "Valeur",
        "time_window": "Fenêtre temporelle",
        "total_papers": "Total",
        "papers_unit": "articles",
        "category_stats": "Statistiques par catégorie",
        "authors": "Auteurs",
        "affiliations": "Affiliations",
        "source": "Source",
        "abstract": "Résumé",
        "assessment": "Évaluation",
        "item": "Élément",
        "content": "Contenu",
        "summary": "Résumé",
        "readability": "Lisibilité",
        "no_papers": "Aucun article dans cette catégorie aujourd'hui.",
    },
    "es": {
        "overview": "Resumen",
        "metric": "Métrica",
        "value": "Valor",
        "time_window": "Ventana de tiempo",
        "total_papers": "Total",
        "papers_unit": "artículos",
        "category_stats": "Estadísticas por categoría",
        "authors": "Autores",
        "affiliations": "Afiliaciones",
        "source": "Fuente",
        "abstract": "Resumen",
        "assessment": "Evaluación",
        "item": "Elemento",
        "content": "Contenido",
        "summary": "Resumen",
        "readability": "Legibilidad",
        "no_papers": "No hay artículos en esta categoría hoy.",
    },
}


def _environment(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(enabled_extensions=("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def get_labels(language: str) -> dict[str, str]:
    """Get labels for specified language."""
    return LABELS.get(language, LABELS["en"])


def render_markdown(template_dir: Path, context: dict[str, Any]) -> str:
    """Render markdown template with multi-language support."""
    env = _environment(template_dir)
    template = env.get_template("blog_template.md.j2")
    
    # Add labels to context based on language
    language = context.get("summary", {}).get("language", "zh")
    context["labels"] = get_labels(language)
    
    return template.render(**context).strip() + "\n"


def render_email(template_dir: Path, context: dict[str, Any]) -> str:
    """Render email template with multi-language support."""
    env = _environment(template_dir)
    template = env.get_template("email_template.html.j2")
    
    # Add labels to context based on language
    language = context.get("summary", {}).get("language", "zh")
    context["labels"] = get_labels(language)
    
    return template.render(**context)
