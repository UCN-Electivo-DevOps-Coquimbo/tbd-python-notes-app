from modules.data_manager import get_notes, save_notes

def edit_note(id):
    notes = get_notes()

    for note in notes:
        if note["id"] == id:
            print("Nota encontrada:")
            
            edit_name = input("Ingrese nuevo Título: ")
            edit_author = input("Ingrese Autor de la nota: ")
            edit_content = input("Contenido de la nota: ")
            edit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_tags = input("Etiquetas (separadas por comas, opcional): ")
            if user_tags:
                tags = [tag.strip() for tag in user_tags.split(",")]
            else:
                tags = []

            note["name"] = edit_name
            note["author"] = edit_author
            note["content"] = edit_content
            note["date"] = edit_date
            note["tags"] = user_tags
            
            save_notes(notes)
            return

    print("Nota no encontrada.")
    
    