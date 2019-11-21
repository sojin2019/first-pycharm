from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pushbuttonTest.ui")[0]


class dialogExample(QMainWindow, form_class):

    def __init__(self):
        #Add button
        super().__init__()
        print('test3')
        self.btnctrl()
        print('test4')

    def btnctrl(self):
        btn = QPushButton(self)
        # Quit Button
        btn_2 = QPushButton(self)
        
        btn.clicked.connect(self.btnfc)
        btn_2.clicked.connect(QCoreApplication.instance().quit)

    def btnfc(self):
        print('exit')








