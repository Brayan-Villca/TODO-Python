"""
MÓDULO: main.py
PROPÓSITO: Punto de entrada (Entrypoint) del programa.
VENTAJA DIDÁCTICA: Enseña el patrón estándar de ejecución en aplicaciones Qt de escritorio.
"""

import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    # 1. QApplication administra el bucle principal de eventos del sistema operativo
    app = QApplication(sys.argv)

    # 2. Instanciamos la ventana principal
    ventana = MainWindow()

    # 3. Las ventanas de Qt se crean ocultas por defecto en memoria; show() las hace visibles
    ventana.show()

    # 4. Inicia el bucle de eventos (event loop). exec_() mantiene el programa en ejecución
    # hasta que el usuario cierra la ventana, retornando un código de salida limpio al sistema.
    sys.exit(app.exec_())