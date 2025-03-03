# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import utils.documentsUtils as doc
import res_rc_rc
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py ; pyside6-rcc res_rc.qrc -o res_rc_rc.py

from ui_form import Ui_MyLovePDF

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MyLovePDF()
		self.ui.setupUi(self)
		self.ui.label_5.setHidden(True)
		self.ui.NombreExtra.setHidden(True)

		self.ui.ListFileSelector_2.listWidget.currentItemChanged.connect(self.UpdatePhoto)
	
	def ObtenerRangos(string: str) -> list[int] :
		lista = set()
		for number in string.split(","):
			if '-' in number:
				start, stop = map(int,number.split('-'))
				lista.update(range(start,stop + 1))
			else :
				lista.add(int(number))
			return sorted(lista)

	def UpdatePhoto(self , item : QListWidgetItem ):
		path_img = QPixmap(item.text())
		self.ui.label_11.setPixmap(path_img)
		self.ui.label_11.setScaledContents(True)

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
			self.ui.ListFileSelector_2.listWidget.addItems(archivo)
		elif sender == self.ui.ButtonFileSelect_6 :
			archivo, _ = QFileDialog.getOpenFileName(self, "Abrir PDF", "", "Archivo PDF (*.pdf)", options=opciones)
			self.ui.ListFileSelector_3.listWidget.addItems(archivo)
		elif sender == self.ui.ButtonFileSelect_7 :
			archivo, _ = QFileDialog.getOpenFileNames(self, "Abrir archivos", "", "All Files (*)", options=opciones)
			self.ui.ListFileSelector_4.listWidget.addItems(archivo)


	def ObtenerTexto( self, listWidget: QListWidget ) -> list[str] : 
		lista = []
		for i in range(listWidget.count()):
			lista.append(listWidget.item(i).text())
		return lista

	def UnirPDF(self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector.listWidget )
		
		if len(entradas) < 2:
			self.ErrorMessage()
			return
		
		idx = self.ui.comboBox.currentIndex()
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			doc.unir_pdfs(entradas,salida,idx)

	def ImageToPDF (self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector_2.listWidget )
		if not entradas :
			self.ErrorMessage()
			return
		
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			doc.imagenes_a_pdf(entradas, salida)

	def PDFtoImage (self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector_3.listWidget )
		if not entradas :
			self.ErrorMessage()
			return
		
		salida = self.SaveFile("Imagen (*.jpg)")
		if salida :
			print("NOT IMPLEMENTED")


	def SepararPDF(self):
		entrada = self.ui.FileSelector_2.text()
		if not entrada : 
			self.ErrorMessage()
			return
		pags = self.ObtenerRangos(self.ui.HojasSeparar.text())
		salida = self.SaveFile("Archivo PDF (*.pdf)")

		if salida : 
			doc.separar_pdf(entrada ,salida , pags ,self.ui.checkBoxConsevar.isChecked() , self.ui.NombreExtra.text())

	def SepararHojas(self):
		entrada = self.ui.FileSelector_3.text()
		if not entrada : 
			self.ErrorMessage()
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
			self.ErrorMessage()
			return
		
		paginas = self.ObtenerRangos(self.ui.HojasSeparar_2.text())

		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			doc.agregar_hojas_blanco(entrada,salida,paginas)

	def Renombrar(self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector_4.listWidget )
		if not entradas :
			self.ErrorMessage()
			return
		
		inicial = self.ui.spinBox.value()
		doc.renombrar_template(entradas, self.ui.NameTemplate.text() , inicial)

	def SaveFile(self, type) :
		file , _ =  QFileDialog.getSaveFileName(self,"Guardar Archivo", "" , type)
		return file
	
	def ErrorMessage(self) :
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Critical)  # Tipo de mensaje: Error
		msg.setWindowTitle("Error")
		msg.setText("No hay archivos de entrada.")
		#msg.setInformativeText("Revisa los datos ingresados e intenta nuevamente.")
		msg.exec()  # Mostrar el cuadro de diálogo


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
