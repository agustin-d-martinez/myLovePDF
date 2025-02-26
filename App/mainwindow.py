# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic App\form.ui -o App\ui_form.py

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
	
	def selectFile(self):
		archivo, _ = QFileDialog.getOpenFileNames(self, "Abrir PDF", "", "Archivos PDF (*.pdf)")
		self.ui.FileSelector1.setText(archivo[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
