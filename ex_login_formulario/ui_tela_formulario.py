import customtkinter as ctk
from cmd_tela_formulario import Usuario

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

        self.frame1 = ctk.CTkFrame(self, width=1050, height=600, fg_color="white")
        self.frame1.grid(columnspan=2, pady=10, padx=20)
        self.frame1.grid_propagate(False)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)

        self.input_nome = ctk.CTkEntry(self.frame1,
                                        placeholder_text="Nome",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_nome.grid(row=0, column=0, pady=40)

        self.linha = ctk.CTkFrame(self.frame1, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=0, column=0, pady=(30, 0))

        self.input_email = ctk.CTkEntry(self.frame1,
                                        placeholder_text="Email",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_email.grid(row=1, column=0)

        self.linha = ctk.CTkFrame(self.frame1, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=1, column=0, pady=(30, 0))

        self.input_senha = ctk.CTkEntry(self.frame1,
                                        placeholder_text="Senha",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left",
                                        show="*")
        self.input_senha.grid(row=2, column=0, pady=(40, 20))

        self.linha = ctk.CTkFrame(self.frame1, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=2, column=0, pady=(45, 0))

        self.input_cpf = ctk.CTkEntry(self.frame1,
                                        placeholder_text="CPF",
                                        fg_color="transparent",
                                        border_width=0,
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.input_cpf.grid(row=3, column=0, pady=(20, 20))

        self.linha = ctk.CTkFrame(self.frame1, height=2, fg_color="#909090", width=300)
        self.linha.grid(row=3, column=0, pady=(45, 0))

        self.txt_obs = ctk.CTkLabel(self.frame1,
                                    text="Observação",
                                    width=300,
                                    font=("poppins", 20),
                                    text_color="#909090",
                                    anchor="w") 
        self.txt_obs.grid(row=5, column=0, pady=(40, 0))

        self.input_obs = ctk.CTkTextbox(self.frame1,
                                        fg_color="transparent",
                                        border_width=1,
                                        font=("poppins", 20),
                                        width=300,
                                        height=100,
                                        text_color="#909090")
        self.input_obs.grid(row=6, column=0, pady=(0, 0))
        
        self.txt_sexo = ctk.CTkLabel(self.frame1,
                                    text="Sexo",
                                    font=("poppins", 20),
                                    width=300,
                                    text_color="#909090",
                                    justify="left")
        self.txt_sexo.grid(row=0, column=1, pady=40)

        self.frame_radio1 = ctk.CTkFrame(self.frame1, width=400, height=25, fg_color="white")
        self.frame_radio1.grid(row=1, column=1, pady=(15, 0))
        self.frame_radio1.columnconfigure(0, weight=1)
        self.frame_radio1.rowconfigure(0, weight=1)
        self.frame_radio1.grid_propagate(False)

        def radio1():
            print(self.radio1_var.get())
        
        self.radio1_var = ctk.IntVar(value=0)

        self.btn_radio_masc = ctk.CTkRadioButton(self.frame_radio1, text="Masculino", text_color="#909090", value=1, variable=self.radio1_var, command=radio1)
        self.btn_radio_masc.grid(row=0, column=0, sticky="nw")

        self.btn_radio_femn = ctk.CTkRadioButton(self.frame_radio1, text="Feminino", value=2, variable=self.radio1_var, command=radio1)
        self.btn_radio_femn.grid(row=0, column=0, sticky="n")

        self.btn_radio_outro = ctk.CTkRadioButton(self.frame_radio1, text="Outro", value=3, variable=self.radio1_var, command=radio1)
        self.btn_radio_outro.grid(row=0, column=0, sticky="ne")

        self.txt_cargo = ctk.CTkLabel(self.frame1,
                                        text="Cargo",
                                        font=("poppins", 20),
                                        width=300,
                                        text_color="#909090",
                                        justify="left")
        self.txt_cargo.grid(column=1, row=2)

        self.frame_radio2 = ctk.CTkFrame(self.frame1, width=200, height=25, fg_color="white")
        self.frame_radio2.grid(row=3, column=1, pady=(15, 0))
        self.frame_radio2.columnconfigure(0, weight=1)
        self.frame_radio2.rowconfigure(0, weight=1)
        self.frame_radio2.grid_propagate(False)


        def radio2():
            print(self.radio2_var.get())
        self.radio2_var = ctk.IntVar(value=0)

        self.btn_radio_adm = ctk.CTkRadioButton(self.frame_radio2, text="ADM", text_color="#909090", value=1, variable=self.radio2_var,command=radio2)
        self.btn_radio_adm.grid(row=0, column=0, sticky="nw")

        self.btn_radio_func = ctk.CTkRadioButton(self.frame_radio2, text="Funcionario", text_color="#909090", value=2, variable=self.radio2_var, command=radio2)
        self.btn_radio_func.grid(row=0, column=0, sticky="ne")

        self.label_img = ctk.CTkLabel(self.frame1, text="", image=None)
        self.label_img.grid(row=6, column=1)

        sexo = self.radio1_var.get()
        cargo = self.radio2_var.get()
        
        self.usuario = Usuario(self.input_nome.get(),
                               self.input_email.get(),
                               self.input_senha.get(),
                               self.input_cpf.get(),
                               self.input_obs.get("1.0", "end"),
                               sexo,
                               cargo)

        self.btn_procurar_arquivo_foto = ctk.CTkButton(self.frame1, text="Procurar Arquivo",
                                                       command=lambda: self.usuario.selecionar_imagem(self.label_img))
        self.btn_procurar_arquivo_foto.grid(column=1, row=5, pady=(40, 0))

        self.btn_enviar_formulario = ctk.CTkButton(self.frame1,
                                                   text="Enviar Formulario",
                                                   command=self.usuario.enviarFormulario)
        self.btn_enviar_formulario.grid(columnspan=2, pady=(40, 20), sticky="s")



if __name__ == "__main__":
    app = telaFormulario()
    app.mainloop()