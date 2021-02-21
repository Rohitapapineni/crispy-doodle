import tkinter as tk
from functools import partial
master=tk.Tk()
master.geometry('400x200+100+200')
master.title('Addition')

def call_result(n1,n2):
    num1=(number1.get())
    num2=(number2.get())
    result=int(num1)+int(num2)
    label5=tk.Label(master,text=result).grid(row=4,column=1)

number1=tk.StringVar()
number2=tk.StringVar()

label1 = tk.Label(master,text='Enter 1st number ').grid(row=1,column=1)
entry1 = tk.Entry(master,textvariable=number1).grid(row=1,column=2)

label2 = tk.Label(master,text='Enter 2nd number ').grid(row=2,column=1)
entry2 = tk.Entry(master,textvariable=number2).grid(row=2,column=2)


call_result=partial(call_result,number1,number2)
buttonCal=tk.Button(master,text='Add',command=call_result).grid(row=3,column=1)

master.mainloop()
