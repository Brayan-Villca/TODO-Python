"""
MÓDULO: config.py
PROPÓSITO: Centralizar rutas del sistema y estilos visuales (QSS).
VENTAJA DIDÁCTICA: Si queremos cambiar colores o nombres de archivos,
lo hacemos aquí sin alterar la lógica de la aplicación.
"""

from pathlib import Path

# Obtenemos la ruta absoluta de la carpeta donde reside este script
# __file__ representa este archivo, resolve() da la ruta completa y parent la carpeta contenedora
CARPETA_PROYECTO = Path(__file__).resolve().parent

# Definimos la ruta completa del archivo JSON donde se guardarán las tareas
ARCHIVO_DATOS = CARPETA_PROYECTO / "tareas.json"

# Estilos en formato QSS (Qt Style Sheets, idéntico a CSS web)
ESTILOS = """
    /* Fondo general para la ventana principal */
    QMainWindow {
        background-color: #1e1e2e;
    }

    /* Estilo para las etiquetas de texto */
    QLabel {
        color: #cdd6f4;
        font-size: 15px;
        font-weight: bold;
        font-family: Arial, sans-serif;
    }

    /* Caja de texto donde el usuario escribe */
    QLineEdit {
        background-color: #313244;
        color: #cdd6f4;
        border: 1px solid #45475a;
        border-radius: 5px;
        padding: 8px;
        font-size: 13px;
    }

    /* Lista interactiva que contendrá los elementos */
    QListWidget {
        background-color: #313244;
        color: #cdd6f4;
        border: 1px solid #45475a;
        border-radius: 5px;
        padding: 5px;
        font-size: 13px;
    }

    /* Cada fila/ítem individual dentro de la lista */
    QListWidget::item {
        padding: 8px;
        border-bottom: 1px solid #45475a;
    }

    /* Estilo del ítem cuando el usuario hace clic sobre él */
    QListWidget::item:selected {
        background-color: #89b4fa;
        color: #11111b;
        font-weight: bold;
    }

    /* Estilo base para todos los botones */
    QPushButton {
        background-color: #89b4fa;
        color: #11111b;
        font-weight: bold;
        padding: 8px 14px;
        border-radius: 5px;
    }

    /* Efecto al pasar el cursor sobre los botones */
    QPushButton:hover {
        background-color: #b4befe;
    }

    /* Selector por ID específico (#btn_eliminar) para darle un tono rojo de alerta */
    QPushButton#btn_eliminar {
        background-color: #f38ba8;
    }

    QPushButton#btn_eliminar:hover {
        background-color: #eba0ac;
    }
"""