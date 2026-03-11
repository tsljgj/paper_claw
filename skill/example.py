"""
Article Claw Skill - Usage Example

This example shows how agents can use the Article Claw Skill
to fetch papers and send digests.
"""

import json
import subprocess
from pathlib import Path

# Skill root directory
SKILL_ROOT = Path(__file__).resolve().parents[1]


def fetch_papers(day: str = None, start_date: str = None, end_date: str = None) -> dict:
    """
    Fetch papers from arXiv.
    
    Args:
        day: Specific date (YYYY-MM-DD)
        start_date: Start date for range (YYYY-MM-DD)
        end_date: End date for range (YYYY-MM-DD)
    
    Returns:
        dict with paths to generated files
    """
    cmd = ["python", str(SKILL_ROOT / "scripts" / "main.py")]
    
    if day:
        cmd.extend(["--day", day])
    elif start_date and end_date:
        cmd.extend(["--start-date", start_date, "--end-date", end_date])
    
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=SKILL_ROOT)
    
    # Parse output to find generated files
    output = result.stdout + result.stderr
    
    # Extract date from command or use today
    if day:
        date_str = day
    else:
        from datetime import datetime
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    return {
        "success": result.returncode == 0,
        "markdown_path": str(SKILL_ROOT / "content" / "posts" / f"{date_str}-arxiv-audio-digest.md"),
        "json_path": str(SKILL_ROOT / "data" / "processed" / f"{date_str}.json"),
        "output": output
    }


def get_digest_content(date: str, format: str = "summary") -> dict:
    """
    Get digest content for a specific date.
    
    Args:
        date: Date string (YYYY-MM-DD)
        format: "markdown", "json", or "summary"
    
    Returns:
        dict with content
    """
    if format == "markdown":
        path = SKILL_ROOT / "content" / "posts" / f"{date}-arxiv-audio-digest.md"
        if path.exists():
            return {"content": path.read_text(encoding="utf-8"), "format": "markdown"}
    
    elif format == "json":
        path = SKILL_ROOT / "data" / "processed" / f"{date}.json"
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            return {"content": data, "format": "json"}
    
    elif format == "summary":
        path = SKILL_ROOT / "data" / "processed" / f"{date}.json"
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            return {
                "format": "summary",
                "date": date,
                "total_papers": data.get("summary", {}).get("total", 0),
                "categories": list(data.get("summary", {}).get("counts", {}).keys()),
                "paper_count_by_category": data.get("summary", {}).get("counts", {})
            }
    
    return {"error": f"Content not found for date {date}"}


def configure_recipients(recipients: list) -> dict:
    """
    Update recipients configuration.
    
    Args:
        recipients: List of dicts with email, name, enabled
    
    Returns:
        dict with success status
    """
    config_path = SKILL_ROOT / "config" / "recipients.json"
    
    config = {
        "recipients": recipients,
        "settings": {
            "display_mode": "full",
            "papers_per_category": 999,
            "show_full_abstract": True
        }
    }
    
    config_path.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")
    
    return {
        "success": True,
        "recipient_count": len(recipients),
        "config_path": str(config_path)
    }


# Example usage
if __name__ == "__main__":
    # Example 1: Fetch papers for a specific date
    print("Fetching papers for 2026-03-10...")
    result = fetch_papers(day="2026-03-10")
    print(f"Success: {result['success']}")
    print(f"Markdown: {result['markdown_path']}")
    
    # Example 2: Get digest summary
    print("\nGetting digest summary...")
    summary = get_digest_content("2026-03-10", format="summary")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    
    # Example 3: Configure recipients
    print("\nConfiguring recipients...")
    recipients = [
        {"email": "professor@university.edu.cn", "name": "Professor", "enabled": True},
        {"email": "student@university.edu.cn", "name": "Student", "enabled": True}
    ]
    config_result = configure_recipients(recipients)
    print(f"Configured {config_result['recipient_count']} recipients")
