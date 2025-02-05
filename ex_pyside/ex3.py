from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela com Nome centralizado e Imagem")
        self.setGeometry(100, 100, 400, 400)
        
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        label = QLabel("Celso", self)
        label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        label.setAlignment(Qt.AlignCenter)

        img_label = QLabel(self)
        pixmap = QPixmap(r"ex_pyside\audirs6.jpg")
        pixmap = pixmap.scaled(400,400, Qt.KeepAspectRatio)
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignCenter)

        botao = QPushButton("Clique Aqui", self)
        botao.setStyleSheet("font-size: 16px; padding: 10px;")
        botao.clicked.connect(self.on_click_button)

        layout.addWidget(label)
        layout.addWidget(img_label)
        layout.addWidget(botao)
        self.setCentralWidget(central_widget)

    def on_click_button(self):
        print("O Botão foi clicado")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())