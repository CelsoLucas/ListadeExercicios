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
                                               user="suporte",
                                               password="suporte",
                                               database="ex001"
                                               )
        self.tela_login = Ui_MainWindow()
        self.tela_login.setupUi(self)
        self.tela_login.btn_login.clicked.connect(self.check_login)

    def check_login(self):
        cursor = self.conexao.cursor()
        comando = f"select usuario, senha, foto_perfil from usuarios where usuario = '{self.tela_login.input_user.text()}'"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        self.conexao.commit()
        
        if not resultado:
            QMessageBox.warning(self, "Erro", "Usuário inválido!")
        else:
            if self.tela_login.input_senha.text() != resultado[0][1]:
                QMessageBox.warning(self, "Erro", "Senha inválida!")
            else:
                pixmap = QPixmap(f'{resultado[0][2]}')
                self.tela_login.icon_login.setPixmap(pixmap)
                self.tela_login.icon_login.setScaledContents(True)
                QMessageBox.information(self, "Sucesso", f"Bem-vindo, {self.tela_login.input_user.text()}!")
                self.tela_formulario = Ui_tela_formulario()
                self.tela_formulario.setupUi(self)
                self.tela_formulario.btn_procurar_arquivo.clicked.connect(self.open_image)
                self.tela_formulario.btn_enviar_formulario.clicked.connect(self.enviar_form)


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

    def enviar_form(self, img):
        nome_usu = self.tela_formulario.input_nome.text()
        senha = self.tela_formulario.input_senha.text()
        cpf = self.tela_formulario.input_cpf.text()
        email = self.tela_formulario.input_email.text()
        idade = self.tela_formulario.input_idade.text()
        foto = self.new_file_path

        if self.tela_formulario.input_cargo_adm.isChecked():
            opc_cargo = 1
        elif self.tela_formulario.input_cargo_func.isChecked():
            opc_cargo = 2

        if self.tela_formulario.sexo_opc_m.isChecked():
            opc_sexo = 1
        elif self.tela_formulario.sexo_opc_f.isChecked():
            opc_sexo = 2
        elif self.tela_formulario.sexo_opc_o.isChecked():
            opc_sexo = 3

        data_contratacao = self.tela_formulario.input_data_contratacao.date().toString("yyyy-MM-dd")
        data_nasc = self.tela_formulario.input_data_nasc.date().toString("yyyy-MM-dd")

        salario = self.tela_formulario.input_salario.value()

        if self.tela_formulario.input_periodo.currentIndex() == 0:
            periodo = 1
        elif self.tela_formulario.input_periodo.currentIndex() == 1:
            periodo = 2
        elif self.tela_formulario.input_periodo.currentIndex() == 2:
            periodo = 3
        elif self.tela_formulario.input_periodo.currentIndex() == 3:
            periodo = 4

        obs = self.tela_formulario.input_obs.toPlainText()

        img_caminho = foto

        cursor = self.conexao.cursor()

        comando = """
            INSERT INTO usuarios 
            (usuario, senha, cpf, email, idade, cargo, data_contratacao, sexo, data_nasc, salario, periodo, obs, foto_perfil) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        dados = (
            nome_usu, senha, cpf, email, idade, opc_cargo, 
            data_contratacao, opc_sexo, data_nasc, salario, periodo, obs, img_caminho
        )

        cursor.execute(comando, dados)
        self.conexao.commit()
        cursor.close()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())