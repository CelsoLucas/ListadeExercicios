import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt
from checker import checker

class telaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LOGIN")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        self.txt_login = QLabel("LOGIN")
        self.txt_login.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.txt_login.setAlignment(Qt.AlignCenter)

        self.txt_user = QLabel("Usuario")
        self.txt_user.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center; min-width: 60; max-width:150;")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.input_user = QLineEdit()
        self.input_user.setStyleSheet("min-width: 60; max-width:150;")

        self.txt_senha = QLabel("Senha")
        self.txt_senha.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center;min-width: 60; max-width:150;")
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.input_senha = QLineEdit()
        self.input_senha.setStyleSheet("min-width: 60; max-width:150;")
        self.input_senha.setEchoMode(QLineEdit.Password)

        func = checker(self, self.input_user.text(), self.input_senha.text())

        self.botao_login = QPushButton("Login")
        self.botao_login.clicked.connect(func.checker())

        layout.addWidget(self.txt_login)
        layout.addWidget(self.txt_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.txt_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.botao_login)
        
    # def abrir_tela_cadastro(self):
    #     self.tela_cadastro = CadastroUsuario()  
    #     self.tela_cadastro.show()
    #     self.close()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaLogin()
    window.show()
    sys.exit(app.exec())