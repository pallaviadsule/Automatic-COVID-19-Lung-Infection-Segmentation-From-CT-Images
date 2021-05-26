from tkinter import * 
from tkinter.ttk import *
import Moduledb
from tkinter import messagebox
from tkinter import filedialog

def openNewWindow(master):
    newWindow = Toplevel(master)
    newWindow.title("Patient Search")
    newWindow.geometry("660x550")

    #Til = Label(newWindow ,width=25,text = "Patient Search").grid(row = 0,column = 0)

             
    ass = Label(newWindow ,width=25,text = "Search Key").grid(row = 1,column = 0,pady=(10, 10),padx=(5, 0))

    aas1 = StringVar()
    as1 = Entry(newWindow,width=30,textvariable=aas1).grid(row = 1,column = 1,pady=(10, 10))

    def Searchrecord():
        if aas1.get()!='':
            Strval="Select * from patient where concat(FirstName,LastName,City,Contact) like '%"+aas1.get()+"%'"
            #print(Strval)
            myresult=Moduledb.Getdata(Strval,Moduledb.mydb)
            mylist.delete('0','end')
            line=0
            for x in myresult:
                line=line+1
                mylist.insert(line,str(x[0])+"-"+str(x[1])+" "+str(x[2]))
                
    def CurSelet(evt):
        value=str((mylist.get(ACTIVE)))
        #print(value)
        v = value.split("-")
        #print(v[0])
        Strval="Select * from patient where pid='"+v[0]+"'"
        #print(Strval)
        myresult=Moduledb.Getdata(Strval,Moduledb.mydb)
        for x in myresult:
            pid11.set(str(x[0]))
            aa1.set(str(x[1]))
            bb1.set(str(x[2]))
            cc1.set(str(x[3]))
            dd1.set(str(x[4]))
            ee1.set(str(x[5]))
            ff1.set(str(x[7])+ "%")
            if int(x[7])>=10:
                gg1.set("High Risk")
            elif int(x[7])>=5 and int(x[7])<10:
                gg1.set("Min Risk")
            elif int(x[7])>=1 and int(x[7])<5:
                gg1.set("Low Risk")
            else:
                gg1.set("No Risk")
            

    btn1 = Button(newWindow,text="Search",width=20,command=Searchrecord).grid(row = 1,column = 2,padx=(5, 0))
    btn2 = Button(newWindow,text="Cancel",width=20,command=newWindow.destroy).grid(row = 1,column = 3,padx=(5, 0))

    sb = Scrollbar(newWindow)  
    sb.grid(column=0, sticky=N+S)
    mylist = Listbox(newWindow,width=100, yscrollcommand = sb.set )
    mylist.bind('<<ListboxSelect>>',CurSelet)
    mylist.grid(row = 2,column = 0,columnspan=4)

    pid = Label(newWindow ,width=25,text = "ID").grid(row = 3,column = 0,pady=(10, 10),padx=(5, 0))
    a = Label(newWindow ,width=25,text = "First Name").grid(row = 4,column = 0,pady=(10, 10),padx=(5, 0))
    b = Label(newWindow ,width=25,text = "Last Name").grid(row = 5,column = 0,pady=(10, 10),padx=(5, 0))
    c = Label(newWindow ,width=25,text = "City").grid(row = 6,column = 0,pady=(10, 10),padx=(5, 0))
    d = Label(newWindow ,width=25,text = "Contact Number").grid(row = 7,column = 0,pady=(10, 10),padx=(5, 0))
    e = Label(newWindow ,width=25,text = "Address").grid(row = 8,column = 0,pady=(10, 10),padx=(5, 0))
    f = Label(newWindow ,width=25,text = "COVID 19 Test (In %)").grid(row = 9,column = 0,pady=(10, 10),padx=(5, 0))
    g = Label(newWindow ,width=25,text = "COVID 19 Risk").grid(row = 10,column = 0,pady=(10, 10),padx=(5, 0))

    aa1 = StringVar()
    bb1 = StringVar()
    cc1 = StringVar()
    dd1 = StringVar()
    ee1 = StringVar()
    ff1 = StringVar()
    pid11 = StringVar()
    gg1 = StringVar()
    
    pid1 = Entry(newWindow,width=30,textvariable=pid11).grid(row = 3,column = 1,pady=(10, 10))
    a1 = Entry(newWindow,width=30,textvariable=aa1).grid(row = 4,column = 1,pady=(10, 10))
    b1 = Entry(newWindow,width=30,textvariable=bb1).grid(row = 5,column = 1,pady=(10, 10))
    c1 = Entry(newWindow,width=30,textvariable=cc1).grid(row = 6,column = 1,pady=(10, 10))
    d1 = Entry(newWindow,width=30,textvariable=dd1).grid(row = 7,column = 1,pady=(10, 10))
    e1 = Entry(newWindow,width=30,textvariable=ee1).grid(row = 8,column = 1,pady=(10, 10))
    f1 = Entry(newWindow,width=30,textvariable=ff1).grid(row = 9,column = 1,pady=(10, 10))
    g1 = Entry(newWindow,width=30,textvariable=gg1).grid(row = 10,column = 1,pady=(10, 10))

