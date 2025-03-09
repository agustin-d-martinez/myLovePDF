from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import * 

class ImageLabel(QLabel):
	def __init__(self, parent = None, pixmap = u"widgets\\add_symbol.svg", editable = False):
		super().__init__(parent)
		fondo = QPixmap(pixmap)
		self.setPixmap(fondo)
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

		self.contextMenu = QMenu("",self)
		action_cut = QAction("Cortar",None)

		if editable:
			self.contextMenu.addAction("cortar", self.cut, shortcut=QKeySequence(Qt.Key.Key_Control | Qt.Key.Key_X) )
	
	def cut (self):
		print(1234567898)
	def copy (self):
		pass
	def paste (self):
		pass