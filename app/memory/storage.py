import json
from pathlib import Path

DATA_DIRECTORY = Path("data")

DATA_DIRECTORY.mkdir(
    exist_ok=True
)

EPISODES_FILE = DATA_DIRECTORY / "episodes.json"

def read_json() -> list:
    if not EPISODES_FILE.exists():
        return []
    return json.loads(
        EPISODES_FILE.read_text(
            encoding="utf-8"
        )
    )

def write_json(
    data: list,
) -> None:
    EPISODES_FILE.write_text(
        json.dumps(
            data,
            indent=4,
        ),
        encoding="utf-8",
    )