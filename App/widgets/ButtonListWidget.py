from PySide6.QtWidgets import *
from .DroppableList import DroppableList

class ButtonListWidget(QWidget):
	_btn_add = None
	_btn_remove = None
	_btn_up = None
	_btn_down = None

	def __init__(self, parent=None):
		super().__init__(parent)
		# Exponer el QListWidget como un atributo público
		self.listWidget = DroppableList()
		# self.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
		# Layout para los botones (Vertical)
		button_layout = QVBoxLayout()

		self._btn_add = QPushButton("+")
		self._btn_remove = QPushButton("-")
		self._btn_up = QPushButton("▲")
		self._btn_down = QPushButton("▼")

		sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)

		self._btn_add.setSizePolicy(sizePolicy)
		self._btn_remove.setSizePolicy(sizePolicy)
		self._btn_up.setSizePolicy(sizePolicy)
		self._btn_down.setSizePolicy(sizePolicy)

		button_layout.addWidget(self._btn_add)
		button_layout.addWidget(self._btn_remove)
		button_layout.addWidget(self._btn_up)
		button_layout.addWidget(self._btn_down)

		# Layout principal
		main_layout = QHBoxLayout(self)
		main_layout.addWidget(self.listWidget,10)  		# revisar el stretch
		main_layout.addLayout(button_layout , 1)

		# Conectar botones con funciones
		self._btn_add.clicked.connect(self.add_item)
		self._btn_remove.clicked.connect(self.remove_item)
		self._btn_up.clicked.connect(self.move_item_up)
		self._btn_down.clicked.connect(self.move_item_down)

	def add_item(self):
		"""Agrega un nuevo elemento a la lista."""
		item = QListWidgetItem("")  # Crear un item vacío
		item.setFlags(item.flags() )
		self.listWidget.addItem(item)  # Agregarlo a la lista
		self.listWidget.setCurrentItem(item)  # Seleccionarlo
		self.listWidget.editItem(item)  # Habilitar la edición

	def remove_item(self):
		"""Elimina el elemento seleccionado."""
		item = self.listWidget.currentItem()
		if item:
			self.listWidget.takeItem(self.listWidget.row(item))

	def move_item_up(self):
		"""Mueve el elemento seleccionado hacia arriba."""
		row = self.listWidget.currentRow()
		if row > 0:
			item = self.listWidget.takeItem(row)
			self.listWidget.insertItem(row - 1, item)
			self.listWidget.setCurrentItem(item)

	def move_item_down(self):
		"""Mueve el elemento seleccionado hacia abajo."""
		row = self.listWidget.currentRow()
		if row < self.listWidget.count() - 1:
			item = self.listWidget.takeItem(row)
			self.listWidget.insertItem(row + 1, item)
			self.listWidget.setCurrentItem(item)