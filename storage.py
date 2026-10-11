"""
MÓDULO: storage.py
PROPÓSITO: Manejar la entrada y salida de datos (disco local con JSON).
VENTAJA DIDÁCTICA: Desacopla por completo la persistencia de la interfaz gráfica.
Si en el futuro usamos SQLite o MySQL, solo modificamos este archivo.
"""

import json
from config import ARCHIVO_DATOS

def cargar_tareas() -> list:
    """
    Lee las tareas almacenadas en el archivo JSON.
    Si el archivo no existe o está corrupto, retorna una lista vacía de forma segura.
    """
    # 1. Comprobamos si el archivo existe físicamente en el disco
    if not ARCHIVO_DATOS.exists():
        return []

    try:
        # 2. Abrimos en modo lectura con codificación UTF-8 (para soportar tildes y caracteres especiales)
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            # json.load convierte la cadena del archivo en una lista de Python
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        # Si el JSON está mal formateado o hay un error de lectura, evitamos que la app se caiga
        return []

def guardar_tareas(tareas: list) -> bool:
    """
    Escribe la lista de tareas en el archivo JSON.
    Retorna True si la operación fue exitosa, o False si hubo un error.
    """
    try:
        # Abrimos en modo escritura ('w') sobrescribiendo con la lista actualizada
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            # indent=4 formatea el archivo con sangría para que sea legible
            # ensure_ascii=False evita que convierta acentos en secuencias de escape tipo \u00e1
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError:
        return False