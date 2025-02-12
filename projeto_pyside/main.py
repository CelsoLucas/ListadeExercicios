from ui_tela_login import Ui_MainWindow
from ui_formulario import Ui_tela_formulario
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import mysql.connector

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.conexao = mysql.connector.connect(host="localhost",
                                               user="suporte",
                                               password="suporte",
                                               database="ex001"
                                               )
        self.tela_login = Ui_MainWindow()
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def check_login(self):
        cursor = self.conexao.cursor()
        comando = f"select usuario, senha from usuarios where usuario = '{self.tela_login.input_user.text()}'"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        self.conexao.commit()
        
        if not resultado:
            QMessageBox.warning(self, "Erro", "Usuário inválido!")
        else:
            if self.tela_login.input_senha.text() != resultado[0][1]:
                QMessageBox.warning(self, "Erro", "Senha inválida!")
            else:
                QMessageBox.information(self, "Sucesso", f"Bem-vindo, {self.tela_login.input_user.text()}!")
                self.tela_formulario = Ui_tela_formulario()
                self.tela_formulario.setupUi(self)
  
    def tela_login(self):
        nome_usu = self.tela_formulario.input_nome.text()
        senha = self.tela_formulario.input_senha.text()
        cpf = self.tela_formulario.input_cpf.text()
        email = self.tela_formulario.input_email.text()
        idade = self.tela_formulario.spinBox_idade.text()


        cursor = self.conexao.cursor()
        comando = f"select usuario, senha from usuarios where usuario = '{self.tela_login.input_user.text()}'"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        self.conexao.commit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())