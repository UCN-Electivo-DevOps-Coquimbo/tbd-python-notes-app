# Gestor de notas en Python
Aplicación pequeña desarrollada en Python que permite gestionar notas.

Este es un ejercicio para el electivo "Introducción a DevOps", donde deberán aplicar Trunk-Based Development para integrar código.

## Funciones por desarrollar
Los estudiantes deberán agruparse de a dos o tres integrantes. Luego, deberán crear una o más de las siguientes funcionalidades a la aplicación. Todas las funcionalidades deben estar desarrolladas para sumar 5 décimas para la prueba 1.

- [X] Crear una nota (pide título y contenido por consola, guarda en un archivo JSON).
- [ ] Listar todas las notas (muestra título, fecha, contenido y autor).
- [X] Buscar una nota por título.
- [ ] Eliminar una nota de los registros.
- [ ] Editar una nota existente (según su ID).
- [ ] Exportar todas las notas a un archivo de texto plano (Definir Estructura).
- [ ] Importar notas desde un archivo externo (JSON o CSV) (Definir Formato).
- [ ] Filtrar notas por fecha de creación.
- [X] Mostrar estadísticas (cantidad total de notas, notas por fecha, notas por autor).

# Instrucciones
1. Se debe generar un archivo con su funcionalidad en la carpeta `modules`. Debe llevar por nombre `<nombreFuncion>.py`.
2. En dicho archivo, deberá desarrollar la funcionalidad solicitada. En estos archivos no se realizan llamadas a la consola de comandos (tanto input como output).
3. Debe modificar la función respectiva en el archivo [functions.py](functions.py). Acá se pueden realizar consultas al usuario por consola de comandos.
4. Probar la aplicación y verificar que todo este funcionando correctamente.
5. Se debe modificar este README para indicar que la funcionalidad se desarrolló.

# Estándares

- Los commits deben realizarse usando conventional commits (feat:, bug:, etc.).
- Los PR's deben llevar una descripción de lo que se fusionará.
- Los PR's no deben tener más de 5 archivos.
- Los PR's deben ser aprobados por al menos 1 persona de su equipo y una persona de otro equipo.
- La aplicación debe compilar y ejecutarse sin problemas al momento de integrar los cambios a main.
- Todos pueden aportar a cualquier funcionalidad si es necesario.

# Ejecución
Para iniciar la aplicación, debe ejecutar lo siguiente en la linea de comandos:

```bash
$ python3 main.py
```
