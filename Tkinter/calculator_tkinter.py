import tkinter as tk
from functools import partial
master=tk.Tk()
master.geometry('400x200+100+200')
master.title('Calculator')

def call_result_add(n1,n2):
    num1=(number1.get())
    num2=(number2.get())
    result=int(num1)+int(num2)
    label5=tk.Label(master,text=result).grid(row=5,column=1)

def call_result_subtract(n1,n2):
    num1=(number1.get())
    num2=(number2.get())
    result=int(num1)-int(num2)
    label5=tk.Label(master,text=result).grid(row=5,column=1)

def call_result_multiply(n1,n2):
    num1=(number1.get())
    num2=(number2.get())
    result=int(num1)*int(num2)
    label5=tk.Label(master,text=result).grid(row=5,column=1)

def call_result_divide(n1,n2):
    num1=(number1.get())
    num2=(number2.get())
    result=int(num1)/int(num2)
    label5=tk.Label(master,text=result).grid(row=5,column=1)

def call_result_percentage(n1,n2):
    num1=(number1.get())
    num2=(number2.get())
    result=(int(num1)/int(num2))*100
    label5=tk.Label(master,text=result).grid(row=5,column=1)

number1=tk.StringVar()
number2=tk.StringVar()

label1 = tk.Label(master,text='Enter 1st number ').grid(row=1,column=1)
entry1 = tk.Entry(master,textvariable=number1).grid(row=1,column=2)

label2 = tk.Label(master,text='Enter 2nd number ').grid(row=2,column=1)
entry2 = tk.Entry(master,textvariable=number2).grid(row=2,column=2)

call_result_add=partial(call_result_add,number1,number2)

call_result_subtract=partial(call_result_subtract,number1,number2)

call_result_multiply=partial(call_result_multiply,number1,number2)

call_result_divide=partial(call_result_divide,number1,number2)

call_result_percentage=partial(call_result_percentage,number1,number2)


buttonCal_add=tk.Button(master,text='Add',command=call_result_add).grid(row=3,column=1)

buttonCal_subtract=tk.Button(master,text='Subtract',command=call_result_subtract).grid(row=3,column=2)

buttonCal_multiply=tk.Button(master,text='Multiply',command=call_result_multiply).grid(row=3,column=3)

buttonCal_divide=tk.Button(master,text='Divide',command=call_result_divide).grid(row=4,column=1)

buttonCal_percentage=tk.Button(master,text='Percentage',command=call_result_percentage).grid(row=4,column=2)


master.mainloop()
