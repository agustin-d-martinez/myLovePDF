from PySide6.QtWidgets import *
from PySide6.QtCore import *

class DroppableList(QListWidget):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setAcceptDrops(True)

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