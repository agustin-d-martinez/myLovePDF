from PySide6.QtWidgets import QApplication, QMainWindow
from ButtonListWidget import ButtonListWidget  # Importamos el widget personalizado

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom List Widget")
        self.setGeometry(100, 100, 400, 300)

        # Instanciar el CustomListWidget
        self.custom_list = ButtonListWidget(self)
        self.setCentralWidget(self.custom_list)
		
        # Acceder directamente al QListWidget
        self.custom_list.listWidget.addItem("Archivo1.pdf")
        self.custom_list.listWidget.addItem("Archivo2.pdf")

        # Obtener todos los elementos
        items = [self.custom_list.listWidget.item(i).text() for i in range(self.custom_list.listWidget.count())]
        print("Archivos en la lista:", items)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

