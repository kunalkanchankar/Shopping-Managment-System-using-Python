from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime
import pywhatkit

screen1 = Tk()

#screen1 = Toplevel(root)
screen1.title("New Order Page")
screen1.geometry('925x500+300+200')
screen1.config(bg='white')
screen1.resizable(False,False)


p2now = datetime.now()
p2date = p2now.strftime("CustID%Y%m%d%H%M%S")

connect = mysql.connector.connect(host='localhost',user='root',passwd='root123',database='grocerym',port='3306')
conn = connect.cursor()


def orderplaced():
    mpname = []
    mquantity=[]
    mprice=[]
    mpprice=[]
    conn.execute("select * from additem where cusid = '"+"CustID20230323215631"+"'")
    i=0
    t=0 
    msg2 = ""
    msg1 = "*Thankyou For Shopping* \nName  : Price*Quantity = Total\n"
    for row in conn:
        mpname.append(row[2])
        mquantity.append(row[3])
        mprice.append(row[4])
        mpprice.append(row[5])
        mp3total = row[5]
        t = int(mp3total) + t
        p3total = "Total Price : "+str(t)+"/-"
        msg2 += "\n{} : {}*{} = {}/- ".format(mpname[i],mprice[i],mquantity[i],mpprice[i])
        # print(msg2)
        i = i+1

    myorder = msg1+msg2+"\n*Total Billing Amount "+str(t)+"/-* \nBilling Time : "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # print(myorder) 
    current_time = datetime.now()
    pywhatkit.sendwhatmsg("+919766748159","myorder",current_time.hour,current_time.minute+1)

b4 = Button(screen1,pady=3,width=25, text=' Save and Place Order ',font=('Time',12,'bold'),border=0,bg='#57a1f8',fg='white',command=orderplaced)
b4.place(x=100,y=400)




screen1.mainloop()