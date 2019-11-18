import sys
import mainWindow
import mpl_squares as ms
import inputSchedule
from PyQt5.QtWidgets import *
import dialogExample as dlex

from _datetime import datetime


now = datetime.now()
    
if __name__ == "__main__":
    mw = mainWindow.mw('addition test')
    mw

    if now.day < 10:
        in_item_date = str(now.year) + str(now.month) + "0" + str(now.day)
    else:
        in_item_date = str(now.year)+str(now.month)+str(now.day)

    inputSchedule.InputSchedule(in_item_date,'2345', 'Coding', 'everyday for 30 days' )

    app = QApplication(sys.argv)
    dlex.dialogExample()
    app.exec_()


    #app = QApplication([])
    #button = QPushButton('Click')

    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('You clicked the button!')
        alert.exec_()

    #button.clicked.connect(on_button_clicked)
    #button.show()
    #app.exec_()

    #ms.testplot()








