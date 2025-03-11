import os
import subprocess
import sys

# Colores para mensajes bonitos
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Mensaje de inicio
print(f"{MESSAGE_COLOR}✅ Proyecto creado exitosamente. Ejecutando pasos posteriores...{RESET_ALL}")

# -------------------------------------------------
# 1. Inicializar repositorio Git
# -------------------------------------------------
print(f"{MESSAGE_COLOR}🚀 Inicializando repositorio Git...{RESET_ALL}")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# -------------------------------------------------
# 2. Crear carpetas necesarias (si no existen)
# -------------------------------------------------
print(f"{MESSAGE_COLOR}📁 Creando carpetas necesarias...{RESET_ALL}")
folders = ['data/raw', 'data/processed', 'notebooks', 'src', 'reports']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"{MESSAGE_COLOR}✅ Carpeta creada: {folder}{RESET_ALL}")

# -------------------------------------------------
# 3. Instalar dependencias (opcional: pip o conda)
# -------------------------------------------------
# NOTA: Descomenta solo uno de los dos métodos siguientes según lo que uses

# ---- Método 1: Pip ----
# print(f"{MESSAGE_COLOR}📦 Instalando dependencias con pip...{RESET_ALL}")
# subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

# ---- Método 2: Conda ----
print(f"{MESSAGE_COLOR}📦 Creando entorno con Conda...{RESET_ALL}")
subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])

# -------------------------------------------------
# 4. Mensaje final
# -------------------------------------------------
print(f"{MESSAGE_COLOR}🎉 Proyecto listo. ¡A trabajar!{RESET_ALL}")
