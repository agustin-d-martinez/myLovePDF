# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import utils.documentsUtils as doc
import utils.videoUtils as vid
import os

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py ; pyside6-rcc res_rc.qrc -o res_rc_rc.py

from ui_form import Ui_MyLovePDF

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MyLovePDF()
		self.ui.setupUi(self)

		#Initial hide() 
		self.ui.pushButtonPDFmini.hide()
		self.ui.widgetIMG.hide()
		self.ui.widgetFILE.hide()
		self.ui.widgetMSC.hide()
		self.ui.label_5.hide()
		self.ui.NombreExtra.hide()

		#Custom connect
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
		path_img = item.text()
		if path_img :
			self.ui.label_11.setPixmap(QPixmap(path_img))
			self.ui.label_11.setScaledContents(True)

	def selectFile(self):
		sender_map = {
			self.ui.ButtonFileSelect: ("pdf", self.ui.ListFileSelector.listWidget, True),
			self.ui.ButtonFileSelect_2: ("pdf", self.ui.FileSelector_2, False),
			self.ui.ButtonFileSelect_3: ("pdf", self.ui.FileSelector_3, False),
			self.ui.ButtonFileSelect_4: ("pdf", self.ui.FileSelector_4, False),
			self.ui.ButtonFileSelect_5: ("img", self.ui.ListFileSelector_2.listWidget, True),
			self.ui.ButtonFileSelect_6: ("pdf", self.ui.ListFileSelector_3.listWidget, True),
			self.ui.ButtonFileSelect_7: ("all", self.ui.ListFileSelector_4.listWidget, True),
			self.ui.ButtonFileSelect_8: ("img", self.ui.FileSelector_8, False),
			self.ui.ButtonFileSelect_9: ("mp4", self.ui.FileSelector_9, False),
		}

		sender = self.sender()
		opciones = QFileDialog.Options()

		if sender in sender_map:
			file_type, target_widget, multiple = sender_map[sender]
			
			filters = {
				"pdf": "Archivos PDF (*.pdf)",
				"img": "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
				"mp4": "Video Files (*.mp4)",
				"all": "All Files (*)"
			}

			if multiple:
				archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivo", "", filters[file_type], options=opciones)
				target_widget.addItems(archivos)
			else:
				archivos, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", filters[file_type], options=opciones)
				target_widget.setText(archivos)


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
		
		salida = QFileDialog.getExistingDirectory(self, "Seleccionar Archivo", "")
		if salida :
			doc.pdf_a_imagen(entradas,salida)

	def ExtensionImg(self):
		entrada = self.ui.FileSelector_8.text()
		extension = self.ui.comboBox_2.currentText()
		doc.cambiar_img_ext(entrada , extension)

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

	def GuardarMusica(self):
		archivo = os.path.join(self.ui.lineEditMusicFolder.text(),self.ui.listWidgetMusic.currentItem().text())
		if not archivo :
			self.ErrorMessage()
			return
		tags = {}
		tags["title"] = self.ui.lineEditSong.text()
		tags["artist"]= self.ui.lineEditInterpeter.text()
		tags["album"]= self.ui.lineEditAlbum.text()
		tags["composer"]= self.ui.lineEditCompositor.text()
		tags["album_artist"]= self.ui.lineEditAlbumInter.text()
		tags["genre"]= self.ui.comboBoxGenre.currentText()
		tags["track"]= f"{self.ui.spinBoxTrack.value()}/{self.ui.spinBoxMaxTrack.value()}"
		tags["lyrics"]= self.ui.TextEditLiryc.toPlainText()
		tags["year"]= self.ui.lineEditYear.text()
		tags["mood"]= self.ui.lineEditMood.text()

		buffer = QBuffer()
		buffer.open(QIODevice.WriteOnly)
		
		self.ui.labelCover.pixmap().save(buffer, "PNG")		# Puedes elegir el formato: "PNG" o "JPEG"
		tags["cover"]= bytes(buffer.data())
		buffer.close()

		doc.setMusicTags(archivo,tags)
		QMessageBox.information(self,"Guardado","Los cambios han sido guardados.")

	def MP4_a_MP3(self):
		mp4 = self.ui.FileSelector_9.text()
		mp3 = self.SaveFile(".mp3")
		if mp3 and mp4 : 
			vid.mp4_a_mp3(mp4,mp3)

	def DescargarVideo(self):
		formato = self.ui.comboBoxFileType.currentText()
		archivo = self.SaveFile(f".{formato}")
		url = self.ui.lineEditUrl.text()
		if url and archivo:
			if formato == "mp3" :
				vid.descargar_audio(url,archivo)
			else :
				vid.descargar_video(url,archivo)

	def SaveFile(self, type) :
		file , _ =  QFileDialog.getSaveFileName(self,"Guardar Archivo", "" , type)
		return file
	
	def ErrorMessage(self) :
		msg = QMessageBox(self)
		msg.setIcon(QMessageBox.Critical)  # Tipo de mensaje: Error
		msg.setWindowTitle("Error")
		msg.setText("No hay archivos de entrada.")
		msg.exec()  # Mostrar el cuadro de diálogo

	def UpdateMusicFile(self):
		self._UpdateMusicList(self.ui.lineEditMusicFolder.text())
	def ChangeMusicFile(self):
		archivo = QFileDialog.getExistingDirectory(self, "Seleccionar Archivo", "")
		self.ui.lineEditMusicFolder.setText(archivo)
		self._UpdateMusicList(archivo)

	def UpdateVideo(self):
		titulo, miniatura = vid.obtenerTituloPortadaVideo(self.ui.lineEditUrl.text())
		self.ui.lineEditVideoTitle.setText(titulo)
		pixmap = QPixmap()
		pixmap.loadFromData(miniatura)
		self.ui.labelThumbnail.setPixmap(pixmap)
		self.ui.labelThumbnail.setScaledContents(True)

	def _UpdateMusicList(self, archivo):
		self.ui.listWidgetMusic.clear()
		archivos = []
		if archivo :
			for root, dirs, files in os.walk(archivo):
				for file in files :
					if file.endswith(".mp3"):
						full_path = os.path.join(root,file)
						archivos.append(os.path.relpath(full_path,archivo))
			self.ui.listWidgetMusic.addItems(archivos)

	def GetItemMusicTags(self, item: QListWidgetItem):
		tags = doc.getMusicTags(os.path.join(self.ui.lineEditMusicFolder.text(),item.text()))
		self.ui.lineEditSong.setText(tags.get("title",""))
		self.ui.lineEditInterpeter.setText(tags.get("artist",""))
		self.ui.lineEditAlbum.setText(tags.get("album",""))
		self.ui.lineEditCompositor.setText(tags.get("composer",""))
		self.ui.lineEditAlbumInter.setText(tags.get("album_artist",""))
		self.ui.TextEditLiryc.setPlainText(tags.get("lyrics",""))
		self.ui.lineEditYear.setText(tags.get("year",""))

		tracks = self.separateTracks(tags.get("track",""))
		self.ui.spinBoxTrack.setValue(tracks[0])
		self.ui.spinBoxMaxTrack.setValue(tracks[1])
		self.ui.comboBoxGenre.setCurrentText(tags.get("genre",""))
		self.ui.lineEditMood.setText(tags.get("mood",""))

		pixmap = QPixmap()
		cover = tags.get("cover",b"")
		pixmap.loadFromData(cover)
		if cover == b"":
			pixmap.load(u":/resources/resources/NoImage.svg")
		pixmap = pixmap.scaled(self.ui.labelCover.size(),Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation)
		self.ui.labelCover.setPixmap(pixmap)

	def separateTracks(self,track_str:str):
		try:
			parts = track_str.split("/")
			if len(parts) == 2:
				track = int(parts[0].strip())
				total = int(parts[1].strip())
				return track, total
			elif len(parts) == 1:
				# Si solo viene un número, asumimos total 0
				return int(parts[0].strip()), 0
		except Exception:
			return 0, 0


	def OpenTab(self):
		mapping = {
			self.ui.pushButtonPDFmini: self.ui.widgetPDF,
			self.ui.pushButtonIMGmini: self.ui.widgetIMG,
			self.ui.pushButtonFILEmini:self.ui.widgetFILE,
			self.ui.pushButtonMSCmini: self.ui.widgetMSC,
		}
		sender = self.sender()
		for button , widget  in mapping.items():
			if button == sender :
				button.hide()
				widget.show()
			else :
				button.show()
				widget.hide()

	def CloseTab(self):
		mapping = {
			self.ui.pushButtonPDF: (self.ui.pushButtonPDFmini, self.ui.widgetPDF),
			self.ui.pushButtonIMG: (self.ui.pushButtonIMGmini, self.ui.widgetIMG),
			self.ui.pushButtonFILE:(self.ui.pushButtonFILEmini, self.ui.widgetFILE),
			self.ui.pushButtonMSC: (self.ui.pushButtonMSCmini, self.ui.widgetMSC),
		}
		sender = self.sender()
		button , widget  = mapping(sender)
		button.show()
		widget.hide()

	def setActiveTab(self, active_key):
		tabs = {'PDF': (self.ui.pushButtonPDF, self.ui.widgetPDF),
		'IMG': (self.ui.pushButtonIMG, self.ui.widgetIMG),
		'FILE': (self.ui.pushButtonFILE, self.ui.widgetFILE),
		'MSC': (self.ui.pushButtonMSC, self.ui.widgetMSC),}

		for key , (button , widget) in tabs.items():
			if key == active_key :
				button.hide()
				widget.show()
			else:
				button.show()
				widget.hide()
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec())
