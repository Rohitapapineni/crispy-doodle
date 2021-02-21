import tkinter as tk
from functools import partial
master=tk.Tk()
master.geometry('600x400+200+300')
master.title('Calculator')

equation=''

def press(num):
    global equation
    equation+=str(num)
    eq.set(equation)

eq = tk.StringVar()

def equalto():
    global equation
    result=str(eval(equation))
    eq.set(result)

def clear():
    global equation
    equation=''
    eq.set(equation)

entry=tk.Entry(master,textvariable=eq).grid(row = 1 ,columnspan=16, ipadx=12, ipady=5, sticky= "WE")
    
button1=tk.Button(master,text='1',command=lambda:press(1),height=1,width=5).grid(row=6,column=1)
button2=tk.Button(master,text='2',command=lambda:press(2),height=1,width=5).grid(row=6,column=2)
button3=tk.Button(master,text='3',command=lambda:press(3),height=1,width=5).grid(row=6,column=3)
button4=tk.Button(master,text='4',command=lambda:press(4),height=1,width=5).grid(row=5,column=1)
button5=tk.Button(master,text='5',command=lambda:press(5),height=1,width=5).grid(row=5,column=2)
button6=tk.Button(master,text='6',command=lambda:press(6),height=1,width=5).grid(row=5,column=3)
button7=tk.Button(master,text='7',command=lambda:press(7),height=1,width=5).grid(row=4,column=1)
button8=tk.Button(master,text='8',command=lambda:press(8),height=1,width=5).grid(row=4,column=2)
button9=tk.Button(master,text='9',command=lambda:press(9),height=1,width=5).grid(row=4,column=3)
button0=tk.Button(master,text='0',command=lambda:press(0),height=1,width=5).grid(row=7,column=2)

plus=tk.Button(master,text='+',command=lambda:press('+'),height=1,width=5).grid(row=6,column=4)
minus=tk.Button(master,text='-',command=lambda:press('-'),height=1,width=5).grid(row=5,column=4)
mult=tk.Button(master,text='x',command=lambda:press('*'),height=1,width=5).grid(row=4,column=4)
div=tk.Button(master,text='/',command=lambda:press('/'),height=1,width=5).grid(row=7,column=4)
equalto=tk.Button(master,text='=',command=equalto,height=1,width=5).grid(row=7,column=3)
clear=tk.Button(master,text='C',command=clear,height=1,width=5).grid(row=7,column=1)

#entry=tk.Entry(master).grid(row=1,column=1)



master.mainloop()
