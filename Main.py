from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Login Page')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
##################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signin():
	username = user.get()
	password = code.get()
	if username=='shruti' and password=='1234':
		root.quit()
		page2 = Toplevel(root)
		page2.title("MainPage")
		width= page2.winfo_screenwidth()
		height= page2.winfo_screenheight()
		#setting tkinter window size
		page2.geometry("%dx%d" % (width, height))
		page2.config(bg='white')
		page2.resizable(False,False)


		p2frame1 = Frame(page2,width=950,height=550,bg="white")
		p2frame1.place(x=5,y=5)

		menubar = Menu(p2frame1)
		page2.config(menu=menubar)
		menubar.add_command(label='File')


		p2e1= Entry(p2frame1,width=15,fg='black',border=0,bg="white",font=('Time',12,''))
		p2e1.place(x=350,y=35)
		Frame(p2frame1,width=150,height=2,bg='black').place(x=350,y=58)

		###############################@@@@@ New Customer Start @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		def new_customer():

			screen1 = Toplevel(page2)
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
			b2.place(x=600,y=400)

			b3 = Button(frame1,pady=3,text=' EXIT ',bg='#F1F1F5',fg='red',font=('Time',12,'bold'),border=0,command=screen1.destroy)
			b3.place(x=800,y=10)




			screen1.mainloop()


			


		###############################@@@@@ New Customer End @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		###############################@@@@@ History Start @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		def History():
			page4 = Toplevel(page2)
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



			p4l1 = Label(p4frame1,text='Enter or Search Customer ID ',bg='#fff',font=('Time',9,'bold'))
			p4l1.place(x=40,y=23)
			combobox = ttk.Combobox(page4,values=newlst,font=('Time',12,''))
			combobox.set(" ")
			combobox.place(x=50,y=50)
			combobox.bind('<KeyRelease>',search)

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

		###############################@@@@@ Histor End @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		###############################@@@@@ ShowMap Start @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		def shopmap():
			page5 = Toplevel(page2)
			page5.title("ShopMap")
			page5.geometry('925x500+300+200')
			page5.config(bg='white')
			page5.resizable(False,False)

			p5frame1 = Frame(page5,width=950,height=550,bg="white")
			p5frame1.place(x=5,y=5)


			p5img1 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon3.png')
			Label(page5,image=p5img1,bg='white').place(x=10,y=0)

			Label(page5,text="ShopMap",bg='white',font=('Time',20,'')).place(x=3,y=0)
			p5img0 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\white.png')
			p5l0 = Label(page5,image=p5img0,bg='white')
			p5l0.place(x=10,y=32)

			##======================================================================== A1 ==========
			def etrchgp5l1(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon4-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3

			def leavechange(e):
				p5img0 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\white.png')
				p5l0.config(image = p5img0)
				p5l0.image = p5img0


			p5img2 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon4.png')
			p5l1 = Label(page5,width=100,height=25,image=p5img2,bg='white')
			p5l1.place(x=530,y=410)

			p5l1.bind('<Enter>',etrchgp5l1)
			p5l1.bind('<Leave>',leavechange)

			##========================================================================== A2 ========
			def etrchgp5l2(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon5-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3


			p5img4 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon5.png')
			p5l2 = Label(page5,width=90,height=25,image=p5img4,bg='white')
			p5l2.place(x=430,y=470)

			p5l2.bind('<Enter>',etrchgp5l2)
			p5l2.bind('<Leave>',leavechange)
			##============================================================================= A3 =====
			def etrchgp5l3(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon6-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3


			p5img5 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon6.png')
			p5l3 = Label(page5,width=90,height=25,image=p5img5,bg='white')
			p5l3.place(x=620,y=30)

			p5l3.bind('<Enter>',etrchgp5l3)
			p5l3.bind('<Leave>',leavechange)
			##=========================================================================== A4 =======
			def etrchgp5l4(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon7-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3


			p5img6 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon7.png')
			p5l4 = Label(page5,width=90,height=25,image=p5img6,bg='white')
			p5l4.place(x=300,y=27)

			p5l4.bind('<Enter>',etrchgp5l4)
			p5l4.bind('<Leave>',leavechange)
			##=========================================================================== A5 =======
			def etrchgp5l5(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon8-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3


			p5img7 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon8.png')
			p5l5 = Label(page5,width=90,height=25, image=p5img7,bg='white')
			p5l5.place(x=230,y=60)

			p5l5.bind('<Enter>',etrchgp5l5)
			p5l5.bind('<Leave>',leavechange)
			##=========================================================================== C1 =======
			def etrchgp5l6(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon9-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3


			p5img8 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon9.png')
			p5l6 = Label(page5,width=90,height=25, image=p5img8,bg='white')
			p5l6.place(x=520,y=25)

			p5l6.bind('<Enter>',etrchgp5l6)
			p5l6.bind('<Leave>',leavechange)
			##=========================================================================== C2 =======
			def etrchgp5l7(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon10-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3


			p5img9 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon10.png')
			p5l7 = Label(page5,width=90,height=25, image=p5img9,bg='white')
			p5l7.place(x=330,y=470)

			p5l7.bind('<Enter>',etrchgp5l7)
			p5l7.bind('<Leave>',leavechange)

			##=========================================================================== C3 =======

			p5img10 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon11.png')
			p5l8 = Label(page5,width=90,height=25, image=p5img10,bg='white')
			p5l8.place(x=257,y=440)

			p5l8.bind('<Enter>',etrchgp5l7)
			p5l8.bind('<Leave>',leavechange)
			##=========================================================================== C4 =======

			p5img11 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon12.png')
			p5l9 = Label(page5,width=90,height=25, image=p5img11,bg='white')
			p5l9.place(x=130,y=400)

			p5l9.bind('<Enter>',etrchgp5l7)
			p5l9.bind('<Leave>',leavechange)
			##=========================================================================== C4 =======
			def etrchgp5l8(e):
				p5img3 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon12-1.png')
				p5l0.config(image = p5img3)
				p5l0.image = p5img3

			p5img12 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icon12.png')
			p5l10 = Label(page5,width=90,height=25, image=p5img12,bg='white')
			p5l10.place(x=20,y=160)

			p5l10.bind('<Enter>',etrchgp5l8)
			p5l10.bind('<Leave>',leavechange)

			page5.mainloop()


		###############################@@@@@ ShowMap End @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		###############################@@@@@ Item Details Start @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		def detailsproduct():
			page6 = Toplevel(page2)
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


		###############################@@@@@ item Details End @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		###############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		#p2img1 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\icons.png')
		#Label(page2,width=50,height=50,image=p2img1,bg='white').place(x=0,y=0)
		menubar.add_command(label='New Customer',command=new_customer)
		menubar.add_command(label='Customer History',command=History)
		menubar.add_command(label='Shop Map',command=shopmap)
		menubar.add_command(label='Product Details',command=detailsproduct)
		spimg1 = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\picture1.png')
		Label(page2,image=spimg1,bg='white').place(x=0,y=0)
		page2.mainloop()
		####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ENDOFPAGE2  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#====================================================================

	elif username != 'shruti' and password!='1234' or username!='shruti' or password!='1234' :
		messagebox.showerror("Invaild","Invalid Input \n Please retry")


##################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

img = PhotoImage(file='G:\\Peoples\\Shruti\\BCCA Project\\Code\\images\\login.png')
Label(root,image=img,bg='white',width=300,height=400).place(x=480,y=50)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=100,y=70)
Button(frame,width=6,pady=3,text='Exit',bg='#F1F1F5',fg='red',border=0,command=signin).place(x=10,y=5)
heading = Label(frame,text='Sign IN',fg='#57a1f8',bg='white')
heading.place(x=100,y=5)
def on_enter(e):
	user.delete(0,'end')

def on_leave(e):
	name=user.get()
	if(name==''):
		user.insert(0,'Username')	

user = Entry(frame,width=25,fg='black',border=0,bg="white")
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
	code.delete(0,'end')

def on_leave(e):
	name=code.get()
	if(name==''):
  		code.insert(0,'Password')	

code = Entry(frame,width=25,fg='black',border=0,bg="white",show='*')
code.place(x=30,y=130)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=155)

Button(frame,width=39,pady=7,text='SignIn',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label1 = Label(frame,text="Don't have an account?",fg='black',bg='white')
label1.place(x=75,y=270)

signup = Button(frame,width=6,text='SignUp',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signup.place(x=215,y=270) 


 

root.mainloop()

