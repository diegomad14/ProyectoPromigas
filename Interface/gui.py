from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class Caja(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.pushButton.setEnabled(False)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    GUI = Caja()
    GUI.show()
    sys.exit(app.exec_())