import json
from pathlib import Path

DATA_DIR = Path("data")

DATA_DIR.mkdir(
    exist_ok=True,
)

EPISODES_FILE = DATA_DIR / "episodes.json"


def read_json():
    if not EPISODES_FILE.exists():
        return []

    return json.loads(
        EPISODES_FILE.read_text(
            encoding="utf-8"
        )
    )


def write_json(
    data,
):
    EPISODES_FILE.write_text(
        json.dumps(
            data,
            indent=4,
        ),
        encoding="utf-8",
    )