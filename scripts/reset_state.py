import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "data" / "state.json"
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
POSTS_DIR = ROOT / "content" / "posts"


def main() -> None:
    STATE_PATH.write_text(
        json.dumps({"last_successful_run": None, "processed_ids": []}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    for directory in [RAW_DIR, PROCESSED_DIR, POSTS_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
        for path in directory.iterdir():
            if path.is_file():
                path.unlink()

    print("State and generated outputs have been reset.")


if __name__ == "__main__":
    main()
