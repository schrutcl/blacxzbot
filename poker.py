# poker.py (glavni fajl)
import sys
from PyQt5.QtWidgets import QApplication
from gui import ZyngaBox

def main():
    app = QApplication(sys.argv)
    window = ZyngaBox()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
