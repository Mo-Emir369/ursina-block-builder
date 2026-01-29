import json
from pathlib import Path

def save_world(path: Path, blocks_data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(blocks_data, ensure_ascii=False, indent=2), encoding="utf-8")

def load_world(path: Path):
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
