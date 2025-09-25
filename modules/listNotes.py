import json

def getNotes():
    try :
        with open("notes.json", "r") as archivo_notas:
            notas = json.load(archivo_notas)
            return notas
    except FileNotFoundError:
        print("Archivo .json no encontrado")

def listNotes():
    notas = getNotes()
    print(" Se encontraron "+ str(len(notas)) + " notas: \n-------------------")
    for i in range (len(notas)):
        print("NOTA "+str(i + 1 ))
        nota = notas[i]
        print("Titulo: "+ nota.get('name') + "\nFecha: " + nota.get('date') + "\nContenido: "+ nota.get('content')+ "\nAutor: " + nota.get('author'))
        print ("-----------------------------------------------------------------------------------------")
