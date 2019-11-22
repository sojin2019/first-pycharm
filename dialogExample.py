from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
#form_class = uic.loadUiType("pushbuttonTest.ui")[0]

class dialogExample(QMainWindow):

    def __init__(self):
        #Add button
        super().__init__()
        print('test3')

        # x,y,width,height
        self.setGeometry(300,300,350,150)
        # window title
        self.setWindowTitle("Button Test")

        btn_1 = QPushButton('Click', self)
        btn_1.setGeometry(50, 80, 120, 40)
        btn_2 = QPushButton('Exit', self)
        btn_2.setGeometry(190,80, 120, 40)


        btn_1.clicked.connect(self.btnfc)
        # Quit Button
        btn_2.clicked.connect(QCoreApplication.instance().quit)



    def btnfc(self):
        print('hello')
        self.close()
        QCoreApplication.instance().quit









