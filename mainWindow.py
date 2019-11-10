import sys
from PyQt5.QtWidgets import *

class mw:

    def __init__(self, menu):
        self.menu = menu
        print("test1")
        self.initUI()

    def initUI(self):
        print("test2")

        #self.setGeometry(300, 300, 350, 450)
        #self.setWindowTitle('Main window')

        #self.statusbar = self.statusBar()

        #self.textedit = QTextEdit(self)
        #self.label = QLabel(self)
        #self.lineedit = QLineEdit(self)

        #self.label.resize(300, 20)  # width, height resizing
        #self.label.move(10, 10) # 10, 10 moving

        #self.lineedit.resize(10, 40)
        #self.lineedit.move(10, 10)

        #self.textedit.move(10, 70)
        #self.textedit.resize(self.textedit.sizeHint())
        #self.show()

        #window = QVBoxLayout()
        # self.comboBox = QComboBox(self)
        #self.comboBox.addItem("1st Item")
        #self.comboBox.addItem("2nd Item")
        #self.comboBox.addItem("3rd Item")
        #self.comboBox.addItem(self.menu)
        #self.comboBox.setEditable(True)
        #self.comboBox.clicked.connect(self.printComboBoxItem)

        #window.addWidget(self.comboBox)
        #window.addWidget(self.label)

        #self.comboBox.activated[str].connect(self.ComboBoxEvent)

        #self.setLayout(window)
        #self.setGeometry(300, 300, 300, 300)
        #self.setWindowTitle('ComboBox Test')
        #self.show()


    def ComboBoxEvent(self, text):
            self.label1.setText(text)
            self.label1.adjustSize()




