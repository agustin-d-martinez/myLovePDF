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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

from widgets import (ButtonListWidget, ModernCheckBox)

class Ui_MyLovePDF(object):
    def setupUi(self, MyLovePDF):
        if not MyLovePDF.objectName():
            MyLovePDF.setObjectName(u"MyLovePDF")
        MyLovePDF.resize(1034, 779)
        self.centralwidget = QWidget(MyLovePDF)
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
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.toolButton = QToolButton(self.tab_UnirPDF)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setSizeIncrement(QSize(2, 0))
        self.toolButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)

        self.label = QLabel(self.tab_UnirPDF)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.ListFileSelector = ButtonListWidget(self.tab_UnirPDF)
        self.ListFileSelector.setObjectName(u"ListFileSelector")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ListFileSelector.sizePolicy().hasHeightForWidth())
        self.ListFileSelector.setSizePolicy(sizePolicy1)
        self.ListFileSelector.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout.addWidget(self.ListFileSelector)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ButtonFileSelect = QPushButton(self.tab_UnirPDF)
        self.ButtonFileSelect.setObjectName(u"ButtonFileSelect")

        self.horizontalLayout.addWidget(self.ButtonFileSelect, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_9 = QSpacerItem(270, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.tab_UnirPDF)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.checkBoxDocPar = ModernCheckBox(self.tab_UnirPDF)
        self.checkBoxDocPar.setObjectName(u"checkBoxDocPar")
        sizePolicy2.setHeightForWidth(self.checkBoxDocPar.sizePolicy().hasHeightForWidth())
        self.checkBoxDocPar.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.checkBoxDocPar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.tab_UnirPDF)
        self.buttonGroup = QButtonGroup(MyLovePDF)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.FileSelector_2.sizePolicy().hasHeightForWidth())
        self.FileSelector_2.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.HojasSeparar.sizePolicy().hasHeightForWidth())
        self.HojasSeparar.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.NombreExtra.sizePolicy().hasHeightForWidth())
        self.NombreExtra.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.FileSelector_3.sizePolicy().hasHeightForWidth())
        self.FileSelector_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.FileSelector_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.ButtonFileSelect_3 = QPushButton(self.layoutWidget_2)
        self.ButtonFileSelect_3.setObjectName(u"ButtonFileSelect_3")

        self.horizontalLayout_4.addWidget(self.ButtonFileSelect_3)

        self.SaveButton_3 = QPushButton(self.tab)
        self.SaveButton_3.setObjectName(u"SaveButton_3")
        self.SaveButton_3.setGeometry(QRect(10, 120, 946, 24))
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 70, 101, 20))
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(20, 20))
        self.HojasSeparar_3 = QLineEdit(self.tab)
        self.HojasSeparar_3.setObjectName(u"HojasSeparar_3")
        self.HojasSeparar_3.setGeometry(QRect(10, 90, 497, 24))
        sizePolicy3.setHeightForWidth(self.HojasSeparar_3.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_3.setSizePolicy(sizePolicy3)
        self.checkBoxSplitAll = QCheckBox(self.tab)
        self.checkBoxSplitAll.setObjectName(u"checkBoxSplitAll")
        self.checkBoxSplitAll.setGeometry(QRect(520, 90, 111, 22))
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
        sizePolicy3.setHeightForWidth(self.FileSelector_4.sizePolicy().hasHeightForWidth())
        self.FileSelector_4.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.HojasSeparar_2.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_2.setSizePolicy(sizePolicy3)
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
        self.SaveButton_5 = QPushButton(self.tab_2)
        self.SaveButton_5.setObjectName(u"SaveButton_5")
        self.SaveButton_5.setGeometry(QRect(20, 150, 946, 24))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(750, 30, 211, 111))
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(20, 20))
        self.ListFileSelector_2 = ButtonListWidget(self.tab_2)
        self.ListFileSelector_2.setObjectName(u"ListFileSelector_2")
        self.ListFileSelector_2.setGeometry(QRect(40, 30, 541, 100))
        sizePolicy1.setHeightForWidth(self.ListFileSelector_2.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_2.setSizePolicy(sizePolicy1)
        self.ListFileSelector_2.setMaximumSize(QSize(16777215, 100))
        self.ButtonFileSelect_5 = QPushButton(self.tab_2)
        self.ButtonFileSelect_5.setObjectName(u"ButtonFileSelect_5")
        self.ButtonFileSelect_5.setGeometry(QRect(620, 30, 110, 24))
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.layoutWidget_5 = QWidget(self.tab_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 30, 631, 102))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ListFileSelector_3 = ButtonListWidget(self.layoutWidget_5)
        self.ListFileSelector_3.setObjectName(u"ListFileSelector_3")
        sizePolicy1.setHeightForWidth(self.ListFileSelector_3.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_3.setSizePolicy(sizePolicy1)
        self.ListFileSelector_3.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_7.addWidget(self.ListFileSelector_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.ButtonFileSelect_6 = QPushButton(self.layoutWidget_5)
        self.ButtonFileSelect_6.setObjectName(u"ButtonFileSelect_6")

        self.horizontalLayout_7.addWidget(self.ButtonFileSelect_6, 0, Qt.AlignmentFlag.AlignTop)

        self.SaveButton_6 = QPushButton(self.tab_4)
        self.SaveButton_6.setObjectName(u"SaveButton_6")
        self.SaveButton_6.setGeometry(QRect(10, 160, 946, 24))
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

        MyLovePDF.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MyLovePDF)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1034, 21))
        self.menuNada = QMenu(self.menubar)
        self.menuNada.setObjectName(u"menuNada")
        MyLovePDF.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.tabWidget, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.ButtonFileSelect)
        QWidget.setTabOrder(self.ButtonFileSelect, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.SaveButton)
        QWidget.setTabOrder(self.SaveButton, self.FileSelector_2)
        QWidget.setTabOrder(self.FileSelector_2, self.ButtonFileSelect_2)
        QWidget.setTabOrder(self.ButtonFileSelect_2, self.HojasSeparar)
        QWidget.setTabOrder(self.HojasSeparar, self.checkBoxConsevar)
        QWidget.setTabOrder(self.checkBoxConsevar, self.NombreExtra)
        QWidget.setTabOrder(self.NombreExtra, self.SaveButton_2)
        QWidget.setTabOrder(self.SaveButton_2, self.FileSelector_3)
        QWidget.setTabOrder(self.FileSelector_3, self.ButtonFileSelect_3)
        QWidget.setTabOrder(self.ButtonFileSelect_3, self.HojasSeparar_3)
        QWidget.setTabOrder(self.HojasSeparar_3, self.checkBoxSplitAll)
        QWidget.setTabOrder(self.checkBoxSplitAll, self.SaveButton_3)
        QWidget.setTabOrder(self.SaveButton_3, self.FileSelector_4)
        QWidget.setTabOrder(self.FileSelector_4, self.ButtonFileSelect_4)
        QWidget.setTabOrder(self.ButtonFileSelect_4, self.HojasSeparar_2)
        QWidget.setTabOrder(self.HojasSeparar_2, self.SaveButton_4)
        QWidget.setTabOrder(self.SaveButton_4, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.SaveButton_5)
        QWidget.setTabOrder(self.SaveButton_5, self.ButtonFileSelect_6)
        QWidget.setTabOrder(self.ButtonFileSelect_6, self.SaveButton_6)

        self.menubar.addAction(self.menuNada.menuAction())

        self.retranslateUi(MyLovePDF)
        self.ButtonFileSelect.clicked.connect(MyLovePDF.selectFile)
        self.checkBoxConsevar.clicked["bool"].connect(self.NombreExtra.setVisible)
        self.checkBoxConsevar.clicked["bool"].connect(self.label_5.setVisible)
        self.ButtonFileSelect_2.clicked.connect(MyLovePDF.selectFile)
        self.ButtonFileSelect_3.clicked.connect(MyLovePDF.selectFile)
        self.ButtonFileSelect_6.clicked.connect(MyLovePDF.selectFile)
        self.ButtonFileSelect_4.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton.clicked.connect(MyLovePDF.UnirPDF)
        self.SaveButton_5.clicked.connect(MyLovePDF.ImageToPDF)
        self.checkBoxSplitAll.clicked["bool"].connect(self.HojasSeparar_3.setDisabled)
        self.checkBoxSplitAll.clicked["bool"].connect(self.label_12.setDisabled)
        self.SaveButton_2.clicked.connect(MyLovePDF.SepararPDF)
        self.SaveButton_6.clicked.connect(MyLovePDF.PDFtoImage)
        self.SaveButton_3.clicked.connect(MyLovePDF.SepararHojas)
        self.SaveButton_4.clicked.connect(MyLovePDF.HojaBlanco)
        self.checkBoxDocPar.clicked["bool"].connect(self.checkBox.setVisible)
        self.checkBoxDocPar.clicked["bool"].connect(self.checkBox_2.setVisible)
        self.ButtonFileSelect_5.clicked.connect(MyLovePDF.selectFile)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MyLovePDF)
    # setupUi

    def retranslateUi(self, MyLovePDF):
        MyLovePDF.setWindowTitle(QCoreApplication.translate("MyLovePDF", u"MyLovePDF", None))
        self.toolButton.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.label.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDFs:", None))
        self.ButtonFileSelect.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.label_2.setText(QCoreApplication.translate("MyLovePDF", u"Documento Par:", None))
        self.checkBoxDocPar.setText(QCoreApplication.translate("MyLovePDF", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MyLovePDF", u"Agegar Pagina Inicial", None))
        self.checkBox_2.setText(QCoreApplication.translate("MyLovePDF", u"Agregar Pagina Final", None))
        self.SaveButton.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_UnirPDF), QCoreApplication.translate("MyLovePDF", u"Unir PDFs", None))
        self.ButtonFileSelect_2.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar", None))
        self.label_3.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setWhatsThis(QCoreApplication.translate("MyLovePDF", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setText(QCoreApplication.translate("MyLovePDF", u"Conservar", None))
        self.label_4.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
        self.label_5.setText(QCoreApplication.translate("MyLovePDF", u"Nombre extra:", None))
        self.SaveButton_2.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SepararPDF), QCoreApplication.translate("MyLovePDF", u"Separar PDFs", None))
        self.label_6.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
        self.ButtonFileSelect_3.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar", None))
        self.SaveButton_3.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label_12.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxSplitAll.setWhatsThis(QCoreApplication.translate("MyLovePDF", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxSplitAll.setText(QCoreApplication.translate("MyLovePDF", u"Separar Todas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MyLovePDF", u"Separar Hojas", None))
        self.SaveButton_4.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label_7.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
        self.ButtonFileSelect_4.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar", None))
        self.label_8.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_HojaBlanco), QCoreApplication.translate("MyLovePDF", u"Hoja en Blanco", None))
        self.label_9.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona Imagenes:", None))
        self.SaveButton_5.setText(QCoreApplication.translate("MyLovePDF", u"Convertir", None))
        self.label_11.setText("")
        self.ButtonFileSelect_5.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MyLovePDF", u"Imagen a PDF", None))
        self.ButtonFileSelect_6.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar", None))
        self.SaveButton_6.setText(QCoreApplication.translate("MyLovePDF", u"Convertir", None))
        self.label_10.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDFs:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MyLovePDF", u"PDF a Imagen", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MyLovePDF", u"Renombrar Carpeta", None))
        self.menuNada.setTitle(QCoreApplication.translate("MyLovePDF", u"Nada", None))
    # retranslateUi

