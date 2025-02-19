import customtkinter as ctk

class telaFormulario(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Formulario")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self._set_appearance_mode("blue")
        self.configure(fg_color="#DBDBDB")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        self.geometry(f"{largura_tela}x{altura_tela}")

        self.txt_formulario = ctk.CTkLabel(self, text="FORMULARIO", font=("poppins", 40, "bold"), text_color="black")
        self.txt_formulario.grid(row=0, columnspan=2, pady=20)

        self.input_usuario = ctk.CTkEntry(self,
                                        placeholder_text="Nome",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_usuario.grid(row=1, column=0, pady=(45, 0))

        self.linha = ctk.CTkFrame(self, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=1, column=0, pady=(100, 30))

        self.input_email = ctk.CTkEntry(self,
                                        placeholder_text="Email",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_email.grid(row=2, column=0, pady=(40, 20))

        self.linha = ctk.CTkFrame(self, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=2, column=0, pady=(45, 0))

        self.input_senha = ctk.CTkEntry(self,
                                        placeholder_text="Senha",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_senha.grid(row=3, column=0, pady=(40, 20))

        self.linha = ctk.CTkFrame(self, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=3, column=0, pady=(45, 0))

        self.input_cpf = ctk.CTkEntry(self,
                                        placeholder_text="Email",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_cpf.grid(row=4, column=0, pady=(40, 20))

        self.linha = ctk.CTkFrame(self, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=4, column=0, pady=(45, 0))

        self.input_cpf = ctk.CTkEntry(self,
                                        placeholder_text="Email",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_cpf.grid(row=4, column=0, pady=(40, 20))

        self.linha = ctk.CTkFrame(self, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=4, column=0, pady=(45, 0))

        self.txt_obs = ctk.CTkLabel(self,
                                    text="Observação",
                                    width=300,
                                    font=("poppins", 20),
                                    text_color="#909090",
                                    anchor="w") 
        self.txt_obs.grid(row=5, column=0, pady=(40, 0))


        self.input_obs = ctk.CTkTextbox(self,
                                        fg_color="transparent",
                                        border_width=1,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090")
        self.input_obs.grid(row=6, column=0, pady=(0, 0))
        
        self.txt_sexo = ctk.CTkLabel(self,
                                    text="Sexo",
                                    font=("poppins", 20),
                                    width=300,
                                    text_color="#909090",
                                    justify="left")
        self.txt_sexo.grid(row=1, column=1, pady=(45, 0))

        self.radio_var = ctk.IntVar(value=0)
        self.btn_radio_masc = ctk.CTkRadioButton(self, text="Masculino", text_color="#909090", value=1, variable=self.radio_var)
        self.btn_radio_masc.grid(row=1, column=1, pady=(80, 0))
        self.btn_radio_femn = ctk.CTkRadioButton(self, text="Feminino", value=2, variable=self.radio_var)
        self.btn_radio_outro = ctk.CTkRadioButton(self, text="Outro", value=2, variable=self.radio_var)


if __name__ == "__main__":
    app = telaFormulario()
    app.mainloop()