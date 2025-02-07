import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class AnimalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cachorro ou Gato")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.dog_button = QPushButton("Cachorro")
        self.dog_button.clicked.connect(self.show_dog)
        layout.addWidget(self.dog_button)

        self.cat_button = QPushButton("Gato")
        self.cat_button.clicked.connect(self.show_cat)
        layout.addWidget(self.cat_button)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

    def show_dog(self):
        pixmap = QPixmap("ex_pyside\cachorro.jpg") 
        self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

    def show_cat(self):
        pixmap = QPixmap("ex_pyside\gato.webp")
        self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimalWindow()
    window.show()
    sys.exit(app.exec())