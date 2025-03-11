import sys
import re

# Obtener las variables definidas en cookiecutter.json
project_slug = '{{ cookiecutter.project_slug }}'
author_name = '{{ cookiecutter.project_author_name }}'

# Validar que el nombre del proyecto no tenga espacios ni caracteres raros
if not re.match(r'^[a-zA-Z0-9_-]+$', project_slug):
    print(f"ERROR: El nombre del proyecto '{project_slug}' contiene caracteres no permitidos.")
    print("Usa solo letras, números, guiones y guiones bajos (a-z, A-Z, 0-9, -, _).")
    sys.exit(1)  # Termina la ejecución si no pasa la validación

# Validar que el nombre del autor no esté vacío
if not author_name.strip():
    print("ERROR: El nombre del autor no puede estar vacío.")
    sys.exit(1)

print("✔ Validaciones completadas con éxito.")
