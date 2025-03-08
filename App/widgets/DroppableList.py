from PySide6.QtWidgets import *
from PySide6.QtCore import *

class DroppableList(QListWidget):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setAcceptDrops(True)

		self.context_menu = QMenu("",self)
		self.context_menu.addAction("Agregar Archivo", self.addFile)
		self.context_menu.addAction("Borrar archivo", self.delFile)
		self.context_menu.addAction("Subir", self.UpFile)
		self.context_menu.addAction("Bajar", self.DownFile)

		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.execContextMenu)

	def execContextMenu(self, pos):
		self.context_menu.exec(self.mapToGlobal(pos))

	def addFile(self):
		archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivo", "","All Files (*)") #TODO CAMBIAR TIPO DE ARCHIVO QUE ADMITE
		if archivos:
			self.addItems(archivos)

	def UpFile(self):
		rows = sorted([self.row(item) for item in self.selectedItems()])
		if not rows or rows[0] == 0:
			return  # No se puede subir si el primer ítem seleccionado está en la posición 0
		for row in rows:
			item = self.takeItem(row)
			self.insertItem(row - 1, item)
			item.setSelected(True)

	def DownFile(self):
		rows = sorted([self.row(item) for item in self.selectedItems()], reverse=True)
		if not rows or rows[0] == self.count() - 1:
			return  # No se puede bajar si el último ítem seleccionado ya está en la última posición
		for row in rows:
			item = self.takeItem(row)
			self.insertItem(row + 1, item)
			item.setSelected(True)

	def delFile(self):
		for item in self.selectedItems():
			self.takeItem(self.row(item))

	def keyPressEvent(self, event):
		if event.key() == Qt.Key.Key_Delete:
			self.delFile()
		return super().keyPressEvent(event)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls:
			event.accept()
		else : 
			event.ignore()
	
	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls:
			event.setDropAction(Qt.CopyAction)
			event.accept()
		else : 
			event.ignore()
	def dropEvent(self, event):
		if event.mimeData().hasUrls : 
			event.setDropAction(Qt.CopyAction)
			event.accept()
			links = []
			for url in event.mimeData().urls() :
				if url.isLocalFile : 
					links.append(str(url.toLocalFile()))
					## links.append(url.toString()) ##Para links de internet
			self.addItems(links)

		else : 
			event.ignore()