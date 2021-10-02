from tkinter import *

root = Tk()
root.title("simple calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=15, pady=15)


# defining the functions

def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def add():
    global first_num
    first_num = e.get()
    global math
    math = "addition"
    e.delete(0, END)


def subtract():
    global first_num
    first_num = e.get()
    global math
    math = "subtraction"
    e.delete(0, END)


def multiply():
    global first_num
    first_num = e.get()
    global math
    math = "multiplication"
    e.delete(0, END)


def divide():
    global first_num
    first_num = e.get()
    global math
    math = "division"
    e.delete(0, END)


def equal():
    sec_number = e.get()
    e.delete(0, END)
    global math
    if math == "addition":
        e.insert(0, int(first_num) + int(sec_number))
    if math == "subtraction":
        e.insert(0, int(first_num) - int(sec_number))
    if math == "multiplication":
        e.insert(0, int(first_num) * int(sec_number))
    if math == "division":
        e.insert(0, int(first_num) / int(sec_number))


# define buttons
Button1 = Button(root, text="1", padx=40, pady=10, command=lambda: click(1))
Button2 = Button(root, text="2", padx=40, pady=10, command=lambda: click(2))
Button3 = Button(root, text="3", padx=40, pady=10, command=lambda: click(3))
Button4 = Button(root, text="4", padx=40, pady=10, command=lambda: click(4))
Button5 = Button(root, text="5", padx=40, pady=10, command=lambda: click(5))
Button6 = Button(root, text="6", padx=40, pady=10, command=lambda: click(6))
Button7 = Button(root, text="7", padx=40, pady=10, command=lambda: click(7))
Button8 = Button(root, text="8", padx=40, pady=10, command=lambda: click(8))
Button9 = Button(root, text="9", padx=40, pady=10, command=lambda: click(9))
Button0 = Button(root, text="0", padx=40, pady=10, command=lambda: click(0))
Button_add = Button(root, text="+", padx=86.45, pady=10, command=add)
Button_equal = Button(root, text="=", padx=86.45, pady=10, command=equal)
Button_clear = Button(root, text="clr", padx=37, pady=10, command=clear)

Button_subtract = Button(root, text="-", padx=40, pady=10, command=subtract)
Button_multiply = Button(root, text="*", padx=40, pady=10, command=multiply)
Button_divide = Button(root, text="/", padx=40, pady=10, command=divide)

# put these buttons on screen

Button0.grid(row=4, column=0)

Button9.grid(row=1, column=2)
Button8.grid(row=1, column=1)
Button7.grid(row=1, column=0)

Button6.grid(row=2, column=2)
Button5.grid(row=2, column=1)
Button4.grid(row=2, column=0)

Button3.grid(row=3, column=2)
Button2.grid(row=3, column=1)
Button1.grid(row=3, column=0)

Button_add.grid(row=4, column=1, columnspan=2)
Button_equal.grid(row=5, column=0, columnspan=2)
Button_clear.grid(row=5, column=2)

Button_subtract.grid(row=6, column=0)
Button_multiply.grid(row=6, column=1)
Button_divide.grid(row=6, column=2)

root.mainloop()