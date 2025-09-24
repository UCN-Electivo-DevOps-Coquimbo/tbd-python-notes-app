from modules.data_manager import get_notes, save_notes

def create_note(name, author, content, date, tags=None):
    notes = get_notes()
    note = {
        "id": len(notes) + 1,
        "name": name,
        "author": author,
        "content": content,
        "date": date,
        "tags": tags
    }
    notes.append(note)
    save_notes(notes)