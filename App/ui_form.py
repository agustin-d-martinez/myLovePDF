# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 638)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(988, 0))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_UnirPDF = QWidget()
        self.tab_UnirPDF.setObjectName(u"tab_UnirPDF")
        self.verticalLayout_2 = QVBoxLayout(self.tab_UnirPDF)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label = QLabel(self.tab_UnirPDF)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.FileSelector_1 = QLineEdit(self.tab_UnirPDF)
        self.FileSelector_1.setObjectName(u"FileSelector_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FileSelector_1.sizePolicy().hasHeightForWidth())
        self.FileSelector_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.FileSelector_1)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ButtonFileSelect = QPushButton(self.tab_UnirPDF)
        self.ButtonFileSelect.setObjectName(u"ButtonFileSelect")

        self.horizontalLayout.addWidget(self.ButtonFileSelect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.tab_UnirPDF)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.tab_UnirPDF)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.tab_UnirPDF)
        self.buttonGroup.addButton(self.checkBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.horizontalSpacer_2 = QSpacerItem(250, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.SaveButton = QPushButton(self.tab_UnirPDF)
        self.SaveButton.setObjectName(u"SaveButton")

        self.verticalLayout.addWidget(self.SaveButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_UnirPDF, "")
        self.tab_SepararPDF = QWidget()
        self.tab_SepararPDF.setObjectName(u"tab_SepararPDF")
        self.layoutWidget = QWidget(self.tab_SepararPDF)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 631, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_2 = QLineEdit(self.layoutWidget)
        self.FileSelector_2.setObjectName(u"FileSelector_2")
        sizePolicy1.setHeightForWidth(self.FileSelector_2.sizePolicy().hasHeightForWidth())
        self.FileSelector_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.FileSelector_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.ButtonFileSelect_2 = QPushButton(self.layoutWidget)
        self.ButtonFileSelect_2.setObjectName(u"ButtonFileSelect_2")

        self.horizontalLayout_3.addWidget(self.ButtonFileSelect_2)

        self.label_3 = QLabel(self.tab_SepararPDF)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 946, 20))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(20, 20))
        self.checkBoxConsevar = QCheckBox(self.tab_SepararPDF)
        self.checkBoxConsevar.setObjectName(u"checkBoxConsevar")
        self.checkBoxConsevar.setGeometry(QRect(520, 90, 81, 22))
        self.label_4 = QLabel(self.tab_SepararPDF)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 101, 20))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(20, 20))
        self.HojasSeparar = QLineEdit(self.tab_SepararPDF)
        self.HojasSeparar.setObjectName(u"HojasSeparar")
        self.HojasSeparar.setGeometry(QRect(10, 90, 497, 24))
        sizePolicy1.setHeightForWidth(self.HojasSeparar.sizePolicy().hasHeightForWidth())
        self.HojasSeparar.setSizePolicy(sizePolicy1)
        self.label_5 = QLabel(self.tab_SepararPDF)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(640, 70, 181, 20))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(20, 20))
        self.NombreExtra = QLineEdit(self.tab_SepararPDF)
        self.NombreExtra.setObjectName(u"NombreExtra")
        self.NombreExtra.setEnabled(True)
        self.NombreExtra.setGeometry(QRect(640, 90, 221, 24))
        sizePolicy1.setHeightForWidth(self.NombreExtra.sizePolicy().hasHeightForWidth())
        self.NombreExtra.setSizePolicy(sizePolicy1)
        self.NombreExtra.setMinimumSize(QSize(7, 0))
        self.NombreExtra.setCursorPosition(0)
        self.SaveButton_2 = QPushButton(self.tab_SepararPDF)
        self.SaveButton_2.setObjectName(u"SaveButton_2")
        self.SaveButton_2.setGeometry(QRect(10, 120, 946, 24))
        self.tabWidget.addTab(self.tab_SepararPDF, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 101, 20))
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(20, 20))
        self.layoutWidget_2 = QWidget(self.tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 631, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_3 = QLineEdit(self.layoutWidget_2)
        self.FileSelector_3.setObjectName(u"FileSelector_3")
        sizePolicy1.setHeightForWidth(self.FileSelector_3.sizePolicy().hasHeightForWidth())
        self.FileSelector_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.FileSelector_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.ButtonFileSelect_3 = QPushButton(self.layoutWidget_2)
        self.ButtonFileSelect_3.setObjectName(u"ButtonFileSelect_3")

        self.horizontalLayout_4.addWidget(self.ButtonFileSelect_3)

        self.SaveButton_3 = QPushButton(self.tab)
        self.SaveButton_3.setObjectName(u"SaveButton_3")
        self.SaveButton_3.setGeometry(QRect(10, 120, 946, 24))
        self.tabWidget.addTab(self.tab, "")
        self.tab_HojaBlanco = QWidget()
        self.tab_HojaBlanco.setObjectName(u"tab_HojaBlanco")
        self.SaveButton_4 = QPushButton(self.tab_HojaBlanco)
        self.SaveButton_4.setObjectName(u"SaveButton_4")
        self.SaveButton_4.setGeometry(QRect(10, 130, 946, 24))
        self.label_7 = QLabel(self.tab_HojaBlanco)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 101, 20))
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(20, 20))
        self.layoutWidget_3 = QWidget(self.tab_HojaBlanco)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 631, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_4 = QLineEdit(self.layoutWidget_3)
        self.FileSelector_4.setObjectName(u"FileSelector_4")
        sizePolicy1.setHeightForWidth(self.FileSelector_4.sizePolicy().hasHeightForWidth())
        self.FileSelector_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.FileSelector_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.ButtonFileSelect_4 = QPushButton(self.layoutWidget_3)
        self.ButtonFileSelect_4.setObjectName(u"ButtonFileSelect_4")

        self.horizontalLayout_5.addWidget(self.ButtonFileSelect_4)

        self.label_8 = QLabel(self.tab_HojaBlanco)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 80, 101, 20))
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(20, 20))
        self.HojasSeparar_2 = QLineEdit(self.tab_HojaBlanco)
        self.HojasSeparar_2.setObjectName(u"HojasSeparar_2")
        self.HojasSeparar_2.setGeometry(QRect(10, 100, 497, 24))
        sizePolicy1.setHeightForWidth(self.HojasSeparar_2.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_2.setSizePolicy(sizePolicy1)
        self.tabWidget.addTab(self.tab_HojaBlanco, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 121, 20))
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(20, 20))
        self.layoutWidget_4 = QWidget(self.tab_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 40, 631, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_5 = QLineEdit(self.layoutWidget_4)
        self.FileSelector_5.setObjectName(u"FileSelector_5")
        sizePolicy1.setHeightForWidth(self.FileSelector_5.sizePolicy().hasHeightForWidth())
        self.FileSelector_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.FileSelector_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.ButtonFileSelect_5 = QPushButton(self.layoutWidget_4)
        self.ButtonFileSelect_5.setObjectName(u"ButtonFileSelect_5")

        self.horizontalLayout_6.addWidget(self.ButtonFileSelect_5)

        self.SaveButton_5 = QPushButton(self.tab_2)
        self.SaveButton_5.setObjectName(u"SaveButton_5")
        self.SaveButton_5.setGeometry(QRect(10, 140, 946, 24))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(740, 10, 211, 111))
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.layoutWidget_5 = QWidget(self.tab_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 40, 631, 26))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_6 = QLineEdit(self.layoutWidget_5)
        self.FileSelector_6.setObjectName(u"FileSelector_6")
        sizePolicy1.setHeightForWidth(self.FileSelector_6.sizePolicy().hasHeightForWidth())
        self.FileSelector_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.FileSelector_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.ButtonFileSelect_6 = QPushButton(self.layoutWidget_5)
        self.ButtonFileSelect_6.setObjectName(u"ButtonFileSelect_6")

        self.horizontalLayout_7.addWidget(self.ButtonFileSelect_6)

        self.SaveButton_6 = QPushButton(self.tab_4)
        self.SaveButton_6.setObjectName(u"SaveButton_6")
        self.SaveButton_6.setGeometry(QRect(10, 80, 946, 24))
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 121, 20))
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.tabWidget_3 = QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_3.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 21))
        self.menuNada = QMenu(self.menubar)
        self.menuNada.setObjectName(u"menuNada")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuNada.menuAction())

        self.retranslateUi(MainWindow)
        self.ButtonFileSelect.clicked.connect(MainWindow.selectFile)
        self.checkBoxConsevar.clicked["bool"].connect(self.NombreExtra.setVisible)
        self.checkBoxConsevar.clicked["bool"].connect(self.label_5.setVisible)
        self.ButtonFileSelect_2.clicked.connect(MainWindow.selectFile)
        self.ButtonFileSelect_5.clicked.connect(MainWindow.selectFile)
        self.ButtonFileSelect_3.clicked.connect(MainWindow.selectFile)
        self.ButtonFileSelect_6.clicked.connect(MainWindow.selectFile)
        self.ButtonFileSelect_4.clicked.connect(MainWindow.selectFile)
        self.SaveButton.clicked.connect(MainWindow.UnirPDF)
        self.SaveButton_5.clicked.connect(MainWindow.ImageToPDF)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecciona PDFs:", None))
        self.ButtonFileSelect.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Documento Par:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Agegar Pagina Inicial", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Agregar Pagina Final", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_UnirPDF), QCoreApplication.translate("MainWindow", u"Unir PDFs", None))
        self.ButtonFileSelect_2.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selecciona PDF:", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setWhatsThis(QCoreApplication.translate("MainWindow", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setText(QCoreApplication.translate("MainWindow", u"Conservar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre extra:", None))
        self.SaveButton_2.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SepararPDF), QCoreApplication.translate("MainWindow", u"Separar PDFs", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selecciona PDF:", None))
        self.ButtonFileSelect_3.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.SaveButton_3.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Separar Hojas", None))
        self.SaveButton_4.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Selecciona PDF:", None))
        self.ButtonFileSelect_4.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_HojaBlanco), QCoreApplication.translate("MainWindow", u"Hoja en Blanco", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Selecciona Imagenes:", None))
        self.ButtonFileSelect_5.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.SaveButton_5.setText(QCoreApplication.translate("MainWindow", u"Convertir", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"FOTO", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Imagen a PDF", None))
        self.ButtonFileSelect_6.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.SaveButton_6.setText(QCoreApplication.translate("MainWindow", u"Convertir", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Selecciona PDFs:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"PDF a Imagen", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Renombrar Carpeta", None))
        self.menuNada.setTitle(QCoreApplication.translate("MainWindow", u"Nada", None))
    # retranslateUi

