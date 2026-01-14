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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

from customWidgets.ButtonListWidget import ButtonListWidget
from customWidgets.DroppableImageLabel import DroppableImageLabel
from customWidgets.ModernCheckBox import ModernCheckBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 529)
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
        self.exit_frame.setStyleSheet(u"")
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
        self.JoinPdf_Inlabel = QLabel(self.JoinPdf_tab)
        self.JoinPdf_Inlabel.setObjectName(u"JoinPdf_Inlabel")
        sizePolicy.setHeightForWidth(self.JoinPdf_Inlabel.sizePolicy().hasHeightForWidth())
        self.JoinPdf_Inlabel.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.JoinPdf_Inlabel)

        self.JoinPdf_InLayout = QHBoxLayout()
        self.JoinPdf_InLayout.setSpacing(0)
        self.JoinPdf_InLayout.setObjectName(u"JoinPdf_InLayout")
        self.JoinPdf_In = ButtonListWidget(self.JoinPdf_tab)
        self.JoinPdf_In.setObjectName(u"JoinPdf_In")
        self.JoinPdf_In.setStyleSheet(u"border-top-right-radius: 0px;")

        self.JoinPdf_InLayout.addWidget(self.JoinPdf_In)

        self.JoinPdf_selFile = QPushButton(self.JoinPdf_tab)
        self.JoinPdf_selFile.setObjectName(u"JoinPdf_selFile")
        self.JoinPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.JoinPdf_InLayout.addWidget(self.JoinPdf_selFile, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addLayout(self.JoinPdf_InLayout)


        self.horizontalLayout_29.addLayout(self.verticalLayout_10)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(16)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 16, -1, -1)
        self.JoinPdf_isEvenLayout = QHBoxLayout()
        self.JoinPdf_isEvenLayout.setSpacing(6)
        self.JoinPdf_isEvenLayout.setObjectName(u"JoinPdf_isEvenLayout")
        self.JoinPdf_isEven_Button = ModernCheckBox(self.JoinPdf_tab)
        self.JoinPdf_isEven_Button.setObjectName(u"JoinPdf_isEven_Button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.JoinPdf_isEven_Button.sizePolicy().hasHeightForWidth())
        self.JoinPdf_isEven_Button.setSizePolicy(sizePolicy6)
        self.JoinPdf_isEven_Button.setMinimumSize(QSize(50, 25))
        self.JoinPdf_isEven_Button.setMaximumSize(QSize(50, 25))

        self.JoinPdf_isEvenLayout.addWidget(self.JoinPdf_isEven_Button)

        self.JoinPdf_isEvenlabel = QLabel(self.JoinPdf_tab)
        self.JoinPdf_isEvenlabel.setObjectName(u"JoinPdf_isEvenlabel")
        sizePolicy6.setHeightForWidth(self.JoinPdf_isEvenlabel.sizePolicy().hasHeightForWidth())
        self.JoinPdf_isEvenlabel.setSizePolicy(sizePolicy6)

        self.JoinPdf_isEvenLayout.addWidget(self.JoinPdf_isEvenlabel)


        self.verticalLayout_35.addLayout(self.JoinPdf_isEvenLayout)

        self.joinPdf_EvenPolicy_comboBox = QComboBox(self.JoinPdf_tab)
        self.joinPdf_EvenPolicy_comboBox.addItem("")
        self.joinPdf_EvenPolicy_comboBox.addItem("")
        self.joinPdf_EvenPolicy_comboBox.setObjectName(u"joinPdf_EvenPolicy_comboBox")
        sizePolicy4.setHeightForWidth(self.joinPdf_EvenPolicy_comboBox.sizePolicy().hasHeightForWidth())
        self.joinPdf_EvenPolicy_comboBox.setSizePolicy(sizePolicy4)

        self.verticalLayout_35.addWidget(self.joinPdf_EvenPolicy_comboBox)

        self.JoinPdf_ApplyEvenLayout = QHBoxLayout()
        self.JoinPdf_ApplyEvenLayout.setSpacing(6)
        self.JoinPdf_ApplyEvenLayout.setObjectName(u"JoinPdf_ApplyEvenLayout")
        self.JoinPdf_ApplyEven_Button = ModernCheckBox(self.JoinPdf_tab)
        self.JoinPdf_ApplyEven_Button.setObjectName(u"JoinPdf_ApplyEven_Button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.JoinPdf_ApplyEven_Button.sizePolicy().hasHeightForWidth())
        self.JoinPdf_ApplyEven_Button.setSizePolicy(sizePolicy7)
        self.JoinPdf_ApplyEven_Button.setMinimumSize(QSize(50, 25))
        self.JoinPdf_ApplyEven_Button.setMaximumSize(QSize(50, 25))

        self.JoinPdf_ApplyEvenLayout.addWidget(self.JoinPdf_ApplyEven_Button)

        self.JoinPdf_ApplyEvenLabel = QLabel(self.JoinPdf_tab)
        self.JoinPdf_ApplyEvenLabel.setObjectName(u"JoinPdf_ApplyEvenLabel")
        sizePolicy6.setHeightForWidth(self.JoinPdf_ApplyEvenLabel.sizePolicy().hasHeightForWidth())
        self.JoinPdf_ApplyEvenLabel.setSizePolicy(sizePolicy6)

        self.JoinPdf_ApplyEvenLayout.addWidget(self.JoinPdf_ApplyEvenLabel)


        self.verticalLayout_35.addLayout(self.JoinPdf_ApplyEvenLayout)

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
        self.SplitPdf_InLayout = QVBoxLayout()
        self.SplitPdf_InLayout.setSpacing(0)
        self.SplitPdf_InLayout.setObjectName(u"SplitPdf_InLayout")
        self.SplitPdf_Inlabel = QLabel(self.SplitPdf_tab)
        self.SplitPdf_Inlabel.setObjectName(u"SplitPdf_Inlabel")

        self.SplitPdf_InLayout.addWidget(self.SplitPdf_Inlabel)

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


        self.SplitPdf_InLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_41.addLayout(self.SplitPdf_InLayout)

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
        self.SplitPdf_Sheetslabel = QLabel(self.SplitPDF_Sheets_widget)
        self.SplitPdf_Sheetslabel.setObjectName(u"SplitPdf_Sheetslabel")
        sizePolicy6.setHeightForWidth(self.SplitPdf_Sheetslabel.sizePolicy().hasHeightForWidth())
        self.SplitPdf_Sheetslabel.setSizePolicy(sizePolicy6)

        self.verticalLayout_12.addWidget(self.SplitPdf_Sheetslabel)

        self.SplitPdf_Sheets = QLineEdit(self.SplitPDF_Sheets_widget)
        self.SplitPdf_Sheets.setObjectName(u"SplitPdf_Sheets")
        sizePolicy5.setHeightForWidth(self.SplitPdf_Sheets.sizePolicy().hasHeightForWidth())
        self.SplitPdf_Sheets.setSizePolicy(sizePolicy5)
        self.SplitPdf_Sheets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_12.addWidget(self.SplitPdf_Sheets)


        self.horizontalLayout_10.addWidget(self.SplitPDF_Sheets_widget)

        self.SplitPdf_SaveAllLayout = QHBoxLayout()
        self.SplitPdf_SaveAllLayout.setSpacing(6)
        self.SplitPdf_SaveAllLayout.setObjectName(u"SplitPdf_SaveAllLayout")
        self.SplitPdf_SaveAll_Button = ModernCheckBox(self.SplitPdf_tab)
        self.SplitPdf_SaveAll_Button.setObjectName(u"SplitPdf_SaveAll_Button")
        self.SplitPdf_SaveAll_Button.setMinimumSize(QSize(50, 22))
        self.SplitPdf_SaveAll_Button.setMaximumSize(QSize(50, 22))

        self.SplitPdf_SaveAllLayout.addWidget(self.SplitPdf_SaveAll_Button, 0, Qt.AlignmentFlag.AlignBottom)

        self.SplitPdf_SaveAlllabel = QLabel(self.SplitPdf_tab)
        self.SplitPdf_SaveAlllabel.setObjectName(u"SplitPdf_SaveAlllabel")
        sizePolicy6.setHeightForWidth(self.SplitPdf_SaveAlllabel.sizePolicy().hasHeightForWidth())
        self.SplitPdf_SaveAlllabel.setSizePolicy(sizePolicy6)

        self.SplitPdf_SaveAllLayout.addWidget(self.SplitPdf_SaveAlllabel, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_10.addLayout(self.SplitPdf_SaveAllLayout)


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
        self.ExtractPdf_InLayout = QVBoxLayout()
        self.ExtractPdf_InLayout.setSpacing(0)
        self.ExtractPdf_InLayout.setObjectName(u"ExtractPdf_InLayout")
        self.ExtractPdf_Inlabel = QLabel(self.ExtractPDF_tab)
        self.ExtractPdf_Inlabel.setObjectName(u"ExtractPdf_Inlabel")

        self.ExtractPdf_InLayout.addWidget(self.ExtractPdf_Inlabel)

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


        self.ExtractPdf_InLayout.addLayout(self.horizontalLayout_12)


        self.verticalLayout_42.addLayout(self.ExtractPdf_InLayout)

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
        self.ExtractPdf_Sheetslabel = QLabel(self.ExtractPDF_SheetsWidget)
        self.ExtractPdf_Sheetslabel.setObjectName(u"ExtractPdf_Sheetslabel")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.ExtractPdf_Sheetslabel.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_Sheetslabel.setSizePolicy(sizePolicy10)

        self.verticalLayout_17.addWidget(self.ExtractPdf_Sheetslabel)

        self.ExtractPdf_Sheets = QLineEdit(self.ExtractPDF_SheetsWidget)
        self.ExtractPdf_Sheets.setObjectName(u"ExtractPdf_Sheets")
        sizePolicy8.setHeightForWidth(self.ExtractPdf_Sheets.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_Sheets.setSizePolicy(sizePolicy8)
        self.ExtractPdf_Sheets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_17.addWidget(self.ExtractPdf_Sheets)


        self.horizontalLayout_11.addWidget(self.ExtractPDF_SheetsWidget)

        self.ExtractPdf_AllLayout = QHBoxLayout()
        self.ExtractPdf_AllLayout.setSpacing(6)
        self.ExtractPdf_AllLayout.setObjectName(u"ExtractPdf_AllLayout")
        self.ExtractPdf_All_Button = ModernCheckBox(self.ExtractPDF_tab)
        self.ExtractPdf_All_Button.setObjectName(u"ExtractPdf_All_Button")
        sizePolicy3.setHeightForWidth(self.ExtractPdf_All_Button.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_All_Button.setSizePolicy(sizePolicy3)
        self.ExtractPdf_All_Button.setMinimumSize(QSize(50, 22))
        self.ExtractPdf_All_Button.setMaximumSize(QSize(50, 22))

        self.ExtractPdf_AllLayout.addWidget(self.ExtractPdf_All_Button, 0, Qt.AlignmentFlag.AlignBottom)

        self.ExtractPdf_Alllabel = QLabel(self.ExtractPDF_tab)
        self.ExtractPdf_Alllabel.setObjectName(u"ExtractPdf_Alllabel")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.ExtractPdf_Alllabel.sizePolicy().hasHeightForWidth())
        self.ExtractPdf_Alllabel.setSizePolicy(sizePolicy11)

        self.ExtractPdf_AllLayout.addWidget(self.ExtractPdf_Alllabel, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_11.addLayout(self.ExtractPdf_AllLayout)


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
        self.BlankPdf_InLayout = QVBoxLayout()
        self.BlankPdf_InLayout.setSpacing(0)
        self.BlankPdf_InLayout.setObjectName(u"BlankPdf_InLayout")
        self.BlankPdf_Inlabel = QLabel(self.BlankPdf_tab)
        self.BlankPdf_Inlabel.setObjectName(u"BlankPdf_Inlabel")

        self.BlankPdf_InLayout.addWidget(self.BlankPdf_Inlabel)

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


        self.BlankPdf_InLayout.addLayout(self.horizontalLayout_13)


        self.verticalLayout_14.addLayout(self.BlankPdf_InLayout)

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
        self.BlankPdf_Sheetslabel = QLabel(self.BlankPdf_SheetsWidget)
        self.BlankPdf_Sheetslabel.setObjectName(u"BlankPdf_Sheetslabel")

        self.verticalLayout_9.addWidget(self.BlankPdf_Sheetslabel)

        self.BlankPdf_Sheets = QLineEdit(self.BlankPdf_SheetsWidget)
        self.BlankPdf_Sheets.setObjectName(u"BlankPdf_Sheets")
        sizePolicy8.setHeightForWidth(self.BlankPdf_Sheets.sizePolicy().hasHeightForWidth())
        self.BlankPdf_Sheets.setSizePolicy(sizePolicy8)
        self.BlankPdf_Sheets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_9.addWidget(self.BlankPdf_Sheets)


        self.horizontalLayout_39.addWidget(self.BlankPdf_SheetsWidget)

        self.BlankPdf_InplaceLayout = QHBoxLayout()
        self.BlankPdf_InplaceLayout.setObjectName(u"BlankPdf_InplaceLayout")
        self.BlankPdf_Inplace_Button = ModernCheckBox(self.BlankPdf_tab)
        self.BlankPdf_Inplace_Button.setObjectName(u"BlankPdf_Inplace_Button")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(50)
        sizePolicy12.setVerticalStretch(22)
        sizePolicy12.setHeightForWidth(self.BlankPdf_Inplace_Button.sizePolicy().hasHeightForWidth())
        self.BlankPdf_Inplace_Button.setSizePolicy(sizePolicy12)
        self.BlankPdf_Inplace_Button.setMinimumSize(QSize(50, 22))

        self.BlankPdf_InplaceLayout.addWidget(self.BlankPdf_Inplace_Button, 0, Qt.AlignmentFlag.AlignBottom)

        self.BlankPdf_Inplacelabel = QLabel(self.BlankPdf_tab)
        self.BlankPdf_Inplacelabel.setObjectName(u"BlankPdf_Inplacelabel")

        self.BlankPdf_InplaceLayout.addWidget(self.BlankPdf_Inplacelabel, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_39.addLayout(self.BlankPdf_InplaceLayout)


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
        self.ImgPdf_Inlabel = QLabel(self.ImgPdf_tab)
        self.ImgPdf_Inlabel.setObjectName(u"ImgPdf_Inlabel")

        self.verticalLayout_21.addWidget(self.ImgPdf_Inlabel)

        self.ImgPdf_InLayout = QHBoxLayout()
        self.ImgPdf_InLayout.setSpacing(0)
        self.ImgPdf_InLayout.setObjectName(u"ImgPdf_InLayout")
        self.ImgPdf_InLayout.setContentsMargins(-1, 2, -1, 2)
        self.ImgPdf_In = QLineEdit(self.ImgPdf_tab)
        self.ImgPdf_In.setObjectName(u"ImgPdf_In")
        sizePolicy8.setHeightForWidth(self.ImgPdf_In.sizePolicy().hasHeightForWidth())
        self.ImgPdf_In.setSizePolicy(sizePolicy8)
        self.ImgPdf_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"\n"
"")

        self.ImgPdf_InLayout.addWidget(self.ImgPdf_In)

        self.ImgPdf_selFile = QPushButton(self.ImgPdf_tab)
        self.ImgPdf_selFile.setObjectName(u"ImgPdf_selFile")
        self.ImgPdf_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.ImgPdf_InLayout.addWidget(self.ImgPdf_selFile)


        self.verticalLayout_21.addLayout(self.ImgPdf_InLayout)

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
        self.PdfImg_Inlabel = QLabel(self.PdfImg_tab)
        self.PdfImg_Inlabel.setObjectName(u"PdfImg_Inlabel")

        self.verticalLayout_22.addWidget(self.PdfImg_Inlabel)

        self.PdfImg_InLayout = QHBoxLayout()
        self.PdfImg_InLayout.setSpacing(0)
        self.PdfImg_InLayout.setObjectName(u"PdfImg_InLayout")
        self.PdfImg_InLayout.setContentsMargins(-1, 2, -1, 2)
        self.PdfImg_In = QLineEdit(self.PdfImg_tab)
        self.PdfImg_In.setObjectName(u"PdfImg_In")
        sizePolicy8.setHeightForWidth(self.PdfImg_In.sizePolicy().hasHeightForWidth())
        self.PdfImg_In.setSizePolicy(sizePolicy8)
        self.PdfImg_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.PdfImg_InLayout.addWidget(self.PdfImg_In)

        self.PdfImg_selFile = QPushButton(self.PdfImg_tab)
        self.PdfImg_selFile.setObjectName(u"PdfImg_selFile")
        self.PdfImg_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.PdfImg_InLayout.addWidget(self.PdfImg_selFile)


        self.verticalLayout_22.addLayout(self.PdfImg_InLayout)

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
        self.ImgExt_InLayout = QVBoxLayout()
        self.ImgExt_InLayout.setSpacing(0)
        self.ImgExt_InLayout.setObjectName(u"ImgExt_InLayout")
        self.ImgExt_Inlabel = QLabel(self.ImgExt_tab)
        self.ImgExt_Inlabel.setObjectName(u"ImgExt_Inlabel")

        self.ImgExt_InLayout.addWidget(self.ImgExt_Inlabel)

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


        self.ImgExt_InLayout.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.ImgExt_InLayout)

        self.ImgExt_ExtLayout = QVBoxLayout()
        self.ImgExt_ExtLayout.setSpacing(0)
        self.ImgExt_ExtLayout.setObjectName(u"ImgExt_ExtLayout")
        self.ImgExt_Extlabel = QLabel(self.ImgExt_tab)
        self.ImgExt_Extlabel.setObjectName(u"ImgExt_Extlabel")

        self.ImgExt_ExtLayout.addWidget(self.ImgExt_Extlabel)

        self.ImgExt_comboBox = QComboBox(self.ImgExt_tab)
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.addItem("")
        self.ImgExt_comboBox.setObjectName(u"ImgExt_comboBox")

        self.ImgExt_ExtLayout.addWidget(self.ImgExt_comboBox)


        self.horizontalLayout_18.addLayout(self.ImgExt_ExtLayout)

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
        self.gridLayout = QGridLayout(self.ImgRsize_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(16)
        self.ImgRsize_InLayout = QVBoxLayout()
        self.ImgRsize_InLayout.setSpacing(0)
        self.ImgRsize_InLayout.setObjectName(u"ImgRsize_InLayout")
        self.ImgRsize_Inlabel = QLabel(self.ImgRsize_tab)
        self.ImgRsize_Inlabel.setObjectName(u"ImgRsize_Inlabel")

        self.ImgRsize_InLayout.addWidget(self.ImgRsize_Inlabel)

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


        self.ImgRsize_InLayout.addLayout(self.horizontalLayout_20)


        self.gridLayout.addLayout(self.ImgRsize_InLayout, 0, 0, 1, 1)

        self.ImgRsize_ActualLayout = QVBoxLayout()
        self.ImgRsize_ActualLayout.setSpacing(0)
        self.ImgRsize_ActualLayout.setObjectName(u"ImgRsize_ActualLayout")
        self.ImgRsize_Actuallabel_2 = QLabel(self.ImgRsize_tab)
        self.ImgRsize_Actuallabel_2.setObjectName(u"ImgRsize_Actuallabel_2")

        self.ImgRsize_ActualLayout.addWidget(self.ImgRsize_Actuallabel_2)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ImgRsize_AW = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_AW.setObjectName(u"ImgRsize_AW")
        sizePolicy8.setHeightForWidth(self.ImgRsize_AW.sizePolicy().hasHeightForWidth())
        self.ImgRsize_AW.setSizePolicy(sizePolicy8)
        self.ImgRsize_AW.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.ImgRsize_AW)

        self.label_13 = QLabel(self.ImgRsize_tab)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_19.addWidget(self.label_13)

        self.ImgRsize_AH = QLineEdit(self.ImgRsize_tab)
        self.ImgRsize_AH.setObjectName(u"ImgRsize_AH")
        sizePolicy8.setHeightForWidth(self.ImgRsize_AH.sizePolicy().hasHeightForWidth())
        self.ImgRsize_AH.setSizePolicy(sizePolicy8)
        self.ImgRsize_AH.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.ImgRsize_AH)


        self.ImgRsize_ActualLayout.addLayout(self.horizontalLayout_19)


        self.gridLayout.addLayout(self.ImgRsize_ActualLayout, 0, 1, 1, 1)

        self.ImgRsize_OptionsLayout = QHBoxLayout()
        self.ImgRsize_OptionsLayout.setSpacing(25)
        self.ImgRsize_OptionsLayout.setObjectName(u"ImgRsize_OptionsLayout")
        self.ImgRsize_Scale_Button = QCheckBox(self.ImgRsize_tab)
        self.ImgRsize_Scale_Button.setObjectName(u"ImgRsize_Scale_Button")

        self.ImgRsize_OptionsLayout.addWidget(self.ImgRsize_Scale_Button)

        self.ImgRsize_Inplace_Button = QCheckBox(self.ImgRsize_tab)
        self.ImgRsize_Inplace_Button.setObjectName(u"ImgRsize_Inplace_Button")

        self.ImgRsize_OptionsLayout.addWidget(self.ImgRsize_Inplace_Button)


        self.gridLayout.addLayout(self.ImgRsize_OptionsLayout, 1, 0, 1, 1)

        self.ImgRsize_NewLayout = QVBoxLayout()
        self.ImgRsize_NewLayout.setSpacing(0)
        self.ImgRsize_NewLayout.setObjectName(u"ImgRsize_NewLayout")
        self.ImgRsize_Newlabel = QLabel(self.ImgRsize_tab)
        self.ImgRsize_Newlabel.setObjectName(u"ImgRsize_Newlabel")

        self.ImgRsize_NewLayout.addWidget(self.ImgRsize_Newlabel)

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


        self.ImgRsize_NewLayout.addLayout(self.horizontalLayout_21)


        self.gridLayout.addLayout(self.ImgRsize_NewLayout, 1, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_13, 2, 0, 1, 1)

        self.ImgRsize_Button = QPushButton(self.ImgRsize_tab)
        self.ImgRsize_Button.setObjectName(u"ImgRsize_Button")

        self.gridLayout.addWidget(self.ImgRsize_Button, 3, 0, 1, 2)

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
        self.FileRname_InLayout = QVBoxLayout()
        self.FileRname_InLayout.setSpacing(0)
        self.FileRname_InLayout.setObjectName(u"FileRname_InLayout")
        self.FileRname_Inlabel = QLabel(self.FileRname_tab)
        self.FileRname_Inlabel.setObjectName(u"FileRname_Inlabel")

        self.FileRname_InLayout.addWidget(self.FileRname_Inlabel)

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


        self.FileRname_InLayout.addLayout(self.horizontalLayout_25)


        self.formLayout_2.setLayout(0, QFormLayout.ItemRole.LabelRole, self.FileRname_InLayout)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.FileRname_Templatelabel = QLabel(self.FileRname_tab)
        self.FileRname_Templatelabel.setObjectName(u"FileRname_Templatelabel")

        self.verticalLayout_32.addWidget(self.FileRname_Templatelabel)

        self.FileRname_Template = QLineEdit(self.FileRname_tab)
        self.FileRname_Template.setObjectName(u"FileRname_Template")
        sizePolicy8.setHeightForWidth(self.FileRname_Template.sizePolicy().hasHeightForWidth())
        self.FileRname_Template.setSizePolicy(sizePolicy8)

        self.verticalLayout_32.addWidget(self.FileRname_Template)

        self.verticalSpacer_15 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_32.addItem(self.verticalSpacer_15)

        self.FileRname_Numlabel = QLabel(self.FileRname_tab)
        self.FileRname_Numlabel.setObjectName(u"FileRname_Numlabel")

        self.verticalLayout_32.addWidget(self.FileRname_Numlabel)

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
        self.VidTag_InLayout = QVBoxLayout()
        self.VidTag_InLayout.setSpacing(0)
        self.VidTag_InLayout.setObjectName(u"VidTag_InLayout")
        self.VidTag_Inlabel = QLabel(self.VidTag_tab)
        self.VidTag_Inlabel.setObjectName(u"VidTag_Inlabel")
        self.VidTag_Inlabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_InLayout.addWidget(self.VidTag_Inlabel)

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


        self.VidTag_InLayout.addLayout(self.horizontalLayout_24)

        self.VidTag_List = ButtonListWidget(self.VidTag_tab)
        self.VidTag_List.setObjectName(u"VidTag_List")
        sizePolicy2.setHeightForWidth(self.VidTag_List.sizePolicy().hasHeightForWidth())
        self.VidTag_List.setSizePolicy(sizePolicy2)

        self.VidTag_InLayout.addWidget(self.VidTag_List)


        self.horizontalLayout_34.addLayout(self.VidTag_InLayout)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.VidTag_Cover = DroppableImageLabel(self.VidTag_tab)
        self.VidTag_Cover.setObjectName(u"VidTag_Cover")
        sizePolicy6.setHeightForWidth(self.VidTag_Cover.sizePolicy().hasHeightForWidth())
        self.VidTag_Cover.setSizePolicy(sizePolicy6)
        self.VidTag_Cover.setMinimumSize(QSize(142, 0))

        self.horizontalLayout_33.addWidget(self.VidTag_Cover)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.VidTag_TitleLayout = QVBoxLayout()
        self.VidTag_TitleLayout.setSpacing(0)
        self.VidTag_TitleLayout.setObjectName(u"VidTag_TitleLayout")
        self.VidTag_Titlelabel = QLabel(self.VidTag_tab)
        self.VidTag_Titlelabel.setObjectName(u"VidTag_Titlelabel")
        sizePolicy5.setHeightForWidth(self.VidTag_Titlelabel.sizePolicy().hasHeightForWidth())
        self.VidTag_Titlelabel.setSizePolicy(sizePolicy5)
        self.VidTag_Titlelabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_TitleLayout.addWidget(self.VidTag_Titlelabel)

        self.VidTag_Title = QLineEdit(self.VidTag_tab)
        self.VidTag_Title.setObjectName(u"VidTag_Title")
        sizePolicy13.setHeightForWidth(self.VidTag_Title.sizePolicy().hasHeightForWidth())
        self.VidTag_Title.setSizePolicy(sizePolicy13)

        self.VidTag_TitleLayout.addWidget(self.VidTag_Title)


        self.horizontalLayout_32.addLayout(self.VidTag_TitleLayout)

        self.VidTag_IntrLayout = QVBoxLayout()
        self.VidTag_IntrLayout.setSpacing(0)
        self.VidTag_IntrLayout.setObjectName(u"VidTag_IntrLayout")
        self.VidTag_Intrlabel = QLabel(self.VidTag_tab)
        self.VidTag_Intrlabel.setObjectName(u"VidTag_Intrlabel")
        sizePolicy5.setHeightForWidth(self.VidTag_Intrlabel.sizePolicy().hasHeightForWidth())
        self.VidTag_Intrlabel.setSizePolicy(sizePolicy5)
        self.VidTag_Intrlabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_IntrLayout.addWidget(self.VidTag_Intrlabel)

        self.VidTag_Intr = QLineEdit(self.VidTag_tab)
        self.VidTag_Intr.setObjectName(u"VidTag_Intr")
        sizePolicy13.setHeightForWidth(self.VidTag_Intr.sizePolicy().hasHeightForWidth())
        self.VidTag_Intr.setSizePolicy(sizePolicy13)

        self.VidTag_IntrLayout.addWidget(self.VidTag_Intr)


        self.horizontalLayout_32.addLayout(self.VidTag_IntrLayout)

        self.VidTag_AlbLayout = QVBoxLayout()
        self.VidTag_AlbLayout.setSpacing(0)
        self.VidTag_AlbLayout.setObjectName(u"VidTag_AlbLayout")
        self.VidTag_Alblabel = QLabel(self.VidTag_tab)
        self.VidTag_Alblabel.setObjectName(u"VidTag_Alblabel")
        sizePolicy5.setHeightForWidth(self.VidTag_Alblabel.sizePolicy().hasHeightForWidth())
        self.VidTag_Alblabel.setSizePolicy(sizePolicy5)
        self.VidTag_Alblabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_AlbLayout.addWidget(self.VidTag_Alblabel)

        self.VidTag_Alb = QLineEdit(self.VidTag_tab)
        self.VidTag_Alb.setObjectName(u"VidTag_Alb")
        sizePolicy13.setHeightForWidth(self.VidTag_Alb.sizePolicy().hasHeightForWidth())
        self.VidTag_Alb.setSizePolicy(sizePolicy13)

        self.VidTag_AlbLayout.addWidget(self.VidTag_Alb)


        self.horizontalLayout_32.addLayout(self.VidTag_AlbLayout)


        self.verticalLayout_46.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.VidTag_GenreLayout = QVBoxLayout()
        self.VidTag_GenreLayout.setSpacing(0)
        self.VidTag_GenreLayout.setObjectName(u"VidTag_GenreLayout")
        self.VidTag_Genrelabel = QLabel(self.VidTag_tab)
        self.VidTag_Genrelabel.setObjectName(u"VidTag_Genrelabel")
        self.VidTag_Genrelabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_GenreLayout.addWidget(self.VidTag_Genrelabel)

        self.VidTag_Genre_comboBox = QComboBox(self.VidTag_tab)
        self.VidTag_Genre_comboBox.setObjectName(u"VidTag_Genre_comboBox")
        sizePolicy11.setHeightForWidth(self.VidTag_Genre_comboBox.sizePolicy().hasHeightForWidth())
        self.VidTag_Genre_comboBox.setSizePolicy(sizePolicy11)
        self.VidTag_Genre_comboBox.setEditable(True)

        self.VidTag_GenreLayout.addWidget(self.VidTag_Genre_comboBox)


        self.horizontalLayout_31.addLayout(self.VidTag_GenreLayout)

        self.VidTag_YearLayout = QVBoxLayout()
        self.VidTag_YearLayout.setSpacing(0)
        self.VidTag_YearLayout.setObjectName(u"VidTag_YearLayout")
        self.VidTag_Yearlabel = QLabel(self.VidTag_tab)
        self.VidTag_Yearlabel.setObjectName(u"VidTag_Yearlabel")
        self.VidTag_Yearlabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_YearLayout.addWidget(self.VidTag_Yearlabel)

        self.VidTag_Year = QLineEdit(self.VidTag_tab)
        self.VidTag_Year.setObjectName(u"VidTag_Year")
        sizePolicy3.setHeightForWidth(self.VidTag_Year.sizePolicy().hasHeightForWidth())
        self.VidTag_Year.setSizePolicy(sizePolicy3)

        self.VidTag_YearLayout.addWidget(self.VidTag_Year)


        self.horizontalLayout_31.addLayout(self.VidTag_YearLayout)

        self.VidTag_TrackLayout = QVBoxLayout()
        self.VidTag_TrackLayout.setSpacing(0)
        self.VidTag_TrackLayout.setObjectName(u"VidTag_TrackLayout")
        self.VidTag_Tracklabel = QLabel(self.VidTag_tab)
        self.VidTag_Tracklabel.setObjectName(u"VidTag_Tracklabel")
        self.VidTag_Tracklabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_TrackLayout.addWidget(self.VidTag_Tracklabel)

        self.verticalLayout_11 = QHBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.VidTag_Track = QSpinBox(self.VidTag_tab)
        self.VidTag_Track.setObjectName(u"VidTag_Track")

        self.verticalLayout_11.addWidget(self.VidTag_Track)

        self.label_25 = QLabel(self.VidTag_tab)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_11.addWidget(self.label_25)

        self.VidTag_TrackAll = QSpinBox(self.VidTag_tab)
        self.VidTag_TrackAll.setObjectName(u"VidTag_TrackAll")

        self.verticalLayout_11.addWidget(self.VidTag_TrackAll)


        self.VidTag_TrackLayout.addLayout(self.verticalLayout_11)


        self.horizontalLayout_31.addLayout(self.VidTag_TrackLayout)


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
        sizePolicy13.setHeightForWidth(self.VidTag_IntrAlb.sizePolicy().hasHeightForWidth())
        self.VidTag_IntrAlb.setSizePolicy(sizePolicy13)

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
        sizePolicy13.setHeightForWidth(self.VidTag_Comp.sizePolicy().hasHeightForWidth())
        self.VidTag_Comp.setSizePolicy(sizePolicy13)

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
        sizePolicy13.setHeightForWidth(self.VidTag_Mood.sizePolicy().hasHeightForWidth())
        self.VidTag_Mood.setSizePolicy(sizePolicy13)

        self.VidTag_MoodLayout.addWidget(self.VidTag_Mood)


        self.horizontalLayout_30.addLayout(self.VidTag_MoodLayout)


        self.verticalLayout_46.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_33.addLayout(self.verticalLayout_46)


        self.verticalLayout_48.addLayout(self.horizontalLayout_33)

        self.VidTag_LyricsLayout = QVBoxLayout()
        self.VidTag_LyricsLayout.setSpacing(0)
        self.VidTag_LyricsLayout.setObjectName(u"VidTag_LyricsLayout")
        self.VidTag_Lyricslabel = QLabel(self.VidTag_tab)
        self.VidTag_Lyricslabel.setObjectName(u"VidTag_Lyricslabel")
        self.VidTag_Lyricslabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.VidTag_LyricsLayout.addWidget(self.VidTag_Lyricslabel)

        self.VidTag_Lyrics = QPlainTextEdit(self.VidTag_tab)
        self.VidTag_Lyrics.setObjectName(u"VidTag_Lyrics")

        self.VidTag_LyricsLayout.addWidget(self.VidTag_Lyrics)


        self.verticalLayout_48.addLayout(self.VidTag_LyricsLayout)


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

        self.MP3toMP4_InLayout = QHBoxLayout()
        self.MP3toMP4_InLayout.setSpacing(0)
        self.MP3toMP4_InLayout.setObjectName(u"MP3toMP4_InLayout")
        self.MP3toMP4_InLayout.setContentsMargins(-1, 2, -1, 2)
        self.MP3toMP4_In = QLineEdit(self.MP3toMP4_tab)
        self.MP3toMP4_In.setObjectName(u"MP3toMP4_In")
        sizePolicy8.setHeightForWidth(self.MP3toMP4_In.sizePolicy().hasHeightForWidth())
        self.MP3toMP4_In.setSizePolicy(sizePolicy8)
        self.MP3toMP4_In.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")

        self.MP3toMP4_InLayout.addWidget(self.MP3toMP4_In)

        self.MP3toMP4_selFile = QPushButton(self.MP3toMP4_tab)
        self.MP3toMP4_selFile.setObjectName(u"MP3toMP4_selFile")
        self.MP3toMP4_selFile.setStyleSheet(u"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"")

        self.MP3toMP4_InLayout.addWidget(self.MP3toMP4_selFile)


        self.verticalLayout_29.addLayout(self.MP3toMP4_InLayout)

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
        self.VidDown_InLayout = QVBoxLayout()
        self.VidDown_InLayout.setSpacing(0)
        self.VidDown_InLayout.setObjectName(u"VidDown_InLayout")
        self.VidDown_Inlabel = QLabel(self.VidDown)
        self.VidDown_Inlabel.setObjectName(u"VidDown_Inlabel")

        self.VidDown_InLayout.addWidget(self.VidDown_Inlabel)

        self.VidDown_In = QLineEdit(self.VidDown)
        self.VidDown_In.setObjectName(u"VidDown_In")
        sizePolicy8.setHeightForWidth(self.VidDown_In.sizePolicy().hasHeightForWidth())
        self.VidDown_In.setSizePolicy(sizePolicy8)

        self.VidDown_InLayout.addWidget(self.VidDown_In)


        self.horizontalLayout_8.addLayout(self.VidDown_InLayout)

        self.VidDown_OnlyAudioLayout = QVBoxLayout()
        self.VidDown_OnlyAudioLayout.setSpacing(0)
        self.VidDown_OnlyAudioLayout.setObjectName(u"VidDown_OnlyAudioLayout")
        self.VidDown_OnlyAudiolabel = QLabel(self.VidDown)
        self.VidDown_OnlyAudiolabel.setObjectName(u"VidDown_OnlyAudiolabel")

        self.VidDown_OnlyAudioLayout.addWidget(self.VidDown_OnlyAudiolabel)

        self.VidDown_OnlyAudio = ModernCheckBox(self.VidDown)
        self.VidDown_OnlyAudio.setObjectName(u"VidDown_OnlyAudio")
        sizePolicy4.setHeightForWidth(self.VidDown_OnlyAudio.sizePolicy().hasHeightForWidth())
        self.VidDown_OnlyAudio.setSizePolicy(sizePolicy4)
        self.VidDown_OnlyAudio.setMinimumSize(QSize(0, 22))

        self.VidDown_OnlyAudioLayout.addWidget(self.VidDown_OnlyAudio)


        self.horizontalLayout_8.addLayout(self.VidDown_OnlyAudioLayout)

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
        self.VidDown_TitleLayout = QVBoxLayout()
        self.VidDown_TitleLayout.setSpacing(0)
        self.VidDown_TitleLayout.setObjectName(u"VidDown_TitleLayout")
        self.VidDown_Titlelabel = QLabel(self.VidDown)
        self.VidDown_Titlelabel.setObjectName(u"VidDown_Titlelabel")

        self.VidDown_TitleLayout.addWidget(self.VidDown_Titlelabel)

        self.VidDown_Title = QLineEdit(self.VidDown)
        self.VidDown_Title.setObjectName(u"VidDown_Title")
        sizePolicy8.setHeightForWidth(self.VidDown_Title.sizePolicy().hasHeightForWidth())
        self.VidDown_Title.setSizePolicy(sizePolicy8)
        self.VidDown_Title.setReadOnly(True)

        self.VidDown_TitleLayout.addWidget(self.VidDown_Title)


        self.horizontalLayout_26.addLayout(self.VidDown_TitleLayout)

        self.VidDown_allLayout = QVBoxLayout()
        self.VidDown_allLayout.setSpacing(0)
        self.VidDown_allLayout.setObjectName(u"VidDown_allLayout")
        self.VidDown_alllabel = QLabel(self.VidDown)
        self.VidDown_alllabel.setObjectName(u"VidDown_alllabel")

        self.VidDown_allLayout.addWidget(self.VidDown_alllabel)

        self.VidDown_all_checkBox = ModernCheckBox(self.VidDown)
        self.VidDown_all_checkBox.setObjectName(u"VidDown_all_checkBox")
        self.VidDown_all_checkBox.setMinimumSize(QSize(0, 22))

        self.VidDown_allLayout.addWidget(self.VidDown_all_checkBox)


        self.horizontalLayout_26.addLayout(self.VidDown_allLayout)


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
        self.JoinPdf_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF's:", None))
        self.JoinPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivos", None))
        self.JoinPdf_isEven_Button.setText("")
        self.JoinPdf_isEvenlabel.setText(QCoreApplication.translate("MainWindow", u"Documento Par", None))
        self.joinPdf_EvenPolicy_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A\u00f1adir Hoja al Inicio", None))
        self.joinPdf_EvenPolicy_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A\u00f1adir Hoja al Final", None))

        self.JoinPdf_ApplyEven_Button.setText("")
        self.JoinPdf_ApplyEvenLabel.setText(QCoreApplication.translate("MainWindow", u"Aplicar a Todos los Documentos", None))
        self.JoinPdf_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.JoinPdf_tab), QCoreApplication.translate("MainWindow", u"Unir Pdf", None))
        self.SplitPdf_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF:", None))
        self.SplitPdf_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\file.pdf", None))
        self.SplitPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.SplitPdf_Sheetslabel.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.SplitPdf_Sheets.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1,4,7-10", None))
        self.SplitPdf_SaveAll_Button.setText("")
        self.SplitPdf_SaveAlllabel.setText(QCoreApplication.translate("MainWindow", u"Guardar las Dem\u00e1s", None))
        self.SplitPdf_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.SplitPdf_tab), QCoreApplication.translate("MainWindow", u"Separar PDF", None))
        self.ExtractPdf_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF:", None))
        self.ExtractPdf_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\file.pdf", None))
        self.ExtractPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.ExtractPdf_Sheetslabel.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.ExtractPdf_Sheets.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1,4,7-10", None))
        self.ExtractPdf_All_Button.setText("")
        self.ExtractPdf_Alllabel.setText(QCoreApplication.translate("MainWindow", u"Separar Todas", None))
        self.ExtractPdf_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.ExtractPDF_tab), QCoreApplication.translate("MainWindow", u"Extraer Hojas", None))
        self.BlankPdf_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar PDF:", None))
        self.BlankPdf_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\file.pdf", None))
        self.BlankPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.BlankPdf_Sheetslabel.setText(QCoreApplication.translate("MainWindow", u"Hojas:", None))
        self.BlankPdf_Sheets.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1,4,7-10", None))
        self.BlankPdf_Inplace_Button.setText("")
        self.BlankPdf_Inplacelabel.setText(QCoreApplication.translate("MainWindow", u"Sobreescribir Archivo", None))
        self.BlankPdf_Button.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pdf_tabs.setTabText(self.pdf_tabs.indexOf(self.BlankPdf_tab), QCoreApplication.translate("MainWindow", u"Hoja en Blanco", None))
        self.ImgPdf_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Selecciona Im\u00e1genes:", None))
        self.ImgPdf_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\image.png", None))
        self.ImgPdf_selFile.setText(QCoreApplication.translate("MainWindow", u"Selecciona Archivos", None))
        self.ImgPdf_Button.setText(QCoreApplication.translate("MainWindow", u"CONVERTIR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.ImgPdf_tab), QCoreApplication.translate("MainWindow", u"Im\u00e1gen a PDF", None))
        self.PdfImg_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccione PDF's:", None))
        self.PdfImg_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\file.pdf", None))
        self.PdfImg_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivos", None))
        self.PdfImg_Button.setText(QCoreApplication.translate("MainWindow", u"CONVERTIR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.PdfImg_tab), QCoreApplication.translate("MainWindow", u"PDF a Im\u00e1gen", None))
        self.ImgExt_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Imagen:", None))
        self.ImgExt_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\image.jpeg", None))
        self.ImgExt_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.ImgExt_Extlabel.setText(QCoreApplication.translate("MainWindow", u"Extensi\u00f3n:", None))
        self.ImgExt_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u".png", None))
        self.ImgExt_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u".jpeg", None))
        self.ImgExt_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u".gif", None))
        self.ImgExt_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u".bmp", None))
        self.ImgExt_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u".dds", None))
        self.ImgExt_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u".ico", None))
        self.ImgExt_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u".xbm", None))

        self.ImgExt_Button.setText(QCoreApplication.translate("MainWindow", u"CONVERTIR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.ImgExt_tab), QCoreApplication.translate("MainWindow", u"Cambiar Extensi\u00f3n", None))
        self.ImgRsize_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Imagen:", None))
        self.ImgRsize_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\image.png", None))
        self.ImgRsize_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.ImgRsize_Actuallabel_2.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o Actual:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.ImgRsize_Scale_Button.setText(QCoreApplication.translate("MainWindow", u"Escalar", None))
        self.ImgRsize_Inplace_Button.setText(QCoreApplication.translate("MainWindow", u"Sobreescribir Imagen", None))
        self.ImgRsize_Newlabel.setText(QCoreApplication.translate("MainWindow", u"Nueva Dimensi\u00f3n:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.ImgRsize_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.img_tabs.setTabText(self.img_tabs.indexOf(self.ImgRsize_tab), QCoreApplication.translate("MainWindow", u"Redimensionar Imagen", None))
        self.FileRname_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccione Archivos:", None))
        self.FileRname_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivos", None))
        self.FileRname_Templatelabel.setText(QCoreApplication.translate("MainWindow", u"Template:", None))
        self.FileRname_Template.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name_#XXX", None))
        self.FileRname_Numlabel.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Inicial:", None))
        self.FileRname_Button.setText(QCoreApplication.translate("MainWindow", u"RENOMBRAR", None))
        self.file_tabs.setTabText(self.file_tabs.indexOf(self.FileRname_tab), QCoreApplication.translate("MainWindow", u"Renombrar Archivos", None))
        self.VidTag_Inlabel.setText(QCoreApplication.translate("MainWindow", u"Seleccione Carpeta:", None))
        self.VidTag_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\music\\", None))
        self.VidTag_selFile.setText(QCoreApplication.translate("MainWindow", u"Selecciona Archivo", None))
        self.VidTag_Update.setText("")
        self.VidTag_Cover.setText(QCoreApplication.translate("MainWindow", u"cover", None))
        self.VidTag_Titlelabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.VidTag_Title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Never Gonna Give You Up", None))
        self.VidTag_Intrlabel.setText(QCoreApplication.translate("MainWindow", u"Int\u00e9rprete:", None))
        self.VidTag_Intr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rick Astley", None))
        self.VidTag_Alblabel.setText(QCoreApplication.translate("MainWindow", u"\u00c1lbum:", None))
        self.VidTag_Alb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Whenever You Need Somebody", None))
        self.VidTag_Genrelabel.setText(QCoreApplication.translate("MainWindow", u"G\u00e9nero:", None))
        self.VidTag_Yearlabel.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o:", None))
        self.VidTag_Year.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1987/07/28", None))
        self.VidTag_Tracklabel.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Pista:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.VidTag_IntrAlblabel.setText(QCoreApplication.translate("MainWindow", u"Int\u00e9rprete de Album:", None))
        self.VidTag_IntrAlb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rick Astley", None))
        self.VidTag_Complabel.setText(QCoreApplication.translate("MainWindow", u"Compositor:", None))
        self.VidTag_Comp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stock Aitken Waterman", None))
        self.VidTag_Moodlabel.setText(QCoreApplication.translate("MainWindow", u"Mood:", None))
        self.VidTag_Mood.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Graciosa", None))
        self.VidTag_Lyricslabel.setText(QCoreApplication.translate("MainWindow", u"Letra:", None))
        self.VidTag_Button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.vid_tabs.setTabText(self.vid_tabs.indexOf(self.VidTag_tab), QCoreApplication.translate("MainWindow", u"Tag M\u00fasica", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Video a Convertir:", None))
        self.MP3toMP4_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\user\\deskopt\\video.mp4", None))
        self.MP3toMP4_selFile.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Archivo", None))
        self.MP3toMP4_Button.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.vid_tabs.setTabText(self.vid_tabs.indexOf(self.MP3toMP4_tab), QCoreApplication.translate("MainWindow", u"MP4 a MP3", None))
        self.VidDown_Inlabel.setText(QCoreApplication.translate("MainWindow", u"URL del Video:", None))
        self.VidDown_In.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=dQw4w9WgXcQ", None))
        self.VidDown_OnlyAudiolabel.setText(QCoreApplication.translate("MainWindow", u"Solo Audio:", None))
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
        self.VidDown_res.setItemText(8, QCoreApplication.translate("MainWindow", u"Best Resolution", None))

        self.VidDown_Titlelabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo del Video:", None))
        self.VidDown_alllabel.setText(QCoreApplication.translate("MainWindow", u"Descargar Todo:", None))
        self.VidDown_all_checkBox.setText("")
        self.VidDown_listLabel.setText(QCoreApplication.translate("MainWindow", u"Lista de Videos:", None))
        self.VidDown_Thumb.setText(QCoreApplication.translate("MainWindow", u"IMG", None))
        self.VidDown_durLabel.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n:", None))
        self.VidDown_sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o:", None))
        self.VidDown_Button.setText(QCoreApplication.translate("MainWindow", u"DESCARGAR", None))
        self.vid_tabs.setTabText(self.vid_tabs.indexOf(self.VidDown), QCoreApplication.translate("MainWindow", u"Descargar Internet", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Python + PySide6", None))
    # retranslateUi
