# Tkinter GUI library import

import tkinter as tk



#window 객체생성
window = tk.Tk()

#window title
window.title("Calculator")

#Disable Resizing (x, y)
window.resizable(False, False)


name = tk.StringVar()
name_entry = tk.Entry(window, width=14, textvariable=name)
name_entry.grid(column=1, row=1, columnspan=6)



#button fuction
def click_button_CE():
    name_entry.delete(first=0, last=tk.END)

def click_button_C():
    name_entry.delete(first=0,last=tk.END)

def click_button_plus():
    name_entry.insert(tk.END, "+")

def click_button_minus():
    name_entry.insert(tk.END, "-")

def click_button_multiply():
    name_entry.insert(tk.END, "*")

def click_button_devide():
    name_entry.insert(tk.END, "/")

def click_button_power():
    name_entry.insert(tk.END, "^")

def click_button_usd():
    str1 = name_entry.get()
    int_str = int(str1)
    result_int = int(int_str/1000)
    print(result_int)
    result_v = str(result_int)
    result = result_v+"USD"
    name_entry.delete(first=0,last=tk.END)
    name_entry.insert(tk.END, result)

def click_button_one():
    name_entry.insert(tk.END, "1")

def click_button_two():
    name_entry.insert(tk.END, "2")

def click_button_three():
    name_entry.insert(tk.END, "3")

def click_button_four():
    name_entry.insert(tk.END, "4")

def click_button_five():
    name_entry.insert(tk.END, "5")

def click_button_six():
    name_entry.insert(tk.END, "6")

def click_button_seven():
    name_entry.insert(tk.END, "7")

def click_button_eight():
    name_entry.insert(tk.END, "8")

def click_button_nine():
    name_entry.insert(tk.END, "9")

def click_button_zero():
    name_entry.insert(tk.END, "0")

def click_button_equal():
    str=name_entry.get()

    if "^" in str:
        indexNo = str.find("^")
        c = indexNo+1
        a = int(str[:indexNo])
        b = int(str[c:])
        print(a,b)
        result = pow(a, b)
    else:
        result=eval(str)

    name_entry.delete(first=0,last=tk.END)
    name_entry.insert(tk.END, result)

#import button
action = tk.Button(window, width=6, height=2, text="CE", command=click_button_CE)
action.grid(column=1, row=2)
action = tk.Button(window, width=6, height=2, text="C", command=click_button_C)
action.grid(column=2, row=2)
action = tk.Button(window, width=6, height=2, text="delete", command=click_button_C)
action.grid(column=3, row=2)
action = tk.Button(window, width=6, height=2, text="/", command=click_button_devide)
action.grid(column=4, row=2)
action = tk.Button(window, width=6, height=2, text="7", command=click_button_seven)
action.grid(column=1, row=3)
action = tk.Button(window, width=6, height=2, text="8", command=click_button_eight)
action.grid(column=2, row=3)
action = tk.Button(window, width=6, height=2, text="9", command=click_button_nine)
action.grid(column=3, row=3)
action = tk.Button(window, width=6, height=2, text="*", command=click_button_multiply)
action.grid(column=4, row=3)
action = tk.Button(window, width=6, height=2, text="4", command=click_button_four)
action.grid(column=1, row=4)
action = tk.Button(window, width=6, height=2, text="5", command=click_button_five)
action.grid(column=2, row=4)
action = tk.Button(window, width=6, height=2, text="6", command=click_button_six)
action.grid(column=3, row=4)
action = tk.Button(window, width=6, height=2, text="-", command=click_button_minus)
action.grid(column=4, row=4)
action = tk.Button(window, width=6, height=2, text="1", command=click_button_one)
action.grid(column=1, row=5)
action = tk.Button(window, width=6, height=2, text="2", command=click_button_two)
action.grid(column=2, row=5)
action = tk.Button(window, width=6, height=2, text="3", command=click_button_three)
action.grid(column=3, row=5)
action = tk.Button(window, width=6, height=2, text="+", command=click_button_plus)
action.grid(column=4, row=5)
action = tk.Button(window, width=6, height=2, text="^", command =click_button_power)
action.grid(column=1, row=6)
action = tk.Button(window, width=6, height=2, text="0", command=click_button_zero)
action.grid(column=2, row=6)
action = tk.Button(window, width=6, height=2, text="to USD", command=click_button_usd)
action.grid(column=3, row=6)
action = tk.Button(window, width=6, height=2, text="=", command=click_button_equal)
action.grid(column=4, row=6)


currency = tk.StringVar()
label_1 = tk.Label(window, width=7, text="Currency")
label_1.grid(column=1, row=7, columnspan=2)
currency_input = tk.Entry(window, width=10, textvariable=currency)
currency_input.grid(column=3, row=7, columnspan=3)


#start window
window.mainloop()
