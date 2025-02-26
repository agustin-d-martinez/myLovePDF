import sys
from PyQt5.QtWidgets import *

class unirPDFPage(QWidget):
	def __init__(self,idx = 0):
		super().__init__()
		layout = QGridLayout()
		## Agrego todos los componentes
		self.label1 = QLabel(f"Elige PDF: {idx}")
		self.PDF_names = QLineEdit()					## self.PDF_names = QTextBrowser()
		self.PDF_findButton = QPushButton('Buscar PDFs')
		self.PDF_findButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.label2 = QLabel('Ubicacion del archivo:')
		self.label3 = QLabel('Nombre resultado:')
		self.PDF_destino_dir = QLineEdit()
		self.PDF_destino_findButton = QPushButton('Buscar')
		self.PDF_destino_findButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

		self.PDF_destino_name = QLineEdit()
		self.OK_button = QPushButton('Unir')

		## Meto los componentes al layout
		layout.addWidget(self.label1 , 0 , 0 )
		layout.addWidget(self.PDF_names , 1 , 0 )
		layout.addWidget(self.PDF_findButton , 1 , 1 )
		layout.addWidget(self.label2 , 2 , 0 )
		layout.addWidget(self.label3 , 2 , 1 )
		layout.addWidget(self.PDF_destino_dir , 3 , 0 )
		layout.addWidget(self.PDF_destino_findButton , 4 , 0 )
		layout.addWidget(self.PDF_destino_name , 3 , 1 )
		layout.addWidget(self.OK_button, 5 , 0)

		self.setLayout(layout)		##Cargo el layout


class MiVentana(QWidget):
	def __init__(self):
		super().__init__()
		# Tamaño y forma de la ventana
		self.setWindowTitle("Mi Aplicación PDF")
		self.setGeometry(100, 100, 600, 400)

		# Widgets de la Ventana ----------
		tabs = QTabWidget()
		tabs.addTab(unirPDFPage(1) , "1")
		tabs.addTab(unirPDFPage(2), "2")

		#Layout de la ventana -------------
		layout = QVBoxLayout()

		# Agrego los widgets al Layout
		layout.addWidget(tabs)


		self.setLayout(layout)	#Seteo el Layout en la App


		# Etiqueta para mostrar mensajes
		#self.label = QLabel("Bienvenido a la aplicación")
		#layout.addWidget(self.label)

		# Botón para seleccionar un archivo PDF (como ejemplo)
		#self.btn_seleccionar = QPushButton("Seleccionar PDF")
		#self.btn_seleccionar.clicked.connect(self.abrir_pdf)
		#layout.addWidget(self.btn_seleccionar)

		# Botón para unir PDFs (solo como ejemplo, aún no implementa la acción)
		#self.btn_unir = QPushButton("Unir PDFs")
		#self.btn_unir.clicked.connect(self.unir_pdfs)
		#layout.addWidget(self.btn_unir)


	def abrir_pdf(self):
		# Abre un diálogo para seleccionar un archivo PDF
		archivo, _ = QFileDialog.getOpenFileNames(self, "Abrir PDF", "", "Archivos PDF (*.pdf)")
		if archivo:
			self.label.setText(f"PDF seleccionado: {archivo}")
			# Aquí podrías guardar la ruta en alguna variable de tu aplicación

	def unir_pdfs(self):
		# Aquí iría la lógica para unir PDFs utilizando tus funciones
		self.label.setText("Función unir PDFs invocada")
		# Por ejemplo, podrías llamar a tu función unir_pdfs(lista_archivos, salida)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ventana = MiVentana()
	ventana.show()
	sys.exit(app.exec_())
