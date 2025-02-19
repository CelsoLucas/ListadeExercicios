# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_formulario.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_tela_formulario(object):
    def setupUi(self, tela_formulario):
        if not tela_formulario.objectName():
            tela_formulario.setObjectName(u"tela_formulario")
        tela_formulario.resize(800, 706)
        self.centralwidget = QWidget(tela_formulario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt__formulario = QLabel(self.centralwidget)
        self.txt__formulario.setObjectName(u"txt__formulario")
        self.txt__formulario.setStyleSheet(u"font-size: 26px;")
        self.txt__formulario.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.txt__formulario, 0, 0, 1, 1)

        self.btn_enviar_formulario = QPushButton(self.centralwidget)
        self.btn_enviar_formulario.setObjectName(u"btn_enviar_formulario")
        self.btn_enviar_formulario.setStyleSheet(u"background-color: rgb(244, 244, 244);")

        self.gridLayout.addWidget(self.btn_enviar_formulario, 2, 0, 1, 1)

        self.layout = QFrame(self.centralwidget)
        self.layout.setObjectName(u"layout")
        self.layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.layout)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.layout_email = QFrame(self.layout)
        self.layout_email.setObjectName(u"layout_email")
        self.layout_email.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_email.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.layout_email)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_email = QLabel(self.layout_email)
        self.txt_email.setObjectName(u"txt_email")

        self.verticalLayout_2.addWidget(self.txt_email)

        self.input_email = QLineEdit(self.layout_email)
        self.input_email.setObjectName(u"input_email")

        self.verticalLayout_2.addWidget(self.input_email)


        self.gridLayout_2.addWidget(self.layout_email, 0, 1, 1, 1)

        self.layout_cargo = QFrame(self.layout)
        self.layout_cargo.setObjectName(u"layout_cargo")
        self.layout_cargo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_cargo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.layout_cargo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.txt_cargo = QLabel(self.layout_cargo)
        self.txt_cargo.setObjectName(u"txt_cargo")

        self.verticalLayout_5.addWidget(self.txt_cargo)

        self.layout_cargo_opc = QFrame(self.layout_cargo)
        self.layout_cargo_opc.setObjectName(u"layout_cargo_opc")
        self.layout_cargo_opc.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_cargo_opc.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.layout_cargo_opc)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_cargo_adm = QRadioButton(self.layout_cargo_opc)
        self.input_cargo_adm.setObjectName(u"input_cargo_adm")

        self.horizontalLayout.addWidget(self.input_cargo_adm)

        self.input_cargo_func = QRadioButton(self.layout_cargo_opc)
        self.input_cargo_func.setObjectName(u"input_cargo_func")

        self.horizontalLayout.addWidget(self.input_cargo_func)


        self.verticalLayout_5.addWidget(self.layout_cargo_opc)


        self.gridLayout_2.addWidget(self.layout_cargo, 6, 0, 2, 1)

        self.layout_cpf = QFrame(self.layout)
        self.layout_cpf.setObjectName(u"layout_cpf")
        self.layout_cpf.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_cpf.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.layout_cpf)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.txt_cpf = QLabel(self.layout_cpf)
        self.txt_cpf.setObjectName(u"txt_cpf")

        self.verticalLayout_12.addWidget(self.txt_cpf)

        self.input_cpf = QLineEdit(self.layout_cpf)
        self.input_cpf.setObjectName(u"input_cpf")
        self.input_cpf.setMaxLength(14)

        self.verticalLayout_12.addWidget(self.input_cpf)


        self.gridLayout_2.addWidget(self.layout_cpf, 1, 0, 1, 1)

        self.layout_sexo = QFrame(self.layout)
        self.layout_sexo.setObjectName(u"layout_sexo")
        self.layout_sexo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_sexo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.layout_sexo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.txt_sexo = QLabel(self.layout_sexo)
        self.txt_sexo.setObjectName(u"txt_sexo")

        self.verticalLayout_6.addWidget(self.txt_sexo)

        self.layout_sexo_opc = QFrame(self.layout_sexo)
        self.layout_sexo_opc.setObjectName(u"layout_sexo_opc")
        self.layout_sexo_opc.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_sexo_opc.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.layout_sexo_opc)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sexo_opc_m = QCheckBox(self.layout_sexo_opc)
        self.sexo_opc_m.setObjectName(u"sexo_opc_m")
        self.sexo_opc_m.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.sexo_opc_m)

        self.sexo_opc_f = QCheckBox(self.layout_sexo_opc)
        self.sexo_opc_f.setObjectName(u"sexo_opc_f")
        self.sexo_opc_f.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.sexo_opc_f)

        self.sexo_opc_o = QCheckBox(self.layout_sexo_opc)
        self.sexo_opc_o.setObjectName(u"sexo_opc_o")
        self.sexo_opc_o.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.sexo_opc_o)


        self.verticalLayout_6.addWidget(self.layout_sexo_opc)


        self.gridLayout_2.addWidget(self.layout_sexo, 6, 1, 1, 1)

        self.layout_nome = QFrame(self.layout)
        self.layout_nome.setObjectName(u"layout_nome")
        self.layout_nome.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_nome.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.layout_nome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_nome = QLabel(self.layout_nome)
        self.txt_nome.setObjectName(u"txt_nome")

        self.verticalLayout.addWidget(self.txt_nome)

        self.input_nome = QLineEdit(self.layout_nome)
        self.input_nome.setObjectName(u"input_nome")

        self.verticalLayout.addWidget(self.input_nome)


        self.gridLayout_2.addWidget(self.layout_nome, 0, 0, 1, 1)

        self.layout_data_contratacao = QFrame(self.layout)
        self.layout_data_contratacao.setObjectName(u"layout_data_contratacao")
        self.layout_data_contratacao.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_data_contratacao.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.layout_data_contratacao)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.txt_data_contratacao = QLabel(self.layout_data_contratacao)
        self.txt_data_contratacao.setObjectName(u"txt_data_contratacao")

        self.verticalLayout_11.addWidget(self.txt_data_contratacao)

        self.input_data_contratacao = QDateEdit(self.layout_data_contratacao)
        self.input_data_contratacao.setObjectName(u"input_data_contratacao")

        self.verticalLayout_11.addWidget(self.input_data_contratacao)


        self.gridLayout_2.addWidget(self.layout_data_contratacao, 5, 0, 1, 1)

        self.layout_senha = QFrame(self.layout)
        self.layout_senha.setObjectName(u"layout_senha")
        self.layout_senha.setMaximumSize(QSize(16777215, 150))
        self.layout_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.layout_senha)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_senha = QLabel(self.layout_senha)
        self.txt_senha.setObjectName(u"txt_senha")

        self.verticalLayout_4.addWidget(self.txt_senha)

        self.input_senha = QLineEdit(self.layout_senha)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.input_senha)


        self.gridLayout_2.addWidget(self.layout_senha, 1, 1, 1, 1)

        self.layout_periodo = QFrame(self.layout)
        self.layout_periodo.setObjectName(u"layout_periodo")
        self.layout_periodo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_periodo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.layout_periodo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_periodo = QLabel(self.layout_periodo)
        self.txt_periodo.setObjectName(u"txt_periodo")

        self.verticalLayout_10.addWidget(self.txt_periodo)

        self.input_periodo = QComboBox(self.layout_periodo)
        self.input_periodo.addItem("")
        self.input_periodo.addItem("")
        self.input_periodo.addItem("")
        self.input_periodo.addItem("")
        self.input_periodo.setObjectName(u"input_periodo")

        self.verticalLayout_10.addWidget(self.input_periodo)


        self.gridLayout_2.addWidget(self.layout_periodo, 5, 1, 1, 1)

        self.layout_data_nasc = QFrame(self.layout)
        self.layout_data_nasc.setObjectName(u"layout_data_nasc")
        self.layout_data_nasc.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_data_nasc.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.layout_data_nasc)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_data_nasc = QLabel(self.layout_data_nasc)
        self.txt_data_nasc.setObjectName(u"txt_data_nasc")

        self.verticalLayout_3.addWidget(self.txt_data_nasc)

        self.input_data_nasc = QDateEdit(self.layout_data_nasc)
        self.input_data_nasc.setObjectName(u"input_data_nasc")

        self.verticalLayout_3.addWidget(self.input_data_nasc)


        self.gridLayout_2.addWidget(self.layout_data_nasc, 8, 0, 1, 1)

        self.layout_salario = QFrame(self.layout)
        self.layout_salario.setObjectName(u"layout_salario")
        self.layout_salario.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_salario.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.layout_salario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.txt_salario = QLabel(self.layout_salario)
        self.txt_salario.setObjectName(u"txt_salario")

        self.verticalLayout_9.addWidget(self.txt_salario)

        self.input_salario = QDoubleSpinBox(self.layout_salario)
        self.input_salario.setObjectName(u"input_salario")
        self.input_salario.setDecimals(2)
        self.input_salario.setMaximum(1000000.000000000000000)
        self.input_salario.setValue(0.000000000000000)

        self.verticalLayout_9.addWidget(self.input_salario)


        self.gridLayout_2.addWidget(self.layout_salario, 2, 1, 1, 1)

        self.layout_idade = QFrame(self.layout)
        self.layout_idade.setObjectName(u"layout_idade")
        self.layout_idade.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_idade.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.layout_idade)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.txt_idade = QLabel(self.layout_idade)
        self.txt_idade.setObjectName(u"txt_idade")

        self.verticalLayout_7.addWidget(self.txt_idade)

        self.input_idade = QSpinBox(self.layout_idade)
        self.input_idade.setObjectName(u"input_idade")

        self.verticalLayout_7.addWidget(self.input_idade)


        self.gridLayout_2.addWidget(self.layout_idade, 2, 0, 1, 1)

        self.layout_obs = QFrame(self.layout)
        self.layout_obs.setObjectName(u"layout_obs")
        self.layout_obs.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_obs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.layout_obs)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_obs = QLabel(self.layout_obs)
        self.txt_obs.setObjectName(u"txt_obs")

        self.verticalLayout_8.addWidget(self.txt_obs)

        self.input_obs = QTextEdit(self.layout_obs)
        self.input_obs.setObjectName(u"input_obs")

        self.verticalLayout_8.addWidget(self.input_obs)


        self.gridLayout_2.addWidget(self.layout_obs, 9, 0, 1, 1)

        self.layout_adc_foto = QFrame(self.layout)
        self.layout_adc_foto.setObjectName(u"layout_adc_foto")
        self.layout_adc_foto.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_adc_foto.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.layout_adc_foto)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.txt_adc_foto = QLabel(self.layout_adc_foto)
        self.txt_adc_foto.setObjectName(u"txt_adc_foto")

        self.verticalLayout_13.addWidget(self.txt_adc_foto)

        self.btn_procurar_arquivo = QPushButton(self.layout_adc_foto)
        self.btn_procurar_arquivo.setObjectName(u"btn_procurar_arquivo")

        self.verticalLayout_13.addWidget(self.btn_procurar_arquivo)

        self.layout_img = QLabel(self.layout_adc_foto)
        self.layout_img.setObjectName(u"layout_img")

        self.verticalLayout_13.addWidget(self.layout_img)


        self.gridLayout_2.addWidget(self.layout_adc_foto, 8, 1, 1, 1)


        self.gridLayout.addWidget(self.layout, 1, 0, 1, 1)

        tela_formulario.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_formulario)

        QMetaObject.connectSlotsByName(tela_formulario)
    # setupUi

    def retranslateUi(self, tela_formulario):
        tela_formulario.setWindowTitle(QCoreApplication.translate("tela_formulario", u"MainWindow", None))
        self.txt__formulario.setText(QCoreApplication.translate("tela_formulario", u"Formulario", None))
        self.btn_enviar_formulario.setText(QCoreApplication.translate("tela_formulario", u"Enviar Formulario", None))
        self.txt_email.setText(QCoreApplication.translate("tela_formulario", u"Email", None))
        self.input_email.setPlaceholderText("")
        self.txt_cargo.setText(QCoreApplication.translate("tela_formulario", u"Cargo", None))
        self.input_cargo_adm.setText(QCoreApplication.translate("tela_formulario", u"ADM", None))
        self.input_cargo_func.setText(QCoreApplication.translate("tela_formulario", u"FUNCIONARIO", None))
        self.txt_cpf.setText(QCoreApplication.translate("tela_formulario", u"CPF", None))
        self.input_cpf.setInputMask(QCoreApplication.translate("tela_formulario", u"000.000.000-00", None))
        self.input_cpf.setText(QCoreApplication.translate("tela_formulario", u"..-", None))
        self.txt_sexo.setText(QCoreApplication.translate("tela_formulario", u"Sexo", None))
        self.sexo_opc_m.setText(QCoreApplication.translate("tela_formulario", u"Masculino", None))
        self.sexo_opc_f.setText(QCoreApplication.translate("tela_formulario", u"Feminino", None))
        self.sexo_opc_o.setText(QCoreApplication.translate("tela_formulario", u"Outro", None))
        self.txt_nome.setText(QCoreApplication.translate("tela_formulario", u"Nome de Usuario", None))
        self.input_nome.setPlaceholderText("")
        self.txt_data_contratacao.setText(QCoreApplication.translate("tela_formulario", u"Data da Contrata\u00e7\u00e3o", None))
        self.txt_senha.setText(QCoreApplication.translate("tela_formulario", u"Senha", None))
        self.txt_periodo.setText(QCoreApplication.translate("tela_formulario", u"Periodo", None))
        self.input_periodo.setItemText(0, QCoreApplication.translate("tela_formulario", u"Matutino", None))
        self.input_periodo.setItemText(1, QCoreApplication.translate("tela_formulario", u"Vespertino", None))
        self.input_periodo.setItemText(2, QCoreApplication.translate("tela_formulario", u"Noturno", None))
        self.input_periodo.setItemText(3, QCoreApplication.translate("tela_formulario", u"Matutino e Vespertino", None))

        self.txt_data_nasc.setText(QCoreApplication.translate("tela_formulario", u"Data de Nascimento", None))
        self.txt_salario.setText(QCoreApplication.translate("tela_formulario", u"Salario", None))
        self.txt_idade.setText(QCoreApplication.translate("tela_formulario", u"Idade", None))
        self.txt_obs.setText(QCoreApplication.translate("tela_formulario", u"Observa\u00e7\u00e3o", None))
        self.txt_adc_foto.setText(QCoreApplication.translate("tela_formulario", u"Adicionar Foto", None))
        self.btn_procurar_arquivo.setText(QCoreApplication.translate("tela_formulario", u"Porcurar Arquivo", None))
        self.layout_img.setText("")
    # retranslateUi

