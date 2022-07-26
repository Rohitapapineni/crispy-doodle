import tkinter as tk
from tkinter import *
import math
from tkinter.ttk import *

root = tk.Tk()
root.geometry('475x580+750+200')
root.title('Scientific Calculator')
root.configure(background='blanched almond')
number1 = tk.StringVar()
number1.set("")

# The .grid method of a widget always returns None. So, you need to place the calls to .pack on their own line
txtDisplay = tk.Entry(root, textvariable=number1,bg='blanched almond', font=('Roboto', 20, 'bold'), bd=15, width=10, justify=RIGHT)
txtDisplay.grid(row=1, columnspan=20, ipadx=20, ipady=10, sticky="WE")

txtDisplay.insert(0, "0")

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        if self.op == "power":
            self.total **= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def gamma(self):
        self.result = False
        self.current = math.gamma(float(txtDisplay.get()))
        self.display(self.current)

    def sin_inv(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.asin(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.asin(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def cos_inv(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.acos(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.acos(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def tan_inv(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.atan(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.atan(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def sinh(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.sinh(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.sinh(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def cosh(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.cosh(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.cosh(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def tanh(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.tanh(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.tanh(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def sin(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.sin(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.sin(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def cos(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.cos(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.cos(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def tan(self):
        self.result = False
        if deg_mode == 1:
            self.current = math.tan(math.radians(float(txtDisplay.get())))
        elif deg_mode == 2:
            self.current = math.tan(math.radians(degree_converter(float(txtDisplay.get()))))
        self.display(self.current)

    def fact(self):
        self.result = False
        self.current = math.factorial(float(txtDisplay.get()))
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def rad(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)


def degree_converter(x):
    pi_value = math.pi
    degree = (x * 180) / pi_value
    return degree

added_value = Calc()

button_Equalto = tk.Button(root, text=' = ', command=added_value.sum_of_total,bg='dark salmon', font=('Roboto', 15, 'bold'), height=2,
                           width=7).grid(row=8, column=3)
button1 = tk.Button(root, text=' 1 ', command=lambda: added_value.numberEnter(1),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=7,
                                  column=1)
button2 = tk.Button(root, text=' 2 ', command=lambda: added_value.numberEnter(2),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=7,
                                  column=2)
button3 = tk.Button(root, text=' 3 ', command=lambda: added_value.numberEnter(3),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=7,
                                  column=3)
button4 = tk.Button(root, text=' 4 ', command=lambda: added_value.numberEnter(4),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=6,
                                  column=1)
button5 = tk.Button(root, text=' 5 ', command=lambda: added_value.numberEnter(5),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=6,
                                  column=2)
button6 = tk.Button(root, text=' 6 ', command=lambda: added_value.numberEnter(6),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=6,
                                  column=3)
button7 = tk.Button(root, text=' 7 ', command=lambda: added_value.numberEnter(7),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=5,
                                  column=1)
button8 = tk.Button(root, text=' 8 ', command=lambda: added_value.numberEnter(8),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=5,
                                  column=2)
button9 = tk.Button(root, text=' 9 ', command=lambda: added_value.numberEnter(9),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=5,
                                  column=3)
button0 = tk.Button(root, text=' 0 ', command=lambda: added_value.numberEnter(0),bg='blanched almond', font=('Roboto', 15, 'bold'), height=2,
                    width=7).grid(row=8,column=2)
button_dot = tk.Button(root, text=' . ', command=lambda: added_value.numberEnter("."), bg='light goldenrod yellow', font=('Roboto', 15, 'bold'),
                       height=2, width=7).grid(row=8,column=1)

button_sin = tk.Button(root, text='sin', command=added_value.sin,  bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=2, column=1)
button_cos = tk.Button(root, text='cos', command=added_value.cos,  bg='light goldenrod yellow',font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=2, column=2)
button_tan = tk.Button(root, text='tan', command=added_value.tan, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=2, column=3)
button_log = tk.Button(root, text='log', command=added_value.log, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=3, column=4)
button_mult = tk.Button(root, text=' * ', command=lambda: added_value.operation("multi"), bg='light goldenrod yellow', font=('Roboto', 15, 'bold'),
                        height=2, width=7).grid(row=5,column=4)
button_add = tk.Button(root, text=' + ', command=lambda: added_value.operation('add'), bg='light goldenrod yellow', font=('Roboto', 15, 'bold'),
                       height=2, width=7).grid(row=4, column=4)
button_minus = tk.Button(root, text=' - ', command=lambda: added_value.operation('sub'), bg='light goldenrod yellow', font=('Roboto', 15, 'bold'),
                         height=2, width=7).grid(row=6, column=4)
button_divide = tk.Button(root, text=' ÷ ', command=lambda: added_value.operation('divide'), bg='light goldenrod yellow',
                          font=('Roboto', 15, 'bold'), height=2, width=7).grid(row=7, column=4)
button_pi = tk.Button(root, text=' π ', command=added_value.pi, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(row=4, column=3)
button_ac = tk.Button(root, text=' AC ', command=added_value.All_Clear_Entry,bg='dark salmon', font=('Roboto', 15, 'bold'), height=2,
                      width=7).grid(row=4, column=2)
button_del = tk.Button(root, text='DEL', command=added_value.Clear_Entry,bg='dark salmon', font=('Roboto', 15, 'bold'), height=2,
                       width=7).grid(row=4, column=1)
button_sq_root = tk.Button(root, text=' √ ', command=added_value.sqrt, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                           width=7).grid(row=3, column=1)
button_sin_inv = tk.Button(root, text='sin⁻¹', command=added_value.sin_inv, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                           width=7).grid(row=2, column=4)
button_cos_inv = tk.Button(root, text='cos⁻¹', command=added_value.cos_inv, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                           width=7).grid(row=2, column=5)
button_tan_inv = tk.Button(root, text='tan⁻¹', command=added_value.tan_inv, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                           width=7).grid(row=3, column=5)
button_power = tk.Button(root, text='xʸ', command=lambda: added_value.operation('power'), bg='light goldenrod yellow', font=('Roboto', 15, 'bold'),
                         height=2, width=7).grid(row=8, column=4)
button_deg = tk.Button(root, text='deg', command=added_value.deg, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=7, column=5)
button_rad = tk.Button(root, text='rad', command=added_value.rad, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=8, column=5)
button_sinh = tk.Button(root, text='sinh', command=added_value.sinh, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                        width=7).grid(row=4, column=5)
button_cosh = tk.Button(root, text='cosh', command=added_value.cosh, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                        width=7).grid(row=5, column=5)
button_tanh = tk.Button(root, text='tanh', command=added_value.tanh, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2,
                        width=7).grid(row=6, column=5)
button_e = tk.Button(root, text='e', command=added_value.e, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(row=3,
                                                                                                                 column=3)
button_fact = tk.Button(root, text='!', command=added_value.fact, bg='light goldenrod yellow', font=('Roboto', 15, 'bold'), height=2, width=7).grid(
    row=3, column=2)
isselected = False


def sel(r):
    global isselected
    if isselected:
        r.deselect()
    else:
        isselected = True

def my_upd():
    global deg_mode
    if (var1.get() == 1):
        deg_mode = 1
    elif (var1.get() == 2):
        deg_mode = 2

deg_mode = 1
var1 = IntVar()
R1 = Radiobutton(root, text="Radians", variable=var1, value=1, command=my_upd).grid(row=9, column=1)
R2 = Radiobutton(root, text="Degree", variable=var1, value=2, command=my_upd).grid(row=9, column=2)

root.mainloop()
