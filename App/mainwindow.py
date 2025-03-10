# This Python file uses the following encoding: utf-8
import sys
import os
import ctypes

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import utils.documentsUtils as doc
import utils.videoUtils as vid
from utils.DownloadThread import DownloadThread

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py ; pyside6-rcc res_rc.qrc -o res_rc_rc.py

from ui_form import Ui_MyLovePDF

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MyLovePDF()
		self.setWindowIcon(QIcon(":/resources/resources/AppIcon.png"))	#Icono arriba a la izq.
		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MyLovePDF.app.1')	#Permite que cambie el logo del taskbar
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

	def ObtenerRangos(self,string: str) -> list[int] :
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
				"mp4": "MP4 Video Files (*.mp4)",
				"all": "All Files (*)"
			}

			if multiple:
				archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivo", "", filters[file_type], options=opciones)
				target_widget.addItems(archivos)
			else:
				archivos, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", filters[file_type], options=opciones)
				target_widget.setText(archivos)

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
		button , widget  = mapping[sender]
		button.show()
		widget.hide()		

	def ObtenerTexto( self, listWidget: QListWidget ) -> list[str] : 
		lista = []
		for i in range(listWidget.count()):
			lista.append(listWidget.item(i).text())
		return lista

	def UnirPDF(self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector.listWidget )
		
		if len(entradas) == 0:
			self.ErrorMessage("No se ingresó ningún archivo.")
			return
		elif len(entradas) == 1:
			self.ErrorMessage("No se ingresaron suficientes archivos.")
			return
		
		idx = self.ui.comboBox.currentIndex()
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			if doc.unir_pdfs(entradas,salida,idx):
				QMessageBox().information(self,"PDF generado", "PDF's unidos con éxito.")
			else:
				self.ErrorMessage("Error al unir los PDF's.")

	def ImageToPDF (self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector_2.listWidget )
		if not entradas :
			self.ErrorMessage("No se ingresó ningún archivo.")
			return
		
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			if doc.imagenes_a_pdf(entradas, salida):
				QMessageBox().information(self,"PDF generado", "PDF guardado con éxito.")
			else:
				self.ErrorMessage("Erroral convertir imágenes a PDF.")

	def PDFtoImage (self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector_3.listWidget )
		if not entradas :
			self.ErrorMessage("No se seleccionó ningún archivo.")
			return
		
		salida = QFileDialog.getExistingDirectory(self, "Seleccionar Archivo", "")
		if salida :
			if doc.pdf_a_imagen(entradas,salida):
				QMessageBox().information(self,"Imagen generada", "Imágenes guardadas con éxito.")
			else:
				self.ErrorMessage("Error al convertir el PDF en imágenes.")

	def ExtensionImg(self):
		entrada = self.ui.FileSelector_8.text()
		if not entrada :
			self.ErrorMessage("No se ingresó ninguna imagen.")
			return
		extension = self.ui.comboBox_2.currentText()
		if doc.cambiar_img_ext(entrada , extension):
			QMessageBox().information(self,"Imagen generada", "Imagen guardada con éxito.")
		else:
			self.ErrorMessage("Error al cambiar la extensión de la imagen.")

	def SepararPDF(self):
		entrada = self.ui.FileSelector_2.text()
		if not entrada : 
			self.ErrorMessage("No se seleccionó ningún archivo.")
			return
		pags = self.ObtenerRangos(self.ui.HojasSeparar.text())
		salida = self.SaveFile("Archivo PDF (*.pdf)")

		if salida : 
			if doc.separar_pdf(entrada ,salida , pags ,self.ui.checkBoxConsevar.isChecked() , self.ui.NombreExtra.text()):
				QMessageBox().information(self,"PDF generado", "PDF's separados con éxito.")
			else:
				self.ErrorMessage("Error al separar los PDFs")

	def SepararHojas(self):
		entrada = self.ui.FileSelector_3.text()
		if not entrada : 
			self.ErrorMessage("No se ingresó ningún archivo.")
			return
		if self.ui.checkBoxSplitAll.isChecked() :
			paginas = None
		else :
			paginas = self.ObtenerRangos(self.ui.HojasSeparar_3.text())

		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			if doc.separar_hojas(entrada , salida , paginas):
				QMessageBox().information(self,"PDF's generados", "Hojas separadas con éxito.")
			else:
				self.ErrorMessage("Error al separar las hojas.")

	def HojaBlanco (self): 
		entrada = self.ui.FileSelector_4.text()
		if not entrada : 
			self.ErrorMessage("No se ingresó ningún archivo.")
			return
		
		paginas = self.ObtenerRangos(self.ui.HojasSeparar_2.text())
		salida = self.SaveFile("Archivo PDF (*.pdf)")
		if salida :
			if doc.agregar_hojas_blanco(entrada,salida,paginas):
				QMessageBox().information(self,"PDF actualizado", "Hojas blancas colocadas con éxito.")
			else:
				self.ErrorMessage("Error al colocar hojas en blanco.")

	def Renombrar(self):
		entradas = self.ObtenerTexto( self.ui.ListFileSelector_4.listWidget )
		if not entradas :
			self.ErrorMessage("No se ingresó ningún archivo.")
			return
		
		inicial = self.ui.spinBox.value()
		if doc.renombrar_template(entradas, self.ui.NameTemplate.text() , inicial):
			QMessageBox().information(self,"Guardado", "Archivos renombrados con éxito.")
		else:
			self.ErrorMessage("Error al renombrar los archivos")

	def GuardarMusica(self):
		archivo = os.path.join(self.ui.lineEditMusicFolder.text(),self.ui.listWidgetMusic.currentItem().text())
		if not archivo :
			self.ErrorMessage("No se seleccionó ningún archivo.")
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

		if doc.setMusicTags(archivo,tags):
			QMessageBox.information(self,"Archivo Actualizado","Música guardada con éxito.")
		else:
			self.ErrorMessage("Error al actualizar MP3.")

	def MP4_a_MP3(self):
		mp4 = self.ui.FileSelector_9.text()
		if not mp4 and not mp4.endswith(".mp4"):
			self.ErrorMessage("No se ingresó ningún archivo MP4.")
			return
		mp3 = self.SaveFile(".mp3")
		if mp3 and mp4 : 
			if vid.mp4_a_mp3(mp4,mp3):
				QMessageBox().information(self,"MP3 generado", "Archivo MP3 guardado con éxito.")
			else:
				self.ErrorMessage("Error al convertir a MP3.")

	def DescargarVideo(self):
		url = self.ui.lineEditUrl.text()
		if not 'youtube.com' in url and not 'youtu.be' in url: 
			self.ErrorMessage("No se colocó ninguna URL.")
			return
		formato = self.ui.comboBoxFileType.currentText()
		archivo_salida = self.SaveFile(f"{formato.upper()} File (*.{formato}))")
		if archivo_salida:
			resolusion = None
			if formato == "mp4" :
				resolusion = int(self.ui.comboBoxResolution.currentText().replace("p",""))
			self.download_thread = DownloadThread(url,archivo_salida,formato,resolusion)
			self.download_thread.finished.connect(self.onDownloadFinished)
			self.download_thread.error.connect(self.onDownloadError)

			self.ui.SaveButton_10.setText("Descargando...")
			self.ui.SaveButton_10.setEnabled(False)
			self.download_thread.start()

	def onDownloadFinished(self):
		self.ui.SaveButton_10.setEnabled(True)
		self.ui.SaveButton_10.setText("Guardar")
		QMessageBox().information(self,"Descarga completa", "Video descargado con éxito.")
	def onDownloadError(self, err_msg):
		self.ErrorMessage(f"No se pudo descargar el video\n{err_msg}")
		self.ui.SaveButton_10.setEnabled(True)
		self.ui.SaveButton_10.setText("Guardar")

	def SaveFile(self, type) :
		file , _ =  QFileDialog.getSaveFileName(self,"Guardar Archivo", "" , type)
		return file		

	def ErrorMessage(self, mensaje: str) :
		msg = QMessageBox(self)
		msg.setIcon(QMessageBox.Critical)  
		msg.setWindowTitle("Error")
		msg.setText(mensaje)
		msg.exec()  
	def UpdateYoutubeVid(self):
		titulo, miniatura = vid.obtenerTituloPortadaVideo(self.ui.lineEditUrl.text())
		self.ui.lineEditVideoTitle.setText(titulo)
		pixmap = QPixmap()
		pixmap.loadFromData(miniatura)
		self.ui.labelThumbnail.setPixmap(pixmap)
		self.ui.labelThumbnail.setScaledContents(True)

	def UpdateMusicFile(self):
		self._UpdateMusicList(self.ui.lineEditMusicFolder.text())
	def ChangeMusicFile(self):
		archivo = QFileDialog.getExistingDirectory(self, "Seleccionar Archivo", "")
		self.ui.lineEditMusicFolder.setText(archivo)
		self._UpdateMusicList(archivo)
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

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec())
