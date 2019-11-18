from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class dialogExample(QMainWindow):

    def __init__(self):
        #Add button
        super().__init__()
        print('test3')
        self.setupUI()




    def setupUI(self):
            btn = QPushButton('Exit', self)
            btn.move(30, 20)









