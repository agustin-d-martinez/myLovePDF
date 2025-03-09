from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import * 

class ImageLabel(QLabel):
	def __init__(self, *args, editable=False, default_pixmap_path=u"widgets/NoImage.svg", **kwargs):
		super().__init__(*args, **kwargs)
		self.setScaledContents(True)

		self._defaultPixmap = QPixmap(default_pixmap_path) 	
		if self.pixmap().isNull():
			self.clear()
			self.setPixmap(self._defaultPixmap)
		self._context_menu = QMenu(self)

		action_cut = QAction(QIcon.fromTheme("edit-cut"),"Cortar",self)
		action_cut.setShortcut(QKeySequence("CTRL+X"))
		action_cut.triggered.connect(self.cut)		

		action_copy = QAction(QIcon.fromTheme("edit-copy"),"Copiar",self)
		action_copy.setShortcut(QKeySequence("CTRL+C"))		
		action_copy.triggered.connect(self.copy)	

		action_paste = QAction(QIcon.fromTheme("edit-paste"),"Pegar",self)
		action_paste.setShortcut(QKeySequence("CTRL+V"))
		action_paste.triggered.connect(self.paste)		

		action_delete = QAction(QIcon.fromTheme("edit-delete"),"Borrar",self)
		action_delete.setShortcut(Qt.Key.Key_Delete)
		action_delete.triggered.connect(self.delete)
		
		self._context_menu.addAction(action_cut)
		self._context_menu.addAction(action_copy)
		self._context_menu.addAction(action_paste)
		self._context_menu.addAction(action_delete)

		if editable:
			self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
			self.customContextMenuRequested.connect(self.execContextMenu)

	def execContextMenu(self, pos):
		self._context_menu.exec(self.mapToGlobal(pos))
	def cut (self):
		self.copy()
		self.delete()
	def copy (self):
		clipboard = QApplication.clipboard()
		pixmap = self.pixmap()
		if pixmap :
			clipboard.setPixmap(pixmap)
	def paste (self):
		pixmap = QApplication.clipboard().pixmap()
		if not pixmap.isNull():
			self.setPixmap(pixmap)
	def delete(self):
		self.clear()
		self.setPixmap(self._defaultPixmap)