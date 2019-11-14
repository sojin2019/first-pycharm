from PyQt5.QtWidgets import *
import sys

class dialogExample(QWidget):

    def __init__(self):
        super().__init__()
        super.initUI()

    def initUI(self):
        #Add button
        self.btn = QPushButton('Please show Input Dialog', self)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.showID)

        #Add label
        self.lb = QLabel(self)
        self.lb.move(30, 62)
        self.lb.resize(400, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showID(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter anything:')
        if ok:
           self.lb.setText(str(text))





