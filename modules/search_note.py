from modules.data_manager import get_notes

def search_note(name):
    notes = get_notes()
    found = False
    for note in notes:
        if note["name"] == name:
            if not found:
                print("Notas encontradas:")
                found = True
            print("-------------")
            print("ID:", note["id"])
            print(f"Título: {note['name']}")
            print(f"Autor: {note['author']}")
            print(f"Contenido: {note['content']}")
            print(f"Fecha: {note['date']}")
            print(f"Etiquetas: {', '.join(note['tags'])}")
    if not found:
        print("No se encontraron notas con ese nombre.")
