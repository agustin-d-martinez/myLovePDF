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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 639)
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
        self.FileSelector1 = QLineEdit(self.tab_UnirPDF)
        self.FileSelector1.setObjectName(u"FileSelector1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FileSelector1.sizePolicy().hasHeightForWidth())
        self.FileSelector1.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.FileSelector1)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.FileSelect = QPushButton(self.tab_UnirPDF)
        self.FileSelect.setObjectName(u"FileSelect")

        self.horizontalLayout.addWidget(self.FileSelect)


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
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.tab_UnirPDF)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.horizontalSpacer_2 = QSpacerItem(250, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_2 = QPushButton(self.tab_UnirPDF)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_UnirPDF, "")
        self.tab_SepararPDF = QWidget()
        self.tab_SepararPDF.setObjectName(u"tab_SepararPDF")
        self.tabWidget.addTab(self.tab_SepararPDF, "")
        self.tab_HojaBlanco = QWidget()
        self.tab_HojaBlanco.setObjectName(u"tab_HojaBlanco")
        self.tabWidget.addTab(self.tab_HojaBlanco, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 988, 21))
        self.menuNada = QMenu(self.menubar)
        self.menuNada.setObjectName(u"menuNada")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuNada.menuAction())

        self.retranslateUi(MainWindow)
        self.FileSelect.clicked.connect(MainWindow.selectFile)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecciona PDFs:", None))
        self.FileSelect.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Documento Par:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Agegar Pagina Inicial", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Agregar Pagina Final", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_UnirPDF), QCoreApplication.translate("MainWindow", u"Unir PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SepararPDF), QCoreApplication.translate("MainWindow", u"Separar PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_HojaBlanco), QCoreApplication.translate("MainWindow", u"Hoja en Blanco", None))
        self.menuNada.setTitle(QCoreApplication.translate("MainWindow", u"Nada", None))
    # retranslateUi

