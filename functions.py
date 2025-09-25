from datetime import datetime
from modules.create_note import create_note
from modules.show_statistics import get_statistics, format_statistics
from modules.listNotes import listNotes
from modules.search_note import search_note
def call_create_note():
    name = input("Nombre de la nota: ")
    author = input("Autor de la nota: ")
    content = input("Contenido de la nota: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_tags = input("Etiquetas (separadas por comas, opcional): ")
    if user_tags:
        tags = [tag.strip() for tag in user_tags.split(",")]
    else:
        tags = []
        
    create_note(name, author, content, date, tags)
    
    print("Nota creada exitosamente.")

def call_list_notes():
    listNotes()

def call_search_note():
    searchName = input("Ingrese Título de la nota: ")
    search_note(searchName)

def call_delete_note():
    print("Por implementar...")

def call_edit_note():
    print("Por implementar...")

def call_export_notes():
    print("Por implementar...")

def call_import_notes():
    print("Por implementar...")

def call_filter_notes_by_date():
    print("Por implementar...")

def call_show_statistics():
    try:
        statistics = get_statistics()
        formatted_stats = format_statistics(statistics)
        print(formatted_stats)
    except Exception as e:
        print(f"Error al obtener las estadísticas: {e}")
