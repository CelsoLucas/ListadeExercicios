from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,                      QVBoxLayout, QHBoxLayout, QRadioButton, QCheckBox, QComboBox, QDateEdit, QSpinBox, QDoubleSpinBox, QTextEdit, QMainWindow
from PySide6.QtCore import Qt
import sys

class CadastroUsuario(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastrar Usuario")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        self.label_nome = QLabel("Nome:")
        self.input_nome = QLineEdit()

        self.label_cpf = QLabel("CPF:")
        self.input_cpf = QLineEdit()
        
        self.label_email = QLabel("E-mail:")
        self.input_email = QLineEdit()
        
        self.label_senha = QLabel("Senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        
        self.label_data_nascimento = QLabel("Data de Nascimento:")
        self.input_data_nascimento = QDateEdit()
        
        self.label_genero = QLabel("Gênero:")
        self.radio_masculino = QRadioButton("Masculino")
        self.radio_feminino = QRadioButton("Feminino")
        self.radio_outro = QRadioButton("Outro")
        layout_genero = QHBoxLayout()
        layout_genero.addWidget(self.radio_masculino)
        layout_genero.addWidget(self.radio_feminino)
        layout_genero.addWidget(self.radio_outro)
        
        self.label_cargo = QLabel("Cargo")
        self.check_adm = QCheckBox("ADM")
        self.check_func = QCheckBox("FUNCIONARIO")
        
        self.label_pais = QLabel("País:")
        self.combo_pais = QComboBox()
        self.combo_pais.addItems(["Brasil", "Estados Unidos", "Canadá", "Portugal"])
        
        self.label_idade = QLabel("Idade:")
        self.spin_idade = QSpinBox()
        self.spin_idade.setRange(1, 120)
        
        self.label_renda = QLabel("Renda Mensal (R$):")
        self.spin_renda = QDoubleSpinBox()
        self.spin_renda.setRange(0, 100000)
        self.spin_renda.setPrefix("R$ ")
        
        self.label_obs = QLabel("Observação:")
        self.texto_obs = QTextEdit()
        
        self.botao_cadastrar = QPushButton("Cadastrar")
        
        layout.addWidget(self.label_nome)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.label_cpf)
        layout.addWidget(self.input_cpf)
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.label_data_nascimento)
        layout.addWidget(self.input_data_nascimento)
        layout.addWidget(self.label_genero)
        layout.addLayout(layout_genero)
        layout.addWidget(self.label_cargo)
        layout.addWidget(self.check_adm)
        layout.addWidget(self.check_func)
        layout.addWidget(self.label_pais)
        layout.addWidget(self.combo_pais)
        layout.addWidget(self.label_idade)
        layout.addWidget(self.spin_idade)
        layout.addWidget(self.label_renda)
        layout.addWidget(self.spin_renda)
        layout.addWidget(self.label_obs)
        layout.addWidget(self.texto_obs)
        layout.addWidget(self.botao_cadastrar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CadastroUsuario()
    janela.show()
    sys.exit(app.exec())
