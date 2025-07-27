import json
from pathlib import Path

save_file = Path("save.json")

def save_progress(level):
    with open(save_file, "w") as f:
        with open(save_file, "w") as f:
            json.dump({"current_level": level}, f)

def load_progress():
    if save_file.exists():
        with open(save_file, "r") as f:
            return json.load(f).get("current_level")
    return None

def clear_save():
    if save_file.exists():
        save_file.unlink()