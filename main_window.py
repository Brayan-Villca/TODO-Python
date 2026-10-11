"""
MÓDULO: main_window.py
PROPÓSITO: Ventana principal de la aplicación (QMainWindow).
VENTAJA DIDÁCTICA: Orquesta todo: importa los widgets modulares,
conecta las señales (eventos de clic/teclas) con los métodos correspondientes (slots)
y llama al módulo de persistencia storage.py.
"""

from PyQt5.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QListWidget, 
    QLabel, 
    QMessageBox
)
import config
import storage
from widgets import EntradaWidget, AccionesWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración básica de la ventana
        self.setWindowTitle("Gestor de Tareas Modular")
        self.setFixedSize(380, 450)
        self.setStyleSheet(config.ESTILOS)

        # 1. Construir la estructura visual
        self.init_ui()
        # 2. Cargar los datos existentes desde el disco
        self.cargar_datos_iniciales()
        # 3. Vincular los eventos de los botones a las funciones
        self.conectar_eventos()

    def init_ui(self):
        """Crea el contenedor central, el layout vertical y monta los widgets."""
        central = QWidget(self)
        self.setCentralWidget(central)

        # Layout vertical principal: los elementos van uno debajo del otro
        layout = QVBoxLayout(central)
        layout.setSpacing(10) # Separación de 10px entre cada bloque

        # Título superior
        self.lbl_titulo = QLabel("Mis Tareas Pendientes")

        # Instancias de nuestros widgets personalizados creados en widgets.py
        self.entrada = EntradaWidget()
        self.lista = QListWidget() # Widget nativo de PyQt para mostrar listas
        self.acciones = AccionesWidget()

        # Agregamos los componentes en orden secuencial vertical
        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.entrada)
        layout.addWidget(self.lista)
        layout.addWidget(self.acciones)

    def conectar_eventos(self):
        """Conexión de Señales y Slots (Eventos -> Acciones)."""
        # Evento 1: Clic en el botón Agregar
        self.entrada.btn_agregar.clicked.connect(self.agregar_tarea)
        # Evento 2: Presionar la tecla Enter dentro del cuadro de texto
        self.entrada.input_texto.returnPressed.connect(self.agregar_tarea)

        # Evento 3: Clic en el botón Marcar Lista
        self.acciones.btn_completar.clicked.connect(self.marcar_completada)
        # Evento 4: Clic en el botón Eliminar
        self.acciones.btn_eliminar.clicked.connect(self.eliminar_tarea)

    def cargar_datos_iniciales(self):
        """Lee el archivo JSON al arrancar y llena el QListWidget."""
        tareas = storage.cargar_tareas()
        # addItems agrega una lista completa de strings directamente a la vista
        self.lista.addItems(tareas)

    def sincronizar_archivo(self):
        """
        Recorre todos los elementos actuales del QListWidget
        y los envía a storage.py para que se guarden en el JSON.
        """
        # Obtenemos el texto de cada fila de la lista mediante una lista por comprensión
        tareas_actuales = [self.lista.item(i).text() for i in range(self.lista.count())]
        storage.guardar_tareas(tareas_actuales)

    def agregar_tarea(self):
        """Inserta un nuevo elemento en la lista visual y en el archivo."""
        texto = self.entrada.obtener_texto()

        # Validación: Evitar que el usuario guarde campos vacíos o solo espacios
        if not texto:
            QMessageBox.warning(self, "Campo Vacío", "Por favor, escribe una descripción para la tarea.")
            return

        # 1. Agregar el elemento a la lista visual
        self.lista.addItem(texto)
        # 2. Limpiar el input para la siguiente entrada
        self.entrada.limpiar()
        # 3. Guardar el estado actualizado en el archivo
        self.sincronizar_archivo()

    def marcar_completada(self):
        """Agrega o quita una marca de verificación al elemento seleccionado."""
        # currentItem() obtiene el objeto de la fila que el usuario tiene seleccionada
        item_seleccionado = self.lista.currentItem()

        # Validación: Si no hay ninguna fila seleccionada, avisar al usuario
        if not item_seleccionado:
            QMessageBox.information(self, "Aviso", "Primero selecciona una tarea de la lista.")
            return

        texto_actual = item_seleccionado.text()

        # Si ya está marcada con el tick, se lo quitamos; si no, se lo añadimos
        if texto_actual.startswith("✔ "):
            item_seleccionado.setText(texto_actual.replace("✔ ", "", 1))
        else:
            item_seleccionado.setText(f"✔ {texto_actual}")

        # Guardar cambios en el archivo JSON
        self.sincronizar_archivo()

    def eliminar_tarea(self):
        """Elimina permanentemente de la lista la fila seleccionada."""
        # currentRow() devuelve el índice numérico de la fila seleccionada (0, 1, 2...)
        # Si no hay nada seleccionado, devuelve -1
        fila = self.lista.currentRow()

        if fila == -1:
            QMessageBox.information(self, "Aviso", "Selecciona la tarea que deseas eliminar.")
            return

        # takeItem() extrae y destruye el elemento en ese índice de la lista
        self.lista.takeItem(fila)
        # Guardar cambios actualizados en el archivo JSON
        self.sincronizar_archivo()