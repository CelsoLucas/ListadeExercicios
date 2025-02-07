import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QDialog, QMessageBox
from PySide6.QtCore import Qt

class telaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cachorro ou Gato")
        self.setGeometry(100, 100, 400, 300)
        
        self.user = "admin"
        self.senha  = "admin"

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)


        self.txt_login = QLabel("LOGIN")
        self.txt_login.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.txt_login.setAlignment(Qt.AlignCenter)

        self.txt_user = QLabel("Usuario")
        self.txt_user.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center;")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.input_user = QLineEdit()

        self.txt_senha = QLabel("Senha")
        self.txt_senha.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center;")
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.botao_login = QPushButton("Login")
        self.botao_login.clicked.connect(self.checker)

        layout.addWidget(self.txt_login)
        layout.addWidget(self.txt_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.txt_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.botao_login)
    
    def checker(self):
        print("foi")
        mensagem = QMessageBox()
        usuario = self.input_user.text()
        senha = self.input_senha.text()
        if usuario != self.user:
            mensagem.setText("Usuario Invalido!")
            mensagem.exec()
        else:
            if senha != self.senha:
                mensagem.setText("Senha Invalida!")
                mensagem.exec()
            else:
                mensagem.setText(f"Bem-Vindo {usuario}")
                mensagem.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaLogin()
    window.show()
    sys.exit(app.exec())