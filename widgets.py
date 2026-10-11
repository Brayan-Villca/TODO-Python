"""
MÓDULO: widgets.py
PROPÓSITO: Construir componentes de interfaz reutilizables heredando de QWidget.
VENTAJA DIDÁCTICA: Muestra cómo encapsular un conjunto de controles relacionados
en una sola 'pieza de Lego' con su propio layout interno.
"""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton

class EntradaWidget(QWidget):
    """
    Componente visual que agrupa un campo de texto y el botón para añadir tareas.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # Usamos un layout horizontal para colocar el input y el botón lado a lado
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) # Eliminamos márgenes exteriores para alinearlo bien

        # 1. Campo de texto de una sola línea
        self.input_texto = QLineEdit()
        self.input_texto.setPlaceholderText("Escribe una nueva tarea...")

        # 2. Botón de agregar
        self.btn_agregar = QPushButton("Agregar")

        # 3. Ensamblamos los controles en el layout horizontal
        layout.addWidget(self.input_texto)
        layout.addWidget(self.btn_agregar)

    def obtener_texto(self) -> str:
        """Devuelve el texto escrito eliminando espacios sobrantes al inicio y final."""
        return self.input_texto.text().strip()

    def limpiar(self):
        """Borra el contenido del campo de texto tras agregar la tarea."""
        self.input_texto.clear()


class AccionesWidget(QWidget):
    """
    Componente visual inferior que contiene los botones de acción para la tarea seleccionada.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Botón para marcar la tarea como realizada
        self.btn_completar = QPushButton("Marcar Lista")

        # Botón para borrar la tarea seleccionada
        self.btn_eliminar = QPushButton("Eliminar")
        # Asignamos el objectName para que aplique el color rojo definido en config.py (#btn_eliminar)
        self.btn_eliminar.setObjectName("btn_eliminar")

        # Agregamos ambos botones al layout horizontal
        layout.addWidget(self.btn_completar)
        layout.addWidget(self.btn_eliminar)