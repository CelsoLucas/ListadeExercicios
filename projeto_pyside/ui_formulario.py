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
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt__formulario = QLabel(self.centralwidget)
        self.txt__formulario.setObjectName(u"txt__formulario")
        self.txt__formulario.setStyleSheet(u"font-size: 26px;")
        self.txt__formulario.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.txt__formulario, 0, 0, 1, 1)

        self.btn_enviar_formulario = QPushButton(self.centralwidget)
        self.btn_enviar_formulario.setObjectName(u"btn_enviar_formulario")

        self.gridLayout.addWidget(self.btn_enviar_formulario, 2, 0, 1, 1)

        self.layout = QFrame(self.centralwidget)
        self.layout.setObjectName(u"layout")
        self.layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.layout)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.layout_senha = QFrame(self.layout)
        self.layout_senha.setObjectName(u"layout_senha")
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

        self.txt_repetir_senha = QLabel(self.layout_senha)
        self.txt_repetir_senha.setObjectName(u"txt_repetir_senha")

        self.verticalLayout_4.addWidget(self.txt_repetir_senha)

        self.input_senha_2 = QLineEdit(self.layout_senha)
        self.input_senha_2.setObjectName(u"input_senha_2")
        self.input_senha_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.input_senha_2)


        self.gridLayout_2.addWidget(self.layout_senha, 1, 1, 2, 1)

        self.layout_data_contratacao = QFrame(self.layout)
        self.layout_data_contratacao.setObjectName(u"layout_data_contratacao")
        self.layout_data_contratacao.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_data_contratacao.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.layout_data_contratacao)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.txt_data_contratacao = QLabel(self.layout_data_contratacao)
        self.txt_data_contratacao.setObjectName(u"txt_data_contratacao")

        self.verticalLayout_11.addWidget(self.txt_data_contratacao)

        self.dateEdit_contratacao = QDateEdit(self.layout_data_contratacao)
        self.dateEdit_contratacao.setObjectName(u"dateEdit_contratacao")

        self.verticalLayout_11.addWidget(self.dateEdit_contratacao)


        self.gridLayout_2.addWidget(self.layout_data_contratacao, 4, 0, 1, 1)

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
        self.checkBox_opc_1 = QCheckBox(self.layout_sexo_opc)
        self.checkBox_opc_1.setObjectName(u"checkBox_opc_1")

        self.horizontalLayout_2.addWidget(self.checkBox_opc_1)

        self.checkBox_opc_4 = QCheckBox(self.layout_sexo_opc)
        self.checkBox_opc_4.setObjectName(u"checkBox_opc_4")

        self.horizontalLayout_2.addWidget(self.checkBox_opc_4)

        self.checkBox_opc_3 = QCheckBox(self.layout_sexo_opc)
        self.checkBox_opc_3.setObjectName(u"checkBox_opc_3")

        self.horizontalLayout_2.addWidget(self.checkBox_opc_3)


        self.verticalLayout_6.addWidget(self.layout_sexo_opc)


        self.gridLayout_2.addWidget(self.layout_sexo, 5, 0, 1, 1)

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
        self.radio_botao2 = QRadioButton(self.layout_cargo_opc)
        self.radio_botao2.setObjectName(u"radio_botao2")

        self.horizontalLayout.addWidget(self.radio_botao2)

        self.radio_botao1 = QRadioButton(self.layout_cargo_opc)
        self.radio_botao1.setObjectName(u"radio_botao1")

        self.horizontalLayout.addWidget(self.radio_botao1)


        self.verticalLayout_5.addWidget(self.layout_cargo_opc)


        self.gridLayout_2.addWidget(self.layout_cargo, 2, 0, 1, 1)

        self.layout_idade = QFrame(self.layout)
        self.layout_idade.setObjectName(u"layout_idade")
        self.layout_idade.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_idade.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.layout_idade)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.txt_idade = QLabel(self.layout_idade)
        self.txt_idade.setObjectName(u"txt_idade")

        self.verticalLayout_7.addWidget(self.txt_idade)

        self.spinBox_idade = QSpinBox(self.layout_idade)
        self.spinBox_idade.setObjectName(u"spinBox_idade")

        self.verticalLayout_7.addWidget(self.spinBox_idade)


        self.gridLayout_2.addWidget(self.layout_idade, 1, 0, 1, 1)

        self.layout_obs = QFrame(self.layout)
        self.layout_obs.setObjectName(u"layout_obs")
        self.layout_obs.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_obs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.layout_obs)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_obs = QLabel(self.layout_obs)
        self.txt_obs.setObjectName(u"txt_obs")

        self.verticalLayout_8.addWidget(self.txt_obs)

        self.txtedit_obs = QTextEdit(self.layout_obs)
        self.txtedit_obs.setObjectName(u"txtedit_obs")

        self.verticalLayout_8.addWidget(self.txtedit_obs)


        self.gridLayout_2.addWidget(self.layout_obs, 8, 1, 1, 1)

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

        self.layout_salario = QFrame(self.layout)
        self.layout_salario.setObjectName(u"layout_salario")
        self.layout_salario.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_salario.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.layout_salario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.txt_salario = QLabel(self.layout_salario)
        self.txt_salario.setObjectName(u"txt_salario")

        self.verticalLayout_9.addWidget(self.txt_salario)

        self.doubleSpinBox = QDoubleSpinBox(self.layout_salario)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMaximum(1000000.000000000000000)
        self.doubleSpinBox.setValue(0.000000000000000)

        self.verticalLayout_9.addWidget(self.doubleSpinBox)


        self.gridLayout_2.addWidget(self.layout_salario, 4, 1, 1, 1)

        self.layout_periodo = QFrame(self.layout)
        self.layout_periodo.setObjectName(u"layout_periodo")
        self.layout_periodo.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_periodo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.layout_periodo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_periodo = QLabel(self.layout_periodo)
        self.txt_periodo.setObjectName(u"txt_periodo")

        self.verticalLayout_10.addWidget(self.txt_periodo)

        self.comboBox_periodo = QComboBox(self.layout_periodo)
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.setObjectName(u"comboBox_periodo")

        self.verticalLayout_10.addWidget(self.comboBox_periodo)


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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.layout_data_nasc, 8, 0, 1, 1)


        self.gridLayout.addWidget(self.layout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt__formulario.setText(QCoreApplication.translate("MainWindow", u"Formulario", None))
        self.btn_enviar_formulario.setText(QCoreApplication.translate("MainWindow", u"Enviar Formulario", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_repetir_senha.setText(QCoreApplication.translate("MainWindow", u"Repetir Senha", None))
        self.txt_data_contratacao.setText(QCoreApplication.translate("MainWindow", u"Data da Contrata\u00e7\u00e3o", None))
        self.txt_sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.checkBox_opc_1.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.checkBox_opc_4.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.checkBox_opc_3.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.txt_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_nome.setPlaceholderText("")
        self.txt_cargo.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.radio_botao2.setText(QCoreApplication.translate("MainWindow", u"ADM", None))
        self.radio_botao1.setText(QCoreApplication.translate("MainWindow", u"FUNCIONARIO", None))
        self.txt_idade.setText(QCoreApplication.translate("MainWindow", u"Idade", None))
        self.txt_obs.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o", None))
        self.txt_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.input_email.setPlaceholderText("")
        self.txt_salario.setText(QCoreApplication.translate("MainWindow", u"Salario", None))
        self.txt_periodo.setText(QCoreApplication.translate("MainWindow", u"Periodo", None))
        self.comboBox_periodo.setItemText(0, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.comboBox_periodo.setItemText(1, QCoreApplication.translate("MainWindow", u"Vespertino", None))
        self.comboBox_periodo.setItemText(2, QCoreApplication.translate("MainWindow", u"Noturno", None))
        self.comboBox_periodo.setItemText(3, QCoreApplication.translate("MainWindow", u"Matutino e Vespertino", None))

        self.txt_data_nasc.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
    # retranslateUi

