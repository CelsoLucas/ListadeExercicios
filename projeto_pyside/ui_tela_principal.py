# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(219, 219, 219);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout = QFrame(self.centralwidget)
        self.layout.setObjectName(u"layout")
        self.layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.layout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_menu = QFrame(self.layout)
        self.layout_menu.setObjectName(u"layout_menu")
        self.layout_menu.setMaximumSize(QSize(16777215, 80))
        self.layout_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.layout_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_logo = QFrame(self.layout_menu)
        self.layout_logo.setObjectName(u"layout_logo")
        self.layout_logo.setMaximumSize(QSize(200, 170))
        self.layout_logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_logo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.layout_logo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.txt_logo_aqui = QLabel(self.layout_logo)
        self.txt_logo_aqui.setObjectName(u"txt_logo_aqui")
        self.txt_logo_aqui.setMaximumSize(QSize(200, 200))
        self.txt_logo_aqui.setStyleSheet(u"font-size: 26px;\n"
"")

        self.verticalLayout_5.addWidget(self.txt_logo_aqui, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout.addWidget(self.layout_logo)

        self.espaco_menu = QSpacerItem(1200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.espaco_menu)

        self.layout_nome = QFrame(self.layout_menu)
        self.layout_nome.setObjectName(u"layout_nome")
        self.layout_nome.setMaximumSize(QSize(180, 16777215))
        self.layout_nome.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_nome.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.layout_nome)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_nome = QLabel(self.layout_nome)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"font-size: 22px;")

        self.horizontalLayout_2.addWidget(self.txt_nome)


        self.horizontalLayout.addWidget(self.layout_nome)

        self.layout_sair = QFrame(self.layout_menu)
        self.layout_sair.setObjectName(u"layout_sair")
        self.layout_sair.setMaximumSize(QSize(160, 50))
        self.layout_sair.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_sair.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.layout_sair)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_sair = QPushButton(self.layout_sair)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMaximumSize(QSize(160, 50))
        self.btn_sair.setStyleSheet(u"font-size: 20px;\n"
"background: #FFFFFF;\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout_3.addWidget(self.btn_sair)


        self.horizontalLayout.addWidget(self.layout_sair)


        self.verticalLayout_2.addWidget(self.layout_menu)

        self.layout_tela_principal = QFrame(self.layout)
        self.layout_tela_principal.setObjectName(u"layout_tela_principal")
        self.layout_tela_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_tela_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.layout_tela_principal)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.layout_botoes_menu = QFrame(self.layout_tela_principal)
        self.layout_botoes_menu.setObjectName(u"layout_botoes_menu")
        self.layout_botoes_menu.setMaximumSize(QSize(280, 1677))
        self.layout_botoes_menu.setStyleSheet(u"font-family: 24px;")
        self.layout_botoes_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_botoes_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.layout_botoes_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_tela_principal = QPushButton(self.layout_botoes_menu)
        self.btn_tela_principal.setObjectName(u"btn_tela_principal")
        self.btn_tela_principal.setMaximumSize(QSize(325, 60))
        self.btn_tela_principal.setStyleSheet(u"background: #FFFFFF;\n"
"box-shadow: 5px 5px 2px rgba(0, 0, 0, 0.4);\n"
"border-radius: 10px;\n"
"font-size: 22px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_tela_principal)

        self.btn_pvd = QPushButton(self.layout_botoes_menu)
        self.btn_pvd.setObjectName(u"btn_pvd")
        self.btn_pvd.setMaximumSize(QSize(315, 60))
        self.btn_pvd.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 22px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_pvd)

        self.btn_estoque = QPushButton(self.layout_botoes_menu)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMaximumSize(QSize(315, 60))
        self.btn_estoque.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 22px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_estoque)

        self.btn_clientes = QPushButton(self.layout_botoes_menu)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMaximumSize(QSize(315, 60))
        self.btn_clientes.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 22px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_clientes)

        self.btn_relatorios = QPushButton(self.layout_botoes_menu)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        self.btn_relatorios.setMaximumSize(QSize(315, 60))
        self.btn_relatorios.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 22px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_relatorios)

        self.btn_configuracoes = QPushButton(self.layout_botoes_menu)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        self.btn_configuracoes.setMaximumSize(QSize(315, 60))
        self.btn_configuracoes.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-size: 22px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_configuracoes)


        self.horizontalLayout_3.addWidget(self.layout_botoes_menu)

        self.espaco_botoes_info = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.espaco_botoes_info)

        self.layout_info_principal = QFrame(self.layout_tela_principal)
        self.layout_info_principal.setObjectName(u"layout_info_principal")
        self.layout_info_principal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.layout_info_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_info_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.layout_info_principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 3, 4, 1, 1)

        self.layout_vendas_semana = QFrame(self.layout_info_principal)
        self.layout_vendas_semana.setObjectName(u"layout_vendas_semana")
        self.layout_vendas_semana.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(219, 219, 219);")
        self.layout_vendas_semana.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_vendas_semana.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.layout_vendas_semana)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.txt_vendas_semana = QLabel(self.layout_vendas_semana)
        self.txt_vendas_semana.setObjectName(u"txt_vendas_semana")
        self.txt_vendas_semana.setStyleSheet(u"font-size: 22px;")

        self.verticalLayout_7.addWidget(self.txt_vendas_semana, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_vendas_semana_bd = QLabel(self.layout_vendas_semana)
        self.txt_vendas_semana_bd.setObjectName(u"txt_vendas_semana_bd")

        self.verticalLayout_7.addWidget(self.txt_vendas_semana_bd)


        self.gridLayout.addWidget(self.layout_vendas_semana, 1, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 3, 0, 1, 1)

        self.layout_produtos_baixo_estoque = QFrame(self.layout_info_principal)
        self.layout_produtos_baixo_estoque.setObjectName(u"layout_produtos_baixo_estoque")
        self.layout_produtos_baixo_estoque.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_produtos_baixo_estoque.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_produtos_baixo_estoque.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.layout_produtos_baixo_estoque)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.layout_produtos_baixo_estoque)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size:22px;")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.txt_produtos_baixo_estoque_bd = QLabel(self.layout_produtos_baixo_estoque)
        self.txt_produtos_baixo_estoque_bd.setObjectName(u"txt_produtos_baixo_estoque_bd")

        self.gridLayout_2.addWidget(self.txt_produtos_baixo_estoque_bd, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.layout_produtos_baixo_estoque, 3, 1, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.layout_vendas_dia = QFrame(self.layout_info_principal)
        self.layout_vendas_dia.setObjectName(u"layout_vendas_dia")
        self.layout_vendas_dia.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_vendas_dia.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_vendas_dia.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.layout_vendas_dia)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.txt_vendas_dia = QLabel(self.layout_vendas_dia)
        self.txt_vendas_dia.setObjectName(u"txt_vendas_dia")
        self.txt_vendas_dia.setStyleSheet(u"font-size: 22px;")

        self.verticalLayout_6.addWidget(self.txt_vendas_dia, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_vendas_dia_bd = QLabel(self.layout_vendas_dia)
        self.txt_vendas_dia_bd.setObjectName(u"txt_vendas_dia_bd")

        self.verticalLayout_6.addWidget(self.txt_vendas_dia_bd)


        self.gridLayout.addWidget(self.layout_vendas_dia, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.layout_vendas_mes = QFrame(self.layout_info_principal)
        self.layout_vendas_mes.setObjectName(u"layout_vendas_mes")
        self.layout_vendas_mes.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border-radius: 20px;")
        self.layout_vendas_mes.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_vendas_mes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.layout_vendas_mes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_vendas_mes = QLabel(self.layout_vendas_mes)
        self.txt_vendas_mes.setObjectName(u"txt_vendas_mes")
        self.txt_vendas_mes.setStyleSheet(u"font-size: 22px;")

        self.verticalLayout_8.addWidget(self.txt_vendas_mes, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.txt_vendas_mes_bd = QLabel(self.layout_vendas_mes)
        self.txt_vendas_mes_bd.setObjectName(u"txt_vendas_mes_bd")

        self.verticalLayout_8.addWidget(self.txt_vendas_mes_bd)


        self.gridLayout.addWidget(self.layout_vendas_mes, 1, 3, 1, 1)


        self.horizontalLayout_3.addWidget(self.layout_info_principal)


        self.verticalLayout_2.addWidget(self.layout_tela_principal)


        self.verticalLayout.addWidget(self.layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_logo_aqui.setText(QCoreApplication.translate("MainWindow", u"Logo Aqui", None))
        self.txt_nome.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, Funcionario", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_tela_principal.setText(QCoreApplication.translate("MainWindow", u" Tela Principal", None))
        self.btn_pvd.setText(QCoreApplication.translate("MainWindow", u"PVD", None))
        self.btn_estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.btn_relatorios.setText(QCoreApplication.translate("MainWindow", u"RELATORIOS", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES", None))
        self.txt_vendas_semana.setText(QCoreApplication.translate("MainWindow", u"Vendas da Semana", None))
        self.txt_vendas_semana_bd.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Produtos com Baixo Estoque", None))
        self.txt_produtos_baixo_estoque_bd.setText(QCoreApplication.translate("MainWindow", u"txt", None))
        self.txt_vendas_dia.setText(QCoreApplication.translate("MainWindow", u"Vendas do Dia", None))
        self.txt_vendas_dia_bd.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.txt_vendas_mes.setText(QCoreApplication.translate("MainWindow", u"Vendas do M\u00eas", None))
        self.txt_vendas_mes_bd.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

