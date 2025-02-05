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

        botao_gato = QPushButton("Clique Aqui", self)
        botao_gato.setStyleSheet("font-size: 16px; padding: 10px;")
        botao_gato.clicked.connect(self.on_click_button_gato)

        botao_cachorro = QPushButton("Clique Aqui", self)
        botao_cachorro.setStyleSheet("font-size: 16px; padding: 10px;")
        botao_cachorro.clicked.connect(self.on_click_button_cachorro)

        layout.addWidget(botao_gato)
        layout.addWidget(botao_cachorro)
        self.setCentralWidget(central_widget)

    def on_click_button_cachorro(self):
        img_cachorro = QLabel(self)
        pixmap = QPixmap(r"ex_pyside\cachorro.jpg")
        pixmap = pixmap.scaled(400,400, Qt.KeepAspectRatio)
        img_cachorro.setPixmap(pixmap)
        img_cachorro.setAlignment(Qt.AlignCenter)
        self.centralWidget().layout().addWidget(img_cachorro)
        print("clico")

    def on_click_button_gato(self):
        img_gato = QLabel(self)
        pixmap_gato = QPixmap(r"ex_pyside\gato.webp")
        pixmap_gato = pixmap_gato.scaled(400,400, Qt.KeepAspectRatio)
        img_gato.setPixmap(pixmap_gato)
        img_gato.setAlignment(Qt.AlignCenter)
        self.centralWidget().layout().addWidget(img_gato)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())