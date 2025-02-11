# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: #DBDBDB;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layout = QFrame(self.centralwidget)
        self.layout.setObjectName(u"layout")
        self.layout.setMinimumSize(QSize(275, 300))
        self.layout.setStyleSheet(u"background: #FFFFFF;\n"
"box-shadow: 6px 6px 9px rgba(0, 0, 0, 0.44);\n"
"border-radius: 19px;\n"
"")
        self.layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_login = QLabel(self.layout)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;")
        self.txt_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_login)

        self.layout_user = QFrame(self.layout)
        self.layout_user.setObjectName(u"layout_user")
        self.layout_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_user.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.layout_user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_user = QLineEdit(self.layout_user)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid black;\n"
"background: transparent;")

        self.verticalLayout_2.addWidget(self.input_user)


        self.verticalLayout_3.addWidget(self.layout_user)

        self.layout_senha = QFrame(self.layout)
        self.layout_senha.setObjectName(u"layout_senha")
        self.layout_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.layout_senha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_senha = QLineEdit(self.layout_senha)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid black;\n"
"background: transparent;")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.input_senha)


        self.verticalLayout_3.addWidget(self.layout_senha)

        self.btn_login = QPushButton(self.layout)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"width: 100px;\n"
"height: 30px;\n"
"\n"
"background: #D9D9D9;\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.35);\n"
"border-radius: 11px;\n"
"font-weight: medium;\n"
"")

        self.verticalLayout_3.addWidget(self.btn_login, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.layout, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.input_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

