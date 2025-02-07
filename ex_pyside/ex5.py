import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt

class LineEditWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cachorro ou Gato")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.label_name = QLabel("Digite seu nome: ")
        self.input_name = QLineEdit()
        self.botao = QPushButton("Clique")
        self.botao.clicked.connect(self.result_label)
        
        self.label_result = QLabel()

        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.botao)
        layout.addWidget(self.label_result)
    
    def result_label(self):
        nome = self.input_name.text()
        print(type(nome))
        self.result = ""
        for i in range(len(nome) -1, -1, -1):
            self.result += nome[i]
        self.label_result.setText(self.result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineEditWindow()
    window.show()
    sys.exit(app.exec())