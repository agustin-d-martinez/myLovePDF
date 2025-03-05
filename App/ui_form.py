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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

from widgets import (ButtonListWidget, ModernCheckBox)
import res_rc_rc

class Ui_MyLovePDF(object):
    def setupUi(self, MyLovePDF):
        if not MyLovePDF.objectName():
            MyLovePDF.setObjectName(u"MyLovePDF")
        MyLovePDF.resize(1195, 1211)
        MyLovePDF.setMinimumSize(QSize(1050, 0))
        self.centralwidget = QWidget(MyLovePDF)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{background-color:#464646;}\n"
"QScrollArea{background:transparent;}\n"
"QWidget#scrollAreaWidgetContents{background:transparent;}\n"
"QWidget#widgetPDF{background:none;}\n"
"QWidget#widgetIMG{background:none;}\n"
"QWidget#widgetFILE{background:none;}\n"
"QToolButton{color: rgba(255,255,255,0);background-color: rgba(0, 0, 0,0);\n"
"border-image: url(:/resources/resources/uicons-regular-rounded/fi-rr-interrogation.svg);}\n"
"QTabWidget#tabWidgetFILE::pane {background: transparent;border: none;border-image: url(':/resources/resources/bgFILE3.png') 0 0 0 0 stretch}\n"
"QTabWidget#tabWidgetIMG::pane {background: transparent;border: none;border-image: url(':/resources/resources/bgIMG3.png') 0 0 0 0 stretch}\n"
"QTabWidget#tabWidgetPDF::pane {background: transparent;border: none;border-image: url(':/resources/resources/bgPDF3.png') 0 0 0 0 stretch}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1195, 1201))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.widgetPDF = QWidget(self.scrollAreaWidgetContents)
        self.widgetPDF.setObjectName(u"widgetPDF")
        self.widgetPDF.setMinimumSize(QSize(960, 0))
        self.widgetPDF.setMaximumSize(QSize(1190, 300))
        self.widgetPDF.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetPDF)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer = QSpacerItem(0, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.pushButtonPDF = QPushButton(self.widgetPDF)
        self.pushButtonPDF.setObjectName(u"pushButtonPDF")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonPDF.sizePolicy().hasHeightForWidth())
        self.pushButtonPDF.setSizePolicy(sizePolicy1)
        self.pushButtonPDF.setMinimumSize(QSize(90, 50))
        self.pushButtonPDF.setMaximumSize(QSize(90, 250))
        self.pushButtonPDF.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgPDF2.png) 0 0 0 0 stretch;}")
        self.pushButtonPDF.setCheckable(False)

        self.verticalLayout_5.addWidget(self.pushButtonPDF)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.tabWidgetPDF = QTabWidget(self.widgetPDF)
        self.tabWidgetPDF.setObjectName(u"tabWidgetPDF")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidgetPDF.sizePolicy().hasHeightForWidth())
        self.tabWidgetPDF.setSizePolicy(sizePolicy2)
        self.tabWidgetPDF.setMinimumSize(QSize(960, 0))
        self.tabWidgetPDF.setMaximumSize(QSize(1100, 16777215))
        self.tabWidgetPDF.setStyleSheet(u"QTabBar::tab {background:#850e0e;padding: 4px;border-top-left-radius: 5px;border-top-right-radius: 5px;color:white;}\n"
"QTabBar::tab:selected {background: #CC0000;border: 1px solid grey;border-bottom: none;}\n"
"QLabel{background-color: transparent;padding:2px;border-bottom: 4px solid #540c0c;}")
        self.tabWidgetPDF.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidgetPDF.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabUnirPDF = QWidget()
        self.tabUnirPDF.setObjectName(u"tabUnirPDF")
        self.gridLayout = QGridLayout(self.tabUnirPDF)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.comboBox = QComboBox(self.tabUnirPDF)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setMaximumSize(QSize(145, 16777215))

        self.gridLayout.addWidget(self.comboBox, 2, 3, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_14 = QSpacerItem(88, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 1, 4, 2, 1)

        self.frame_4 = QFrame(self.tabUnirPDF)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setMinimumSize(QSize(560, 75))
        self.frame_4.setMaximumSize(QSize(560, 100))
        self.frame_4.setStyleSheet(u"QFrame#frame_4 {background-color: #ff544e;border: 2px solid #540c0c;border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;border-bottom-right-radius: 10px;}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_4.setLineWidth(2)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 4, 0, 4)
        self.ListFileSelector = ButtonListWidget(self.frame_4)
        self.ListFileSelector.setObjectName(u"ListFileSelector")
        sizePolicy4.setHeightForWidth(self.ListFileSelector.sizePolicy().hasHeightForWidth())
        self.ListFileSelector.setSizePolicy(sizePolicy4)
        self.ListFileSelector.setMinimumSize(QSize(300, 75))
        self.ListFileSelector.setMaximumSize(QSize(560, 100))

        self.horizontalLayout_10.addWidget(self.ListFileSelector)


        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_9 = QSpacerItem(125, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 2, 2, 1, 1)

        self.label_2 = QLabel(self.tabUnirPDF)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.ButtonFileSelect = QPushButton(self.tabUnirPDF)
        self.ButtonFileSelect.setObjectName(u"ButtonFileSelect")
        self.ButtonFileSelect.setMinimumSize(QSize(135, 26))
        self.ButtonFileSelect.setMaximumSize(QSize(135, 26))
        self.ButtonFileSelect.setStyleSheet(u"QPushButton{border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        icon = QIcon()
        icon.addFile(u":/resources/resources/uicons-regular-rounded/fi-rr-files-medical.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonFileSelect.setIcon(icon)

        self.gridLayout.addWidget(self.ButtonFileSelect, 2, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.SaveButton = QPushButton(self.tabUnirPDF)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout.addWidget(self.SaveButton, 3, 0, 1, 5)

        self.label = QLabel(self.tabUnirPDF)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(20, 20))
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.toolButton = QToolButton(self.tabUnirPDF)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setSizeIncrement(QSize(2, 0))
        self.toolButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.toolButton, 0, 5, 1, 1)

        self.tabWidgetPDF.addTab(self.tabUnirPDF, "")
        self.tabSepararPDF = QWidget()
        self.tabSepararPDF.setObjectName(u"tabSepararPDF")
        self.gridLayout_7 = QGridLayout(self.tabSepararPDF)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.HojasSeparar = QLineEdit(self.tabSepararPDF)
        self.HojasSeparar.setObjectName(u"HojasSeparar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.HojasSeparar.sizePolicy().hasHeightForWidth())
        self.HojasSeparar.setSizePolicy(sizePolicy6)
        self.HojasSeparar.setMinimumSize(QSize(520, 0))

        self.gridLayout_7.addWidget(self.HojasSeparar, 4, 0, 1, 2, Qt.AlignmentFlag.AlignTop)

        self.label_5 = QLabel(self.tabSepararPDF)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(20, 20))
        self.label_5.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_7.addWidget(self.label_5, 3, 5, 1, 1)

        self.NombreExtra = QLineEdit(self.tabSepararPDF)
        self.NombreExtra.setObjectName(u"NombreExtra")
        self.NombreExtra.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.NombreExtra.sizePolicy().hasHeightForWidth())
        self.NombreExtra.setSizePolicy(sizePolicy6)
        self.NombreExtra.setMinimumSize(QSize(300, 0))
        self.NombreExtra.setMaximumSize(QSize(200, 16777215))
        self.NombreExtra.setCursorPosition(0)

        self.gridLayout_7.addWidget(self.NombreExtra, 4, 5, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.FileSelector_2 = QLineEdit(self.tabSepararPDF)
        self.FileSelector_2.setObjectName(u"FileSelector_2")
        sizePolicy6.setHeightForWidth(self.FileSelector_2.sizePolicy().hasHeightForWidth())
        self.FileSelector_2.setSizePolicy(sizePolicy6)
        self.FileSelector_2.setStyleSheet(u"border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-left-radius: 10px;border-top-left-radius: 10px")

        self.gridLayout_7.addWidget(self.FileSelector_2, 1, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(25, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 4, 4, 1, 1)

        self.SaveButton_2 = QPushButton(self.tabSepararPDF)
        self.SaveButton_2.setObjectName(u"SaveButton_2")
        self.SaveButton_2.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout_7.addWidget(self.SaveButton_2, 5, 0, 1, 7)

        self.checkBoxConsevar = ModernCheckBox(self.tabSepararPDF)
        self.checkBoxConsevar.setObjectName(u"checkBoxConsevar")
        self.checkBoxConsevar.setMinimumSize(QSize(135, 44))

        self.gridLayout_7.addWidget(self.checkBoxConsevar, 4, 3, 1, 1)

        self.label_3 = QLabel(self.tabSepararPDF)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_15, 4, 2, 1, 1)

        self.label_4 = QLabel(self.tabSepararPDF)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 4)

        self.toolButton_7 = QToolButton(self.tabSepararPDF)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setSizeIncrement(QSize(2, 0))
        self.toolButton_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_7.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_7.setIconSize(QSize(16, 16))

        self.gridLayout_7.addWidget(self.toolButton_7, 0, 7, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_8 = QSpacerItem(10, 177, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 0, 6, 5, 1)

        self.ButtonFileSelect_2 = QPushButton(self.tabSepararPDF)
        self.ButtonFileSelect_2.setObjectName(u"ButtonFileSelect_2")
        self.ButtonFileSelect_2.setMinimumSize(QSize(135, 26))
        self.ButtonFileSelect_2.setMaximumSize(QSize(135, 26))
        self.ButtonFileSelect_2.setStyleSheet(u"QPushButton{border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        self.ButtonFileSelect_2.setIcon(icon)

        self.gridLayout_7.addWidget(self.ButtonFileSelect_2, 1, 3, 1, 1)

        self.tabWidgetPDF.addTab(self.tabSepararPDF, "")
        self.tabSepararHojas = QWidget()
        self.tabSepararHojas.setObjectName(u"tabSepararHojas")
        self.gridLayout_6 = QGridLayout(self.tabSepararHojas)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.checkBoxSplitAll = ModernCheckBox(self.tabSepararHojas)
        self.checkBoxSplitAll.setObjectName(u"checkBoxSplitAll")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.checkBoxSplitAll.sizePolicy().hasHeightForWidth())
        self.checkBoxSplitAll.setSizePolicy(sizePolicy7)
        self.checkBoxSplitAll.setMinimumSize(QSize(135, 44))

        self.gridLayout_6.addWidget(self.checkBoxSplitAll, 4, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(400, 68, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 1, 4, 4, 1)

        self.ButtonFileSelect_3 = QPushButton(self.tabSepararHojas)
        self.ButtonFileSelect_3.setObjectName(u"ButtonFileSelect_3")
        self.ButtonFileSelect_3.setMinimumSize(QSize(135, 26))
        self.ButtonFileSelect_3.setMaximumSize(QSize(135, 24))
        self.ButtonFileSelect_3.setStyleSheet(u"QPushButton{border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        self.ButtonFileSelect_3.setIcon(icon)

        self.gridLayout_6.addWidget(self.ButtonFileSelect_3, 1, 3, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.HojasSeparar_3 = QLineEdit(self.tabSepararHojas)
        self.HojasSeparar_3.setObjectName(u"HojasSeparar_3")
        sizePolicy6.setHeightForWidth(self.HojasSeparar_3.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_3.setSizePolicy(sizePolicy6)
        self.HojasSeparar_3.setMinimumSize(QSize(520, 0))

        self.gridLayout_6.addWidget(self.HojasSeparar_3, 4, 0, 1, 2, Qt.AlignmentFlag.AlignTop)

        self.toolButton_6 = QToolButton(self.tabSepararHojas)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setSizeIncrement(QSize(2, 0))
        self.toolButton_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_6.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_6.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.toolButton_6, 0, 5, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_16, 4, 2, 1, 1)

        self.FileSelector_3 = QLineEdit(self.tabSepararHojas)
        self.FileSelector_3.setObjectName(u"FileSelector_3")
        sizePolicy6.setHeightForWidth(self.FileSelector_3.sizePolicy().hasHeightForWidth())
        self.FileSelector_3.setSizePolicy(sizePolicy6)
        self.FileSelector_3.setMaximumSize(QSize(560, 16777215))
        self.FileSelector_3.setStyleSheet(u"border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-left-radius: 10px;border-top-left-radius: 10px")

        self.gridLayout_6.addWidget(self.FileSelector_3, 1, 0, 1, 3)

        self.label_6 = QLabel(self.tabSepararHojas)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(20, 20))
        self.label_6.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 4)

        self.SaveButton_3 = QPushButton(self.tabSepararHojas)
        self.SaveButton_3.setObjectName(u"SaveButton_3")
        self.SaveButton_3.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout_6.addWidget(self.SaveButton_3, 5, 0, 1, 5)

        self.label_12 = QLabel(self.tabSepararHojas)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(20, 20))
        self.label_12.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_12, 3, 0, 1, 4)

        self.tabWidgetPDF.addTab(self.tabSepararHojas, "")
        self.tabHojaBlanco = QWidget()
        self.tabHojaBlanco.setObjectName(u"tabHojaBlanco")
        self.gridLayout_5 = QGridLayout(self.tabHojaBlanco)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.label_7 = QLabel(self.tabHojaBlanco)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 2)

        self.toolButton_5 = QToolButton(self.tabHojaBlanco)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setSizeIncrement(QSize(2, 0))
        self.toolButton_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_5.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_5.setIconSize(QSize(16, 16))

        self.gridLayout_5.addWidget(self.toolButton_5, 0, 3, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.FileSelector_4 = QLineEdit(self.tabHojaBlanco)
        self.FileSelector_4.setObjectName(u"FileSelector_4")
        sizePolicy6.setHeightForWidth(self.FileSelector_4.sizePolicy().hasHeightForWidth())
        self.FileSelector_4.setSizePolicy(sizePolicy6)
        self.FileSelector_4.setMinimumSize(QSize(560, 0))
        self.FileSelector_4.setMaximumSize(QSize(16777215, 16777215))
        self.FileSelector_4.setStyleSheet(u"border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-left-radius: 10px;border-top-left-radius: 10px")

        self.gridLayout_5.addWidget(self.FileSelector_4, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.ButtonFileSelect_4 = QPushButton(self.tabHojaBlanco)
        self.ButtonFileSelect_4.setObjectName(u"ButtonFileSelect_4")
        self.ButtonFileSelect_4.setMinimumSize(QSize(0, 26))
        self.ButtonFileSelect_4.setMaximumSize(QSize(135, 26))
        self.ButtonFileSelect_4.setStyleSheet(u"QPushButton{border: 2px solid #540c0c;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        self.ButtonFileSelect_4.setIcon(icon)

        self.gridLayout_5.addWidget(self.ButtonFileSelect_4, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_2 = QSpacerItem(350, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 2, 2, 1)

        self.label_8 = QLabel(self.tabHojaBlanco)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 2)

        self.HojasSeparar_2 = QLineEdit(self.tabHojaBlanco)
        self.HojasSeparar_2.setObjectName(u"HojasSeparar_2")
        sizePolicy6.setHeightForWidth(self.HojasSeparar_2.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_2.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.HojasSeparar_2, 3, 0, 1, 2)

        self.SaveButton_4 = QPushButton(self.tabHojaBlanco)
        self.SaveButton_4.setObjectName(u"SaveButton_4")
        self.SaveButton_4.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout_5.addWidget(self.SaveButton_4, 4, 0, 1, 3)

        self.tabWidgetPDF.addTab(self.tabHojaBlanco, "")

        self.horizontalLayout_2.addWidget(self.tabWidgetPDF)


        self.verticalLayout.addWidget(self.widgetPDF, 0, Qt.AlignmentFlag.AlignTop)

        self.widgetIMG = QWidget(self.scrollAreaWidgetContents)
        self.widgetIMG.setObjectName(u"widgetIMG")
        self.widgetIMG.setMinimumSize(QSize(960, 298))
        self.widgetIMG.setMaximumSize(QSize(1190, 300))
        self.widgetIMG.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widgetIMG)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(0, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButtonIMG = QPushButton(self.widgetIMG)
        self.pushButtonIMG.setObjectName(u"pushButtonIMG")
        sizePolicy1.setHeightForWidth(self.pushButtonIMG.sizePolicy().hasHeightForWidth())
        self.pushButtonIMG.setSizePolicy(sizePolicy1)
        self.pushButtonIMG.setMinimumSize(QSize(90, 50))
        self.pushButtonIMG.setMaximumSize(QSize(16777215, 250))
        self.pushButtonIMG.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgIMG2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_4.addWidget(self.pushButtonIMG)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.tabWidgetIMG = QTabWidget(self.widgetIMG)
        self.tabWidgetIMG.setObjectName(u"tabWidgetIMG")
        sizePolicy2.setHeightForWidth(self.tabWidgetIMG.sizePolicy().hasHeightForWidth())
        self.tabWidgetIMG.setSizePolicy(sizePolicy2)
        self.tabWidgetIMG.setMinimumSize(QSize(960, 0))
        self.tabWidgetIMG.setMaximumSize(QSize(1100, 16777215))
        self.tabWidgetIMG.setBaseSize(QSize(1100, 0))
        self.tabWidgetIMG.setStyleSheet(u"QTabBar::tab {background:#0f2384;padding: 4px;border-top-left-radius: 5px;border-top-right-radius: 5px;color:white;}\n"
"QTabBar::tab:selected {background: #12299f;border:1px solid grey;border-bottom: none;}\n"
"QLabel{background-color: transparent;padding:2px;border-bottom: 4px solid #0f0f54;}\n"
"")
        self.tabIMG2PDF = QWidget()
        self.tabIMG2PDF.setObjectName(u"tabIMG2PDF")
        self.tabIMG2PDF.setMinimumSize(QSize(0, 174))
        self.gridLayout_4 = QGridLayout(self.tabIMG2PDF)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.toolButton_2 = QToolButton(self.tabIMG2PDF)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setSizeIncrement(QSize(2, 0))
        self.toolButton_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_2.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_2.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.toolButton_2, 0, 5, 1, 1)

        self.frame = QFrame(self.tabIMG2PDF)
        self.frame.setObjectName(u"frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy8)
        self.frame.setMinimumSize(QSize(560, 100))
        self.frame.setMaximumSize(QSize(560, 100))
        self.frame.setBaseSize(QSize(560, 100))
        self.frame.setStyleSheet(u"QFrame#frame {background-color: #1971ff;border: 2px solid #070454;border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;border-bottom-right-radius: 10px;}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 4, 0, 4)
        self.ListFileSelector_2 = ButtonListWidget(self.frame)
        self.ListFileSelector_2.setObjectName(u"ListFileSelector_2")
        sizePolicy8.setHeightForWidth(self.ListFileSelector_2.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_2.setSizePolicy(sizePolicy8)
        self.ListFileSelector_2.setMinimumSize(QSize(0, 75))
        self.ListFileSelector_2.setMaximumSize(QSize(560, 100))

        self.horizontalLayout.addWidget(self.ListFileSelector_2)


        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.ButtonFileSelect_5 = QPushButton(self.tabIMG2PDF)
        self.ButtonFileSelect_5.setObjectName(u"ButtonFileSelect_5")
        self.ButtonFileSelect_5.setMinimumSize(QSize(0, 26))
        self.ButtonFileSelect_5.setMaximumSize(QSize(135, 26))
        self.ButtonFileSelect_5.setStyleSheet(u"QPushButton{border: 2px solid #070454;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        self.ButtonFileSelect_5.setIcon(icon)

        self.gridLayout_4.addWidget(self.ButtonFileSelect_5, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_10 = QSpacerItem(80, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.label_11 = QLabel(self.tabIMG2PDF)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(110, 100))
        self.label_11.setMaximumSize(QSize(110, 110))
        self.label_11.setStyleSheet(u"border:none;")

        self.gridLayout_4.addWidget(self.label_11, 1, 3, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 1, 4, 1, 1)

        self.SaveButton_5 = QPushButton(self.tabIMG2PDF)
        self.SaveButton_5.setObjectName(u"SaveButton_5")
        self.SaveButton_5.setMinimumSize(QSize(0, 20))
        self.SaveButton_5.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout_4.addWidget(self.SaveButton_5, 2, 0, 1, 5)

        self.label_9 = QLabel(self.tabIMG2PDF)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 2)

        self.tabWidgetIMG.addTab(self.tabIMG2PDF, "")
        self.tabPDF2IMG = QWidget()
        self.tabPDF2IMG.setObjectName(u"tabPDF2IMG")
        self.gridLayout_3 = QGridLayout(self.tabPDF2IMG)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.toolButton_4 = QToolButton(self.tabPDF2IMG)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(19, 19))
        self.toolButton_4.setMaximumSize(QSize(19, 19))
        self.toolButton_4.setSizeIncrement(QSize(0, 0))
        self.toolButton_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_4.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_4.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.toolButton_4, 0, 3, 1, 1)

        self.ButtonFileSelect_6 = QPushButton(self.tabPDF2IMG)
        self.ButtonFileSelect_6.setObjectName(u"ButtonFileSelect_6")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.ButtonFileSelect_6.sizePolicy().hasHeightForWidth())
        self.ButtonFileSelect_6.setSizePolicy(sizePolicy9)
        self.ButtonFileSelect_6.setMinimumSize(QSize(135, 26))
        self.ButtonFileSelect_6.setMaximumSize(QSize(135, 26))
        self.ButtonFileSelect_6.setStyleSheet(u"QPushButton{border: 2px solid #070454;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        self.ButtonFileSelect_6.setIcon(icon)

        self.gridLayout_3.addWidget(self.ButtonFileSelect_6, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.SaveButton_6 = QPushButton(self.tabPDF2IMG)
        self.SaveButton_6.setObjectName(u"SaveButton_6")
        sizePolicy4.setHeightForWidth(self.SaveButton_6.sizePolicy().hasHeightForWidth())
        self.SaveButton_6.setSizePolicy(sizePolicy4)
        self.SaveButton_6.setMinimumSize(QSize(0, 20))
        self.SaveButton_6.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout_3.addWidget(self.SaveButton_6, 2, 0, 1, 3)

        self.label_10 = QLabel(self.tabPDF2IMG)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(20, 21))

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 2)

        self.horizontalSpacer_11 = QSpacerItem(10, 100, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 1, 3, 1, 1)

        self.frame_2 = QFrame(self.tabPDF2IMG)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy8.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy8)
        self.frame_2.setMinimumSize(QSize(560, 100))
        self.frame_2.setMaximumSize(QSize(560, 100))
        self.frame_2.setBaseSize(QSize(560, 100))
        self.frame_2.setStyleSheet(u"QFrame#frame_2 {background-color: #1971ff;border: 2px solid #070454;border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;border-bottom-right-radius: 10px;}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(2)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 4, 0, 4)
        self.ListFileSelector_3 = ButtonListWidget(self.frame_2)
        self.ListFileSelector_3.setObjectName(u"ListFileSelector_3")
        sizePolicy8.setHeightForWidth(self.ListFileSelector_3.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_3.setSizePolicy(sizePolicy8)
        self.ListFileSelector_3.setMinimumSize(QSize(300, 75))
        self.ListFileSelector_3.setMaximumSize(QSize(560, 100))

        self.horizontalLayout_7.addWidget(self.ListFileSelector_3)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.tabWidgetIMG.addTab(self.tabPDF2IMG, "")

        self.horizontalLayout_6.addWidget(self.tabWidgetIMG, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addWidget(self.widgetIMG, 0, Qt.AlignmentFlag.AlignTop)

        self.widgetFILE = QWidget(self.scrollAreaWidgetContents)
        self.widgetFILE.setObjectName(u"widgetFILE")
        self.widgetFILE.setMinimumSize(QSize(960, 220))
        self.widgetFILE.setMaximumSize(QSize(1190, 300))
        self.widgetFILE.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widgetFILE)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(25, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.horizontalSpacer_6)

        self.pushButtonFILE = QPushButton(self.widgetFILE)
        self.pushButtonFILE.setObjectName(u"pushButtonFILE")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.pushButtonFILE.sizePolicy().hasHeightForWidth())
        self.pushButtonFILE.setSizePolicy(sizePolicy10)
        self.pushButtonFILE.setMinimumSize(QSize(90, 50))
        self.pushButtonFILE.setMaximumSize(QSize(16777215, 250))
        self.pushButtonFILE.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgFILE2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_6.addWidget(self.pushButtonFILE)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.tabWidgetFILE = QTabWidget(self.widgetFILE)
        self.tabWidgetFILE.setObjectName(u"tabWidgetFILE")
        sizePolicy2.setHeightForWidth(self.tabWidgetFILE.sizePolicy().hasHeightForWidth())
        self.tabWidgetFILE.setSizePolicy(sizePolicy2)
        self.tabWidgetFILE.setMinimumSize(QSize(960, 0))
        self.tabWidgetFILE.setMaximumSize(QSize(1100, 16777215))
        self.tabWidgetFILE.setStyleSheet(u"QTabBar::tab {background: #CCC000;padding: 4px;border-top-left-radius: 5px;border-top-right-radius: 5px;color:white;}\n"
"QTabBar::tab:selected {background: #83840e;border:1px solid grey;border-bottom: none;}\n"
"QLabel{background-color: transparent;padding:2px;border-bottom: 4px solid #53540f;}\n"
"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.SaveButton_7 = QPushButton(self.tab_3)
        self.SaveButton_7.setObjectName(u"SaveButton_7")
        self.SaveButton_7.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")

        self.gridLayout_2.addWidget(self.SaveButton_7, 5, 0, 1, 5)

        self.ButtonFileSelect_7 = QPushButton(self.tab_3)
        self.ButtonFileSelect_7.setObjectName(u"ButtonFileSelect_7")
        self.ButtonFileSelect_7.setMinimumSize(QSize(135, 26))
        self.ButtonFileSelect_7.setMaximumSize(QSize(135, 26))
        self.ButtonFileSelect_7.setStyleSheet(u"QPushButton{border: 2px solid #545407;padding:2px;color: black;background-color: white;\n"
"border-bottom-right-radius: 10px;border-top-right-radius: 10px}\n"
"QPushButton:hover{border-color: #050343;background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: #020224;background-color: darkgrey}")
        self.ButtonFileSelect_7.setIcon(icon)

        self.gridLayout_2.addWidget(self.ButtonFileSelect_7, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(150, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 4, 1, 1)

        self.toolButton_3 = QToolButton(self.tab_3)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setSizeIncrement(QSize(2, 0))
        self.toolButton_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_3.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_3.setIconSize(QSize(16, 16))

        self.gridLayout_2.addWidget(self.toolButton_3, 0, 5, 1, 1)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setMinimumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.label_15, 2, 3, 1, 1)

        self.NameTemplate = QLineEdit(self.tab_3)
        self.NameTemplate.setObjectName(u"NameTemplate")
        sizePolicy6.setHeightForWidth(self.NameTemplate.sizePolicy().hasHeightForWidth())
        self.NameTemplate.setSizePolicy(sizePolicy6)
        self.NameTemplate.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_2.addWidget(self.NameTemplate, 1, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 3, 1, 1)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(20, 20))
        self.label_14.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_14, 0, 3, 1, 1)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.spinBox, 3, 3, 1, 1)

        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(100)
        sizePolicy11.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy11)
        self.frame_3.setMinimumSize(QSize(560, 100))
        self.frame_3.setMaximumSize(QSize(560, 100))
        self.frame_3.setStyleSheet(u"QFrame#frame_3 {background-color: #fff78a;border: 2px solid #545407;border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;border-bottom-right-radius: 10px;}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(2)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 4, 0, 4)
        self.ListFileSelector_4 = ButtonListWidget(self.frame_3)
        self.ListFileSelector_4.setObjectName(u"ListFileSelector_4")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(75)
        sizePolicy12.setHeightForWidth(self.ListFileSelector_4.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_4.setSizePolicy(sizePolicy12)
        self.ListFileSelector_4.setMinimumSize(QSize(300, 75))
        self.ListFileSelector_4.setMaximumSize(QSize(560, 100))

        self.horizontalLayout_9.addWidget(self.ListFileSelector_4)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 4, 1, Qt.AlignmentFlag.AlignTop)

        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(20, 20))
        self.label_13.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 2)

        self.tabWidgetFILE.addTab(self.tab_3, "")

        self.horizontalLayout_8.addWidget(self.tabWidgetFILE)


        self.verticalLayout.addWidget(self.widgetFILE, 0, Qt.AlignmentFlag.AlignTop)

        self.widgetMSC = QWidget(self.scrollAreaWidgetContents)
        self.widgetMSC.setObjectName(u"widgetMSC")
        self.widgetMSC.setMinimumSize(QSize(960, 290))
        self.widgetMSC.setMaximumSize(QSize(1190, 300))
        self.horizontalLayout_4 = QHBoxLayout(self.widgetMSC)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(25, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.horizontalSpacer_13)

        self.pushButtonMSC = QPushButton(self.widgetMSC)
        self.pushButtonMSC.setObjectName(u"pushButtonMSC")
        sizePolicy1.setHeightForWidth(self.pushButtonMSC.sizePolicy().hasHeightForWidth())
        self.pushButtonMSC.setSizePolicy(sizePolicy1)
        self.pushButtonMSC.setMinimumSize(QSize(90, 50))
        self.pushButtonMSC.setMaximumSize(QSize(16777215, 250))
        self.pushButtonMSC.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgFILE2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_7.addWidget(self.pushButtonMSC)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.tabWidget = QTabWidget(self.widgetMSC)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(960, 0))
        self.tabWidget.setMaximumSize(QSize(1100, 16777215))
        self.tabWidget.setBaseSize(QSize(1100, 0))
        self.tabMusica = QWidget()
        self.tabMusica.setObjectName(u"tabMusica")
        self.listWidgetMusic = QListWidget(self.tabMusica)
        self.listWidgetMusic.setObjectName(u"listWidgetMusic")
        self.listWidgetMusic.setGeometry(QRect(20, 10, 251, 191))
        self.label_16 = QLabel(self.tabMusica)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(400, 20, 111, 101))
        self.ButtonUpdateMusic = QPushButton(self.tabMusica)
        self.ButtonUpdateMusic.setObjectName(u"ButtonUpdateMusic")
        self.ButtonUpdateMusic.setGeometry(QRect(280, 50, 80, 24))
        self.ButtonChangeMusic = QPushButton(self.tabMusica)
        self.ButtonChangeMusic.setObjectName(u"ButtonChangeMusic")
        self.ButtonChangeMusic.setGeometry(QRect(280, 20, 80, 24))
        self.lineEdit = QLineEdit(self.tabMusica)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(540, 30, 113, 24))
        self.label_17 = QLabel(self.tabMusica)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(540, 10, 101, 16))
        self.label_18 = QLabel(self.tabMusica)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(670, 10, 101, 16))
        self.comboBox_2 = QComboBox(self.tabMusica)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(810, 30, 111, 24))
        self.comboBox_2.setEditable(True)
        self.label_19 = QLabel(self.tabMusica)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(810, 10, 101, 16))
        self.lineEdit_2 = QLineEdit(self.tabMusica)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(670, 30, 113, 24))
        self.lineEdit_3 = QLineEdit(self.tabMusica)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(540, 90, 113, 24))
        self.label_20 = QLabel(self.tabMusica)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(540, 70, 101, 16))
        self.label_21 = QLabel(self.tabMusica)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(810, 70, 101, 16))
        self.lineEdit_4 = QLineEdit(self.tabMusica)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(810, 90, 113, 24))
        self.label_22 = QLabel(self.tabMusica)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(930, 10, 101, 16))
        self.lineEdit_5 = QLineEdit(self.tabMusica)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(930, 30, 113, 24))
        self.label_23 = QLabel(self.tabMusica)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(670, 70, 111, 16))
        self.lineEdit_6 = QLineEdit(self.tabMusica)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(670, 90, 113, 24))
        self.label_24 = QLabel(self.tabMusica)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(940, 70, 101, 16))
        self.label_26 = QLabel(self.tabMusica)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(410, 130, 101, 16))
        self.TextEditLiryc = QPlainTextEdit(self.tabMusica)
        self.TextEditLiryc.setObjectName(u"TextEditLiryc")
        self.TextEditLiryc.setGeometry(QRect(410, 150, 641, 51))
        self.SaveButton_8 = QPushButton(self.tabMusica)
        self.SaveButton_8.setObjectName(u"SaveButton_8")
        self.SaveButton_8.setGeometry(QRect(10, 210, 991, 20))
        self.SaveButton_8.setStyleSheet(u"QPushButton{border: 2px solid grey;border-radius: 10px;color: black;background-color: white}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: lightgrey;}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: darkgrey}\n"
"")
        self.layoutWidget = QWidget(self.tabMusica)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(940, 90, 121, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.spinBox_2 = QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_3.addWidget(self.spinBox_2)

        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_3.addWidget(self.label_25)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_3.addWidget(self.spinBox_3)

        self.label_27 = QLabel(self.tabMusica)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(540, 10, 101, 16))
        self.tabWidget.addTab(self.tabMusica, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widgetMSC, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_6 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        MyLovePDF.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.ListFileSelector)
        self.label_9.setBuddy(self.ListFileSelector_2)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.SaveButton, self.FileSelector_2)
        QWidget.setTabOrder(self.FileSelector_2, self.HojasSeparar)
        QWidget.setTabOrder(self.HojasSeparar, self.NombreExtra)
        QWidget.setTabOrder(self.NombreExtra, self.SaveButton_2)
        QWidget.setTabOrder(self.SaveButton_2, self.HojasSeparar_3)
        QWidget.setTabOrder(self.HojasSeparar_3, self.checkBoxSplitAll)
        QWidget.setTabOrder(self.checkBoxSplitAll, self.SaveButton_3)
        QWidget.setTabOrder(self.SaveButton_3, self.FileSelector_4)
        QWidget.setTabOrder(self.FileSelector_4, self.ButtonFileSelect_4)
        QWidget.setTabOrder(self.ButtonFileSelect_4, self.HojasSeparar_2)
        QWidget.setTabOrder(self.HojasSeparar_2, self.SaveButton_4)
        QWidget.setTabOrder(self.SaveButton_4, self.tabWidgetIMG)
        QWidget.setTabOrder(self.tabWidgetIMG, self.SaveButton_5)
        QWidget.setTabOrder(self.SaveButton_5, self.ButtonFileSelect_6)
        QWidget.setTabOrder(self.ButtonFileSelect_6, self.SaveButton_6)

        self.retranslateUi(MyLovePDF)
        self.ButtonFileSelect_7.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton_7.clicked.connect(MyLovePDF.Renombrar)
        self.SaveButton.clicked.connect(MyLovePDF.UnirPDF)
        self.SaveButton_3.clicked.connect(MyLovePDF.SepararHojas)
        self.checkBoxSplitAll.clicked["bool"].connect(self.HojasSeparar_3.setDisabled)
        self.checkBoxConsevar.clicked["bool"].connect(self.label_5.setVisible)
        self.ButtonFileSelect_3.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton_4.clicked.connect(MyLovePDF.HojaBlanco)
        self.checkBoxConsevar.clicked["bool"].connect(self.NombreExtra.setVisible)
        self.ButtonFileSelect_4.clicked.connect(MyLovePDF.selectFile)
        self.ButtonFileSelect_2.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton_2.clicked.connect(MyLovePDF.SepararPDF)
        self.ButtonFileSelect.clicked.connect(MyLovePDF.selectFile)
        self.checkBoxSplitAll.clicked["bool"].connect(self.label_12.setDisabled)
        self.pushButtonPDF.clicked.connect(self.widgetPDF.hide)
        self.ButtonFileSelect_5.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton_5.clicked.connect(MyLovePDF.ImageToPDF)
        self.ButtonFileSelect_6.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton_6.clicked.connect(MyLovePDF.PDFtoImage)
        self.pushButtonIMG.clicked.connect(self.widgetIMG.hide)
        self.pushButton_4.clicked.connect(self.widgetMSC.show)
        self.pushButtonFILE.clicked.connect(self.widgetFILE.hide)
        self.pushButtonMSC.clicked.connect(self.widgetMSC.hide)
        self.pushButton.clicked.connect(self.widgetPDF.show)
        self.pushButton_2.clicked.connect(self.widgetIMG.show)
        self.pushButton_3.clicked.connect(self.widgetFILE.show)
        self.ButtonChangeMusic.clicked.connect(MyLovePDF.ChangeMusicFile)
        self.ButtonUpdateMusic.clicked.connect(MyLovePDF.UpdateMusicFile)

        self.tabWidgetPDF.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.tabWidgetIMG.setCurrentIndex(0)
        self.tabWidgetFILE.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MyLovePDF)
    # setupUi

    def retranslateUi(self, MyLovePDF):
        MyLovePDF.setWindowTitle(QCoreApplication.translate("MyLovePDF", u"MyLovePDF", None))
        self.pushButton.setText(QCoreApplication.translate("MyLovePDF", u"PDF", None))
        self.pushButton_2.setText(QCoreApplication.translate("MyLovePDF", u"IMAGEN", None))
        self.pushButton_3.setText(QCoreApplication.translate("MyLovePDF", u"ARCHIVO", None))
        self.pushButton_4.setText(QCoreApplication.translate("MyLovePDF", u"M\u00daSICA", None))
        self.pushButtonPDF.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MyLovePDF", u"No Forzar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MyLovePDF", u"Agregar P\u00e1gina Inicial", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MyLovePDF", u"Agregar P\u00e1gina Final", None))

        self.label_2.setText(QCoreApplication.translate("MyLovePDF", u"Forzar Documento Par:", None))
        self.ButtonFileSelect.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.SaveButton.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("MyLovePDF", u"&Selecciona PDFs:", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Une los PDFs seleccionados en uno solo. </p><p>Si FORZAR par, les agregar\u00e1 una p\u00e1gina al inicio/final para que todos los PDF sean pares antes de realizar la uni\u00f3n.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tabUnirPDF), QCoreApplication.translate("MyLovePDF", u"Unir PDFs", None))
        self.label_5.setText(QCoreApplication.translate("MyLovePDF", u"Nombre extra:", None))
        self.FileSelector_2.setPlaceholderText(QCoreApplication.translate("MyLovePDF", u"E:\\deskopt\\file.pdf", None))
        self.SaveButton_2.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setWhatsThis(QCoreApplication.translate("MyLovePDF", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setText(QCoreApplication.translate("MyLovePDF", u"Conservar", None))
        self.label_3.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
        self.label_4.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_7.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Separa las hojas seleccionadas en un PDF nuevo.</p><p>Si CONSERVAR esta activo las hojas restantes se guardar\u00e1n en un 2do PDF.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_7.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_2.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tabSepararPDF), QCoreApplication.translate("MyLovePDF", u"Separar PDFs", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxSplitAll.setWhatsThis(QCoreApplication.translate("MyLovePDF", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxSplitAll.setText(QCoreApplication.translate("MyLovePDF", u"Separar Todas", None))
        self.ButtonFileSelect_3.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
#if QT_CONFIG(tooltip)
        self.toolButton_6.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Separa las Hojas indicadas del PDF y las guarda en PDFs individuales.</p><p>Si SEPARAR TODAS, se separa al PDF en la totalidad de las hojas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_6.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.FileSelector_3.setPlaceholderText(QCoreApplication.translate("MyLovePDF", u"E:\\deskopt\\file.pdf", None))
        self.label_6.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
        self.SaveButton_3.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label_12.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tabSepararHojas), QCoreApplication.translate("MyLovePDF", u"Separar Hojas", None))
        self.label_7.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_5.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Agrega hojas en blanco en las posiciones indicadas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_5.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.FileSelector_4.setPlaceholderText(QCoreApplication.translate("MyLovePDF", u"E:\\deskopt\\file.pdf", None))
        self.ButtonFileSelect_4.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.label_8.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
        self.SaveButton_4.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tabHojaBlanco), QCoreApplication.translate("MyLovePDF", u"Hoja en Blanco", None))
        self.pushButtonIMG.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Convierte los archivos seleccionados a PDF.</p><p>Deben ser archivos tipo imagen (.jpg, .png, .webp, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_2.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_5.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar Archivos", None))
        self.label_11.setText("")
        self.SaveButton_5.setText(QCoreApplication.translate("MyLovePDF", u"Convertir", None))
        self.label_9.setText(QCoreApplication.translate("MyLovePDF", u"&Selecciona Imagenes:", None))
        self.tabWidgetIMG.setTabText(self.tabWidgetIMG.indexOf(self.tabIMG2PDF), QCoreApplication.translate("MyLovePDF", u"Imagen a PDF", None))
#if QT_CONFIG(tooltip)
        self.toolButton_4.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Convierte los PDFs seleccionados en im\u00e1genes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_4.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_6.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar Archivos", None))
        self.SaveButton_6.setText(QCoreApplication.translate("MyLovePDF", u"Convertir", None))
        self.label_10.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDFs:", None))
        self.tabWidgetIMG.setTabText(self.tabWidgetIMG.indexOf(self.tabPDF2IMG), QCoreApplication.translate("MyLovePDF", u"PDF a Imagen", None))
        self.pushButtonFILE.setText(QCoreApplication.translate("MyLovePDF", u"PushButton", None))
        self.SaveButton_7.setText(QCoreApplication.translate("MyLovePDF", u"Renombrar", None))
        self.ButtonFileSelect_7.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivos", None))
#if QT_CONFIG(tooltip)
        self.toolButton_3.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Renombra todos los archivos seleccionados utilizando el template.</p><p>El template reemplazar\u00e1 XXX por el n\u00famero de archivo.</p><p>En caso de no encontrar indicarlo, se agrega numeraci\u00f3n al final.</p><p>La numeraci\u00f3n inicia desde el n\u00famero indicado (0 por defecto).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_3.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.label_15.setText(QCoreApplication.translate("MyLovePDF", u"N\u00famero Inicial:", None))
        self.NameTemplate.setText("")
        self.NameTemplate.setPlaceholderText(QCoreApplication.translate("MyLovePDF", u"nombre_#XXX", None))
        self.label_14.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
        self.label_13.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona archivos:", None))
        self.tabWidgetFILE.setTabText(self.tabWidgetFILE.indexOf(self.tab_3), QCoreApplication.translate("MyLovePDF", u"Renombrar Carpeta", None))
        self.pushButtonMSC.setText(QCoreApplication.translate("MyLovePDF", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("MyLovePDF", u"Portada Cancion", None))
        self.ButtonUpdateMusic.setText(QCoreApplication.translate("MyLovePDF", u"actualizar", None))
        self.ButtonChangeMusic.setText(QCoreApplication.translate("MyLovePDF", u"Cambiar Carpeta", None))
        self.label_17.setText(QCoreApplication.translate("MyLovePDF", u"T\u00edtulo:", None))
        self.label_18.setText(QCoreApplication.translate("MyLovePDF", u"Int\u00e9rprete:", None))
        self.label_19.setText(QCoreApplication.translate("MyLovePDF", u"G\u00e9nero:", None))
        self.label_20.setText(QCoreApplication.translate("MyLovePDF", u"Album:", None))
        self.label_21.setText(QCoreApplication.translate("MyLovePDF", u"Compositor:", None))
        self.label_22.setText(QCoreApplication.translate("MyLovePDF", u"A\u00f1o:", None))
        self.label_23.setText(QCoreApplication.translate("MyLovePDF", u"Int\u00e9rprete de album:", None))
        self.label_24.setText(QCoreApplication.translate("MyLovePDF", u"Pista:", None))
        self.label_26.setText(QCoreApplication.translate("MyLovePDF", u"Letra:", None))
        self.SaveButton_8.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label_25.setText(QCoreApplication.translate("MyLovePDF", u"de", None))
        self.label_27.setText(QCoreApplication.translate("MyLovePDF", u"T\u00edtulo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMusica), QCoreApplication.translate("MyLovePDF", u"M\u00fasica", None))
    # retranslateUi

