import json
from modules.data_manager import get_notes

def listNotes():
    notas = get_notes()
    print(" Se encontraron "+ str(len(notas)) + " notas: \n-------------------")
    for i in range (len(notas)):
        print("NOTA "+str(i + 1 ))
        nota = notas[i]
        print("Titulo: "+ nota.get('name') + "\nFecha: " + nota.get('date') + "\nContenido: "+ nota.get('content')+ "\nAutor: " + nota.get('author'))
        print ("-----------------------------------------------------------------------------------------")
