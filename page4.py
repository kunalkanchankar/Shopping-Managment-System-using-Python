from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk

page4 = Tk()
#page4 = Toplevel(root)
page4.title("History")
page4.geometry('925x500+300+200')
page4.config(bg='white')
page4.resizable(False,False)

p4frame1 = Frame(page4,width=950,height=550,bg="white")
p4frame1.place(x=5,y=5)

p3now = datetime.now()
p3date = p3now.strftime("CustID%Y%m%d%H%M")

connect = mysql.connector.connect(host='localhost',user='root',passwd='root123',database='grocerym',port='3306')
conn = connect.cursor()

########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# data with duplicate customer id 
lst = []
conn.execute("select * from additem ")
i=0
t=0
for row in conn:
    lst.append(row[0])

# data without duplication
newlst = []
for item in lst:
	if item not in newlst:
		newlst.append(item)

def search(event):
	value = event.widget.get()
	if value == '':
		combobox['values'] = newlst
	else:
		data = []
		for item in newlst: 
			if value.lower() in item.lower():
				data.append(item)
				print(combobox.get())

		combobox['values'] = data

def selecttt(e):
	print(combobox.get())



p4l1 = Label(p4frame1,text='Enter or Search Customer ID ',bg='#fff',font=('Time',9,'bold'))
p4l1.place(x=40,y=23)
combobox = ttk.Combobox(page4,values=newlst,font=('Time',12,''))
combobox.place(x=50,y=50)
combobox.bind('<KeyRelease>',search)
combobox.bind("<<ComboboxSelected>>",selecttt)


#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def searchbtn():
	custid = combobox.get()

	conn.execute("select * from additem where cusid = '"+custid+"'")

	p4columns = ('pname','quantity','pprice','tprice')
	p4tree = ttk.Treeview(p4frame1,columns=p4columns,show="headings")
	p4tree.column('pname',anchor=CENTER)
	p4tree.column('quantity',anchor=CENTER)
	p4tree.column('pprice',anchor=CENTER)
	p4tree.column('tprice',anchor=CENTER)

	p4tree.heading('pname',text="Product Name",anchor=CENTER)
	p4tree.heading('quantity',text="Quantity")
	p4tree.heading('pprice',text="Product Price")
	p4tree.heading('tprice',text="Total Price")

	i=0
	t=0

	for row in conn:

		p4tree.insert('',i,text="",values=(row[2],row[3],row[4],row[5]))
		var = row[5]
		print(var)
		t = int(var) + t
		total = "Total Price : "+str(t)+" /-"
		p4l4 = Label(p4frame1,text=total,bg='red',font=('Time',11,'bold'))
		p4l4.place(x=50,y=100)
	    
		i = i+1
	p4tree.place(x=50,y=150)
	    


b3 = Button(p4frame1,width=20,pady=2,text=' Search ',bg='#57a1f8',fg='white',font=('Time',12,'bold'),border=0,command=searchbtn)
b3.place(x=255,y=40)
p4l4 = Label(p4frame1,text=" Total Price :	        ",bg='red',font=('Time',11,'bold'))
p4l4.place(x=50,y=100)
	    
page4.mainloop()