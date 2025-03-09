from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from DroppableList import DroppableList

class ButtonListWidget(QWidget):
	_btn_add = None
	_btn_remove = None
	_btn_up = None
	_btn_down = None

	def __init__(self, parent=None):
		super().__init__(parent)
		# Exponer el QListWidget como un atributo público
		self.listWidget = DroppableList()
		self.listWidget.setEditTriggers(QListWidget.AllEditTriggers)
		self.setStyleSheet('''QPushButton { background-color: rgba(255, 255, 255, 180);color: transparent; border: none;border-radius: 7px;} 
					 QPushButton:hover{background-color: rgba(255, 255, 255, 220);;}
					 QPushButton:pressed{background-color: rgba(255, 255, 255, 250);;}
					 QListWidget{background-color: rgb(255, 255, 255);border-radius:10px;}''')

		# Layout para los botones (Vertical)
		button_layout = QVBoxLayout()
		button_layout.setSpacing(1)

		self._btn_add = QPushButton()
		self._btn_remove = QPushButton()
		self._btn_up = QPushButton()
		self._btn_down = QPushButton()

		self._btn_add.setIcon(QIcon("widgets\\add_symbol.svg"))				## No es generico!!!
		self._btn_remove.setIcon(QIcon("widgets\\remove_symbol.svg"))
		self._btn_up.setIcon(QIcon("widgets\\up_symbol.svg"))
		self._btn_down.setIcon(QIcon("widgets\\down_symbol.svg"))

		button_layout.addWidget(self._btn_add)
		button_layout.addWidget(self._btn_remove)
		button_layout.addWidget(self._btn_up)
		button_layout.addWidget(self._btn_down)

		# Layout principal
		main_layout = QHBoxLayout(self)
		main_layout.addWidget(self.listWidget,10)  		# revisar el stretch
		main_layout.addLayout(button_layout , 1)
		main_layout.setContentsMargins(QMargins(2,0,2,0))
		main_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

		# Conectar botones con funciones
		self._btn_add.clicked.connect(self.add_item)
		self._btn_remove.clicked.connect(self.remove_item)
		self._btn_up.clicked.connect(self.move_item_up)
		self._btn_down.clicked.connect(self.move_item_down)

		#Conect para habilitar botones
		self.listWidget.model().rowsInserted.connect(self.UpdateButtons)
		self.listWidget.model().rowsRemoved.connect(self.UpdateButtons)

		self.UpdateButtons()

	def UpdateButtons(self, *args):
		if self.listWidget.count() == 0:
			self._btn_remove.setDisabled(True)
			self._btn_up.setDisabled(True)
			self._btn_down.setDisabled(True)
		else:
			self._btn_remove.setDisabled(False)
			self._btn_up.setDisabled(False)
			self._btn_down.setDisabled(False)

	def resizeEvent(self, event):
		btn_widht = min(self.width()//11,self.height()//4 - 2)
		btn_size = QSize(btn_widht , btn_widht)

		for btn in [self._btn_add , self._btn_remove , self._btn_up , self._btn_down] :
			btn.setIconSize(btn_size)
			btn.setFixedSize(btn_size)
		return super().resizeEvent(event)

	def add_item(self):
		"""Agrega un nuevo elemento a la lista."""
		item = QListWidgetItem("")  
		self.listWidget.addItem(item)  
		self.listWidget.setCurrentItem(item)  

		# Crear un editor manualmente
		editor = QLineEdit(self.listWidget)  
		self.listWidget.setItemWidget(item, editor)  # Asignar el editor al item
		editor.setFocus()  
		editor.selectAll()  

		# Guardar el texto en el item cuando el usuario termine de editar
		editor.editingFinished.connect(lambda: self.finalizar_edicion(item, editor))

	def finalizar_edicion(self, item: QListWidgetItem, editor: QLineEdit):
		self.listWidget.setItemWidget(item, None)  # Remover el editor
		text = editor.text()
		if not text :
			self.remove_item()
		else:
			item.setText(editor.text())  
	
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