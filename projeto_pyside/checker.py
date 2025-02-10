from PySide6.QtWidgets import QMessageBox
class checker():
    def __init__(self, parent, input_user, input_senha):
        self.parent = parent
        self.usuario = input_user
        self.senha = input_senha
        self.user = "admin"
        self.senha_correta  = "admin"
        self.botao_login.clicked.connect(checker())

    def checker(self):
        if self.usuario != self.user:
            QMessageBox.warning(self.parent, "Erro", "Usuário inválido!")
        elif self.senha != self.senha:
            QMessageBox.warning(self.parent, "Erro", "Senha inválida!")
        else:
            QMessageBox.information(self.parent, "Sucesso", f"Bem-vindo, {self.usuario}!")
