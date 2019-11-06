import sys
from PyQt5.QtWidgets import *

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.get_size()

    def initUI(self):
        self.setGeometry(300, 300, 350, 450)
        self.setWindowTitle('Main window')

        self.statusbar = self.statusBar()

        self.textedit = QTextEdit(self)
        self.label = QLabel(self)
        self.lineedit = QLineEdit(self)

        self.label.resize(300, 20)  # width, height resizing
        self.label.move(10, 10) # 10, 10 moving

        self.lineedit.resize(10, 40)
        self.lineedit.move(10, 10)

        self.textedit.move(10, 70)
        self.textedit.resize(self.textedit.sizeHint())
        self.show()





