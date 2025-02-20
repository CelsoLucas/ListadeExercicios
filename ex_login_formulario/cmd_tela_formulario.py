import customtkinter as ctk
from tkinter import filedialog
import os
import shutil
import re
from conexao_db import conexaoDB
from PIL import Image

class Usuario():
    def __init__(self, nome, email, senha, cpf, obs, sexo, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.obs = obs
        self.sexo = sexo
        self.cargo = cargo

    def selecionar_imagem(self, label):
        pasta_destino = "images"
        
        # Verifique se a pasta de destino existe, senão crie-a
        caminho_pasta_destino = os.path.join("ex_login_formulario", pasta_destino)
        os.makedirs(caminho_pasta_destino, exist_ok=True)

        # Selecione a imagem
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        
        if caminho_imagem:
            # Obter a extensão e limpar o nome do arquivo
            extensao = os.path.splitext(caminho_imagem)[1]
            nome_limpo = re.sub(r'[^a-zA-Z0-9]', '_', self.nome)  # Substitui caracteres especiais por "_"

            # Verifique se o nome não está vazio, caso contrário, use um nome padrão
            if not nome_limpo:
                nome_limpo = "imagem_sem_nome"  # Nome padrão caso não seja fornecido

            novo_nome = f"{nome_limpo}{extensao}"

            # Caminho de destino (incluindo a pasta 'images')
            self.destino = os.path.join(caminho_pasta_destino, novo_nome)
            print(f"Renomeando imagem para: {novo_nome}")  # Debug: verifique o novo nome

            try:
                # Verifique se o arquivo existe e copie
                if os.path.exists(caminho_imagem):
                    shutil.copy(caminho_imagem, self.destino)
                    print(f"Imagem copiada para: {self.destino}")  # Debug: verifique se a imagem foi copiada
                else:
                    print("Erro: Arquivo de imagem não encontrado.")
                    return

                # Carregar a imagem para exibição no label
                self.img_form = ctk.CTkImage(light_image=Image.open(self.destino), size=(150, 100))
                label.configure(text="", image=self.img_form)

            except Exception as e:
                print(f"Erro ao copiar imagem: {e}")
        print(novo_nome)

    def abrir_popup(self, mensagem):
        popup = ctk.CTkToplevel()
        popup.geometry("300x150")
        popup.title("Aviso")

        label = ctk.CTkLabel(popup, text=mensagem, font=("Arial", 14), wraplength=280)
        label.pack(pady=20)

        botao_fechar = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        botao_fechar.pack(pady=10)

        popup.grab_set()  # Bloqueia interação com a janela principal até fechar o pop-up
        popup.mainloop()  # Mantém a janela aberta até interação do usuário

    def validar_email(self, email):  # Adicionando 'self' no método
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
    
    def verificarFormulario(self, email, cpf, sexo, cargo):
        self.is_valid = True

        if sexo == 0:
            self.abrir_popup("Sexo inválido!")
            self.is_valid = False
        if cargo == 0:
            self.abrir_popup("Cargo inválido!")
            self.is_valid = False

        # Verificar no banco de dados se o email ou CPF já existem
        self.conexao = conexaoDB()
        comando = "SELECT email, cpf FROM usuarios WHERE email = %s OR cpf = %s"
        valores = (email, cpf)
        resultado = self.conexao.select_bd(comando, valores)
        
        if resultado:
            for usuario in resultado:
                if usuario[0] == email:
                    self.abrir_popup(f"Email {email} já cadastrado!")
                    self.is_valid = False
                if usuario[1] == cpf:
                    self.abrir_popup(f"CPF {cpf} já cadastrado!")
                    self.is_valid = False

        # Verifica se o email é válido
        if not self.validar_email(email):
            self.abrir_popup("Email inválido!")
            self.is_valid = False

    def enviarFormulario(self):
        self.verificarFormulario(self.email, self.cpf, self.sexo, self.cargo)
        self.conexao = conexaoDB()

        comando = """
        INSERT INTO usuarios 
        (nome, email, senha, cpf, obs, sexo, cargo, local_img)
        VALUES (%s, %s, SHA2(%s, 256), %s, %s, %s, %s, %s)
        """
        valores = (self.nome, self.email, self.senha, self.cpf, self.obs, self.sexo, self.cargo, self.destino)
        self.conexao.insert_bd(comando, valores)

