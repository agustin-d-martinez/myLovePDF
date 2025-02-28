from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ButtonListWidget import ButtonListWidget  # Importamos el widget personalizado
from ModernCheckBox import ModernCheckBox

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(500,500)

		self.containter = QFrame()
		self._layout = QHBoxLayout()


		# Instanciar el CustomListWidget
		self.custom_list = ButtonListWidget(self)
		self.custom_list.setFixedSize(300,200)
		self.boton = ModernCheckBox("hola",self)
		
		self._layout.addWidget(self.custom_list, Qt.AlignCenter, Qt.AlignCenter)
		self._layout.addWidget(self.boton, Qt.AlignCenter, Qt.AlignCenter)

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

