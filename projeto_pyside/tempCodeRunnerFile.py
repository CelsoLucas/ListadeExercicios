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
            self.tela_login.icon_login.setPixmap(pixmap)
            self.tela_formulario.layout_img.setScaledContents(True)
            self.tela_formulario.layout_img.setPixmap(pixmap)

    def valida_cpf(self, cpf):
        # Remove caracteres especiais
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se o CPF é uma sequência de números iguais (ex: 111.111.111-11)
        if cpf == cpf[0] * 11:
            return False

        # Cálculo do primeiro dígito verificador
        soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma1 * 10) % 11
        if digito1 == 10 or digito1 == 11:
            digito1 = 0
        if digito1 != int(cpf[9]):
            return False

        # Cálculo do segundo dígito verificador
        soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma2 * 10) % 11
        if digito2 == 10 or digito2 == 11:
            digito2 = 0
        if digito2 != int(cpf[10]):
            return False

        return True
    def enviar_form(self):
        cursor = self.conexao.cursor()
        comando = "SELECT nome_usu FROM usuarios WHERE nome_usu = %s"
        cursor.execute(comando, (self.tela_formulario.input_nome.text(),))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(self, "Erro", "Usuário ja sendo usado!")
        else:
            nome_usu = self.tela_formulario.input_nome.text()

        senha = self.tela_formulario.input_senha.text()

        cpf_input = self.tela_formulario.input_cpf.text()

        # Verificar se o CPF é válido
        if not self.valida_cpf(cpf_input):
            QMessageBox.warning(self, "Erro", "Digite um CPF válido!")
            return
        comando = "SELECT cpf FROM usuarios WHERE cpf = %s"
        cursor.execute(comando, (self.tela_formulario.input_cpf.text(),))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(self, "Erro", "CPF já Cadastrado!")
        else:
            cpf = self.tela_formulario.input_cpf.text()

        comando = "SELECT email FROM usuarios WHERE email = %s"
        cursor.execute(comando, (self.tela_formulario.input_email.text(),))
        resultado = cursor.fetchone()
        if resultado:
            QMessageBox.warning(self, "Erro", "Email já Cadastrado!")
        else:
            email = self.tela_formulario.input_email.text()
        if not (email.endswith("@gmail.com") or email.endswith("@hotmail.com") or email.endswith("@icloud.com")):            
            QMessageBox.warning(self, "Erro", "Email inválido!")
        idade = self.tela_formulario.input_idade.text()
        if int(idade) <= 15:
            QMessageBox.warning(self, "Erro", "Precisa ser maior de 16 anos")

        foto = self.new_file_path

        if self.tela_formulario.input_cargo_adm.isChecked():
            opc_cargo = 1
        elif self.tela_formulario.input_cargo_func.isChecked():
            opc_cargo = 2
        else:
            QMessageBox.warning(self, "Erro", "Cargo Invalido!")

        opc_sexo = None

        if self.tela_formulario.sexo_opc_m.isChecked():
            opc_sexo = 1
        elif self.tela_formulario.sexo_opc_f.isChecked():
            opc_sexo = 2
        elif self.tela_formulario.sexo_opc_o.isChecked():
            opc_sexo = 3
            QMessageBox.warning(self, "Erro", "Sexo Invalido!")
        if opc_sexo is None:
            QMessageBox.warning(self, "Erro", "Selecione um sexo válido.")
            return

        data_contratacao = self.tela_formulario.input_data_contratacao.date().toString("yyyy-MM-dd")

        salario = self.tela_formulario.input_salario.value()

        # Verificar se nenhum item foi selecionado
        if self.tela_formulario.input_periodo.currentIndex() == -1:
            QMessageBox.warning(self, "Erro", "Selecione um período!")
        else:
            if self.tela_formulario.input_periodo.currentIndex() == 0:
                periodo = 1
            elif self.tela_formulario.input_periodo.currentIndex() == 1:
                periodo = 2
            elif self.tela_formulario.input_periodo.currentIndex() == 2:
                periodo = 3
            elif self.tela_formulario.input_periodo.currentIndex() == 3:
                periodo = 4
            else:
                QMessageBox.warning(self, "Erro", "Período inválido!")

        obs = self.tela_formulario.input_obs.toPlainText()
        if obs in '☺☻♥♦♣♠•◘○':
            QMessageBox.warning(self, "Erro", "Obs inválida!")
        img_caminho = foto

        cursor = self.conexao.cursor()

        comando = """
            INSERT INTO usuarios 
            (nome_usu, email, senha, cpf, idade, salario, data_contratacao, periodo, cargo, sexo, obs, img_local)
            VALUES (%s, SHA2(%s, 256), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        dados = (
            nome_usu, email, senha, cpf, idade, salario, 
            data_contratacao, periodo, opc_cargo, opc_sexo, obs, img_caminho
        )

        cursor.execute(comando, dados)
        self.conexao.commit()
        cursor.close()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())