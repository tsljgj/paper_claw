#!/usr/bin/env python3
"""
Interactive configurator for paper_claw.

Run it to tweak the digest's behavior without hand-editing JSON:

    python scripts/configure.py

Menu-driven: research-interest profile, watched authors, filtering thresholds,
models, deep-read, Hugging Face, arXiv categories, and the daily send time.
On exit it shows what changed and offers to commit + push so the next GitHub
Actions run picks it up.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "default.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "daily_digest.yml"


# ---------------------------------------------------------------------------
# small input helpers
# ---------------------------------------------------------------------------
def ask(prompt: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default is not None else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val or (default or "")


def ask_int(prompt: str, current: int, lo: int, hi: int) -> int:
    while True:
        raw = ask(prompt, str(current))
        try:
            n = int(raw)
        except ValueError:
            print(f"  ⚠️  please enter a number between {lo} and {hi}")
            continue
        if not (lo <= n <= hi):
            print(f"  ⚠️  must be between {lo} and {hi}")
            continue
        return n


def ask_yes(prompt: str, default_yes: bool = True) -> bool:
    d = "Y/n" if default_yes else "y/N"
    raw = input(f"{prompt} [{d}]: ").strip().lower()
    if not raw:
        return default_yes
    return raw in ("y", "yes")


def pause() -> None:
    input("\n(press Enter to continue)")


# ---------------------------------------------------------------------------
# config load/save
# ---------------------------------------------------------------------------
def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def _compact_small_objects(text: str) -> str:
    """Collapse a flat object spanning few lines (e.g. a category {id,name,url}) to one line."""
    def collapse(m: re.Match) -> str:
        indent = m.group(1)
        body = m.group(2)
        if "{" in body or "[" in body:
            return m.group(0)
        parts = [ln.strip().rstrip(",") for ln in body.splitlines() if ln.strip()]
        one_line = indent + "{" + ", ".join(parts) + "}"
        return one_line if len(one_line) <= 120 else m.group(0)

    return re.sub(r"^(\s*)\{\n((?:[^{}\n]*\n)+?)\s*\}", collapse, text, flags=re.MULTILINE)


def _compact_scalar_arrays(text: str) -> str:
    """Collapse short arrays of scalars onto one line."""
    def collapse(m: re.Match) -> str:
        body = m.group(1)
        if "{" in body or "[" in body:
            return m.group(0)
        items = [ln.strip().rstrip(",") for ln in body.splitlines() if ln.strip()]
        one_line = "[" + ", ".join(items) + "]"
        return one_line if len(one_line) <= 100 else m.group(0)

    return re.sub(r"\[\n((?:[^\[\]]*\n)+?)\s*\]", collapse, text)


def save_config(cfg: dict) -> None:
    text = json.dumps(cfg, ensure_ascii=False, indent=2)
    text = _compact_scalar_arrays(text)
    text = _compact_small_objects(text)
    CONFIG_PATH.write_text(text + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# editors (each mutates cfg in place)
# ---------------------------------------------------------------------------
def edit_profile(cfg: dict) -> None:
    rel = cfg.setdefault("relevance", {})
    print("\n=== Research-interest profile ===")
    print("This plain-English description is what the LLM scores every paper")
    print("against. The more specific it is, the better the filtering.\n")
    print("Current profile:\n")
    print("  " + rel.get("profile", "(empty)").replace("\n", "\n  "))
    print()
    if not ask_yes("Replace it?", default_yes=False):
        return
    print("\nPaste/type the new profile. End with a single line containing only END:")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    new = "\n".join(lines).strip()
    if new:
        rel["profile"] = new
        print("  ✅ profile updated")
    else:
        print("  (left unchanged)")


def edit_authors(cfg: dict) -> None:
    wa = cfg.setdefault("watched_authors", {"enabled": True, "authors": []})
    while True:
        authors = wa.get("authors", [])
        print("\n=== Watched authors / groups ===")
        print(f"enabled: {wa.get('enabled', True)}")
        for i, a in enumerate(authors, 1):
            aliases = ", ".join(a.get("aliases", []))
            print(f"  {i}. {a.get('name')}   (aliases: {aliases})")
        print("\n  a) add author   d) delete author   t) toggle enabled   b) back")
        choice = ask("choose").lower()
        if choice == "b":
            return
        elif choice == "t":
            wa["enabled"] = not wa.get("enabled", True)
            print(f"  ✅ enabled = {wa['enabled']}")
        elif choice == "a":
            name = ask("  canonical name (as on Google Scholar)")
            if not name:
                continue
            extra = ask("  extra aliases, comma-separated (optional)")
            aliases = [name] + [x.strip() for x in extra.split(",") if x.strip()]
            authors.append({"name": name, "aliases": list(dict.fromkeys(aliases))})
            wa["authors"] = authors
            print(f"  ✅ added {name}")
        elif choice == "d":
            n = ask_int("  number to delete", 0, 0, len(authors))
            if n:
                removed = authors.pop(n - 1)
                print(f"  ✅ removed {removed.get('name')}")


def edit_filtering(cfg: dict) -> None:
    rel = cfg.setdefault("relevance", {})
    print("\n=== Filtering thresholds ===")
    print("min_score: only papers scoring this high (0-10) are kept. Higher =")
    print("  stricter/fewer. max_papers: hard cap on how many make the digest.\n")
    rel["min_score"] = ask_int("min_score", rel.get("min_score", 6), 0, 10)
    rel["max_papers"] = ask_int("max_papers", rel.get("max_papers", 18), 1, 100)
    print("  ✅ filtering updated")


def edit_models(cfg: dict) -> None:
    prov = cfg.setdefault("llm", {}).setdefault("providers", {}).setdefault("openai", {})
    print("\n=== OpenAI models ===")
    print("Tiered: a cheap model for scoring + normal summaries, a strong one for")
    print("the top-N deep reads. Use exact OpenAI model IDs.\n")
    print(f"  scoring + normal summaries (model):  {prov.get('model')}")
    print(f"  deep-read (deep_read_model):         {prov.get('deep_read_model')}")
    print(f"  relevance scoring (score_model):     {prov.get('score_model')}")
    print()
    if not ask_yes("Change models?", default_yes=False):
        return
    prov["model"] = ask("  model (summaries)", prov.get("model", ""))
    prov["deep_read_model"] = ask("  deep_read_model", prov.get("deep_read_model", ""))
    prov["score_model"] = ask("  score_model", prov.get("score_model", ""))
    print("  ✅ models updated")
    print("  ⚠️  note: gpt-5.5* models reject custom temperature — the code already")
    print("     handles that, but if you switch to another family verify it works.")


def edit_deep_read(cfg: dict) -> None:
    dr = cfg.setdefault("deep_read", {"enabled": True, "top_n": 5})
    print("\n=== Deep read ===")
    print("The top-N highest-scoring papers get a separate, deeper pass with the")
    print("stronger model.\n")
    dr["enabled"] = ask_yes("enabled?", dr.get("enabled", True))
    if dr["enabled"]:
        dr["top_n"] = ask_int("top_n (how many to deep-read)", dr.get("top_n", 5), 0, 30)
    print("  ✅ deep_read updated")


def edit_huggingface(cfg: dict) -> None:
    hf = cfg.setdefault("huggingface", {"enabled": True, "upvote_boost": 2, "lookback_days": 2})
    print("\n=== Hugging Face Daily Papers ===")
    print("Pulls HF Daily Papers as a popularity signal (upvotes → relevance boost)")
    print("and an extra source for papers the arXiv RSS feed missed.\n")
    hf["enabled"] = ask_yes("enabled?", hf.get("enabled", True))
    if hf["enabled"]:
        hf["upvote_boost"] = ask_int(
            "upvote_boost (max extra points from upvotes)", hf.get("upvote_boost", 2), 0, 10
        )
        hf["lookback_days"] = ask_int(
            "lookback_days (how many days of HF Daily to pull)", hf.get("lookback_days", 2), 1, 7
        )
    print("  ✅ huggingface updated")


def edit_categories(cfg: dict) -> None:
    arx = cfg.setdefault("sources", {}).setdefault("arxiv", {})
    cats = arx.setdefault("categories", [])
    while True:
        print("\n=== arXiv categories to fetch ===")
        for i, c in enumerate(cats, 1):
            print(f"  {i}. {c.get('id')}  — {c.get('name')}")
        print("\n  a) add   d) delete   b) back")
        print("  (common: cs.AI cs.CL cs.HC cs.LG cs.CV cs.RO cs.MA)")
        choice = ask("choose").lower()
        if choice == "b":
            return
        elif choice == "a":
            cid = ask("  category id (e.g. cs.RO)")
            if not re.match(r"^[a-z]+\.[A-Z]{2}$", cid):
                print("  ⚠️  expected form like cs.RO")
                continue
            name = ask("  display name", cid)
            cats.append({"id": cid, "name": name, "url": f"https://arxiv.org/list/{cid}/recent"})
            print(f"  ✅ added {cid}")
        elif choice == "d":
            n = ask_int("  number to delete", 0, 0, len(cats))
            if n:
                removed = cats.pop(n - 1)
                print(f"  ✅ removed {removed.get('id')}")


def edit_send_time(state: dict) -> None:
    """Edit the daily cron in the workflow file (separate from config JSON)."""
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    m = re.search(r'cron:\s*"(\d+)\s+(\d+)\s+\*\s+\*\s+\*"', text)
    print("\n=== Daily send time ===")
    if not m:
        print("  ⚠️  couldn't find a single daily cron in the workflow; edit it by hand.")
        return
    cur_min, cur_hour = int(m.group(1)), int(m.group(2))
    # The cron is in UTC; ET (EDT) = UTC-4.
    et_hour = (cur_hour - 4) % 24
    print(f"current: {cur_hour:02d}:{cur_min:02d} UTC  ≈  {et_hour:02d}:{cur_min:02d} ET (EDT)")
    print("Enter the desired US-Eastern (EDT) time. It runs a few min early on")
    print("purpose; the email lands ~5 min after.\n")
    if not ask_yes("Change send time?", default_yes=False):
        return
    eh = ask_int("  hour (0-23, ET)", et_hour, 0, 23)
    em = ask_int("  minute (0-59)", cur_min, 0, 59)
    uh = (eh + 4) % 24
    est = (eh - 1) % 24  # winter (EST = UTC-5), so ET wall-clock shifts an hour
    new_line = (
        f'cron: "{em} {uh} * * *"  '
        f'# {uh:02d}:{em:02d} UTC = {eh:02d}:{em:02d} America/New_York (EDT) / {est:02d}:{em:02d} (EST)'
    )
    # Replace the whole cron line (value + trailing comment) so the comment stays accurate.
    new_text = re.sub(r'cron:\s*"\d+\s+\d+\s+\*\s+\*\s+\*".*', new_line, text, count=1)
    WORKFLOW_PATH.write_text(new_text, encoding="utf-8")
    state["workflow_changed"] = True
    print(f"  ✅ send time set to {eh:02d}:{em:02d} ET  ({uh:02d}:{em:02d} UTC)")


def show_sender_name_help() -> None:
    print("\n=== Sender display name ===")
    print("The name recipients see (e.g. \"Zhihao's Paper Assistant\") is NOT in")
    print("this config — it's the EMAIL_FROM_NAME GitHub secret (or env var).")
    print("Change it at: your repo → Settings → Secrets and variables → Actions")
    print("→ EMAIL_FROM_NAME. Default if unset: \"Zhihao's Paper Assistant\".")
    pause()


# ---------------------------------------------------------------------------
# git
# ---------------------------------------------------------------------------
def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def offer_commit() -> None:
    status = git("status", "--short", "config/default.json", ".github/workflows/daily_digest.yml")
    if not status.stdout.strip():
        print("\nNo changes to save.")
        return
    print("\n=== Pending changes ===")
    print(git("diff", "--stat", "config/default.json", ".github/workflows/daily_digest.yml").stdout)
    if not ask_yes("Commit and push so the next run uses these settings?", default_yes=False):
        print("Left uncommitted. Run `git add -p && git commit && git push` when ready.")
        return
    git("add", "config/default.json", ".github/workflows/daily_digest.yml")
    msg = ask("  commit message", "Tune digest config")
    cm = git("commit", "-m", msg)
    if cm.returncode != 0:
        print("  ⚠️  commit failed:\n" + cm.stderr)
        return
    push = git("push")
    if push.returncode != 0:
        print("  ⚠️  push failed (auth?). Commit is saved locally; push manually.\n" + push.stderr)
    else:
        print("  ✅ committed and pushed — next scheduled run will use the new settings.")


# ---------------------------------------------------------------------------
# main loop
# ---------------------------------------------------------------------------
MENU = """
╔══════════════════════════════════════════╗
║          paper_claw — configure           ║
╠══════════════════════════════════════════╣
║  1) Research-interest profile             ║
║  2) Watched authors / groups              ║
║  3) Filtering thresholds (min_score, cap) ║
║  4) Models (scoring / summary / deep)     ║
║  5) Deep read (top-N, on/off)             ║
║  6) Hugging Face source                   ║
║  7) arXiv categories                      ║
║  8) Daily send time                       ║
║  9) Sender display name (how-to)          ║
║                                           ║
║  s) save   q) save & quit   x) quit no-save║
╚══════════════════════════════════════════╝"""


def main() -> None:
    if not CONFIG_PATH.exists():
        print(f"config not found: {CONFIG_PATH}")
        sys.exit(1)
    cfg = load_config()
    state: dict = {"workflow_changed": False}
    dirty = False

    while True:
        print(MENU)
        choice = ask("choose").lower()
        if choice == "1":
            edit_profile(cfg); dirty = True
        elif choice == "2":
            edit_authors(cfg); dirty = True
        elif choice == "3":
            edit_filtering(cfg); dirty = True
        elif choice == "4":
            edit_models(cfg); dirty = True
        elif choice == "5":
            edit_deep_read(cfg); dirty = True
        elif choice == "6":
            edit_huggingface(cfg); dirty = True
        elif choice == "7":
            edit_categories(cfg); dirty = True
        elif choice == "8":
            edit_send_time(state)
        elif choice == "9":
            show_sender_name_help()
        elif choice == "s":
            save_config(cfg); dirty = False
            print("  💾 saved to config/default.json")
        elif choice in ("q", "x"):
            break
        else:
            print("  ?  unknown choice")

    if choice == "x":
        if dirty or state["workflow_changed"]:
            if ask_yes("Discard unsaved changes?", default_yes=True):
                print("Discarded in-memory config changes (files on disk unchanged).")
                return
        return

    # q: save and offer to commit
    save_config(cfg)
    print("\n💾 saved to config/default.json")
    offer_commit()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nAborted (no changes pushed).")
