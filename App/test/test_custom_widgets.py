import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from customWidgets.ButtonListWidget import ButtonListWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Prueba ButtonListWidget")
        self.resize(500, 300)
        self.c_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.list_widget = ButtonListWidget(self)
        self.button = QPushButton("hola")
        self.button1 = QPushButton("chau")
        self.v_layout.addWidget(self.list_widget)
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.button1)
        self.c_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.c_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
