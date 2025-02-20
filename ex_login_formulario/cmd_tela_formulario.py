import re
import customtkinter as ctk

class Usuario():
    def __init__(self, nome, email, senha, cpf, obs, sexo, cargo, img):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.obs = obs
        self.sexo = sexo
        self.cargo = cargo
        self.img = img

    def abrir_popup(mensagem):
        popup = ctk.CTkToplevel()
        popup.geometry("300x150")
        popup.title("Aviso")

        label = ctk.CTkLabel(popup, text=mensagem, font=("Arial", 14), wraplength=280)
        label.pack(pady=20)

        botao_fechar = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        botao_fechar.pack(pady=10)

        popup.grab_set()  # Bloqueia interação com a janela principal até fechar o pop-up
        popup.mainloop()  # Mantém a janela aberta até interação do usuário

    def email_valido(self, email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(padrao, email) is not None
    
    def verificarFormularui(self):
        self.is_valid = True

        if not self.email_valido(self.email):
            self.abrir_popup("Email inválido!")
            self.is_valid = False

        if self.sexo == 0:
            self.abrir_popup("Sexo inválido!")
            self.is_valid = False
        if self.cargo == 0:
            self.abrir_popup("Cargo inválido!")
            self.is_valid = False
