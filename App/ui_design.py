# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

from customWidgets.ButtonListWidget import ButtonListWidget
from customWidgets.DroppableImageLabel import DroppableImageLabel
from customWidgets.ModernCheckBox import ModernCheckBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1157, 666)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.exit_frame = QFrame(self.centralwidget)
        self.exit_frame.setObjectName(u"exit_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_frame.sizePolicy().hasHeightForWidth())
        self.exit_frame.setSizePolicy(sizePolicy)
        self.exit_frame.setStyleSheet(u"/* ===== BOTONES DE VENTANA ===== */ \n"
"#exit_frame {\n"
"    background-color: #181818;\n"
"}\n"
"\n"
"QPushButton#minimize_button, \n"
"QPushButton#maximize_button, \n"
"QPushButton#close_button { \n"
"background-color: transparent; \n"
"border: none; \n"
"min-width: 28px; \n"
"max-width: 28px; \n"
"min-height: 28px; \n"
"max-height: 28px; \n"
"border-radius: 14px; \n"
"} \n"
"\n"
"/* Hover */ \n"
"QPushButton#minimize_button:hover { \n"
"background-color: #0d86f0; \n"
"} \n"
"QPushButton#maximize_button:hover { \n"
"background-color: #2f2f2f; \n"
"} \n"
"QPushButton#close_button:hover { \n"
"background-color: #b53030; } \n"
"\n"
"/* Pressed */\n"
" QPushButton#minimize_button:pressed, \n"
"QPushButton#maximize_button:pressed { \n"
"background-color: #3a3a3a; \n"
"} \n"
"QPushButton#close_button:pressed { \n"
"background-color: #8f2424; \n"
"}\n"
"\n"
"")
        self.exit_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.exit_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.exit_frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(10000, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(self.exit_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        icon = QIcon()
        icon.addFile(u":/Icons/minimise_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self.exit_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/stop_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon1)
        self.maximize_button.setIconSize(QSize(24, 24))
        self.maximize_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.maximize_button)

        self.close_button = QPushButton(self.exit_frame)
        self.close_button.setObjectName(u"close_button")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/close_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.verticalLayout_8.addWidget(self.exit_frame)

        self.app_widget = QWidget(self.centralwidget)
        self.app_widget.setObjectName(u"app_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_widget.sizePolicy().hasHeightForWidth())
        self.app_widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.app_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.l_widget = QWidget(self.app_widget)
        self.l_widget.setObjectName(u"l_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_widget.sizePolicy().hasHeightForWidth())
        self.l_widget.setSizePolicy(sizePolicy2)
        self.l_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.l_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.opt_frame = QFrame(self.l_widget)
        self.opt_frame.setObjectName(u"opt_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.opt_frame.sizePolicy().hasHeightForWidth())
        self.opt_frame.setSizePolicy(sizePolicy3)
        self.opt_frame.setMinimumSize(QSize(0, 0))
        self.opt_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.opt_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.opt_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.opt_frame)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy4)
        self.menu_button.setMinimumSize(QSize(100, 0))
        self.menu_button.setMaximumSize(QSize(100, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/menu_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_button.setIcon(icon3)
        self.menu_button.setIconSize(QSize(24, 24))
        self.menu_button.setCheckable(True)
        self.menu_button.setChecked(True)

        self.verticalLayout_4.addWidget(self.menu_button)


        self.verticalLayout.addWidget(self.opt_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.menu_frame = QFrame(self.l_widget)
        self.menu_frame.setObjectName(u"menu_frame")
        sizePolicy1.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy1)
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pdf_button = QPushButton(self.menu_frame)
        self.pdf_button.setObjectName(u"pdf_button")
        sizePolicy4.setHeightForWidth(self.pdf_button.sizePolicy().hasHeightForWidth())
        self.pdf_button.setSizePolicy(sizePolicy4)
        self.pdf_button.setMinimumSize(QSize(0, 0))
        self.pdf_button.setMaximumSize(QSize(220, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdf_button.setIcon(icon4)
        self.pdf_button.setIconSize(QSize(24, 24))
        self.pdf_button.setCheckable(True)
        self.pdf_button.setChecked(True)
        self.pdf_button.setAutoExclusive(False)
        self.pdf_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.pdf_button)

        self.img_button = QPushButton(self.menu_frame)
        self.img_button.setObjectName(u"img_button")
        sizePolicy4.setHeightForWidth(self.img_button.sizePolicy().hasHeightForWidth())
        self.img_button.setSizePolicy(sizePolicy4)
        self.img_button.setMinimumSize(QSize(0, 0))
        self.img_button.setMaximumSize(QSize(220, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.img_button.setIcon(icon5)
        self.img_button.setIconSize(QSize(24, 24))
        self.img_button.setCheckable(True)
        self.img_button.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.img_button)

        self.file_button = QPushButton(self.menu_frame)
        self.file_button.setObjectName(u"file_button")
        sizePolicy4.setHeightForWidth(self.file_button.sizePolicy().hasHeightForWidth())
        self.file_button.setSizePolicy(sizePolicy4)
        self.file_button.setMinimumSize(QSize(0, 0))
        self.file_button.setMaximumSize(QSize(220, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_button.setIcon(icon6)
        self.file_button.setIconSize(QSize(24, 24))
        self.file_button.setCheckable(True)
        self.file_button.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.file_button)

        self.video_button = QPushButton(self.menu_frame)
        self.video_button.setObjectName(u"video_button")
        sizePolicy4.setHeightForWidth(self.video_button.sizePolicy().hasHeightForWidth())
        self.video_button.setSizePolicy(sizePolicy4)
        self.video_button.setMinimumSize(QSize(0, 0))
        self.video_button.setMaximumSize(QSize(220, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/video.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.video_button.setIcon(icon7)
        self.video_button.setIconSize(QSize(24, 24))
        self.video_button.setCheckable(True)
        self.video_button.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.video_button)


        self.verticalLayout.addWidget(self.menu_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(40, 10000, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.config_frame = QFrame(self.l_widget)
        self.config_frame.setObjectName(u"config_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.config_frame.sizePolicy().hasHeightForWidth())
        self.config_frame.setSizePolicy(sizePolicy5)
        self.config_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.config_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.config_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.config_frame)
        self.toolButton.setObjectName(u"toolButton")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/setting_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon8)
        self.toolButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.toolButton)


        self.verticalLayout.addWidget(self.config_frame)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.l_widget)

        self.r_widget = QWidget(self.app_widget)
        self.r_widget.setObjectName(u"r_widget")
        sizePolicy.setHeightForWidth(self.r_widget.sizePolicy().hasHeightForWidth())
        self.r_widget.setSizePolicy(sizePolicy)
        self.r_widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.r_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.r_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.main_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pdf_page = QWidget()
        self.pdf_page.setObjectName(u"pdf_page")
        self.horizontalLayout_5 = QHBoxLayout(self.pdf_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, -1, -1, -1)
        self.pdf_tabs = QTabWidget(self.pdf_page)
        self.pdf_tabs.setObjectName(u"pdf_tabs")
        self.JoinPdf_tab = QWidget()
        self.JoinPdf_tab.setObjectName(u"JoinPdf_tab")
        self.verticalLayout_37 = QVBoxLayout(self.JoinPdf_tab)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.JoinPdf_tab)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.label_15)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.JoinPdf_In = ButtonListWidget(self.JoinPdf_tab)
        self.JoinPdf_In.setObjectName(u"JoinPdf_In")
        self.JoinPdf_In.setStyleSheet(u"border-top-right-radius: 0px;")

        self.horizontalLayout_7.addWidget(self.JoinPdf_In)

        self.JoinPdf_selFile = QPushButton(self.JoinPdf_tab)
        self.JoinPdf_selFile.setObjectName(u"JoinPdf_selFile")
        self.JoinPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_7.addWidget(self.JoinPdf_selFile, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_29.addLayout(self.verticalLayout_10)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(16)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.JoinPdf_isEven_Button = ModernCheckBox(self.JoinPdf_tab)
        self.JoinPdf_isEven_Button.setObjectName(u"JoinPdf_isEven_Button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.JoinPdf_isEven_Button.sizePolicy().hasHeightForWidth())
        self.JoinPdf_isEven_Button.setSizePolicy(sizePolicy6)
        self.JoinPdf_isEven_Button.setMinimumSize(QSize(50, 25))
        self.JoinPdf_isEven_Button.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_38.addWidget(self.JoinPdf_isEven_Button)

        self.label_19 = QLabel(self.JoinPdf_tab)
        self.label_19.setObjectName(u"label_19")
        sizePolicy6.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy6)

        self.horizontalLayout_38.addWidget(self.label_19)


        self.verticalLayout_35.addLayout(self.horizontalLayout_38)

        self.joinPdf_EvenPolicy_comboBox = QComboBox(self.JoinPdf_tab)
        self.joinPdf_EvenPolicy_comboBox.addItem("")
        self.joinPdf_EvenPolicy_comboBox.addItem("")
        self.joinPdf_EvenPolicy_comboBox.setObjectName(u"joinPdf_EvenPolicy_comboBox")
        sizePolicy4.setHeightForWidth(self.joinPdf_EvenPolicy_comboBox.sizePolicy().hasHeightForWidth())
        self.joinPdf_EvenPolicy_comboBox.setSizePolicy(sizePolicy4)

        self.verticalLayout_35.addWidget(self.joinPdf_EvenPolicy_comboBox)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(6)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.JoinPdf_ApplyEven_Button = ModernCheckBox(self.JoinPdf_tab)
        self.JoinPdf_ApplyEven_Button.setObjectName(u"JoinPdf_ApplyEven_Button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.JoinPdf_ApplyEven_Button.sizePolicy().hasHeightForWidth())
        self.JoinPdf_ApplyEven_Button.setSizePolicy(sizePolicy7)
        self.JoinPdf_ApplyEven_Button.setMinimumSize(QSize(50, 25))
        self.JoinPdf_ApplyEven_Button.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_37.addWidget(self.JoinPdf_ApplyEven_Button)

        self.JoinPdf_ApplyEvenLabel = QLabel(self.JoinPdf_tab)
        self.JoinPdf_ApplyEvenLabel.setObjectName(u"JoinPdf_ApplyEvenLabel")
        sizePolicy6.setHeightForWidth(self.JoinPdf_ApplyEvenLabel.sizePolicy().hasHeightForWidth())
        self.JoinPdf_ApplyEvenLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_37.addWidget(self.JoinPdf_ApplyEvenLabel)


        self.verticalLayout_35.addLayout(self.horizontalLayout_37)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_2)


        self.horizontalLayout_29.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_29)

        self.JoinPdf_Button = QPushButton(self.JoinPdf_tab)
        self.JoinPdf_Button.setObjectName(u"JoinPdf_Button")

        self.verticalLayout_37.addWidget(self.JoinPdf_Button)

        self.pdf_tabs.addTab(self.JoinPdf_tab, "")
        self.SplitPdf_tab = QWidget()
        self.SplitPdf_tab.setObjectName(u"SplitPdf_tab")
        self.verticalLayout_41 = QVBoxLayout(self.SplitPdf_tab)
        self.verticalLayout_41.setSpacing(16)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.SplitPdf_tab)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_13.addWidget(self.label_17)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.SplitPdf_In = QLineEdit(self.SplitPdf_tab)
        self.SplitPdf_In.setObjectName(u"SplitPdf_In")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.SplitPdf_In.sizePolicy().hasHeightForWidth())
        self.SplitPdf_In.setSizePolicy(sizePolicy8)
        self.SplitPdf_In.setMaximumSize(QSize(800, 16777215))
        self.SplitPdf_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")

        self.horizontalLayout_9.addWidget(self.SplitPdf_In)

        self.SplitPdf_selFile = QPushButton(self.SplitPdf_tab)
        self.SplitPdf_selFile.setObjectName(u"SplitPdf_selFile")
        sizePolicy3.setHeightForWidth(self.SplitPdf_selFile.sizePolicy().hasHeightForWidth())
        self.SplitPdf_selFile.setSizePolicy(sizePolicy3)
        self.SplitPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_9.addWidget(self.SplitPdf_selFile)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)


        self.verticalLayout_41.addLayout(self.verticalLayout_13)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.SplitPDF_Sheets_widget = QWidget(self.SplitPdf_tab)
        self.SplitPDF_Sheets_widget.setObjectName(u"SplitPDF_Sheets_widget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.SplitPDF_Sheets_widget.sizePolicy().hasHeightForWidth())
        self.SplitPDF_Sheets_widget.setSizePolicy(sizePolicy9)
        self.SplitPDF_Sheets_widget.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.SplitPDF_Sheets_widget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.SplitPDF_Sheets_widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy6.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy6)

        self.verticalLayout_12.addWidget(self.label_16)

        self.SplitPdf_Sheets = QLineEdit(self.SplitPDF_Sheets_widget)
        self.SplitPdf_Sheets.setObjectName(u"SplitPdf_Sheets")
        sizePolicy5.setHeightForWidth(self.SplitPdf_Sheets.sizePolicy().hasHeightForWidth())
        self.SplitPdf_Sheets.setSizePolicy(sizePolicy5)
        self.SplitPdf_Sheets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_12.addWidget(self.SplitPdf_Sheets)


        self.horizontalLayout_10.addWidget(self.SplitPDF_Sheets_widget)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(6)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.SplitPdf_SaveAll_Button = ModernCheckBox(self.SplitPdf_tab)
        self.SplitPdf_SaveAll_Button.setObjectName(u"SplitPdf_SaveAll_Button")
        self.SplitPdf_SaveAll_Button.setMinimumSize(QSize(50, 22))
        self.SplitPdf_SaveAll_Button.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_35.addWidget(self.SplitPdf_SaveAll_Button, 0, Qt.AlignmentFlag.AlignBottom)

        self.label_22 = QLabel(self.SplitPdf_tab)
        self.label_22.setObjectName(u"label_22")
        sizePolicy6.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy6)

        self.horizontalLayout_35.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_35)


        self.verticalLayout_41.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_4)

        self.SplitPdf_Button = QPushButton(self.SplitPdf_tab)
        self.SplitPdf_Button.setObjectName(u"SplitPdf_Button")

        self.verticalLayout_41.addWidget(self.SplitPdf_Button)

        self.pdf_tabs.addTab(self.SplitPdf_tab, "")
        self.ExtractPDF_tab = QWidget()
        self.ExtractPDF_tab.setObjectName(u"ExtractPDF_tab")
        self.verticalLayout_42 = QVBoxLayout(self.ExtractPDF_tab)
        self.verticalLayout_42.setSpacing(16)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_33 = QLabel(self.ExtractPDF_tab)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_16.addWidget(self.label_33)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 2, -1, 2)
        self.ExtractPdf_In = QLineEdit(self.ExtractPDF_tab)
        self.ExtractPdf_In.setObjectName(u"ExtractPdf_In")
        sizePolicy8.setHeightForWidth(self.ExtractPdf_In.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_In.setSizePolicy(sizePolicy8)
        self.ExtractPdf_In.setMaximumSize(QSize(800, 16777215))
        self.ExtractPdf_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")

        self.horizontalLayout_12.addWidget(self.ExtractPdf_In)

        self.ExtractPdf_selFile = QPushButton(self.ExtractPDF_tab)
        self.ExtractPdf_selFile.setObjectName(u"ExtractPdf_selFile")
        self.ExtractPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_12.addWidget(self.ExtractPdf_selFile)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)


        self.verticalLayout_42.addLayout(self.verticalLayout_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ExtractPDF_SheetsWidget = QWidget(self.ExtractPDF_tab)
        self.ExtractPDF_SheetsWidget.setObjectName(u"ExtractPDF_SheetsWidget")
        sizePolicy.setHeightForWidth(self.ExtractPDF_SheetsWidget.sizePolicy().hasHeightForWidth())
        self.ExtractPDF_SheetsWidget.setSizePolicy(sizePolicy)
        self.ExtractPDF_SheetsWidget.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.ExtractPDF_SheetsWidget)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.ExtractPDF_SheetsWidget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy10)

        self.verticalLayout_17.addWidget(self.label_34)

        self.ExtractPdf_Sheets = QLineEdit(self.ExtractPDF_SheetsWidget)
        self.ExtractPdf_Sheets.setObjectName(u"ExtractPdf_Sheets")
        sizePolicy8.setHeightForWidth(self.ExtractPdf_Sheets.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_Sheets.setSizePolicy(sizePolicy8)
        self.ExtractPdf_Sheets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_17.addWidget(self.ExtractPdf_Sheets)


        self.horizontalLayout_11.addWidget(self.ExtractPDF_SheetsWidget)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.ExtractPdf_All_Button = ModernCheckBox(self.ExtractPDF_tab)
        self.ExtractPdf_All_Button.setObjectName(u"ExtractPdf_All_Button")
        sizePolicy3.setHeightForWidth(self.ExtractPdf_All_Button.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_All_Button.setSizePolicy(sizePolicy3)
        self.ExtractPdf_All_Button.setMinimumSize(QSize(50, 22))
        self.ExtractPdf_All_Button.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_36.addWidget(self.ExtractPdf_All_Button, 0, Qt.AlignmentFlag.AlignBottom)

        self.label_24 = QLabel(self.ExtractPDF_tab)
        self.label_24.setObjectName(u"label_24")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy11)

        self.horizontalLayout_36.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_36)


        self.verticalLayout_42.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_6)

        self.ExtractPdf_Button = QPushButton(self.ExtractPDF_tab)
        self.ExtractPdf_Button.setObjectName(u"ExtractPdf_Button")

        self.verticalLayout_42.addWidget(self.ExtractPdf_Button)

        self.pdf_tabs.addTab(self.ExtractPDF_tab, "")
        self.BlankPdf_tab = QWidget()
        self.BlankPdf_tab.setObjectName(u"BlankPdf_tab")
        self.verticalLayout_14 = QVBoxLayout(self.BlankPdf_tab)
        self.verticalLayout_14.setSpacing(16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.BlankPdf_tab)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_19.addWidget(self.label_13)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 2, -1, 2)
        self.BlankPdf_In = QLineEdit(self.BlankPdf_tab)
        self.BlankPdf_In.setObjectName(u"BlankPdf_In")
        sizePolicy8.setHeightForWidth(self.BlankPdf_In.sizePolicy().hasHeightForWidth())
        self.BlankPdf_In.setSizePolicy(sizePolicy8)
        self.BlankPdf_In.setMaximumSize(QSize(800, 16777215))
        self.BlankPdf_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")

        self.horizontalLayout_13.addWidget(self.BlankPdf_In)

        self.BlankPdf_selFile = QPushButton(self.BlankPdf_tab)
        self.BlankPdf_selFile.setObjectName(u"BlankPdf_selFile")
        self.BlankPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_13.addWidget(self.BlankPdf_selFile)


        self.verticalLayout_19.addLayout(self.horizontalLayout_13)


        self.verticalLayout_14.addLayout(self.verticalLayout_19)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.BlankPdf_SheetsWidget = QWidget(self.BlankPdf_tab)
        self.BlankPdf_SheetsWidget.setObjectName(u"BlankPdf_SheetsWidget")
        sizePolicy9.setHeightForWidth(self.BlankPdf_SheetsWidget.sizePolicy().hasHeightForWidth())
        self.BlankPdf_SheetsWidget.setSizePolicy(sizePolicy9)
        self.BlankPdf_SheetsWidget.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.BlankPdf_SheetsWidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.BlankPdf_SheetsWidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.BlankPdf_Sheets = QLineEdit(self.BlankPdf_SheetsWidget)
        self.BlankPdf_Sheets.setObjectName(u"BlankPdf_Sheets")
        sizePolicy8.setHeightForWidth(self.BlankPdf_Sheets.sizePolicy().hasHeightForWidth())
        self.BlankPdf_Sheets.setSizePolicy(sizePolicy8)
        self.BlankPdf_Sheets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_9.addWidget(self.BlankPdf_Sheets)


        self.horizontalLayout_39.addWidget(self.BlankPdf_SheetsWidget)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.BlankPdf_Inplace_Button = ModernCheckBox(self.BlankPdf_tab)
        self.BlankPdf_Inplace_Button.setObjectName(u"BlankPdf_Inplace_Button")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(50)
        sizePolicy12.setVerticalStretch(22)
        sizePolicy12.setHeightForWidth(self.BlankPdf_Inplace_Button.sizePolicy().hasHeightForWidth())
        self.BlankPdf_Inplace_Button.setSizePolicy(sizePolicy12)
        self.BlankPdf_Inplace_Button.setMinimumSize(QSize(50, 22))

        self.horizontalLayout_14.addWidget(self.BlankPdf_Inplace_Button, 0, Qt.AlignmentFlag.AlignBottom)

        self.label_26 = QLabel(self.BlankPdf_tab)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_14.addWidget(self.label_26, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_14)


        self.verticalLayout_14.addLayout(self.horizontalLayout_39)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_8)

        self.BlankPdf_Button = QPushButton(self.BlankPdf_tab)
        self.BlankPdf_Button.setObjectName(u"BlankPdf_Button")

        self.verticalLayout_14.addWidget(self.BlankPdf_Button)

        self.pdf_tabs.addTab(self.BlankPdf_tab, "")

        self.horizontalLayout_5.addWidget(self.pdf_tabs)

        self.stackedWidget.addWidget(self.pdf_page)
        self.img_page = QWidget()
        self.img_page.setObjectName(u"img_page")
        self.horizontalLayout_6 = QHBoxLayout(self.img_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, -1, -1, -1)
        self.img_tabs = QTabWidget(self.img_page)
        self.img_tabs.setObjectName(u"img_tabs")
        self.ImgPdf_tab = QWidget()
        self.ImgPdf_tab.setObjectName(u"ImgPdf_tab")
        self.verticalLayout_21 = QVBoxLayout(self.ImgPdf_tab)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_6 = QLabel(self.ImgPdf_tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_21.addWidget(self.label_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 2, -1, 2)
        self.ImgPdf_In = QLineEdit(self.ImgPdf_tab)
        self.ImgPdf_In.setObjectName(u"ImgPdf_In")
        sizePolicy8.setHeightForWidth(self.ImgPdf_In.sizePolicy().hasHeightForWidth())
        self.ImgPdf_In.setSizePolicy(sizePolicy8)
        self.ImgPdf_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.ImgPdf_In)

        self.ImgPdf_selFile = QPushButton(self.ImgPdf_tab)
        self.ImgPdf_selFile.setObjectName(u"ImgPdf_selFile")
        self.ImgPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_15.addWidget(self.ImgPdf_selFile)


        self.verticalLayout_21.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_10)

        self.ImgPdf_Button = QPushButton(self.ImgPdf_tab)
        self.ImgPdf_Button.setObjectName(u"ImgPdf_Button")

        self.verticalLayout_21.addWidget(self.ImgPdf_Button)

        self.img_tabs.addTab(self.ImgPdf_tab, "")
        self.PdfImg_tab = QWidget()
        self.PdfImg_tab.setObjectName(u"PdfImg_tab")
        self.verticalLayout_22 = QVBoxLayout(self.PdfImg_tab)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_12 = QLabel(self.PdfImg_tab)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_22.addWidget(self.label_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 2, -1, 2)
        self.PdfImg_In = QLineEdit(self.PdfImg_tab)
        self.PdfImg_In.setObjectName(u"PdfImg_In")
        sizePolicy8.setHeightForWidth(self.PdfImg_In.sizePolicy().hasHeightForWidth())
        self.PdfImg_In.setSizePolicy(sizePolicy8)
        self.PdfImg_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.horizontalLayout_16.addWidget(self.PdfImg_In)

        self.PdfImg_selFile = QPushButton(self.PdfImg_tab)
        self.PdfImg_selFile.setObjectName(u"PdfImg_selFile")
        self.PdfImg_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_16.addWidget(self.PdfImg_selFile)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_11)

        self.PdfImg_Button = QPushButton(self.PdfImg_tab)
        self.PdfImg_Button.setObjectName(u"PdfImg_Button")

        self.verticalLayout_22.addWidget(self.PdfImg_Button)

        self.img_tabs.addTab(self.PdfImg_tab, "")
        self.ImgExt_tab = QWidget()
        self.ImgExt_tab.setObjectName(u"ImgExt_tab")
        self.verticalLayout_25 = QVBoxLayout(self.ImgExt_tab)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(50)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_4 = QLabel(self.ImgExt_tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_24.addWidget(self.label_4)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 2, -1, 2)
        self.ImgExt_In = QLineEdit(self.ImgExt_tab)
        self.ImgExt_In.setObjectName(u"ImgExt_In")
        sizePolicy8.setHeightForWidth(self.ImgExt_In.sizePolicy().hasHeightForWidth())
        self.ImgExt_In.setSizePolicy(sizePolicy8)
        self.ImgExt_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.horizontalLayout_17.addWidget(self.ImgExt_In)

        self.ImgExt_selFile = QPushButton(self.ImgExt_tab)
        self.ImgExt_selFile.setObjectName(u"ImgExt_selFile")
        self.ImgExt_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_17.addWidget(self.ImgExt_selFile)


        self.verticalLayout_24.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_24)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_5 = QLabel(self.ImgExt_tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_23.addWidget(self.label_5)

        self.ImgExt_comboBox = QComboBox(self.ImgExt_tab)
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.setObjectName(u"ImgExt_comboBox")

        self.verticalLayout_23.addWidget(self.ImgExt_comboBox)


        self.horizontalLayout_18.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_12)

        self.ImgExt_Button = QPushButton(self.ImgExt_tab)
        self.ImgExt_Button.setObjectName(u"ImgExt_Button")

        self.verticalLayout_25.addWidget(self.ImgExt_Button)

        self.img_tabs.addTab(self.ImgExt_tab, "")
        self.ImgRsize_tab = QWidget()
        self.ImgRsize_tab.setObjectName(u"ImgRsize_tab")
        self.formLayout = QFormLayout(self.ImgRsize_tab)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(50)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_7 = QLabel(self.ImgRsize_tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_28.addWidget(self.label_7)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 2, -1, 2)
        self.ImgRsize_In = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_In.setObjectName(u"ImgRsize_In")
        sizePolicy8.setHeightForWidth(self.ImgRsize_In.sizePolicy().hasHeightForWidth())
        self.ImgRsize_In.setSizePolicy(sizePolicy8)
        self.ImgRsize_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.horizontalLayout_20.addWidget(self.ImgRsize_In)

        self.ImgRsize_selFile = QPushButton(self.ImgRsize_tab)
        self.ImgRsize_selFile.setObjectName(u"ImgRsize_selFile")
        self.ImgRsize_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_20.addWidget(self.ImgRsize_selFile)


        self.verticalLayout_28.addLayout(self.horizontalLayout_20)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.LabelRole, self.verticalLayout_28)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_8 = QLabel(self.ImgRsize_tab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_26.addWidget(self.label_8)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ImgRsize_AW = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_AW.setObjectName(u"ImgRsize_AW")
        sizePolicy8.setHeightForWidth(self.ImgRsize_AW.sizePolicy().hasHeightForWidth())
        self.ImgRsize_AW.setSizePolicy(sizePolicy8)
        self.ImgRsize_AW.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.ImgRsize_AW)

        self.label_9 = QLabel(self.ImgRsize_tab)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_19.addWidget(self.label_9)

        self.ImgRsize_AH = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_AH.setObjectName(u"ImgRsize_AH")
        sizePolicy8.setHeightForWidth(self.ImgRsize_AH.sizePolicy().hasHeightForWidth())
        self.ImgRsize_AH.setSizePolicy(sizePolicy8)
        self.ImgRsize_AH.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.ImgRsize_AH)


        self.verticalLayout_26.addLayout(self.horizontalLayout_19)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.verticalLayout_26)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(25)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.ImgRsize_Scale_Button = QCheckBox(self.ImgRsize_tab)
        self.ImgRsize_Scale_Button.setObjectName(u"ImgRsize_Scale_Button")

        self.horizontalLayout_22.addWidget(self.ImgRsize_Scale_Button)

        self.ImgRsize_Inplace_Button = QCheckBox(self.ImgRsize_tab)
        self.ImgRsize_Inplace_Button.setObjectName(u"ImgRsize_Inplace_Button")

        self.horizontalLayout_22.addWidget(self.ImgRsize_Inplace_Button)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.LabelRole, self.horizontalLayout_22)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_11 = QLabel(self.ImgRsize_tab)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_27.addWidget(self.label_11)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.ImgRsize_NW = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_NW.setObjectName(u"ImgRsize_NW")
        sizePolicy8.setHeightForWidth(self.ImgRsize_NW.sizePolicy().hasHeightForWidth())
        self.ImgRsize_NW.setSizePolicy(sizePolicy8)
        self.ImgRsize_NW.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.ImgRsize_NW)

        self.label_10 = QLabel(self.ImgRsize_tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_21.addWidget(self.label_10)

        self.ImgRsize_NH = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_NH.setObjectName(u"ImgRsize_NH")
        sizePolicy8.setHeightForWidth(self.ImgRsize_NH.sizePolicy().hasHeightForWidth())
        self.ImgRsize_NH.setSizePolicy(sizePolicy8)
        self.ImgRsize_NH.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.ImgRsize_NH)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.verticalLayout_27)

        self.ImgRsize_Button = QPushButton(self.ImgRsize_tab)
        self.ImgRsize_Button.setObjectName(u"ImgRsize_Button")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.ImgRsize_Button)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_13)

        self.img_tabs.addTab(self.ImgRsize_tab, "")

        self.horizontalLayout_6.addWidget(self.img_tabs)

        self.stackedWidget.addWidget(self.img_page)
        self.file_page = QWidget()
        self.file_page.setObjectName(u"file_page")
        self.horizontalLayout_3 = QHBoxLayout(self.file_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, -1, -1, -1)
        self.file_tabs = QTabWidget(self.file_page)
        self.file_tabs.setObjectName(u"file_tabs")
        self.FileRname_tab = QWidget()
        self.FileRname_tab.setObjectName(u"FileRname_tab")
        self.formLayout_2 = QFormLayout(self.FileRname_tab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_1 = QLabel(self.FileRname_tab)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_31.addWidget(self.label_1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.FileRname_In = ButtonListWidget(self.FileRname_tab)
        self.FileRname_In.setObjectName(u"FileRname_In")
        self.FileRname_In.setStyleSheet(u"border-top-right-radius: 0px;")

        self.horizontalLayout_25.addWidget(self.FileRname_In)

        self.FileRname_selFile = QPushButton(self.FileRname_tab)
        self.FileRname_selFile.setObjectName(u"FileRname_selFile")
        self.FileRname_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")

        self.horizontalLayout_25.addWidget(self.FileRname_selFile, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_31.addLayout(self.horizontalLayout_25)


        self.formLayout_2.setLayout(0, QFormLayout.ItemRole.LabelRole, self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_2 = QLabel(self.FileRname_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_32.addWidget(self.label_2)

        self.FileRname_Template = QLineEdit(self.FileRname_tab)
        self.FileRname_Template.setObjectName(u"FileRname_Template")
        sizePolicy8.setHeightForWidth(self.FileRname_Template.sizePolicy().hasHeightForWidth())
        self.FileRname_Template.setSizePolicy(sizePolicy8)

        self.verticalLayout_32.addWidget(self.FileRname_Template)

        self.verticalSpacer_15 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_32.addItem(self.verticalSpacer_15)

        self.label_3 = QLabel(self.FileRname_tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_32.addWidget(self.label_3)

        self.FileRname_Num = QSpinBox(self.FileRname_tab)
        self.FileRname_Num.setObjectName(u"FileRname_Num")

        self.verticalLayout_32.addWidget(self.FileRname_Num)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_16)


        self.formLayout_2.setLayout(0, QFormLayout.ItemRole.FieldRole, self.verticalLayout_32)

        self.FileRname_Button = QPushButton(self.FileRname_tab)
        self.FileRname_Button.setObjectName(u"FileRname_Button")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.FileRname_Button)

        self.file_tabs.addTab(self.FileRname_tab, "")

        self.horizontalLayout_3.addWidget(self.file_tabs)

        self.stackedWidget.addWidget(self.file_page)
        self.vid_page = QWidget()
        self.vid_page.setObjectName(u"vid_page")
        self.horizontalLayout_4 = QHBoxLayout(self.vid_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, -1, -1, -1)
        self.vid_tabs = QTabWidget(self.vid_page)
        self.vid_tabs.setObjectName(u"vid_tabs")
        self.VidTag_tab = QWidget()
        self.VidTag_tab.setObjectName(u"VidTag_tab")
        self.verticalLayout_49 = QVBoxLayout(self.VidTag_tab)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_80 = QLabel(self.VidTag_tab)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_30.addWidget(self.label_80)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.VidTag_In = QLineEdit(self.VidTag_tab)
        self.VidTag_In.setObjectName(u"VidTag_In")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.VidTag_In.sizePolicy().hasHeightForWidth())
        self.VidTag_In.setSizePolicy(sizePolicy13)
        self.VidTag_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")

        self.horizontalLayout_24.addWidget(self.VidTag_In)

        self.VidTag_selFile = QPushButton(self.VidTag_tab)
        self.VidTag_selFile.setObjectName(u"VidTag_selFile")
        self.VidTag_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_24.addWidget(self.VidTag_selFile)

        self.VidTag_Update = QPushButton(self.VidTag_tab)
        self.VidTag_Update.setObjectName(u"VidTag_Update")

        self.horizontalLayout_24.addWidget(self.VidTag_Update)


        self.verticalLayout_30.addLayout(self.horizontalLayout_24)

        self.VidTag_List = ButtonListWidget(self.VidTag_tab)
        self.VidTag_List.setObjectName(u"VidTag_List")
        sizePolicy2.setHeightForWidth(self.VidTag_List.sizePolicy().hasHeightForWidth())
        self.VidTag_List.setSizePolicy(sizePolicy2)

        self.verticalLayout_30.addWidget(self.VidTag_List)


        self.horizontalLayout_34.addLayout(self.verticalLayout_30)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(16)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.VidTag_Cover = DroppableImageLabel(self.VidTag_tab)
        self.VidTag_Cover.setObjectName(u"VidTag_Cover")
        sizePolicy.setHeightForWidth(self.VidTag_Cover.sizePolicy().hasHeightForWidth())
        self.VidTag_Cover.setSizePolicy(sizePolicy)
        self.VidTag_Cover.setMinimumSize(QSize(158, 0))

        self.horizontalLayout_33.addWidget(self.VidTag_Cover)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.VidTag_TitleLayout = QVBoxLayout()
        self.VidTag_TitleLayout.setSpacing(0)
        self.VidTag_TitleLayout.setObjectName(u"VidTag_TitleLayout")
        self.label_90 = QLabel(self.VidTag_tab)
        self.label_90.setObjectName(u"label_90")
        sizePolicy5.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy5)
        self.label_90.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_TitleLayout.addWidget(self.label_90)

        self.VidTag_Title = QLineEdit(self.VidTag_tab)
        self.VidTag_Title.setObjectName(u"VidTag_Title")
        sizePolicy8.setHeightForWidth(self.VidTag_Title.sizePolicy().hasHeightForWidth())
        self.VidTag_Title.setSizePolicy(sizePolicy8)

        self.VidTag_TitleLayout.addWidget(self.VidTag_Title)


        self.horizontalLayout_32.addLayout(self.VidTag_TitleLayout)

        self.VidTag_IntrLayout = QVBoxLayout()
        self.VidTag_IntrLayout.setSpacing(0)
        self.VidTag_IntrLayout.setObjectName(u"VidTag_IntrLayout")
        self.label_23 = QLabel(self.VidTag_tab)
        self.label_23.setObjectName(u"label_23")
        sizePolicy5.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy5)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_IntrLayout.addWidget(self.label_23)

        self.VidTag_Intr = QLineEdit(self.VidTag_tab)
        self.VidTag_Intr.setObjectName(u"VidTag_Intr")
        sizePolicy8.setHeightForWidth(self.VidTag_Intr.sizePolicy().hasHeightForWidth())
        self.VidTag_Intr.setSizePolicy(sizePolicy8)

        self.VidTag_IntrLayout.addWidget(self.VidTag_Intr)


        self.horizontalLayout_32.addLayout(self.VidTag_IntrLayout)

        self.VidTag_AlbLayout = QVBoxLayout()
        self.VidTag_AlbLayout.setSpacing(0)
        self.VidTag_AlbLayout.setObjectName(u"VidTag_AlbLayout")
        self.label_32 = QLabel(self.VidTag_tab)
        self.label_32.setObjectName(u"label_32")
        sizePolicy5.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy5)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_AlbLayout.addWidget(self.label_32)

        self.VidTag_Alb = QLineEdit(self.VidTag_tab)
        self.VidTag_Alb.setObjectName(u"VidTag_Alb")
        sizePolicy8.setHeightForWidth(self.VidTag_Alb.sizePolicy().hasHeightForWidth())
        self.VidTag_Alb.setSizePolicy(sizePolicy8)

        self.VidTag_AlbLayout.addWidget(self.VidTag_Alb)


        self.horizontalLayout_32.addLayout(self.VidTag_AlbLayout)


        self.verticalLayout_46.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.VidTag_GenreLayout = QVBoxLayout()
        self.VidTag_GenreLayout.setSpacing(0)
        self.VidTag_GenreLayout.setObjectName(u"VidTag_GenreLayout")
        self.label_30 = QLabel(self.VidTag_tab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_GenreLayout.addWidget(self.label_30)

        self.VidTag_Genre_comboBox = QComboBox(self.VidTag_tab)
        self.VidTag_Genre_comboBox.setObjectName(u"VidTag_Genre_comboBox")
        self.VidTag_Genre_comboBox.setEditable(True)

        self.VidTag_GenreLayout.addWidget(self.VidTag_Genre_comboBox)


        self.horizontalLayout_31.addLayout(self.VidTag_GenreLayout)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_29 = QLabel(self.VidTag_tab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_11.addWidget(self.label_29)

        self.VidTag_Year = QLineEdit(self.VidTag_tab)
        self.VidTag_Year.setObjectName(u"VidTag_Year")
        sizePolicy8.setHeightForWidth(self.VidTag_Year.sizePolicy().hasHeightForWidth())
        self.VidTag_Year.setSizePolicy(sizePolicy8)

        self.verticalLayout_11.addWidget(self.VidTag_Year)


        self.horizontalLayout_31.addLayout(self.verticalLayout_11)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_31 = QLabel(self.VidTag_tab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_36.addWidget(self.label_31)

        self.VidTag_TrackLayout = QHBoxLayout()
        self.VidTag_TrackLayout.setObjectName(u"VidTag_TrackLayout")
        self.VidTag_Track = QSpinBox(self.VidTag_tab)
        self.VidTag_Track.setObjectName(u"VidTag_Track")

        self.VidTag_TrackLayout.addWidget(self.VidTag_Track)

        self.label_25 = QLabel(self.VidTag_tab)
        self.label_25.setObjectName(u"label_25")

        self.VidTag_TrackLayout.addWidget(self.label_25)

        self.VidTag_TrackAll = QSpinBox(self.VidTag_tab)
        self.VidTag_TrackAll.setObjectName(u"VidTag_TrackAll")

        self.VidTag_TrackLayout.addWidget(self.VidTag_TrackAll)


        self.verticalLayout_36.addLayout(self.VidTag_TrackLayout)


        self.horizontalLayout_31.addLayout(self.verticalLayout_36)


        self.verticalLayout_46.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.VidTag_IntrAlbLayout = QVBoxLayout()
        self.VidTag_IntrAlbLayout.setSpacing(0)
        self.VidTag_IntrAlbLayout.setObjectName(u"VidTag_IntrAlbLayout")
        self.VidTag_IntrAlblabel = QLabel(self.VidTag_tab)
        self.VidTag_IntrAlblabel.setObjectName(u"VidTag_IntrAlblabel")
        self.VidTag_IntrAlblabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_IntrAlbLayout.addWidget(self.VidTag_IntrAlblabel)

        self.VidTag_IntrAlb = QLineEdit(self.VidTag_tab)
        self.VidTag_IntrAlb.setObjectName(u"VidTag_IntrAlb")
        sizePolicy8.setHeightForWidth(self.VidTag_IntrAlb.sizePolicy().hasHeightForWidth())
        self.VidTag_IntrAlb.setSizePolicy(sizePolicy8)

        self.VidTag_IntrAlbLayout.addWidget(self.VidTag_IntrAlb)


        self.horizontalLayout_30.addLayout(self.VidTag_IntrAlbLayout)

        self.VidTag_CompLayout = QVBoxLayout()
        self.VidTag_CompLayout.setSpacing(0)
        self.VidTag_CompLayout.setObjectName(u"VidTag_CompLayout")
        self.VidTag_Complabel = QLabel(self.VidTag_tab)
        self.VidTag_Complabel.setObjectName(u"VidTag_Complabel")
        self.VidTag_Complabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_CompLayout.addWidget(self.VidTag_Complabel)

        self.VidTag_Comp = QLineEdit(self.VidTag_tab)
        self.VidTag_Comp.setObjectName(u"VidTag_Comp")
        sizePolicy8.setHeightForWidth(self.VidTag_Comp.sizePolicy().hasHeightForWidth())
        self.VidTag_Comp.setSizePolicy(sizePolicy8)

        self.VidTag_CompLayout.addWidget(self.VidTag_Comp)


        self.horizontalLayout_30.addLayout(self.VidTag_CompLayout)

        self.VidTag_MoodLayout = QVBoxLayout()
        self.VidTag_MoodLayout.setSpacing(0)
        self.VidTag_MoodLayout.setObjectName(u"VidTag_MoodLayout")
        self.VidTag_Moodlabel = QLabel(self.VidTag_tab)
        self.VidTag_Moodlabel.setObjectName(u"VidTag_Moodlabel")
        self.VidTag_Moodlabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_MoodLayout.addWidget(self.VidTag_Moodlabel)

        self.VidTag_Mood = QLineEdit(self.VidTag_tab)
        self.VidTag_Mood.setObjectName(u"VidTag_Mood")
        sizePolicy8.setHeightForWidth(self.VidTag_Mood.sizePolicy().hasHeightForWidth())
        self.VidTag_Mood.setSizePolicy(sizePolicy8)

        self.VidTag_MoodLayout.addWidget(self.VidTag_Mood)


        self.horizontalLayout_30.addLayout(self.VidTag_MoodLayout)


        self.verticalLayout_46.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_33.addLayout(self.verticalLayout_46)


        self.verticalLayout_48.addLayout(self.horizontalLayout_33)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.VidTag_Lyricslabel = QLabel(self.VidTag_tab)
        self.VidTag_Lyricslabel.setObjectName(u"VidTag_Lyricslabel")
        self.VidTag_Lyricslabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_47.addWidget(self.VidTag_Lyricslabel)

        self.VidTag_Lyrics = QPlainTextEdit(self.VidTag_tab)
        self.VidTag_Lyrics.setObjectName(u"VidTag_Lyrics")

        self.verticalLayout_47.addWidget(self.VidTag_Lyrics)


        self.verticalLayout_48.addLayout(self.verticalLayout_47)


        self.horizontalLayout_34.addLayout(self.verticalLayout_48)


        self.verticalLayout_49.addLayout(self.horizontalLayout_34)

        self.VidTag_Button = QPushButton(self.VidTag_tab)
        self.VidTag_Button.setObjectName(u"VidTag_Button")

        self.verticalLayout_49.addWidget(self.VidTag_Button)

        self.vid_tabs.addTab(self.VidTag_tab, "")
        self.MP3toMP4_tab = QWidget()
        self.MP3toMP4_tab.setObjectName(u"MP3toMP4_tab")
        self.verticalLayout_29 = QVBoxLayout(self.MP3toMP4_tab)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_18 = QLabel(self.MP3toMP4_tab)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_29.addWidget(self.label_18)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 2, -1, 2)
        self.MP3toMP4_In = QLineEdit(self.MP3toMP4_tab)
        self.MP3toMP4_In.setObjectName(u"MP3toMP4_In")
        sizePolicy8.setHeightForWidth(self.MP3toMP4_In.sizePolicy().hasHeightForWidth())
        self.MP3toMP4_In.setSizePolicy(sizePolicy8)
        self.MP3toMP4_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")

        self.horizontalLayout_23.addWidget(self.MP3toMP4_In)

        self.MP3toMP4_selFile = QPushButton(self.MP3toMP4_tab)
        self.MP3toMP4_selFile.setObjectName(u"MP3toMP4_selFile")
        self.MP3toMP4_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.horizontalLayout_23.addWidget(self.MP3toMP4_selFile)


        self.verticalLayout_29.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_14)

        self.MP3toMP4_Button = QPushButton(self.MP3toMP4_tab)
        self.MP3toMP4_Button.setObjectName(u"MP3toMP4_Button")

        self.verticalLayout_29.addWidget(self.MP3toMP4_Button)

        self.vid_tabs.addTab(self.MP3toMP4_tab, "")
        self.VidDown = QWidget()
        self.VidDown.setObjectName(u"VidDown")
        self.verticalLayout_39 = QVBoxLayout(self.VidDown)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(16)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_20 = QLabel(self.VidDown)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_18.addWidget(self.label_20)

        self.VidDown_In = QLineEdit(self.VidDown)
        self.VidDown_In.setObjectName(u"VidDown_In")
        sizePolicy8.setHeightForWidth(self.VidDown_In.sizePolicy().hasHeightForWidth())
        self.VidDown_In.setSizePolicy(sizePolicy8)

        self.verticalLayout_18.addWidget(self.VidDown_In)


        self.horizontalLayout_8.addLayout(self.verticalLayout_18)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_27 = QLabel(self.VidDown)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_15.addWidget(self.label_27)

        self.VidDown_OnlyAudio = ModernCheckBox(self.VidDown)
        self.VidDown_OnlyAudio.setObjectName(u"VidDown_OnlyAudio")
        sizePolicy4.setHeightForWidth(self.VidDown_OnlyAudio.sizePolicy().hasHeightForWidth())
        self.VidDown_OnlyAudio.setSizePolicy(sizePolicy4)
        self.VidDown_OnlyAudio.setMinimumSize(QSize(0, 22))

        self.verticalLayout_15.addWidget(self.VidDown_OnlyAudio)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.VidDown_resLayout = QVBoxLayout()
        self.VidDown_resLayout.setSpacing(0)
        self.VidDown_resLayout.setObjectName(u"VidDown_resLayout")
        self.VidDown_resLabel = QLabel(self.VidDown)
        self.VidDown_resLabel.setObjectName(u"VidDown_resLabel")

        self.VidDown_resLayout.addWidget(self.VidDown_resLabel)

        self.VidDown_res = QComboBox(self.VidDown)
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.addItem("")
        self.VidDown_res.setObjectName(u"VidDown_res")
        sizePolicy11.setHeightForWidth(self.VidDown_res.sizePolicy().hasHeightForWidth())
        self.VidDown_res.setSizePolicy(sizePolicy11)

        self.VidDown_resLayout.addWidget(self.VidDown_res)


        self.horizontalLayout_8.addLayout(self.VidDown_resLayout)


        self.verticalLayout_34.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.VidDown_Titlelabel = QLabel(self.VidDown)
        self.VidDown_Titlelabel.setObjectName(u"VidDown_Titlelabel")

        self.verticalLayout_33.addWidget(self.VidDown_Titlelabel)

        self.VidDown_Title = QLineEdit(self.VidDown)
        self.VidDown_Title.setObjectName(u"VidDown_Title")
        sizePolicy8.setHeightForWidth(self.VidDown_Title.sizePolicy().hasHeightForWidth())
        self.VidDown_Title.setSizePolicy(sizePolicy8)
        self.VidDown_Title.setReadOnly(True)

        self.verticalLayout_33.addWidget(self.VidDown_Title)


        self.horizontalLayout_26.addLayout(self.verticalLayout_33)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_28 = QLabel(self.VidDown)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_20.addWidget(self.label_28)

        self.VidDown_all_checkBox = ModernCheckBox(self.VidDown)
        self.VidDown_all_checkBox.setObjectName(u"VidDown_all_checkBox")
        self.VidDown_all_checkBox.setMinimumSize(QSize(0, 22))

        self.verticalLayout_20.addWidget(self.VidDown_all_checkBox)


        self.horizontalLayout_26.addLayout(self.verticalLayout_20)


        self.verticalLayout_34.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_17)

        self.VidDown_listFrame = QFrame(self.VidDown)
        self.VidDown_listFrame.setObjectName(u"VidDown_listFrame")
        self.VidDown_listLayout = QVBoxLayout(self.VidDown_listFrame)
        self.VidDown_listLayout.setSpacing(0)
        self.VidDown_listLayout.setObjectName(u"VidDown_listLayout")
        self.VidDown_listLayout.setContentsMargins(4, 4, 4, 4)
        self.VidDown_listLabel = QLabel(self.VidDown_listFrame)
        self.VidDown_listLabel.setObjectName(u"VidDown_listLabel")

        self.VidDown_listLayout.addWidget(self.VidDown_listLabel)

        self.VidDown_list = QListWidget(self.VidDown_listFrame)
        self.VidDown_list.setObjectName(u"VidDown_list")

        self.VidDown_listLayout.addWidget(self.VidDown_list)


        self.verticalLayout_34.addWidget(self.VidDown_listFrame)


        self.horizontalLayout_27.addLayout(self.verticalLayout_34)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(16)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.VidDown_Thumb = QLabel(self.VidDown)
        self.VidDown_Thumb.setObjectName(u"VidDown_Thumb")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.VidDown_Thumb.sizePolicy().hasHeightForWidth())
        self.VidDown_Thumb.setSizePolicy(sizePolicy14)
        self.VidDown_Thumb.setMinimumSize(QSize(0, 0))

        self.verticalLayout_38.addWidget(self.VidDown_Thumb)

        self.VidDown_durLayout = QVBoxLayout()
        self.VidDown_durLayout.setSpacing(0)
        self.VidDown_durLayout.setObjectName(u"VidDown_durLayout")
        self.VidDown_durLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.VidDown_durLabel = QLabel(self.VidDown)
        self.VidDown_durLabel.setObjectName(u"VidDown_durLabel")
        sizePolicy5.setHeightForWidth(self.VidDown_durLabel.sizePolicy().hasHeightForWidth())
        self.VidDown_durLabel.setSizePolicy(sizePolicy5)

        self.VidDown_durLayout.addWidget(self.VidDown_durLabel)

        self.VidDown_dur = QLineEdit(self.VidDown)
        self.VidDown_dur.setObjectName(u"VidDown_dur")
        sizePolicy8.setHeightForWidth(self.VidDown_dur.sizePolicy().hasHeightForWidth())
        self.VidDown_dur.setSizePolicy(sizePolicy8)
        self.VidDown_dur.setReadOnly(True)

        self.VidDown_durLayout.addWidget(self.VidDown_dur, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_38.addLayout(self.VidDown_durLayout)

        self.VidDown_sizeLayout = QVBoxLayout()
        self.VidDown_sizeLayout.setSpacing(0)
        self.VidDown_sizeLayout.setObjectName(u"VidDown_sizeLayout")
        self.VidDown_sizeLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.VidDown_sizeLabel = QLabel(self.VidDown)
        self.VidDown_sizeLabel.setObjectName(u"VidDown_sizeLabel")
        sizePolicy5.setHeightForWidth(self.VidDown_sizeLabel.sizePolicy().hasHeightForWidth())
        self.VidDown_sizeLabel.setSizePolicy(sizePolicy5)

        self.VidDown_sizeLayout.addWidget(self.VidDown_sizeLabel)

        self.VidDown_size = QLineEdit(self.VidDown)
        self.VidDown_size.setObjectName(u"VidDown_size")
        sizePolicy8.setHeightForWidth(self.VidDown_size.sizePolicy().hasHeightForWidth())
        self.VidDown_size.setSizePolicy(sizePolicy8)
        self.VidDown_size.setReadOnly(True)

        self.VidDown_sizeLayout.addWidget(self.VidDown_size, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_38.addLayout(self.VidDown_sizeLayout)


        self.horizontalLayout_27.addLayout(self.verticalLayout_38)


        self.verticalLayout_39.addLayout(self.horizontalLayout_27)

        self.VidDown_Button = QPushButton(self.VidDown)
        self.VidDown_Button.setObjectName(u"VidDown_Button")

        self.verticalLayout_39.addWidget(self.VidDown_Button)

        self.VidDown_progressBar = QProgressBar(self.VidDown)
        self.VidDown_progressBar.setObjectName(u"VidDown_progressBar")
        self.VidDown_progressBar.setValue(0)
        self.VidDown_progressBar.setInvertedAppearance(False)
        self.VidDown_progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_39.addWidget(self.VidDown_progressBar)

        self.vid_tabs.addTab(self.VidDown, "")

        self.horizontalLayout_4.addWidget(self.vid_tabs)

        self.stackedWidget.addWidget(self.vid_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.main_frame)

        self.frame = QFrame(self.r_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.r_widget)


        self.verticalLayout_8.addWidget(self.app_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.minimize_button, self.maximize_button)
        QWidget.setTabOrder(self.maximize_button, self.close_button)
        QWidget.setTabOrder(self.close_button, self.menu_button)
        QWidget.setTabOrder(self.menu_button, self.pdf_button)
        QWidget.setTabOrder(self.pdf_button, self.img_button)
        QWidget.setTabOrder(self.img_button, self.file_button)
        QWidget.setTabOrder(self.file_button, self.video_button)
        QWidget.setTabOrder(self.video_button, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.pdf_tabs)
        QWidget.setTabOrder(self.pdf_tabs, self.JoinPdf_In)
        QWidget.setTabOrder(self.JoinPdf_In, self.JoinPdf_selFile)
        QWidget.setTabOrder(self.JoinPdf_selFile, self.JoinPdf_isEven_Button)
        QWidget.setTabOrder(self.JoinPdf_isEven_Button, self.joinPdf_EvenPolicy_comboBox)
        QWidget.setTabOrder(self.joinPdf_EvenPolicy_comboBox, self.JoinPdf_ApplyEven_Button)
        QWidget.setTabOrder(self.JoinPdf_ApplyEven_Button, self.JoinPdf_Button)
        QWidget.setTabOrder(self.JoinPdf_Button, self.SplitPdf_In)
        QWidget.setTabOrder(self.SplitPdf_In, self.SplitPdf_selFile)
        QWidget.setTabOrder(self.SplitPdf_selFile, self.SplitPdf_Sheets)
        QWidget.setTabOrder(self.SplitPdf_Sheets, self.SplitPdf_Button)
        QWidget.setTabOrder(self.SplitPdf_Button, self.ExtractPdf_In)
        QWidget.setTabOrder(self.ExtractPdf_In, self.ExtractPdf_selFile)
        QWidget.setTabOrder(self.ExtractPdf_selFile, self.ExtractPdf_Sheets)
        QWidget.setTabOrder(self.ExtractPdf_Sheets, self.ExtractPdf_All_Button)
        QWidget.setTabOrder(self.ExtractPdf_All_Button, self.ExtractPdf_Button)
        QWidget.setTabOrder(self.ExtractPdf_Button, self.BlankPdf_In)
        QWidget.setTabOrder(self.BlankPdf_In, self.BlankPdf_selFile)
        QWidget.setTabOrder(self.BlankPdf_selFile, self.BlankPdf_Sheets)
        QWidget.setTabOrder(self.BlankPdf_Sheets, self.BlankPdf_Inplace_Button)
        QWidget.setTabOrder(self.BlankPdf_Inplace_Button, self.BlankPdf_Button)
        QWidget.setTabOrder(self.BlankPdf_Button, self.img_tabs)
        QWidget.setTabOrder(self.img_tabs, self.ImgPdf_In)
        QWidget.setTabOrder(self.ImgPdf_In, self.ImgPdf_selFile)
        QWidget.setTabOrder(self.ImgPdf_selFile, self.ImgPdf_Button)
        QWidget.setTabOrder(self.ImgPdf_Button, self.PdfImg_In)
        QWidget.setTabOrder(self.PdfImg_In, self.PdfImg_selFile)
        QWidget.setTabOrder(self.PdfImg_selFile, self.PdfImg_Button)
        QWidget.setTabOrder(self.PdfImg_Button, self.ImgExt_In)
        QWidget.setTabOrder(self.ImgExt_In, self.ImgExt_selFile)
        QWidget.setTabOrder(self.ImgExt_selFile, self.ImgExt_comboBox)
        QWidget.setTabOrder(self.ImgExt_comboBox, self.ImgExt_Button)
        QWidget.setTabOrder(self.ImgExt_Button, self.ImgRsize_In)
        QWidget.setTabOrder(self.ImgRsize_In, self.ImgRsize_selFile)
        QWidget.setTabOrder(self.ImgRsize_selFile, self.ImgRsize_Scale_Button)
        QWidget.setTabOrder(self.ImgRsize_Scale_Button, self.ImgRsize_AW)
        QWidget.setTabOrder(self.ImgRsize_AW, self.ImgRsize_Inplace_Button)
        QWidget.setTabOrder(self.ImgRsize_Inplace_Button, self.ImgRsize_AH)
        QWidget.setTabOrder(self.ImgRsize_AH, self.ImgRsize_NW)
        QWidget.setTabOrder(self.ImgRsize_NW, self.ImgRsize_NH)
        QWidget.setTabOrder(self.ImgRsize_NH, self.ImgRsize_Button)
        QWidget.setTabOrder(self.ImgRsize_Button, self.file_tabs)
        QWidget.setTabOrder(self.file_tabs, self.FileRname_In)
        QWidget.setTabOrder(self.FileRname_In, self.FileRname_selFile)
        QWidget.setTabOrder(self.FileRname_selFile, self.FileRname_Template)
        QWidget.setTabOrder(self.FileRname_Template, self.FileRname_Num)
        QWidget.setTabOrder(self.FileRname_Num, self.FileRname_Button)
        QWidget.setTabOrder(self.FileRname_Button, self.vid_tabs)
        QWidget.setTabOrder(self.vid_tabs, self.VidTag_In)
        QWidget.setTabOrder(self.VidTag_In, self.VidTag_selFile)
        QWidget.setTabOrder(self.VidTag_selFile, self.VidTag_Update)
        QWidget.setTabOrder(self.VidTag_Update, self.VidTag_List)
        QWidget.setTabOrder(self.VidTag_List, self.VidTag_Title)
        QWidget.setTabOrder(self.VidTag_Title, self.VidTag_Intr)
        QWidget.setTabOrder(self.VidTag_Intr, self.VidTag_Alb)
        QWidget.setTabOrder(self.VidTag_Alb, self.VidTag_Genre_comboBox)
        QWidget.setTabOrder(self.VidTag_Genre_comboBox, self.VidTag_Year)
        QWidget.setTabOrder(self.VidTag_Year, self.VidTag_Track)
        QWidget.setTabOrder(self.VidTag_Track, self.VidTag_TrackAll)
        QWidget.setTabOrder(self.VidTag_TrackAll, self.VidTag_IntrAlb)
        QWidget.setTabOrder(self.VidTag_IntrAlb, self.VidTag_Comp)
        QWidget.setTabOrder(self.VidTag_Comp, self.VidTag_Mood)
        QWidget.setTabOrder(self.VidTag_Mood, self.VidTag_Lyrics)
        QWidget.setTabOrder(self.VidTag_Lyrics, self.VidTag_Button)
        QWidget.setTabOrder(self.VidTag_Button, self.MP3toMP4_In)
        QWidget.setTabOrder(self.MP3toMP4_In, self.MP3toMP4_selFile)
        QWidget.setTabOrder(self.MP3toMP4_selFile, self.MP3toMP4_Button)
        QWidget.setTabOrder(self.MP3toMP4_Button, self.VidDown_In)
        QWidget.setTabOrder(self.VidDown_In, self.VidDown_OnlyAudio)
        QWidget.setTabOrder(self.VidDown_OnlyAudio, self.VidDown_res)
        QWidget.setTabOrder(self.VidDown_res, self.VidDown_Title)
        QWidget.setTabOrder(self.VidDown_Title, self.VidDown_all_checkBox)
        QWidget.setTabOrder(self.VidDown_all_checkBox, self.VidDown_list)
        QWidget.setTabOrder(self.VidDown_list, self.VidDown_dur)
        QWidget.setTabOrder(self.VidDown_dur, self.VidDown_size)
        QWidget.setTabOrder(self.VidDown_size, self.VidDown_Button)

        self.retranslateUi(MainWindow)
        self.JoinPdf_isEven_Button.toggled.connect(self.joinPdf_EvenPolicy_comboBox.setVisible)
        self.JoinPdf_isEven_Button.toggled.connect(self.JoinPdf_ApplyEven_Button.setVisible)
        self.JoinPdf_isEven_Button.toggled.connect(self.JoinPdf_ApplyEvenLabel.setVisible)

        self.stackedWidget.setCurrentIndex(0)
        self.pdf_tabs.setCurrentIndex(0)
        self.img_tabs.setCurrentIndex(0)
        self.vid_tabs.setCurrentIndex(0)
        self.VidDown_res.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimize_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        self.pdf_button.setText(QCoreApplication.translate("MainWindow", u" PDF", None))
        self.img_button.setText(QCoreApplication.translate("MainWindow", u" Images", None))
        self.file_button.setText(QCoreApplication.translate("MainWindow", u" Files", None))
        self.video_button.setText(QCoreApplication.translate("MainWindow", u" Video", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF's:", None))
        self.JoinPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivos", None))
        self.JoinPdf_isEven_Button.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Documento Par", None))
        self.joinPdf_EvenPolicy_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A\u00f1adir Hoja al Inicio", None))
        self.joinPdf_EvenPolicy_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A\u00f1adir Hoja al Final", None))

        self.JoinPdf_ApplyEven_Button.setText("")
        self.JoinPdf_ApplyEvenLabel.setText(QCoreApplication.translate("MainWindow", u"Aplicar a Todos los Documentos", None))
        self.JoinPdf_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.JoinPdf_tab), QCoreApplication.translate("MainWindow", u"Unir Pdf", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF:", None))
        self.SplitPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.SplitPdf_SaveAll_Button.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Guardar las Dem\u00e1s", None))
        self.SplitPdf_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.SplitPdf_tab), QCoreApplication.translate("MainWindow", u"Separar PDF", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF:", None))
        self.ExtractPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.ExtractPdf_All_Button.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Separar Todas", None))
        self.ExtractPdf_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.ExtractPDF_tab), QCoreApplication.translate("MainWindow", u"Extraer Hojas", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF:", None))
        self.BlankPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.BlankPdf_Inplace_Button.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Sobreescribir Archivo", None))
        self.BlankPdf_Button.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.BlankPdf_tab), QCoreApplication.translate("MainWindow", u"Hoja en Blanco", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selecciona Im\u00e1genes:", None))
        self.ImgPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Selecciona Archivos", None))
        self.ImgPdf_Button.setText(QCoreApplication.translate("MainWindow", u"CONVERTIR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.ImgPdf_tab), QCoreApplication.translate("MainWindow", u"Im\u00e1gen a PDF", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Seleccione PDF's:", None))
        self.PdfImg_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivos", None))
        self.PdfImg_Button.setText(QCoreApplication.translate("MainWindow", u"CONVERTIR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.PdfImg_tab), QCoreApplication.translate("MainWindow", u"PDF a Im\u00e1gen", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Imagen:", None))
        self.ImgExt_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Extensi\u00f3n:", None))
        self.ImgExt_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u".png", None))
        self.ImgExt_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u".jpeg", None))
        self.ImgExt_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u".gif", None))
        self.ImgExt_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u".bmp", None))
        self.ImgExt_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u".dds", None))
        self.ImgExt_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u".ico", None))
        self.ImgExt_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u".xbm", None))

        self.ImgExt_Button.setText(QCoreApplication.translate("MainWindow", u"CONVERTIR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.ImgExt_tab), QCoreApplication.translate("MainWindow", u"Cambiar Extensi\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Imagen:", None))
        self.ImgRsize_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o Actual:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.ImgRsize_Scale_Button.setText(QCoreApplication.translate("MainWindow", u"Escalar", None))
        self.ImgRsize_Inplace_Button.setText(QCoreApplication.translate("MainWindow", u"Sobreescribir Imagen", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nueva Dimensi\u00f3n:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.ImgRsize_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.ImgRsize_tab), QCoreApplication.translate("MainWindow", u"Redimensionar Imagen", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Seleccione Archivos:", None))
        self.FileRname_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Template:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Inicial:", None))
        self.FileRname_Button.setText(QCoreApplication.translate("MainWindow", u"RENOMBRAR", None))
        self.file_tabs.setTabText(self.file_tabs.indexOf(self.FileRname_tab), QCoreApplication.translate("MainWindow", u"Renombrar Archivos", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Seleccione Carpeta:", None))
        self.VidTag_selFile.setText(QCoreApplication.translate("MainWindow", u"Selecciona Archivo", None))
        self.VidTag_Update.setText("")
        self.VidTag_Cover.setText(QCoreApplication.translate("MainWindow", u"cover", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Int\u00e9rprete:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u00c1lbum:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"G\u00e9nero:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Pista:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.VidTag_IntrAlblabel.setText(QCoreApplication.translate("MainWindow", u"Int\u00e9rprete de Album:", None))
        self.VidTag_Complabel.setText(QCoreApplication.translate("MainWindow", u"Compositor:", None))
        self.VidTag_Moodlabel.setText(QCoreApplication.translate("MainWindow", u"Mood:", None))
        self.VidTag_Lyricslabel.setText(QCoreApplication.translate("MainWindow", u"Letra:", None))
        self.VidTag_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.vid_tabs.setTabText(self.vid_tabs.indexOf(self.VidTag_tab), QCoreApplication.translate("MainWindow", u"Tag M\u00fasica", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Video a Convertir:", None))
        self.MP3toMP4_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.MP3toMP4_Button.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.vid_tabs.setTabText(self.vid_tabs.indexOf(self.MP3toMP4_tab), QCoreApplication.translate("MainWindow", u"MP4 a MP3", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"URL del Video:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Solo Audio:", None))
        self.VidDown_OnlyAudio.setText("")
        self.VidDown_resLabel.setText(QCoreApplication.translate("MainWindow", u"Resoluci\u00f3n:", None))
        self.VidDown_res.setItemText(0, QCoreApplication.translate("MainWindow", u"144", None))
        self.VidDown_res.setItemText(1, QCoreApplication.translate("MainWindow", u"240", None))
        self.VidDown_res.setItemText(2, QCoreApplication.translate("MainWindow", u"360", None))
        self.VidDown_res.setItemText(3, QCoreApplication.translate("MainWindow", u"480", None))
        self.VidDown_res.setItemText(4, QCoreApplication.translate("MainWindow", u"720", None))
        self.VidDown_res.setItemText(5, QCoreApplication.translate("MainWindow", u"1080", None))
        self.VidDown_res.setItemText(6, QCoreApplication.translate("MainWindow", u"1440", None))
        self.VidDown_res.setItemText(7, QCoreApplication.translate("MainWindow", u"2160", None))
        self.VidDown_res.setItemText(8, QCoreApplication.translate("MainWindow", u"Best resolution", None))

        self.VidDown_Titlelabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo del Video:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Descargar Todo:", None))
        self.VidDown_all_checkBox.setText("")
        self.VidDown_listLabel.setText(QCoreApplication.translate("MainWindow", u"Lista de Videos:", None))
        self.VidDown_Thumb.setText(QCoreApplication.translate("MainWindow", u"IMG", None))
        self.VidDown_durLabel.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n:", None))
        self.VidDown_sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o:", None))
        self.VidDown_Button.setText(QCoreApplication.translate("MainWindow", u"DESCARGAR", None))
        self.vid_tabs.setTabText(self.vid_tabs.indexOf(self.VidDown), QCoreApplication.translate("MainWindow", u"Descargar Internet", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Python + PySide6", None))
    # retranslateUi