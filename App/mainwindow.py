# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import *
import utils.documentsUtils as doc

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic App\form.ui -o App\ui_form.py

from ui_form import Ui_MyLovePDF

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MyLovePDF()
		self.ui.setupUi(self)
		self.ui.label_5.setHidden(True)
		self.ui.NombreExtra.setHidden(True)
	

	def selectFile(self):
		sender = self.sender()
		opciones = QFileDialog.Options()
		if sender == self.ui.ButtonFileSelect : 
			archivo, _ = QFileDialog.getOpenFileNames(self, "Abrir PDF", "", "Archivos PDF (*.pdf)", options=opciones)
			self.ui.ListFileSelector.listWidget.addItems(archivo)
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

	def ObtenerTexto( self, listWidget: QListWidget ) -> list[str] : 
		lista = []
		for i in range(listWidget.count()):
			lista.append(listWidget.item(i).text())
		if not lista :
			return None
		else :
			return lista

	def UnirPDF(self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector.listWidget )
		
		if len(entradas) < 2:
			print("ERROR1")
			return
		
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			doc.unir_pdfs(entradas,salida, self.ui.checkBox.isChecked() , self.ui.checkBox_2.isChecked() )

	def ImageToPDF (self):
		entradas = self.ObtenerTexto( self.ui.FileSelector_5.text() )
		if not entradas :
			print("ERROR1")
			return
		
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			doc.imagenes_a_pdf(entradas, salida)

	def PDFtoImage (self):
		entradas = self.ObtenerTexto( self.ui.FileSelector_6.text() )
		if not entradas :
			print("ERROR1")
			return
		
		salida = self.SaveFile("Imagen (*.jpg)")
		if salida :
			print("NOT IMPLEMENTED")


	def SepararPDF(self):
		entrada = self.ui.FileSelector_2.text()
		if not entrada : 
			print("ERROR 1")
			return
		pags = self.ui.HojasSeparar.text().split(",")
		pags_int = list(map(int,pags))

		salida = self.SaveFile("Archivo PDF (*.pdf)")

		if salida : 
			doc.separar_pdf(entrada ,salida ,pags_int ,self.ui.checkBoxConsevar.isChecked() , self.ui.NombreExtra.text())

	def SepararHojas(self):
		entrada = self.ui.FileSelector_3.text()
		if not entrada : 
			print("ERROR 1")
			return
		if self.ui.checkBoxSplitAll.isChecked() :
			paginas = None
		else :
			paginas = self.ui.HojasSeparar_3.text()
			paginas = list(map(int, paginas))

		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			doc.separar_hojas(entrada , salida , paginas)

	def HojaBlanco (self): 
		entrada = self.ui.FileSelector_4.text()
		if not entrada : 
			print("ERROR 1")
			return
		
		paginas = self.ui.HojasSeparar_2.text()
		paginas = list(map(int, paginas))

		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			print("NO IMPLEMENTADO")


	def SaveFile(self, type) :
		file , _ =  QFileDialog.getSaveFileName(self,"Guardar Archivo", "" , type)
		return file

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
