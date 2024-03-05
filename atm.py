balance1=98456.25
usr_password=1234

from tkinter import *
import time as time
from PIL import Image, ImageTk

win=Tk()
win.geometry=('800x800')
win.title('ATM SOFTWARE')

def hide_widgets(e):
    if e=='A':
        withdraw_entry.place_forget()
        btn1.place_forget()
        
        deposit_entry.place_forget()
        btn2.place_forget()
        
        old_pin_entry.place_forget()
        new_pin_entry.place_forget()
        btn3.place_forget()
        
    elif e=='D':
        withdraw_entry.place_forget()
        btn1.place_forget()
        
        old_pin_entry.place_forget()
        new_pin_entry.place_forget()
        btn3.place_forget()
        
    elif e=='W':
        deposit_entry.place_forget()
        btn2.place_forget()
        
        old_pin_entry.place_forget()
        new_pin_entry.place_forget()
        btn3.place_forget()
        
    elif e=='P':
        withdraw_entry.place_forget()
        btn1.place_forget()
         
        deposit_entry.place_forget()
        btn2.place_forget()
     
        
def show_widgets(z):
    
    if z=='W':
        withdraw_entry.place(x=650,y=500)
        btn1.place(x=650,y=600)
        
    elif z=='D':
        deposit_entry.place(x=650,y=500)
        btn2.place(x=650,y=600)
        
    elif z=='P':
        old_pin_entry.place(x=600,y=500)
        new_pin_entry.place(x=600,y=600)
        btn3.place(x=700,y=650)  
        
def balance():
    hide_widgets('A')
    show_label.config(text='')
    withdraw_label.config(text='')
    deposit_label.config(text='')
    balance_label.config(text='')
    old_pin.config(text='')
    new_pin.config(text='')
    
    text_bal='Your current balance is : Rs '+str(balance1)
    balance_label.config(text=text_bal)
    
    

def withdraw():
    show_widgets('W')
    hide_widgets('W')
    
    show_label.config(text='')
    withdraw_label.config(text='')
    deposit_label.config(text='')
    balance_label.config(text='')
    old_pin.config(text='')
    new_pin.config(text='')
    
    def show():
        global balance1
        
        if int(withdraw_entry.get())> balance1:
            show_label.config(text='Withdraw amount is greater than balance')
        else:
            show_label.config(text='You have withdrawn ' + ' Rs '+ withdraw_entry.get())
            balance1=balance1-int(withdraw_entry.get())
            
            withdraw_entry.delete(0,END)
    
    
    
    
    text_withdraw='Enter the amount you wish to withdraw: '
    withdraw_label.config(text=text_withdraw)
    
    btn1.config(command=show)
    
  

def deposit():
    hide_widgets('D')
    show_widgets('D')
    
    show_label.config(text='')
    withdraw_label.config(text='')
    deposit_label.config(text='')
    balance_label.config(text='')
    old_pin.config(text='')
    new_pin.config(text='')
    
    def show2():
        global balance1
        
        show_label.config(text='You have deposited ' + ' Rs '+ deposit_entry.get())
        balance1=balance1+int(deposit_entry.get())
        deposit_entry.delete(0,END)
    
    text_deposit='Enter the amount you wish to deposit :'
    deposit_label.config(text=text_deposit)
    
    btn2.config(command=show2)
    
  
def change():
    hide_widgets('P')
    show_widgets('P')
    
    show_label.config(text='')
    withdraw_label.config(text='')
    deposit_label.config(text='')
    balance_label.config(text='')
    old_pin.config(text='')
    new_pin.config(text='')
    
    def show3():
        global usr_password
        
        
        usr_password=int(new_pin_entry.get())
        show_label.config(text='Your pin has been successfully changed')
        old_pin_entry.delete(0,END)
        new_pin_entry.delete(0,END)
    
    old_pin.config(text='Enter the old pin:')
    new_pin.config(text='Enter the new pin:')
    
    
    btn3.config(command=show3)
    
    
back_ground=Image.open('atm.jpg')
back_ground=ImageTk.PhotoImage(back_ground,master=win)

back_label=Label(win,image=back_ground)
back_label.image=back_ground
back_label.pack(fill='both', expand='yes')

bank_text=Label(win,text='Welcome to XYZ Bank', bg='orange',fg='white',font=("Arial Bold",30))
bank_text.place(x=200,y=50)


view_account_balance=Button(win, text='1.  Account Balance',justify='left',width=25,height=1,cursor='hand2',bg='burlywood1',
                            activeforeground='white',activebackground='burlywood1',bd=0,fg='white',font=("Arial",20),command=balance)

view_account_balance.place(x=200,y=150)

withdraw_cash=Button(win, text='2.   Withdraw Cash',justify='left',width=25,height=1,cursor='hand2',bg='orange',
                            activeforeground='white',activebackground='orange',bd=0,fg='white',font=("Arial",20),command=withdraw)

withdraw_cash.place(x=200,y=200)


deposit_cash=Button(win, text='3.    Deposit Cash',justify='left',width=25,height=1,cursor='hand2',bg='burlywood1',
                            activeforeground='white',activebackground='burlywood1',bd=0,fg='white',font=("Arial",20),command=deposit)

deposit_cash.place(x=200,y=250)

change_pin=Button(win, text='4.     Change Pin',justify='left',width=25,height=1,cursor='hand2',bg='orange',
                            activeforeground='white',activebackground='orange',bd=0,fg='white',font=("Arial",20),command=change)

change_pin.place(x=200,y=300)

logout_and_exit=Button(win, text='5.   Logout and Exit ',justify='left',width=25,height=1,cursor='hand2',bg='burlywood1',
                            activeforeground='white',activebackground='burlywood1',bd=0,fg='white',font=("Arial",20),command=lambda:win.destroy())

logout_and_exit.place(x=200,y=350)

balance_label=Label(win,text='',bg='orange',fg='white',font=("Arial",17))
balance_label.place(x=100,y=500)

withdraw_label=Label(win,text='',bg='orange',fg='white',font=("Arial",17))
withdraw_label.place(x=200,y=500)

deposit_label=Label(win,text='',bg='orange',fg='white',font=("Arial",17))
deposit_label.place(x=200,y=500)

old_pin=Label(win,text='',bg='orange',fg='white',font=("Arial",17))
old_pin.place(x=200,y=500)

new_pin=Label(win,text='',bg='orange',fg='white',font=("Arial",17))
new_pin.place(x=200,y=600)

show_label=Label(win,text='',bg='orange',fg='white',font=("Arial",17))
show_label.place(x=250,y=650)

withdraw_entry=Entry(win,bg='burlywood1')
withdraw_entry.place(x=650,y=500)

withdraw_entry.place_forget()

btn1=Button(win,text='SUBMIT',bg='burlywood1')
btn1.place(x=650,y=600)
btn1.place_forget()

deposit_entry=Entry(win,bg='orange')
deposit_entry.place(x=650,y=500)

deposit_entry.place_forget()

btn2=Button(win,text='SUBMIT',bg='burlywood1')
btn2.place(x=650,y=600)
btn2.place_forget()

oldpin=StringVar()
newpin=StringVar()

old_pin_entry=Entry(win,show='*',textvariable=oldpin,bg='burlywood1')
old_pin_entry.place(x=600,y=500)
old_pin_entry.place_forget()


new_pin_entry=Entry(win,show='*',textvariable=newpin,bg='burlywood1')
new_pin_entry.place(x=600,y=600)
new_pin_entry.place_forget()

btn3=Button(win,text="SUBMIT",bg='burlywood1')
btn3.place(x=700,y=650)
btn3.place_forget()

win.mainloop()
