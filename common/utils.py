import json
from pathlib import Path

def get_data(path: str):
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)