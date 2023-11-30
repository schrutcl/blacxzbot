# gui.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QIcon

class ZyngaBox(QMainWindow):
    def __init__(self):
        super(ZyngaBox, self).__init__()

        # Postavljanje osnovnih svojstava prozora
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Zynga Box Poker Bot")
        self.setWindowIcon(QIcon('images/icons/icobot.png'))

        # Dodavanje gumba za pokretanje bota
        self.start_button = QPushButton("Start Bot", self)
        self.start_button.clicked.connect(self.start_bot)
        self.start_button.setGeometry(50, 50, 150, 50)

        # Dodavanje labela ili drugih elemenata GUI-a po potrebi

        # Postavljanje verzije programa
        self.version_label = QLabel("Version: v1.0", self)
        self.version_label.setGeometry(50, 80, 150, 20)

    def start_bot(self):  # Dodajte ovu funkciju
        print("Bot started!")  # Ovdje pozovi funkcije za pokretanje bota

    # ... ostatak koda ...
