from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import * 

class DroppableLineEdit(QLineEdit):
	def __init__(self, parent = None):
		super().__init__(parent)
		#self.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

	def dragEnterEvent(self, event: QDragEnterEvent):
		if event.mimeData().hasUrls() :
			event.accept()
		else : 
			event.ignore()
	def dragMoveEvent(self, event: QDragMoveEvent):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.DropAction.CopyAction)
			event.accept()
		else : 
			event.ignore()
	def dropEvent(self, event: QDropEvent):
		if event.mimeData().hasUrls() : 
			url = event.mimeData().urls()[0]
			event.setDropAction(Qt.DropAction.CopyAction)
			event.accept()
			if url.isLocalFile():
				self.setText(url.toLocalFile())
			else:
				self.setText(url.toString())
		elif event.mimeData().hasText() : 
			event.setDropAction(Qt.DropAction.CopyAction)
			event.accept()
			self.setText(event.mimeData().text())
		else :
			event.ignore()