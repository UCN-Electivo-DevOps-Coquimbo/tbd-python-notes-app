import os
import json

JSON_FILE_PATH = "notes.json"

# Get notes from the JSON app file
def get_notes():
    if not os.path.exists(JSON_FILE_PATH):
        return []
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Save notes to the JSON app file
def save_notes(notas):
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(notas, f, indent=3, ensure_ascii=False)