from modules.data_manager import get_notes, save_notes

def create_note(name, author, content, date, tags=None):
    notes = get_notes()
    note = {
        "id": max(note["id"] for note in notes) + 1 if notes else 1,
        "name": name,
        "author": author,
        "content": content,
        "date": date,
        "tags": tags
    }
    notes.append(note)
    save_notes(notes)