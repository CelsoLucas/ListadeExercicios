import customtkinter as ctk
from tkinter import filedialog
from conexao_db import conexaoDB
import bcrypt
import os
import shutil
from PIL import Image, ImageTk


class verificarFormulario:
    def __init__(self, email, cpf):
        self.is_valid = True
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

    def abrir_popup(self, mensagem):
        popup = ctk.CTkToplevel()
        popup.geometry("300x150")
        popup.title("Erro")
        
        label = ctk.CTkLabel(popup, text=mensagem, font=("Arial", 14))
        label.pack(pady=20)
        
        botao_fechar = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        botao_fechar.pack(pady=10)


class adcUser:
    def __init__(self, nome, email, senha, cpf, obs, sexo, cargo, img_local):
        self.conexao = conexaoDB()

        # Verifique o formulário antes de continuar
        form_check = verificarFormulario(email, cpf)
        if not form_check.is_valid:
            return  # Se o formulário for inválido, não faz o cadastro

        salt = bcrypt.gensalt()
        hash_senha = bcrypt.hashpw(senha.encode(), salt)

        comando = "INSERT INTO usuarios (nome, email, senha, cpf, obs, sexo, cargo, local_img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, email, hash_senha, cpf, obs, sexo, cargo, img_local)

        try:
            self.conexao.insert_bd(comando, valores)
            self.abrir_popup("Cadastro realizado com sucesso!")
        except Exception as e:
            self.abrir_popup(f"Erro ao cadastrar: {e}")
            
    def abrir_popup(self, mensagem):
        popup = ctk.CTkToplevel()
        popup.geometry("300x150")
        popup.title("Mensagem")

        label = ctk.CTkLabel(popup, text=mensagem, font=("Arial", 14))
        label.pack(pady=20)

        botao_fechar = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        botao_fechar.pack(pady=10)

class adcFoto():
    def __init__(self):
        file_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Images", "*.png;*.xpm;*.jpg;*.jpeg;*.bmp"), ("All Files", "*")])
        
        if file_path:
            # Criar diretório de destino se não existir
            save_dir = "images"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            
            # Definir novo nome para a imagem
            user_name = self.input_nome.get().strip().replace(" ", "_")
            new_file_name = f"{user_name}.jpg"  # Padronização para JPG
            self.new_file_path = os.path.join("ex_login_formulario/", save_dir, new_file_name)
            
            # Copiar a imagem para a pasta de destino
            shutil.copy(file_path, self.new_file_path)
            
            # Exibir a imagem na interface
            img = Image.open(self.new_file_path)
            img = img.resize((150, 150), Image.LANCZOS)  # Ajuste de tamanho
            img = ImageTk.PhotoImage(img)
            
            self.img_label.configure(image=img, text="")
            self.img_label.image = img  # Manter referência da imagem