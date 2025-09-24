from modules.create_note import create_note
import json

def importJson(fileName):
    try:
        with open(fileName+".json", 'r') as file:
            notes = json.load(file)

        for note in notes:
            name = note.get("name")
            author = note.get("author")
            content = note.get("content")
            date = note.get("date")
            tags = note.get("tags", [])
            create_note(name, author, content, date, tags)
        
        print(f"Archivo {fileName} leído exitosamente.")
    
    except FileNotFoundError:
        print(f"El archivo {fileName} no se encontró.")
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Asegúrate de que el archivo esté bien formado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
importJson('notes.json')