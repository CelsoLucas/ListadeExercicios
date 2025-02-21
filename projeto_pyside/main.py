from ui_tela_login import Ui_MainWindow
from ui_formulario import Ui_tela_formulario
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
import sys
import mysql.connector
import os
import shutil
from PySide6.QtWidgets import QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.conexao = mysql.connector.connect(host="localhost",
                                               user="celsadas",
                                               password="33880188",
                                               database="ex001"
                                               )
        self.tela_login = Ui_MainWindow()
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def check_login(self):
        cursor = self.conexao.cursor()
        
        comando = "SELECT senha, img_local FROM usuarios WHERE nome_usu = %s"
        cursor.execute(comando, (self.tela_login.input_user.text(),))
        resultado = cursor.fetchone()
        
        if not resultado:
            QMessageBox.warning(self, "Erro", "Usuário inválido!")
            return
        
        senha_armazenada, foto_perfil = resultado

        comando_senha = "SELECT SHA2(%s, 256)"
        cursor.execute(comando_senha, (self.tela_login.input_senha.text(),))
        senha_digitada_hash = cursor.fetchone()[0]

        if senha_digitada_hash != senha_armazenada:
            QMessageBox.warning(self, "Erro", "Senha inválida!")
        else:
            if foto_perfil:
                pixmap = QPixmap(foto_perfil)
                self.tela_login.icon_login.setPixmap(pixmap)
                self.tela_login.icon_login.setScaledContents(True)

            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {self.tela_login.input_user.text()}!")

            self.tela_formulario = Ui_tela_formulario()
            self.tela_formulario.setupUi(self)
            self.tela_formulario.btn_enviar_formulario.clicked.connect(self.enviar_form)
            self.tela_formulario.btn_procurar_arquivo.clicked.connect(self.open_image)
        
        cursor.close()



    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Images(*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")

        if file_path:
            # Criar diretório de destino se não existir
            save_dir = "images"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Definir novo nome para a imagem (exemplo: usando o nome do usuário)
            user_name = self.tela_formulario.input_nome.text().replace(" ", "_")
            new_file_name = f"{user_name}.jpg"  # Salvar sempre como .jpg para padronização

            # Caminho completo do arquivo de destino
            self.new_file_path = os.path.join(f"projeto_pyside/", save_dir, new_file_name)

            # Copiar a imagem para a pasta de destino
            shutil.copy(file_path, self.new_file_path)

            # Exibir a imagem na interface
            pixmap = QPixmap(self.new_file_path)
            self.tela_formulario.layout_img.setPixmap(pixmap)
            self.tela_formulario.layout_img.setScaledContents(True)
            self.tela_formulario.layout_img.setPixmap(pixmap)

    def valida_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma1 * 10) % 11
        if digito1 == 10 or digito1 == 11:
            digito1 = 0
        if digito1 != int(cpf[9]):
            return False

        soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma2 * 10) % 11
        if digito2 == 10 or digito2 == 11:
            digito2 = 0
        if digito2 != int(cpf[10]):
            return False

        return True
    
    def enviar_form(self):
        cursor = self.conexao.cursor()

        # Verificar se o nome de usuário já existe
        comando = "SELECT nome_usu FROM usuarios WHERE nome_usu = %s"
        cursor.execute(comando, (self.tela_formulario.input_nome.text(),))
        if cursor.fetchone():
            QMessageBox.warning(self, "Erro", "Usuário já cadastrado!")
            return

        # Verificar se o CPF é válido
        cpf_input = self.tela_formulario.input_cpf.text()
        if not self.valida_cpf(cpf_input):
            QMessageBox.warning(self, "Erro", "Digite um CPF válido!")
            return

        # Verificar se o CPF já existe
        comando = "SELECT cpf FROM usuarios WHERE cpf = %s"
        cursor.execute(comando, (cpf_input,))
        if cursor.fetchone():
            QMessageBox.warning(self, "Erro", "CPF já cadastrado!")
            return

        # Verificar se o e-mail é válido
        email = self.tela_formulario.input_email.text()
        if not (email.endswith("@gmail.com") or email.endswith("@hotmail.com") or email.endswith("@icloud.com")):
            QMessageBox.warning(self, "Erro", "Email inválido!")
            return

        # Verificar se o usuário é maior de 16 anos
        idade = self.tela_formulario.input_idade.text()
        if int(idade) <= 15:
            QMessageBox.warning(self, "Erro", "Precisa ser maior de 16 anos!")
            return

        # Verificar se o cargo foi selecionado
        if not (self.tela_formulario.input_cargo_adm.isChecked() or self.tela_formulario.input_cargo_func.isChecked()):
            QMessageBox.warning(self, "Erro", "Selecione um cargo!")
            return

        # Verificar se o sexo foi selecionado
        opc_sexo = None
        if self.tela_formulario.sexo_opc_m.isChecked():
            opc_sexo = 1
        elif self.tela_formulario.sexo_opc_f.isChecked():
            opc_sexo = 2
        elif self.tela_formulario.sexo_opc_o.isChecked():
            opc_sexo = 3
        if opc_sexo is None:
            QMessageBox.warning(self, "Erro", "Selecione um sexo válido!")
            return

        # Verificar se o período foi selecionado
        if self.tela_formulario.input_periodo.currentIndex() == -1:
            QMessageBox.warning(self, "Erro", "Selecione um período!")
            return
        periodo = self.tela_formulario.input_periodo.currentIndex() + 1

        # Verificar se a observação contém caracteres inválidos
        obs = self.tela_formulario.input_obs.toPlainText()
        if any(c in '☺☻♥♦♣♠•◘○' for c in obs):
            QMessageBox.warning(self, "Erro", "Observação inválida!")
            return

        # Recuperar caminho da foto
        foto = self.new_file_path

        # Definir cargo
        opc_cargo = 1 if self.tela_formulario.input_cargo_adm.isChecked() else 2

        # Recuperar data de contratação e salário
        data_contratacao = self.tela_formulario.input_data_contratacao.date().toString("yyyy-MM-dd")
        salario = self.tela_formulario.input_salario.value()

        # Inserir dados no banco
        comando = """
            INSERT INTO usuarios 
            (nome_usu, email, senha, cpf, idade, salario, data_contratacao, periodo, cargo, sexo, obs, img_local)
            VALUES (%s, %s,SHA2(%s, 256), %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        dados = (
            self.tela_formulario.input_nome.text(), email, self.tela_formulario.input_senha.text(), cpf_input, idade, salario, 
            data_contratacao, periodo, opc_cargo, opc_sexo, obs, foto
        )

        cursor.execute(comando, dados)
        self.conexao.commit()
        cursor.close()

        QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso!")
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())