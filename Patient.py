from tkinter import * 
from tkinter.ttk import *
import Moduledb
from tkinter import messagebox
from tkinter import filedialog

def openNewWindow(master):
    newWindow = Toplevel(master)
    newWindow.title("Patient Registration")
    newWindow.geometry("400x300")

    #Til = Label(newWindow ,width=25,text = "Patient Registration").grid(row = 0,column = 0)

    a = Label(newWindow ,width=25,text = "First Name").grid(row = 1,column = 0,pady=(10, 10),padx=(5, 0))
    b = Label(newWindow ,width=25,text = "Last Name").grid(row = 2,column = 0,pady=(10, 10),padx=(5, 0))
    c = Label(newWindow ,width=25,text = "City").grid(row = 3,column = 0,pady=(10, 10),padx=(5, 0))
    d = Label(newWindow ,width=25,text = "Contact Number").grid(row = 4,column = 0,pady=(10, 10),padx=(5, 0))
    e = Label(newWindow ,width=25,text = "Address").grid(row = 5,column = 0,pady=(10, 10),padx=(5, 0))

    def Saverrecord():
        if aa1.get()!='' and bb1.get()!='' and cc1.get()!='' and dd1.get()!='' and ee1.get()!='':
            Strval="INSERT INTO patient(FirstName,LastName,City,Contact,Address,Pimage,COVID) VALUES('"+aa1.get()+"','"+bb1.get()+"','"+cc1.get()+"','"+dd1.get()+"','"+ee1.get()+"','','')"
            a=Moduledb.Updatedata(Strval,Moduledb.mydb)
            messagebox.showinfo(title="Saved", message="New Record Added")
            newWindow.destroy()
        else:
            messagebox.showinfo(title="Alert", message="Enter All Information")


        
    aa1 = StringVar()
    bb1 = StringVar()
    cc1 = StringVar()
    dd1 = StringVar()
    ee1 = StringVar()
    
    a1 = Entry(newWindow,width=30,textvariable=aa1).grid(row = 1,column = 1,pady=(10, 10))
    b1 = Entry(newWindow,width=30,textvariable=bb1).grid(row = 2,column = 1,pady=(10, 10))
    c1 = Entry(newWindow,width=30,textvariable=cc1).grid(row = 3,column = 1,pady=(10, 10))
    d1 = Entry(newWindow,width=30,textvariable=dd1).grid(row = 4,column = 1,pady=(10, 10))
    e1 = Entry(newWindow,width=30,textvariable=ee1).grid(row = 5,column = 1,pady=(10, 10))

    btn1 = Button(newWindow,text="Save",width=20,command=Saverrecord).grid(row = 6,column = 0,padx=(5, 0))
    btn2 = Button(newWindow,text="Cancel",width=20,command=newWindow.destroy).grid(row = 6,column = 1,padx=(5, 0))
