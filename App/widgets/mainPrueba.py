from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ButtonListWidget import ButtonListWidget  # Importamos el widget personalizado
from ModernCheckBox import ModernCheckBox
from DroppableLineEdit import DroppableLineEdit
from ImageLabel import ImageLabel

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(500,500)

		self.containter = QFrame()
		self._layout = QVBoxLayout()
		self.lineEdit = DroppableLineEdit()

		# Instanciar el CustomListWidget
		self.custom_list = ButtonListWidget(self)
		self.custom_list.setFixedSize(300,200)
		self.boton = ModernCheckBox(self,"hola")
		self.imagen = ImageLabel(self,editable=True)
		self.imagen2 = ImageLabel(self,editable=True)
		self.imagen.setFixedHeight(80)
		self.imagen2.setFixedHeight(80)
		self._layout.addWidget(self.custom_list, Qt.AlignCenter, Qt.AlignCenter)
		self._layout.addWidget(self.boton, Qt.AlignCenter, Qt.AlignCenter)
		self._layout.addWidget(self.lineEdit)
		self._layout.addWidget(self.imagen)
		self._layout.addWidget(self.imagen2)
		# Acceder directamente al QListWidget
		self.custom_list.listWidget.addItem("Archivo1.pdf")
		self.custom_list.listWidget.addItem("Archivo2.pdf")

		self.containter.setLayout(self._layout)
		self.setCentralWidget(self.containter)


		# Obtener todos los elementos
		items = [self.custom_list.listWidget.item(i).text() for i in range(self.custom_list.listWidget.count())]
		print("Archivos en la lista:", items)

		#self.show()

if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec()

