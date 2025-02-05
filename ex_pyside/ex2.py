import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela com Nome e Imagem")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        nome_label = QLabel("Meu Nome")
        nome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        imagem_label = QLabel()
        pixmap = QPixmap("ex_pyside/audirs6.jpg")  
        imagem_label.setPixmap(pixmap)
        imagem_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(nome_label)
        layout.addWidget(imagem_label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())