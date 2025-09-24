from modules.data_manager import get_notes

def search_note(name):
    notes = get_notes()
    for note in notes:
        if note["name"] == name:
            print("Nota encontrada:")
            print(f"Título: {note['name']}")
            print(f"Autor: {note['author']}")
            print(f"Contenido: {note['content']}")
            print(f"Fecha: {note['date']}")
            print(f"Etiquetas: {', '.join(note['tags'])}")
            return

    print("Nota no encontrada.")
