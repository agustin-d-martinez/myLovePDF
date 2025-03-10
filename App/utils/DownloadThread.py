from PySide6.QtCore import *
import utils.videoUtils as vid

class DownloadThread(QThread):
	finished = Signal()
	error = Signal(str)

	def __init__(self, url, archivo, formato , resolusion=None , parent=None ):
		super().__init__(parent)
		self.url = url
		self.archivo = archivo
		self.formato = formato
		self.resolusion = resolusion
	
	def run(self):
		try:
			if self.formato == 'mp3':
				if not vid.descargar_audio(self.url, self.archivo):
					self.error.emit("Error al descargar.")
					return
			else:
				if not vid.descargar_video(self.url,self.archivo,self.resolusion) :
					self.error.emit("Error al descargar.")
					return
			self.finished.emit()
		except Exception as e:
			self.error.emit(str(e))

