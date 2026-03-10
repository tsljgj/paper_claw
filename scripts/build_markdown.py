from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape


def _environment(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(enabled_extensions=("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_markdown(template_dir: Path, context: dict[str, Any]) -> str:
    env = _environment(template_dir)
    template = env.get_template("blog_template.md.j2")
    return template.render(**context).strip() + "\n"


def render_email(template_dir: Path, context: dict[str, Any]) -> str:
    env = _environment(template_dir)
    template = env.get_template("email_template.html.j2")
    return template.render(**context)
