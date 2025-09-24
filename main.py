from functions import (
  call_create_note,
  call_list_notes,
  call_search_note,
  call_delete_note,
  call_edit_note,
  call_export_notes,
  call_import_notes,
  call_filter_notes_by_date,
  call_show_statistics
)

def check_database():
  try:
    with open("notes.json", "r", encoding="utf-8") as f:
      pass
  except FileNotFoundError:
    with open("notes.json", "w", encoding="utf-8") as f:
      f.write("[]")

def show_menu():
  print("\n===== Gestor de Notas =====")
  print("1. Crear nota")
  print("2. Listar notas")
  print("3. Buscar nota por título")
  print("4. Eliminar nota")
  print("5. Editar nota")
  print("6. Exportar notas a TXT")
  print("7. Importar notas desde archivo")
  print("8. Filtrar notas por fecha")
  print("9. Mostrar estadísticas")
  print("0. Salir")

def main():
  while True:
    show_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
      call_create_note()
    elif opcion == "2":
      call_list_notes()
    elif opcion == "3":
      call_search_note()
    elif opcion == "4":
      call_delete_note()
    elif opcion == "5":
      call_edit_note()
    elif opcion == "6":
      call_export_notes()
    elif opcion == "7":
      call_import_notes()
    elif opcion == "8":
      call_filter_notes_by_date()
    elif opcion == "9":
      call_show_statistics()
    elif opcion == "0":
      print("¡Hasta luego!")
      break
    else:
      print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
  check_database()
  main()