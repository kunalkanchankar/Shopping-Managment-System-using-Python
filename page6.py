from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk

page6 = Tk()
#page6 = Toplevel(root)
page6.title("Stocks Details")
page6.geometry('925x500+300+200')
page6.config(bg='white')
page6.resizable(False,False)

connect = mysql.connector.connect(host='localhost',user='root',passwd='root123',database='grocerym',port='3306')
conn = connect.cursor()
	
p6now = datetime.now()
p6date = p6now.strftime("BATCH%Y%m%d")
p6now1 = datetime.now()
p6date1 = p6now.strftime("%Y-%m-%d")

p6frame1 = Frame(page6,width=950,height=550,bg="white")
p6frame1.place(x=5,y=15)
Label(page6,text="Add New Batch : ",bg='white',font=('Time',11,'bold')).place(x=15,y=0)
p6l0 = Label(p6frame1,text='BatchNo.: ',bg='#fff',font=('Time',10,''))
p6l0.place(x=10,y=10)
p6l01 = Label(p6frame1,text=p6date,bg='#fff',font=('Time',10,''))
p6l01.place(x=80,y=10)

p6l1 = Label(p6frame1,text='Product Name :',bg='#fff',font=('Time',10,''))
p6l1.place(x=10,y=30)
# data with duplicate customer id 
p6lst0 = []
conn.execute("select * from productlist ")
for row in conn:
    p6lst0.append(row[1])


def p6cbselect(e):
	p3adrs = (combobox.get(), )
	conn.execute("select * from productlist where title = %s",p3adrs)
	for row in conn:
	    p6e2.delete(0,END)
	    p6e2.insert(0,row[3]+"/-")
def donew():
	p3adrs = (combobox.get(), )
	conn.execute("select * from productlist where title = %s",p3adrs)
	for row in conn:
		p6t = int(row[3])*int(p6e3.get())
		p6e4.delete(0,END)
		p6e4.insert(0,p6t)

def newentry():
	batchn = p6l01.cget("text")
	titlee = combobox.get()
	qua = p6e3.get()
	pric = p6e2.get()
	tamt = p6e4.get()
	bdate = p6e5.get()
	if(batchn and titlee and qua and pric and tamt and bdate):
		conn.execute('Insert into newentry (batchno, title, quantity, productprice, totalamount, batchdate) values (%s,%s,%s,%s,%s,%s)',(batchn,titlee,qua,pric,tamt,bdate))
		connect.commit()
	print(tamt)    
    

combobox = ttk.Combobox(p6frame1,values=p6lst0,width=25,height=8,font=('Time',9,''),state='readonly')
combobox.place(x=120,y=30)
# combobox.bind('<KeyRelease>',search)
combobox.bind("<<ComboboxSelected>>",p6cbselect)

# p6e1 = Entry(p6frame1,width=27,fg='#050929',border=0,bg="#FAFAFA",font=('Time',10,''))
# p6e1.place(x=120,y=30)

p6l2 = Label(p6frame1,text='Product Price :',bg='#fff',font=('Time',10,''))
p6l2.place(x=10,y=50)
p6e2 = Entry(p6frame1,width=25,fg='#050929',border=0,bg="#FAFAFA",font=('Time',10,''))
p6e2.place(x=120,y=50)

p6l3 = Label(p6frame1,text='No.of Pack in Batch :',bg='#fff',font=('Time',10,''))
p6l3.place(x=10,y=70)	
p6e3 = Spinbox(p6frame1,width=25,from_=0,to=500,fg='#050929',border=0,bg="#FAFAFA",font=('Time',10,''))
p6e3.place(x=140,y=70)

p6l4 = Label(p6frame1,text='Batch total amount :',bg='#fff',font=('Time',10,''))
p6l4.place(x=10,y=90)
p6e4 = Entry(p6frame1,width=25,fg='#050929',border=0,bg="#FAFAFA",font=('Time',10,''))
p6e4.place(x=140,y=90)
# p6e4.bind('<Key>',foc)

p6l5 = Label(p6frame1,text='Batch Date :',bg='#fff',font=('Time',10,''))
p6l5.place(x=10,y=110)
p6e5 = Entry(p6frame1,width=25,fg='#050929',border=0,bg="#FAFAFA",font=('Time',10,''))
p6e5.insert(0,p6date1)
p6e5.place(x=140,y=110)

p6b1 = Button(p6frame1,width=10,pady=2,text=' Calculate ',font=('Time',10,'bold'),border=0,bg='#57a1f8',fg='white',command=donew)
p6b1.place(x=30,y=140)

p6b2 = Button(p6frame1,width=15,pady=2,text=' New Entry ',font=('Time',10,'bold'),border=0,bg='#57a1f8',fg='white',command=newentry)
p6b2.place(x=140,y=140)


conn.execute("select * from productlist")
p6columns0 = ('uniqueid','ptitle','pinfo','pprice','pwigth')
p6tree0 = ttk.Treeview(p6frame1,columns=p6columns0,show="headings")
p6tree0.column('uniqueid',anchor=CENTER)
p6tree0.column('ptitle',anchor=CENTER)
p6tree0.column('pinfo',anchor=CENTER)
p6tree0.column('pprice',width=90,anchor=CENTER)
p6tree0.column('pwigth',anchor=CENTER)

p6tree0.heading('uniqueid',text="Unique ID",anchor=CENTER)
p6tree0.heading('ptitle',text="Product Name ")
p6tree0.heading('pinfo',text="Manufacture")
p6tree0.heading('pprice',text="Price")
p6tree0.heading('pwigth',text="Quantity")

i=0
t=0
for row in conn:
	p6tree0.insert('',i,text="",values=(row[0],row[1],row[2],row[3]+"/-",row[4]))
	i = i+1
c = str(i)
p6l5 = Label(p6frame1,text="Details of ALL "+c+" Available Product :			",bg='#fff',font=('Time',11,'bold'))
p6l5.place(x=290,y=210)
p6tree0.place(x=10,y=240)

#===========================================================================================================
p6l5 = Label(p6frame1,text="Batch Details :			",bg='#fff',font=('Time',11,'bold'))
p6l5.place(x=400,y=0)


p6lst=[]
conn.execute("select * from newentry")
for row in conn:
    p6lst.append(row[0])
batchnoo = []
for item in p6lst:
	if item not in batchnoo:
		batchnoo.append(item)

def p6cb1select(e):
	cheh = combobox1.get()
	if(cheh=="ALL"):
		conn.execute("select * from newentry")
		p6columns = ('ptitle','pwigth','pprice','tamtt')
		p6tree = ttk.Treeview(p6frame1,height=7, columns=p6columns,show="headings")
		p6tree.column('ptitle',anchor=CENTER)
		p6tree.column('pwigth',width=90,anchor=CENTER)
		p6tree.column('pprice',width=90,anchor=CENTER)
		p6tree.column('tamtt',width=130,anchor=CENTER)

		p6tree.heading('ptitle',text="Product Name ")
		p6tree.heading('pwigth',text="Quantity")
		p6tree.heading('pprice',text="Price")
		p6tree.heading('tamtt',text="Total Amount")

		i=0
		t=0

		for row in conn:
			p6tree.insert('',i,text="",values=(row[1],row[2],row[3],row[4]+"/-"))

		p6tree.place(x=360,y=30)
	else:
		conn.execute("select * from newentry where batchno = '"+cheh+"'")
		p6columns = ('ptitle','pwigth','pprice','tamtt')
		p6tree = ttk.Treeview(p6frame1,height=7, columns=p6columns,show="headings")
		p6tree.column('ptitle',anchor=CENTER)
		p6tree.column('pwigth',width=90,anchor=CENTER)
		p6tree.column('pprice',width=90,anchor=CENTER)
		p6tree.column('tamtt',width=130,anchor=CENTER)

		p6tree.heading('ptitle',text="Product Name ")
		p6tree.heading('pwigth',text="Quantity")
		p6tree.heading('pprice',text="Price")
		p6tree.heading('tamtt',text="Total Amount")

		i=0
		t=0

		for row in conn:
			p6tree.insert('',i,text="",values=(row[1],row[2],row[3],row[4]+"/-"))

		p6tree.place(x=360,y=30)
		print("bsd")

combobox1 = ttk.Combobox(p6frame1,values=batchnoo,width=35,height=8,font=('Time',9,''),state='readonly')
combobox1.set("All")
combobox1.place(x=550,y=1)
combobox1.bind("<<ComboboxSelected>>",p6cb1select)

conn.execute("select * from newentry")
p6columns = ('ptitle','pwigth','pprice','tamtt')
p6tree = ttk.Treeview(p6frame1,height=7, columns=p6columns,show="headings")
# p6tree.column('uniqueid',anchor=CENTER)
p6tree.column('ptitle',anchor=CENTER)
p6tree.column('pwigth',width=90,anchor=CENTER)
p6tree.column('pprice',width=90,anchor=CENTER)
p6tree.column('tamtt',width=130,anchor=CENTER)

# p6tree.heading('uniqueid',text="Unique ID",anchor=CENTER)
p6tree.heading('ptitle',text="Product Name ")
p6tree.heading('pwigth',text="Quantity")
p6tree.heading('pprice',text="Price")
p6tree.heading('tamtt',text="Total Amount")

i=0
t=0
for row in conn:
	p6tree.insert('',i,text="",values=(row[1],row[2],row[3],row[4]+"/-"))
	i = i+1
c = str(i)
p6tree.place(x=360,y=30)

page6.mainloop()