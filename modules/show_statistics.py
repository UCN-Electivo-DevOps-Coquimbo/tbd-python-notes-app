from modules.data_manager import get_notes
from collections import Counter
from datetime import datetime

def get_statistics():

    notes = get_notes()
    
    total_notes = len(notes)
    
    dates = []
    for note in notes:
        try:
            date_str = note['date'].split(' ')[0]  
            dates.append(date_str)
        except (KeyError, IndexError):
           
            dates.append("Fecha no disponible")
    
    notes_by_date = dict(Counter(dates))
    
    # Estadísticas por autor
    authors = []
    for note in notes:
        author = note.get('author', 'Autor no disponible')
        authors.append(author)
    
    notes_by_author = dict(Counter(authors))
    
    return {
        'total_notes': total_notes,
        'notes_by_date': notes_by_date,
        'notes_by_author': notes_by_author
    }

def format_statistics(statistics):
   
    if statistics['total_notes'] == 0:
        return "No hay notas disponibles para mostrar estadísticas."
    
    result = []
    result.append("=== ESTADÍSTICAS DE NOTAS ===\n")
    
    # cantidad total
    result.append(f"Cantidad total de notas: {statistics['total_notes']}\n")
    
    # notas por fecha
    result.append("Notas por fecha:")
    if statistics['notes_by_date']:
        for date, count in sorted(statistics['notes_by_date'].items()):
            result.append(f"   • {date}: {count} nota(s)")
    else:
        result.append("No hay datos de fechas disponibles")
    result.append("")
    
    # notas por autor
    result.append(" Notas por autor:")
    if statistics['notes_by_author']:
        # ordenar de forma descendente 
        sorted_authors = sorted(statistics['notes_by_author'].items(), 
                              key=lambda x: x[1], reverse=True)
        for author, count in sorted_authors:
            result.append(f"   • {author}: {count} nota(s)")
    else:
        result.append("No hay datos de autores disponibles")
    
    return "\n".join(result)