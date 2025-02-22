# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowWgZAMm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(67, 67, 67);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_file_1 = QLabel(self.frame)
        self.label_file_1.setObjectName(u"label_file_1")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_file_1.setFont(font)
        self.label_file_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_file_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_file_1, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_id_1 = QLabel(self.frame)
        self.label_id_1.setObjectName(u"label_id_1")
        self.label_id_1.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.label_id_1.setFont(font1)
        self.label_id_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_id_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_id_1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.spinBox_1 = QSpinBox(self.frame)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setMaximumSize(QSize(120, 120))
        self.spinBox_1.setFont(font)
        self.spinBox_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox_1.setStyleSheet(u"QSpinBox {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.spinBox_1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.Graph_widget_1 = QWidget(self.frame)
        self.Graph_widget_1.setObjectName(u"Graph_widget_1")
        self.Graph_widget_1.setMinimumSize(QSize(512, 512))
        self.Graph_widget_1.setMaximumSize(QSize(512, 512))

        self.verticalLayout.addWidget(self.Graph_widget_1)

        self.horizontalSlider_1 = QSlider(self.frame)
        self.horizontalSlider_1.setObjectName(u"horizontalSlider_1")
        self.horizontalSlider_1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.79, x2:0.909, y2:0.784091, stop:0 rgba(103, 111, 122, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin: 2px 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.horizontalSlider_1.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_1)

        self.pushButton_load_1 = QPushButton(self.frame)
        self.pushButton_load_1.setObjectName(u"pushButton_load_1")
        self.pushButton_load_1.setFont(font)
        self.pushButton_load_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_load_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 31, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color:rgb(20, 22, 25)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(41, 46, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(33, 37, 42);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_load_1)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_file_2 = QLabel(self.frame_2)
        self.label_file_2.setObjectName(u"label_file_2")
        self.label_file_2.setFont(font)
        self.label_file_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_file_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_file_2, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_id_2 = QLabel(self.frame_2)
        self.label_id_2.setObjectName(u"label_id_2")
        self.label_id_2.setFont(font)
        self.label_id_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border-radius: 10px;")
        self.label_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_id_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.spinBox_2 = QSpinBox(self.frame_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet(u"QSpinBox {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.spinBox_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.Graph_widget_2 = QWidget(self.frame_2)
        self.Graph_widget_2.setObjectName(u"Graph_widget_2")
        self.Graph_widget_2.setMinimumSize(QSize(512, 512))
        self.Graph_widget_2.setMaximumSize(QSize(512, 512))

        self.verticalLayout_2.addWidget(self.Graph_widget_2)

        self.horizontalSlider_2 = QSlider(self.frame_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.79, x2:0.909, y2:0.784091, stop:0 rgba(103, 111, 122, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin: 2px 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_2)

        self.pushButton_load_2 = QPushButton(self.frame_2)
        self.pushButton_load_2.setObjectName(u"pushButton_load_2")
        self.pushButton_load_2.setFont(font)
        self.pushButton_load_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_load_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 31, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color:rgb(20, 22, 25)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(41, 46, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(33, 37, 42);\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_load_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_mask = QPushButton(self.frame_3)
        self.pushButton_mask.setObjectName(u"pushButton_mask")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.pushButton_mask.setFont(font2)
        self.pushButton_mask.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 31, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color:rgb(20, 22, 25)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(41, 46, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(33, 37, 42);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_mask)


        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_file_1.setText(QCoreApplication.translate("MainWindow", u"patient_23.nii", None))
        self.label_id_1.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.pushButton_load_1.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.label_file_2.setText(QCoreApplication.translate("MainWindow", u"patient_23_1.nii", None))
        self.label_id_2.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.pushButton_load_2.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.pushButton_mask.setText(QCoreApplication.translate("MainWindow", u"Load masks", None))
    # retranslateUi

