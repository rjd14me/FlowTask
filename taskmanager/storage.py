import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "tasks.json"

def ensure_data_file():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


def load_tasks():
    ensure_data_file()

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        save_tasks([])
        return []


def save_tasks(tasks):
    ensure_data_file()
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def generate_new_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
