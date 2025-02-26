# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import *
import documentsUtils as doc

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic App\form.ui -o App\ui_form.py

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.label_5.setHidden(True)
		self.ui.NombreExtra.setHidden(True)


	
	def selectFile(self):
		sender = self.sender()
		opciones = QFileDialog.Options()
		if sender == self.ui.ButtonFileSelect : 
			archivo, _ = QFileDialog.getOpenFileNames(self, "Abrir PDF", "", "Archivos PDF (*.pdf)", options=opciones)
			self.ui.FileSelector_1.setText("; ".join(archivo))
		elif sender == self.ui.ButtonFileSelect_2 :
			archivo, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivo PDF (*.pdf)", options=opciones)
			self.ui.FileSelector_2.setText(archivo)
		elif sender == self.ui.ButtonFileSelect_3 :
			archivo, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivo PDF (*.pdf)", options=opciones)
			self.ui.FileSelector_3.setText(archivo)
		elif sender == self.ui.ButtonFileSelect_4 :
			archivo, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivo PDF (*.pdf)", options=opciones)
			self.ui.FileSelector_4.setText(archivo)
		elif sender == self.ui.ButtonFileSelect_5 :
			archivo, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivo", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=opciones)
			self.ui.FileSelector_5.setText("; ".join(archivo))
		elif sender == self.ui.ButtonFileSelect_6 :
			archivo, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivo PDF (*.pdf)", options=opciones)
			self.ui.FileSelector_6.setText(archivo)

	def ObtenerTexto( self, string: str ) -> list[str] : 
		return string.split("; ")

	def UnirPDF(self):
		entradas = self.ObtenerTexto( self.ui.FileSelector_1.text() )
		
		if len(entradas) < 2:
			print("ERROR1")
			return
		
		salida , _ = QFileDialog.getSaveFileName(self,"Guardar Archivo", "" , "Archivo PDF (*.pdf)")
		if salida :
			doc.unir_pdfs(entradas,salida, self.ui.checkBox.isChecked() , self.ui.checkBox_2.isChecked() )

	def ImageToPDF (self):
		entradas = self.ObtenerTexto( self.ui.FileSelector_5.text() )
		if not entradas :
			print("ERROR1")
			return
		
		salida , _ = QFileDialog.getSaveFileName(self,"Guardar Archivo", "" , "Archivo PDF (*.pdf)")
		if salida :
			doc.imagenes_a_pdf(entradas, salida)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
