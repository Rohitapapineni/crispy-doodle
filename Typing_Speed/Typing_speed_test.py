import time
import tkinter as tk
from tkinter.ttk import Label
from tkinter.ttk import Button
from datetime import datetime
from keyboard import press
root=tk.Tk()
import mysql.connector as ms
db=ms.connect(host='localhost',database='newdb',password='root',user='root')
mycursor=db.cursor()
mycursor1=db.cursor()
intro='''
- First click the NEXT button after reading all the rules
- Enter the level you want and click on the SUBMIT button
- Then press the READY button once you are ready to take the test
- The text will be appeared after clicking on the READY button 
- The clock will start once u press on the READY button
- Start typing..
- Your speed will be calculated according to the correct words you enter

'''

username_entry=tk.StringVar()
password_entry=tk.StringVar()
level_entry=tk.StringVar()
speedcheck_entry=tk.StringVar()

def level():
    global level_entry
    global level_window
    global wlc_window
    wlc_window.destroy()
    level_window=tk.Toplevel()
    level_window.geometry('900x600')
    level_window['background']='light goldenrod'
    llabel3=tk.Label(level_window,text='Enter the level of the test you need:\n1.Easy \n2.Intermediate \n3.Advanced\n',font=('Verdana',14),bg='light goldenrod',fg='DeepSkyBlue').place(relx=0.5,rely=0.3,anchor='center')
    eentry1=tk.Entry(level_window,textvariable=level_entry)
    eentry1.place(relx=0.5,rely=0.4,anchor='center')
    eentry1.focus()
    bbutton2=tk.Button(level_window,text='SUBMIT',command=checkprg).place(relx=0.5,rely=0.5,anchor='center')
    

def checkprg():
    global k
    global level_window
    global text
    level_window.destroy()
    if level_entry.get()=='1':
        f=open(r'easy_prg.txt','r')
        k=f.read()
        text=k.split()
        f.close()
        
    elif level_entry.get()=='2':
        f=open(r'intermediate_prg.txt','r')
        k=f.read()
        text=k.split()
        f.close()
        
    elif level_entry.get()=='3':
        f=open(r'advanced_prg.txt','r')
        k=f.read()
        text=k.split()
        f.close()
        
    else:
        print('Invalid entry')
    ready()
    
def ready():
    global k
    global ready_window
    level_window.destroy()
    ready_window=tk.Toplevel()
    ready_window.geometry('900x600')
    ready_window['background']='thistle'
    llabel4=tk.Label(ready_window,text='Once you are ready to start typing, click on READY button down below',font=('Verdana',14),bg='thistle',fg='blue4').place(relx=0.5,rely=0.4,anchor='center')
    bbutton3=tk.Button(ready_window,text='READY',command=input,bg='salmon',fg='DodgerBlue4').place(relx=0.5,rely=0.5,anchor='center')


def wlc_page():
    global wlc_window
    global records_window
    global new_window2
    global speedcheck_window
    try:
        if bool(speedcheck_window.winfo_exists())==True:
            speedcheck_window.destroy()
    except (NameError, AttributeError):
        pass
    try:
        if bool(records_window.winfo_exists())==True:
            records_window.destroy()
    except (NameError, AttributeError):
        pass
    try:
        if bool(new_window2.winfo_exists())==True:
            new_window2.destroy()
    except (NameError, AttributeError):
        pass
    wlc_window=tk.Toplevel()
    wlc_window.geometry('900x600')
    wlc_window['background']='RoyalBlue3'
    llabel1=tk.Label(wlc_window,text='Hey there! So this is how it goes',font=('Verdana', 15),bg='RoyalBlue3',fg='PaleTurquoise2').place(relx=0.5,rely=0.25,anchor='center')
    llabel2=tk.Label(wlc_window,text=intro,font=('Verdana', 13),bg='RoyalBlue3',fg='thistle1').place(relx=0.5,rely=0.5,anchor='center')
    bbutton1=tk.Button(wlc_window,text='NEXT',font=('Verdana', 15),bg='plum1',fg='black',command=level).place(relx=0.5,rely=0.7,anchor='center')

def input():
    global k
    global start_time
    global speedcheck_entry
    global input_window
    global ready_window
    global text
    ready_window.destroy()
    input_window=tk.Toplevel()
    input_window['background']='pale green'
    input_window.geometry('900x600')
    llabel5=tk.Label(input_window,text=k,font=('Verdana',15),bg='pale green',fg='dark slate gray').place(relx=0.5,rely=0.3,anchor='center')
    eentry2=tk.Entry(input_window,textvariable=speedcheck_entry)
    eentry2.place(relx=0.5,rely=0.7,anchor='center',height=200, width=800)
    eentry2.focus()
    start_time = time.time()
    bbutton4=tk.Button(input_window,text='Done',font=('Verdana',14),command=speedcheck,bg='midnight blue',fg='snow2').place(relx=0.5,rely=0.9,anchor='center')

    
def speedcheck():
    global k
    global speedcheck_entry
    global start_time
    global input_window
    global speedcheck_window
    global speed
    global entry1
    global date_time
    now = datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')
    unm=username_entry.get()
    input_window.destroy()
    time_taken=time.time()-start_time
    speedcheck_window=tk.Toplevel()
    speedcheck_window.geometry('900x600')
    speedcheck_window['background']='CadetBlue1'
    total_words=k.split()
    entered_words=(speedcheck_entry.get()).split()
    errorcount=0
    correct_words=0
    for i in range(0,len(entered_words)):
        if total_words[i]==entered_words[i]:
            correct_words+=1
        else:
            errorcount+=1
    speed=round((correct_words/(time_taken/60)),2)
    accuracy=round(((correct_words/len(total_words))*100),0)
    llabel6=tk.Label(speedcheck_window,text=('Speed:'+str(speed)+'WPM'),font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.2,anchor='center')
    llabel7=tk.Label(speedcheck_window,text=('Accuracy:'+str(accuracy)+'%'),font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.3,anchor='center')
    if speed<=26:
        llabel8=tk.Label(speedcheck_window,text=str(speed)+"WPM is very slow, but it's ok, you can improve",font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.4,anchor='center')
    elif speed>26 and speed<=35:
        llabel8=tk.Label(speedcheck_window,text=str(speed)+"WPM is a slow speed, but you can improve",font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.4,anchor='center')
    elif speed>35 and speed<=45:
        llabel8=tk.Label(speedcheck_window,text=str(speed)+"WPM is an intermediate speed",font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.4,anchor='center')
    else:
        llabel8=tk.Label(speedcheck_window,text=str(speed)+"WPM is a really good speed",font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.4,anchor='center')        
    llabell=tk.Label(speedcheck_window,text='Thank you for taking the test!!',font=('Verdana',14),bg='CadetBlue1',fg='red3').place(relx=0.5,rely=0.5,anchor='center')
    mycursor.execute("insert into SPEED(Username,Date_Time,Speed) values('{}','{}',{})".format(unm,date_time,speed))
    db.commit()
    bbuttonn1=tk.Button(speedcheck_window,text='Take another test',font=('Verdana',14),bg='saddle brown',fg='white',command=lambda:[wlc_page(),quit]).place(relx=0.53,rely=0.6,anchor='center')
    bbuttonn2=tk.Button(speedcheck_window,text='Main menu',font=('Verdana',14),bg='saddle brown',fg='white',command=lambda:[open_page(),quit]).place(relx=0.7,rely=0.6,anchor='center')
    bbuttonn3=tk.Button(speedcheck_window,text='Quit',font=('Verdana',14),bg='saddle brown',fg='white',command=quit).place(relx=0.8,rely=0.6,anchor='center')
    
def login():
    global username_entry
    global password_entry
    global open_window
    global login_window
    global entry1
    global entry2
    global newwindow
    try:
        if bool(newwindow.winfo_exists())==True:
            newwindow.destroy()
    except (NameError, AttributeError):
        pass
    open_window.destroy()
    login_window=tk.Toplevel()
    login_window.geometry('900x600')
    login_window['background']='turquoise'

    label2=tk.Label(login_window,text='PLEASE ENTER YOUR DETAILS BELOW',font=('Verdana',16),bg='turquoise',fg='salmon').place(relx=0.5,rely=0.3,anchor='center')
    label3=tk.Label(login_window,text='Username',font=('Verdana',14),bg='turquoise',fg='peach puff').place(relx=0.4,rely=0.4,anchor='center')
    entry1=tk.Entry(login_window,textvariable=username_entry)
    entry1.place(relx=0.55,rely=0.4,anchor='center')
    entry1.focus()
    label4=tk.Label(login_window,text='Password',font=('Verdana',14),bg='turquoise',fg='peach puff').place(relx=0.4,rely=0.5,anchor='center')
    entry2=tk.Entry(login_window,textvariable=password_entry).place(relx=0.55,rely=0.5,anchor='center')
    button4=tk.Button(login_window,text='SUBMIT',font=('Verdana',14),command=check_login,bg='dodger blue',fg='white').place(relx=0.55,rely=0.6,anchor='center')


def previous_records():
    global login_window
    login_window.destroy()
    global records_window
    global sign_up_window
    try:
        if bool(sign_up_window.winfo_exists())==True:
            sign_up_window.destroy()
    except (NameError, AttributeError):
        pass
    records_window=tk.Toplevel()
    records_window.geometry('900x600')
    records_window['background']='black'
    label11=tk.Label(records_window,text='Do you want to check your previous results?',font=('Verdana',16),bg='black',fg='IndianRed3').place(relx=0.5,rely=0.4,anchor='center')
    button_yes=tk.Button(records_window,text='YES',command=records,bg='grey',fg='black').place(relx=0.4,rely=0.5,anchor='center')
    button_no=tk.Button(records_window,text='NO, Take a new test',command=wlc_page,bg='grey',fg='black').place(relx=0.5,rely=0.5,anchor='center')

def records():
    global records_window
    global date_time
    global entry1
    global new_window2
    usernm=username_entry.get()
    records_window.destroy()
    new_window2=tk.Toplevel()
    new_window2.geometry('900x600')
    new_window2['background']='Lavender'
    mycursor.execute("select * from SPEED where Username='{}'".format(usernm))
    row1=mycursor.fetchall()
    x=0
    if len(row1)==0:
            labelll=tk.Label(new_window2,text='No results yet',font=('Verdana',16),bg='Lavender',fg='navy').place(relx=0.5,rely=0.5,anchor='center')
            button7=tk.Button(new_window2,text='Take a New Test',command=wlc_page,bg='medium purple',fg='light cyan').place(relx=0.2,rely=0.6,anchor='center')
            button8=tk.Button(new_window2,text='Quit',command=quit1,bg='medium purple',fg='light cyan').place(relx=0.8,rely=0.6,anchor='center')
        
    for i in range(0,len(row1)):
        x+=1
        label13=tk.Label(new_window2,text='Date and Time:'+row1[i][1],font=('Verdana',16),bg='Lavender',fg='navy').pack()
        label14=tk.Label(new_window2,text='Speed:'+str(row1[i][2])+'WPM',font=('Verdana',16),bg='Lavender',fg='navy').pack()
        if i==len(row1)-1:
            button7=tk.Button(new_window2,text='Take a New Test',command=wlc_page,bg='medium purple',fg='light cyan').place(relx=0.2,rely=0.6,anchor='center')
            button8=tk.Button(new_window2,text='Quit',command=quit1,bg='medium purple',fg='light cyan').place(relx=0.8,rely=0.6,anchor='center')
        
def quit1():
    global new_window2
    new_window2.destroy()
    
def check_login():
    global entry1
    global entry2
    global login_window
    global relogin_window
    un=username_entry.get()
    pw=password_entry.get()
    mycursor.execute("SELECT * from USERS where Username ='{}' AND Password='{}'".format(un,pw))
    row=mycursor.fetchone()
    if row==None:
        try:
            if bool(login_window.winfo_exists())==True:
                login_window.destroy()
        except (NameError, AttributeError):
            pass
        relogin_window=tk.Toplevel()
        relogin_window.geometry('900x600')
        relogin_window['background']='old lace'
        label10=tk.Label(relogin_window,text="Looks like You haven't signed up earlier.Click on the button below to sign up.",font=('Verdana',16),bg='old lace',fg='goldenrod').place(relx=0.5,rely=0.5,anchor='center')
        button10=tk.Button(relogin_window,text='SIGN UP',command=sign_up,bg='salmon3',fg='white').place(relx=0.5,rely=0.6,anchor='center')
    else:
        previous_records()

       
new_username_entry=tk.StringVar()
new_emailid_entry=tk.StringVar()
new_password_entry=tk.StringVar()

def sign_up():
    global open_window
    open_window.destroy()
    global sign_up_window
    global entry6
    global entry7
    global entry8
    global relogin_window
    try:
        if bool(relogin_window.winfo_exists())==True:
            relogin_window.destroy()
    except (NameError, AttributeError):
        pass
    sign_up_window=tk.Toplevel()
    sign_up_window.geometry('900x600')
    sign_up_window['background']='AntiqueWhite3'
    label5=tk.Label(sign_up_window,text='FILL UP THE FOLLOWING DETAILS AND GET STARTED!',font=('Verdana',14),bg='AntiqueWhite3',fg='black').place(relx=0.5,rely=0.3,anchor='center')
    label6=tk.Label(sign_up_window,text='Username',font=('Verdana',14),bg='AntiqueWhite3',fg='black').place(relx=0.45,rely=0.4,anchor='center')
    label7=tk.Label(sign_up_window,text='Email ID',font=('Verdana',14),bg='AntiqueWhite3',fg='black').place(relx=0.45,rely=0.5,anchor='center')
    label8=tk.Label(sign_up_window,text='Password',font=('Verdana',14),bg='AntiqueWhite3',fg='black').place(relx=0.45,rely=0.6,anchor='center')
    entry6=tk.Entry(sign_up_window,textvariable=new_username_entry)
    entry6.place(relx=0.59,rely=0.4,anchor='center')
    entry6.focus()
    entry7=tk.Entry(sign_up_window,textvariable=new_emailid_entry).place(relx=0.59,rely=0.5,anchor='center')
    entry8=tk.Entry(sign_up_window,textvariable=new_password_entry).place(relx=0.59,rely=0.6,anchor='center')
    button5=tk.Button(sign_up_window,text='SUBMIT',command=back_login,bg='RosyBrown4',fg='white').place(relx=0.5,rely=0.7,anchor='center')
    

def back_login():
    global entry6
    global entry7
    global entry8
    global newwindow
    v1=new_username_entry.get()
    v2=new_emailid_entry.get()
    v3=new_password_entry.get()
    mycursor.execute("insert into USERS(Username,Email_ID,Password)values('{}','{}','{}')".format(v1,v2,v3))
    db.commit()
    newwindow=tk.Toplevel()
    newwindow.geometry('900x600')
    newwindow['background']='green yellow'
    global sign_up_window
    sign_up_window.destroy()
    label9=tk.Label(newwindow,text="Congrats! You have successfully created an account.\n Now click on the 'LOGIN' Button below and enter your details",bg='green yellow',fg='dark orange',font=('Verdana',16)).place(relx=0.5,rely=0.4,anchor='center')
    button6=tk.Button(newwindow,text='LOGIN',command=login,bg='orange red',fg='white').place(relx=0.5,rely=0.5,anchor='center')
    

def open_page():
    global open_window
    global speedcheck_window
    try:
        if bool(speedcheck_window.winfo_exists())==True:
            speedcheck_window.destroy()
    except (NameError, AttributeError):
        pass
    open_window=tk.Toplevel(root)
    root.withdraw()
    open_window.geometry('900x600')
    open_window['background']='pale turquoise'
    label1=tk.Label(open_window,text='Hello there!',font=('Verdana',16),bg='pale turquoise',fg='white').place(relx=0.5,rely=0.4,anchor='center')
    button2=tk.Button(open_window,text='LOGIN',font=('Verdana',15),command=login,bg='dodger blue',fg='DarkOrange3').place(relx=0.45,rely=0.5,anchor='center')
    button3=tk.Button(open_window,text='SIGN UP',font=('Verdana',15),command=sign_up,bg='dodger blue',fg='DarkOrange3').place(relx=0.55,rely=0.5,anchor='center')
    
open_page()
