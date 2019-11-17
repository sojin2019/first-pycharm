from PyQt5.QtWidgets import *
import sys

class dialogExample(QMainWindow):

    def __init__(self):
        #Add button
        btn = QPushButton('Please show Input Dialog', self)
        btn.move(30, 20)
        btn.clicked.connect(self.showID)

        #Add label
        lb = QLabel(self)
        lb.move(30, 62)
        lb.resize(400, 22)

        setGeometry(300, 300, 290, 150)
        setWindowTitle('Input Dialog')
        self.show()

    def showID(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter anything:')
        if ok:
           self.lb.setText(str(text))






