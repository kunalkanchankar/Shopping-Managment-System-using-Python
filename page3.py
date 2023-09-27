from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import pywhatkit
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime



screen1 = Tk()

#screen1 = Toplevel(root)
screen1.title("New Order Page")
screen1.geometry('925x500+300+200')
screen1.config(bg='white')
screen1.resizable(False,False)

frame1 = Frame(screen1,width=950,height=550,bg="white")
frame1.place(x=5,y=5)

p2now = datetime.now()
p2date = p2now.strftime("CustID%Y%m%d%H%M%S")

connect = mysql.connector.connect(host='localhost',user='root',passwd='root123',database='grocerym',port='3306')
conn = connect.cursor()
p3adrs = (p2date, )
conn.execute("select * from additem where cusid = %s",p3adrs)

p3columns = ('pname','quantity','pprice','tprice')
p3tree = ttk.Treeview(frame1,columns=p3columns,show="headings")
p3tree.heading('pname',text="Product Name")
p3tree.heading('quantity',text="No.of Item")
p3tree.heading('pprice',text="Product Price")
p3tree.heading('tprice',text="Total Price")

i=0

for row in conn:
    p3tree.insert('',i,text="",values=(row[2],row[3],row[4],row[5]))
    i = i+1

p3tree.place(x=50,y=150)

def totalprice():
    conn.execute("select * from additem where cusid = '"+p2date+"'")
    i=0
    t=0
    for row in conn:
        var = row[5]
        t = int(var) + t
        total = "Total Price : "+str(t)+" /-"
        l4 = Label(frame1,text=total,bg='red',font=('Time',11,'bold'))
        l4.place(x=30,y=400)
        
        i = i+1


def insert(): 
    pname = combobox.get()
    quantity = e2.get()
    pprice = e3.get()
    if(pname or quantity or pprice):
        price = int(quantity)*int(pprice)
        conn.execute('Insert into additem (cusid,mobileno,productname,quantity,productprice,totalprice) values (%s,%s,%s,%s,%s,%s)',(p2date,'-',pname,quantity,pprice,price))
        connect.commit()
        p3tree.insert('','end',text="",values=(pname,quantity,pprice,price))
        #e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        totalprice()
        #bmessagebox.showinfo("Inserted","Your item Added ")
    else:
        print()
        #messagebox.showinfo("Invaild Input","Invaild Input")
    

def deleteitem():
    selecteditem = p3tree.selection()[0]
    print(p3tree.item(selecteditem)['values'])
    uid = p3tree.item(selecteditem)['values'][0]
    delquery = "delete from additem where productname = %s"
    selitem = (uid,)
    conn.execute(delquery,selitem)
    connect.commit()
    p3tree.delete(selecteditem)
    totalprice()
   # messagebox.showinfo("Deleted","Selected item deleted")


entryframe = Frame(frame1,width=900,height=100,bg="white")
entryframe.place(x=10,y=40)
Label(frame1,text='Add Product',bg='#fff',font=('Time',10,'bold')).place(x=455,y=10)
Label(frame1,text=p2date,bg='red',font=('Time',10,'bold')).place(x=30,y=20)

l1 = Label(entryframe,text='Product Name :',bg='#fff',font=('Time',9,'bold'))
l1.place(x=10,y=10)
lst = []
conn.execute("select * from productlist ")
i=0
t=0
for row in conn:
    lst.append(row[1])
combobox = ttk.Combobox(entryframe,width=20,height=8, values=lst,font=('Time',12,''))
combobox.set(" ")
combobox.place(x=10,y=35)
Frame(entryframe,width=200,height=2,bg='black').place(x=10,y=58)

l2 = Label(entryframe,text='No.of item :',bg='#fff',font=('Time',9,'bold'))
l2.place(x=220,y=10)
e2 = Entry(entryframe,width=15,fg='black',border=0,bg="white",font=('Time',12,''))
e2.place(x=220,y=35)
Frame(entryframe,width=150,height=2,bg='black').place(x=220,y=58)

l3 = Label(entryframe,text='Product Price :',bg='#fff',font=('Time',9,'bold'))
l3.place(x=400,y=10)
e3 = Entry(entryframe,width=15,fg='black',border=0,bg="white",font=('Time',12,''))
e3.place(x=400,y=35)
Frame(entryframe,width=150,height=2,bg='black').place(x=400,y=58)

b1 = Button(entryframe,width=15,pady=3,text=' + Add  ',font=('Time',12,'bold'),border=0,bg='#57a1f8',fg='white',command=insert)
b1.place(x=600,y=30)

b2 = Button(frame1,width=25,pady=3,text=' - Remove item  ',font=('Time',12,'bold'),border=0,bg='#57a1f8',fg='white',command=deleteitem)
b2.place(x=550,y=400)

b3 = Button(frame1,pady=3,text=' EXIT ',bg='#F1F1F5',fg='red',font=('Time',12,'bold'),border=0,command=screen1.destroy)
b3.place(x=800,y=10)

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
    pywhatkit.sendwhatmsg("+919766748159",myorder,current_time.hour,current_time.minute+1)

b4 = Button(frame1,pady=3,width=25, text=' Save and Place Order ',font=('Time',12,'bold'),border=0,bg='#57a1f8',fg='white',command=orderplaced)
b4.place(x=100,y=400)


screen1.mainloop()
