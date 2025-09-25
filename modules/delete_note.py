from modules.data_manager import get_notes, save_notes

def delete_note(note_id):
    try:
        note_id = int(note_id)  # Asegurarse de que note_id sea un entero
    except ValueError:
        return False  # Si no se puede convertir, retornar False

    notes = get_notes()
    nota_por_borrar = [note for note in notes if note["id"] != note_id]
    if len(nota_por_borrar) < len(notes):
        save_notes(nota_por_borrar)
        return True
    else:
        return False