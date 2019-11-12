import sys
import mainWindow
import inputSchedule
from PyQt5.QtWidgets import *

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


