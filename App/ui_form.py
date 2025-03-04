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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

from widgets import (ButtonListWidget, ModernCheckBox)
import res_rc_rc

class Ui_MyLovePDF(object):
    def setupUi(self, MyLovePDF):
        if not MyLovePDF.objectName():
            MyLovePDF.setObjectName(u"MyLovePDF")
        MyLovePDF.resize(988, 668)
        self.centralwidget = QWidget(MyLovePDF)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(988, 0))
        self.centralwidget.setStyleSheet(u"QWidget#widgetPDF{background-color: rgb(255, 255, 255);}\n"
"QWidget#widgetIMG{background-color: rgb(255, 255, 255);}\n"
"QWidget#widgetFILE{background-color: rgb(255, 255, 255);}\n"
"QToolButton{color: rgba(255,255,255,0);background-color: rgba(0, 0, 0,0);\n"
"border-image: url(:/resources/resources/uicons-regular-rounded/fi-rr-interrogation.svg);}\n"
"QTabWidget#tabWidgetFILE::pane {background: transparent;border: none;border-image: url(':/resources/resources/bgFILE3.png') 0 0 0 0 stretch}\n"
"QTabWidget#tabWidgetIMG::pane {background: transparent;border: none;border-image: url(':/resources/resources/bgIMG3.png') 0 0 0 0 stretch}\n"
"QTabWidget#tabWidgetPDF::pane {background: transparent;border: none;border-image: url(':/resources/resources/bgPDF3.png') 0 0 0 0 stretch}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widgetPDF = QWidget(self.centralwidget)
        self.widgetPDF.setObjectName(u"widgetPDF")
        self.widgetPDF.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetPDF)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widgetPDF)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(90, 175))
        self.pushButton_2.setMaximumSize(QSize(16777215, 10000))
        self.pushButton_2.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgPDF2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_5.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.tabWidgetPDF = QTabWidget(self.widgetPDF)
        self.tabWidgetPDF.setObjectName(u"tabWidgetPDF")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidgetPDF.sizePolicy().hasHeightForWidth())
        self.tabWidgetPDF.setSizePolicy(sizePolicy1)
        self.tabWidgetPDF.setMaximumSize(QSize(2000, 16777215))
        self.tabWidgetPDF.setStyleSheet(u"")
        self.tabWidgetPDF.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidgetPDF.setElideMode(Qt.TextElideMode.ElideNone)
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
        self.toolButton.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)

        self.label = QLabel(self.tab_UnirPDF)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ListFileSelector.sizePolicy().hasHeightForWidth())
        self.ListFileSelector.setSizePolicy(sizePolicy3)
        self.ListFileSelector.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout.addWidget(self.ListFileSelector)

        self.ButtonFileSelect = QPushButton(self.tab_UnirPDF)
        self.ButtonFileSelect.setObjectName(u"ButtonFileSelect")
        icon = QIcon()
        icon.addFile(u":/resources/resources/uicons-regular-rounded/fi-rr-files-medical.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonFileSelect.setIcon(icon)

        self.horizontalLayout.addWidget(self.ButtonFileSelect, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_9 = QSpacerItem(320, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.tab_UnirPDF)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.tab_UnirPDF)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMaximumSize(QSize(145, 16777215))

        self.verticalLayout.addWidget(self.comboBox)

        self.SaveButton = QPushButton(self.tab_UnirPDF)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;background-color: rgb(255, 255, 255);}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")

        self.verticalLayout.addWidget(self.SaveButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidgetPDF.addTab(self.tab_UnirPDF, "")
        self.tab_SepararPDF = QWidget()
        self.tab_SepararPDF.setObjectName(u"tab_SepararPDF")
        self.layoutWidget = QWidget(self.tab_SepararPDF)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 701, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_2 = QLineEdit(self.layoutWidget)
        self.FileSelector_2.setObjectName(u"FileSelector_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.FileSelector_2.sizePolicy().hasHeightForWidth())
        self.FileSelector_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.FileSelector_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.ButtonFileSelect_2 = QPushButton(self.layoutWidget)
        self.ButtonFileSelect_2.setObjectName(u"ButtonFileSelect_2")
        self.ButtonFileSelect_2.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.ButtonFileSelect_2)

        self.label_3 = QLabel(self.tab_SepararPDF)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 946, 20))
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(20, 20))
        self.checkBoxConsevar = ModernCheckBox(self.tab_SepararPDF)
        self.checkBoxConsevar.setObjectName(u"checkBoxConsevar")
        self.checkBoxConsevar.setGeometry(QRect(520, 70, 61, 41))
        self.label_4 = QLabel(self.tab_SepararPDF)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(20, 20))
        self.HojasSeparar = QLineEdit(self.tab_SepararPDF)
        self.HojasSeparar.setObjectName(u"HojasSeparar")
        self.HojasSeparar.setGeometry(QRect(10, 90, 497, 24))
        sizePolicy5.setHeightForWidth(self.HojasSeparar.sizePolicy().hasHeightForWidth())
        self.HojasSeparar.setSizePolicy(sizePolicy5)
        self.label_5 = QLabel(self.tab_SepararPDF)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(640, 70, 181, 20))
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(20, 20))
        self.NombreExtra = QLineEdit(self.tab_SepararPDF)
        self.NombreExtra.setObjectName(u"NombreExtra")
        self.NombreExtra.setEnabled(True)
        self.NombreExtra.setGeometry(QRect(640, 90, 221, 24))
        sizePolicy5.setHeightForWidth(self.NombreExtra.sizePolicy().hasHeightForWidth())
        self.NombreExtra.setSizePolicy(sizePolicy5)
        self.NombreExtra.setMinimumSize(QSize(7, 0))
        self.NombreExtra.setCursorPosition(0)
        self.SaveButton_2 = QPushButton(self.tab_SepararPDF)
        self.SaveButton_2.setObjectName(u"SaveButton_2")
        self.SaveButton_2.setGeometry(QRect(10, 120, 946, 24))
        self.SaveButton_2.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")
        self.toolButton_7 = QToolButton(self.tab_SepararPDF)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setGeometry(QRect(985, 5, 20, 20))
        self.toolButton_7.setSizeIncrement(QSize(2, 0))
        self.toolButton_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_7.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_7.setIconSize(QSize(16, 16))
        self.toolButton_8 = QToolButton(self.tab_SepararPDF)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setGeometry(QRect(590, 190, 18, 19))
        self.toolButton_8.setSizeIncrement(QSize(2, 0))
        self.toolButton_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_8.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_8.setIconSize(QSize(16, 16))
        self.tabWidgetPDF.addTab(self.tab_SepararPDF, "")
        self.tabSepararHojas = QWidget()
        self.tabSepararHojas.setObjectName(u"tabSepararHojas")
        self.label_6 = QLabel(self.tabSepararHojas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(20, 20))
        self.SaveButton_3 = QPushButton(self.tabSepararHojas)
        self.SaveButton_3.setObjectName(u"SaveButton_3")
        self.SaveButton_3.setGeometry(QRect(10, 120, 946, 24))
        self.SaveButton_3.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")
        self.label_12 = QLabel(self.tabSepararHojas)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 70, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(20, 20))
        self.HojasSeparar_3 = QLineEdit(self.tabSepararHojas)
        self.HojasSeparar_3.setObjectName(u"HojasSeparar_3")
        self.HojasSeparar_3.setGeometry(QRect(10, 90, 497, 24))
        sizePolicy5.setHeightForWidth(self.HojasSeparar_3.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_3.setSizePolicy(sizePolicy5)
        self.checkBoxSplitAll = QCheckBox(self.tabSepararHojas)
        self.checkBoxSplitAll.setObjectName(u"checkBoxSplitAll")
        self.checkBoxSplitAll.setGeometry(QRect(520, 90, 111, 22))
        self.toolButton_6 = QToolButton(self.tabSepararHojas)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setGeometry(QRect(985, 5, 20, 20))
        self.toolButton_6.setSizeIncrement(QSize(2, 0))
        self.toolButton_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_6.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_6.setIconSize(QSize(16, 16))
        self.FileSelector_3 = QLineEdit(self.tabSepararHojas)
        self.FileSelector_3.setObjectName(u"FileSelector_3")
        self.FileSelector_3.setGeometry(QRect(10, 30, 563, 24))
        sizePolicy5.setHeightForWidth(self.FileSelector_3.sizePolicy().hasHeightForWidth())
        self.FileSelector_3.setSizePolicy(sizePolicy5)
        self.ButtonFileSelect_3 = QPushButton(self.tabSepararHojas)
        self.ButtonFileSelect_3.setObjectName(u"ButtonFileSelect_3")
        self.ButtonFileSelect_3.setGeometry(QRect(590, 30, 131, 24))
        self.ButtonFileSelect_3.setIcon(icon)
        self.tabWidgetPDF.addTab(self.tabSepararHojas, "")
        self.tab_HojaBlanco = QWidget()
        self.tab_HojaBlanco.setObjectName(u"tab_HojaBlanco")
        self.SaveButton_4 = QPushButton(self.tab_HojaBlanco)
        self.SaveButton_4.setObjectName(u"SaveButton_4")
        self.SaveButton_4.setGeometry(QRect(10, 120, 946, 24))
        self.SaveButton_4.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")
        self.label_7 = QLabel(self.tab_HojaBlanco)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(20, 20))
        self.layoutWidget_3 = QWidget(self.tab_HojaBlanco)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 701, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FileSelector_4 = QLineEdit(self.layoutWidget_3)
        self.FileSelector_4.setObjectName(u"FileSelector_4")
        sizePolicy5.setHeightForWidth(self.FileSelector_4.sizePolicy().hasHeightForWidth())
        self.FileSelector_4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.FileSelector_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.ButtonFileSelect_4 = QPushButton(self.layoutWidget_3)
        self.ButtonFileSelect_4.setObjectName(u"ButtonFileSelect_4")
        self.ButtonFileSelect_4.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.ButtonFileSelect_4)

        self.label_8 = QLabel(self.tab_HojaBlanco)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 70, 101, 20))
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(20, 20))
        self.HojasSeparar_2 = QLineEdit(self.tab_HojaBlanco)
        self.HojasSeparar_2.setObjectName(u"HojasSeparar_2")
        self.HojasSeparar_2.setGeometry(QRect(10, 90, 497, 24))
        sizePolicy5.setHeightForWidth(self.HojasSeparar_2.sizePolicy().hasHeightForWidth())
        self.HojasSeparar_2.setSizePolicy(sizePolicy5)
        self.toolButton_5 = QToolButton(self.tab_HojaBlanco)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(985, 5, 20, 20))
        self.toolButton_5.setSizeIncrement(QSize(2, 0))
        self.toolButton_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_5.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_5.setIconSize(QSize(16, 16))
        self.tabWidgetPDF.addTab(self.tab_HojaBlanco, "")

        self.horizontalLayout_2.addWidget(self.tabWidgetPDF)


        self.verticalLayout_3.addWidget(self.widgetPDF)

        self.widgetIMG = QWidget(self.centralwidget)
        self.widgetIMG.setObjectName(u"widgetIMG")
        self.widgetIMG.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widgetIMG)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(5, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.widgetIMG)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(90, 0))
        self.pushButton.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgIMG2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.tabWidgetIMG = QTabWidget(self.widgetIMG)
        self.tabWidgetIMG.setObjectName(u"tabWidgetIMG")
        self.tabWidgetIMG.setMaximumSize(QSize(100000, 16777215))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(125, 125))

        self.gridLayout_3.addWidget(self.label_11, 0, 3, 2, 1)

        self.toolButton_2 = QToolButton(self.tab_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setSizeIncrement(QSize(2, 0))
        self.toolButton_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_2.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_2.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.toolButton_2, 0, 5, 1, 1)

        self.ListFileSelector_2 = ButtonListWidget(self.tab_2)
        self.ListFileSelector_2.setObjectName(u"ListFileSelector_2")
        sizePolicy3.setHeightForWidth(self.ListFileSelector_2.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_2.setSizePolicy(sizePolicy3)
        self.ListFileSelector_2.setMaximumSize(QSize(560, 100))

        self.gridLayout_3.addWidget(self.ListFileSelector_2, 1, 0, 1, 1)

        self.ButtonFileSelect_5 = QPushButton(self.tab_2)
        self.ButtonFileSelect_5.setObjectName(u"ButtonFileSelect_5")
        self.ButtonFileSelect_5.setIcon(icon)

        self.gridLayout_3.addWidget(self.ButtonFileSelect_5, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_10 = QSpacerItem(200, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(32, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 1, 4, 1, 1)

        self.SaveButton_5 = QPushButton(self.tab_2)
        self.SaveButton_5.setObjectName(u"SaveButton_5")
        self.SaveButton_5.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")

        self.gridLayout_3.addWidget(self.SaveButton_5, 2, 0, 1, 5)

        self.tabWidgetIMG.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.tab_4)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setSizeIncrement(QSize(2, 0))
        self.toolButton_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_4.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_4.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.toolButton_4, 0, 3, 1, 1)

        self.ListFileSelector_3 = ButtonListWidget(self.tab_4)
        self.ListFileSelector_3.setObjectName(u"ListFileSelector_3")
        sizePolicy3.setHeightForWidth(self.ListFileSelector_3.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_3.setSizePolicy(sizePolicy3)
        self.ListFileSelector_3.setMaximumSize(QSize(560, 100))

        self.gridLayout_4.addWidget(self.ListFileSelector_3, 1, 0, 1, 1)

        self.ButtonFileSelect_6 = QPushButton(self.tab_4)
        self.ButtonFileSelect_6.setObjectName(u"ButtonFileSelect_6")
        self.ButtonFileSelect_6.setMinimumSize(QSize(135, 24))
        self.ButtonFileSelect_6.setMaximumSize(QSize(16777215, 24))
        self.ButtonFileSelect_6.setIcon(icon)

        self.gridLayout_4.addWidget(self.ButtonFileSelect_6, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_11 = QSpacerItem(355, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)

        self.SaveButton_6 = QPushButton(self.tab_4)
        self.SaveButton_6.setObjectName(u"SaveButton_6")
        self.SaveButton_6.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")

        self.gridLayout_4.addWidget(self.SaveButton_6, 2, 0, 1, 3)

        self.tabWidgetIMG.addTab(self.tab_4, "")

        self.horizontalLayout_6.addWidget(self.tabWidgetIMG)


        self.verticalLayout_3.addWidget(self.widgetIMG)

        self.widgetFILE = QWidget(self.centralwidget)
        self.widgetFILE.setObjectName(u"widgetFILE")
        self.widgetFILE.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widgetFILE)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(25, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_6)

        self.pushButton_3 = QPushButton(self.widgetFILE)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy6)
        self.pushButton_3.setMinimumSize(QSize(90, 0))
        self.pushButton_3.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgFILE2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_6.addWidget(self.pushButton_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.tabWidgetFILE = QTabWidget(self.widgetFILE)
        self.tabWidgetFILE.setObjectName(u"tabWidgetFILE")
        self.tabWidgetFILE.setMaximumSize(QSize(100000, 16777215))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.label_14, 0, 3, 1, 1)

        self.toolButton_3 = QToolButton(self.tab_3)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setSizeIncrement(QSize(2, 0))
        self.toolButton_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.toolButton_3.setStyleSheet(u"QToolTip {background-color: rgba(50, 50, 50, 128);color: #ffffff;\n"
"border: 1px solid #ffffff;padding: 5px;font-size: 10pt;}")
        self.toolButton_3.setIconSize(QSize(16, 16))

        self.gridLayout_2.addWidget(self.toolButton_3, 0, 5, 1, 1)

        self.ListFileSelector_4 = ButtonListWidget(self.tab_3)
        self.ListFileSelector_4.setObjectName(u"ListFileSelector_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.ListFileSelector_4.sizePolicy().hasHeightForWidth())
        self.ListFileSelector_4.setSizePolicy(sizePolicy7)
        self.ListFileSelector_4.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_2.addWidget(self.ListFileSelector_4, 1, 0, 3, 1)

        self.ButtonFileSelect_7 = QPushButton(self.tab_3)
        self.ButtonFileSelect_7.setObjectName(u"ButtonFileSelect_7")
        self.ButtonFileSelect_7.setIcon(icon)

        self.gridLayout_2.addWidget(self.ButtonFileSelect_7, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(160, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.NameTemplate = QLineEdit(self.tab_3)
        self.NameTemplate.setObjectName(u"NameTemplate")
        sizePolicy5.setHeightForWidth(self.NameTemplate.sizePolicy().hasHeightForWidth())
        self.NameTemplate.setSizePolicy(sizePolicy5)
        self.NameTemplate.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_2.addWidget(self.NameTemplate, 1, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(25, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 4, 1, 1)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.label_15, 2, 3, 1, 1)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.spinBox, 3, 3, 1, 1)

        self.SaveButton_7 = QPushButton(self.tab_3)
        self.SaveButton_7.setObjectName(u"SaveButton_7")
        self.SaveButton_7.setStyleSheet(u"QPushButton{border-style: solid;border-width: 2px;border-radius: 10px;\n"
"border-color: rgba(140, 140, 140,255); ;color: black;}\n"
"QPushButton:hover{border-color: rgba(140, 120, 150,255);background-color: rgba(0, 172, 252, 50);}\n"
"QPushButton:pressed{border-color: rgba(140, 110, 170,255);background-color: rgba(0, 172, 252, 100);}")

        self.gridLayout_2.addWidget(self.SaveButton_7, 4, 0, 1, 6)

        self.tabWidgetFILE.addTab(self.tab_3, "")

        self.horizontalLayout_8.addWidget(self.tabWidgetFILE)


        self.verticalLayout_3.addWidget(self.widgetFILE)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(25, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_13)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy6.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy6)
        self.pushButton_4.setMinimumSize(QSize(90, 0))
        self.pushButton_4.setStyleSheet(u"QPushButton {border: none;color: transparent;border-image: url(:/resources/resources/bgFILE2.png) 0 0 0 0 stretch;}")

        self.verticalLayout_7.addWidget(self.pushButton_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabMusica = QWidget()
        self.tabMusica.setObjectName(u"tabMusica")
        self.tabWidget.addTab(self.tabMusica, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.widget)

        MyLovePDF.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.toolButton, self.SaveButton)
        QWidget.setTabOrder(self.SaveButton, self.FileSelector_2)
        QWidget.setTabOrder(self.FileSelector_2, self.ButtonFileSelect_2)
        QWidget.setTabOrder(self.ButtonFileSelect_2, self.HojasSeparar)
        QWidget.setTabOrder(self.HojasSeparar, self.checkBoxConsevar)
        QWidget.setTabOrder(self.checkBoxConsevar, self.NombreExtra)
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
        self.ButtonFileSelect_6.clicked.connect(MyLovePDF.selectFile)
        self.SaveButton_5.clicked.connect(MyLovePDF.ImageToPDF)
        self.SaveButton_6.clicked.connect(MyLovePDF.PDFtoImage)
        self.ButtonFileSelect_5.clicked.connect(MyLovePDF.selectFile)
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

        self.tabWidgetPDF.setCurrentIndex(1)
        self.comboBox.setCurrentIndex(0)
        self.tabWidgetIMG.setCurrentIndex(0)
        self.tabWidgetFILE.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MyLovePDF)
    # setupUi

    def retranslateUi(self, MyLovePDF):
        MyLovePDF.setWindowTitle(QCoreApplication.translate("MyLovePDF", u"MyLovePDF", None))
        self.pushButton_2.setText(QCoreApplication.translate("MyLovePDF", u"PushButton", None))
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Une los PDFs seleccionados en uno solo. </p><p>Si FORZAR par, les agregar\u00e1 una p\u00e1gina al inicio/final para que todos los PDF sean pares antes de realizar la uni\u00f3n.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.label.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDFs:", None))
        self.ButtonFileSelect.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.label_2.setText(QCoreApplication.translate("MyLovePDF", u"Forzar Documento Par:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MyLovePDF", u"No Forzar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MyLovePDF", u"Agregar P\u00e1gina Inicial", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MyLovePDF", u"Agregar P\u00e1gina Final", None))

        self.SaveButton.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tab_UnirPDF), QCoreApplication.translate("MyLovePDF", u"Unir PDFs", None))
        self.ButtonFileSelect_2.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.label_3.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setWhatsThis(QCoreApplication.translate("MyLovePDF", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxConsevar.setText(QCoreApplication.translate("MyLovePDF", u"Conservar", None))
        self.label_4.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
        self.label_5.setText(QCoreApplication.translate("MyLovePDF", u"Nombre extra:", None))
        self.SaveButton_2.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
#if QT_CONFIG(tooltip)
        self.toolButton_7.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Separa las hojas seleccionadas en un PDF nuevo.</p><p>Si CONSERVAR esta activo las hojas restantes se guardar\u00e1n en un 2do PDF.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_7.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButton_8.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Une los PDFs seleccionados en uno solo. </p><p>Si FORZAR par, les agregar\u00e1 una p\u00e1gina al inicio/final para que todos los PDF sean pares antes de realizar la uni\u00f3n.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_8.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tab_SepararPDF), QCoreApplication.translate("MyLovePDF", u"Separar PDFs", None))
        self.label_6.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
        self.SaveButton_3.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label_12.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
#if QT_CONFIG(whatsthis)
        self.checkBoxSplitAll.setWhatsThis(QCoreApplication.translate("MyLovePDF", u"Crea un 2do PDF con las hojas no elegidas.", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxSplitAll.setText(QCoreApplication.translate("MyLovePDF", u"Separar Todas", None))
#if QT_CONFIG(tooltip)
        self.toolButton_6.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Separa las Hojas indicadas del PDF y las guarda en PDFs individuales.</p><p>Si SEPARAR TODAS, se separa al PDF en la totalidad de las hojas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_6.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_3.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tabSepararHojas), QCoreApplication.translate("MyLovePDF", u"Separar Hojas", None))
        self.SaveButton_4.setText(QCoreApplication.translate("MyLovePDF", u"Guardar", None))
        self.label_7.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDF:", None))
        self.ButtonFileSelect_4.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivo", None))
        self.label_8.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_5.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Agrega hojas en blanco en las posiciones indicadas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_5.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.tabWidgetPDF.setTabText(self.tabWidgetPDF.indexOf(self.tab_HojaBlanco), QCoreApplication.translate("MyLovePDF", u"Hoja en Blanco", None))
        self.pushButton.setText("")
        self.label_9.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona Imagenes:", None))
        self.label_11.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Convierte los archivos seleccionados a PDF.</p><p>Deben ser archivos tipo imagen (.jpg, .png, .webp, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_2.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_5.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar Archivos", None))
        self.SaveButton_5.setText(QCoreApplication.translate("MyLovePDF", u"Convertir", None))
        self.tabWidgetIMG.setTabText(self.tabWidgetIMG.indexOf(self.tab_2), QCoreApplication.translate("MyLovePDF", u"Imagen a PDF", None))
        self.label_10.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona PDFs:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_4.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Convierte los PDFs seleccionados en im\u00e1genes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_4.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_6.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar Archivos", None))
        self.SaveButton_6.setText(QCoreApplication.translate("MyLovePDF", u"Convertir", None))
        self.tabWidgetIMG.setTabText(self.tabWidgetIMG.indexOf(self.tab_4), QCoreApplication.translate("MyLovePDF", u"PDF a Imagen", None))
        self.pushButton_3.setText(QCoreApplication.translate("MyLovePDF", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("MyLovePDF", u"Selecciona archivos:", None))
        self.label_14.setText(QCoreApplication.translate("MyLovePDF", u"Hojas:", None))
#if QT_CONFIG(tooltip)
        self.toolButton_3.setToolTip(QCoreApplication.translate("MyLovePDF", u"<html><head/><body><p>Renombra todos los archivos seleccionados utilizando el template.</p><p>El template reemplazar\u00e1 XXX por el n\u00famero de archivo.</p><p>En caso de no encontrar indicarlo, se agrega numeraci\u00f3n al final.</p><p>La numeraci\u00f3n inicia desde el n\u00famero indicado (0 por defecto).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_3.setText(QCoreApplication.translate("MyLovePDF", u"...", None))
        self.ButtonFileSelect_7.setText(QCoreApplication.translate("MyLovePDF", u"Seleccionar archivos", None))
        self.NameTemplate.setText(QCoreApplication.translate("MyLovePDF", u"nombre_#XXX", None))
        self.label_15.setText(QCoreApplication.translate("MyLovePDF", u"N\u00famero Inicial:", None))
        self.SaveButton_7.setText(QCoreApplication.translate("MyLovePDF", u"Renombrar", None))
        self.tabWidgetFILE.setTabText(self.tabWidgetFILE.indexOf(self.tab_3), QCoreApplication.translate("MyLovePDF", u"Renombrar Carpeta", None))
        self.pushButton_4.setText(QCoreApplication.translate("MyLovePDF", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMusica), QCoreApplication.translate("MyLovePDF", u"M\u00fasica", None))
    # retranslateUi

