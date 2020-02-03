import sys
from PyQt5.QtWidgets import *
from tkinter import *
from functools import partial

class mw:

    def __init__(self, menu):
        self.menu = menu
        print("test1")
        self.initUI()

    def initUI(self):
        print("test2")
        root = Tk()
        root.geometry('300X200+100+200')
        root.title('Plus')
        num1 = StringVar()
        num2 = StringVar()

        lb1 = Label(root, text="num1").grid(row=1, column=0)
        lb2 = Label(root, text="num2").grid(row=2, column=0)
        lbr = Label(root)
        lbr.grid(row=7, column=2)
        entry_num1 = Entry(root, textvariable=num1).grid(row=1, column=2)
        entry_num2 = Entry(root, textvariable=num2).grid(row=2, column=2)
        show_result = partial(self.show_result, lbr, num1, num2)

        btn = Button(root, text="Plus", command=show_result).grid(row=3, column=0)

        root = mainloop()
        print("test2")


    def ComboBoxEvent(self, text):
            self.label1.setText(text)
            self.label1.adjustSize()

    def show_result(lbr, n1, n2):
        num_1 = (n1.get())
        num_2 = (n2.get())
        result = int(num_2) + int(num_2)
        lbr.config(text="result = %d" % result)
        return


