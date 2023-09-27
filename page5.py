from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk

page5 = Tk()
#page5 = Toplevel(root)
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