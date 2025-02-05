from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
import sys

class Celso(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela com nome centralizado")
        self.setGeometry(100, 100, 400, 200)

        label = QLabel("Celso", self)
        label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Celso()
    window.show()
    app.exec()
