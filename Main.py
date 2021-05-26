from tkinter import * 
from tkinter.ttk import *
import Patient
import Search
import COVID

master = Tk()
master.title("COVID 19 Test")
master.geometry("400x300")
#master.resizable(False, False)


label = Label(master,text ="Select Options")
label.pack(pady = 10)

btn1 = Button(master,text="Patient Registration",width=50,command=lambda:Patient.openNewWindow(master))
btn1.pack(pady = 10)

btn2 = Button(master,text="Search Patient",width=50,command=lambda:Search.openNewWindow(master))
btn2.pack(pady = 10)

btn3 = Button(master,text="COVID 19 Detect",width=50,command=lambda:COVID.openNewWindow(master))
btn3.pack(pady = 10)

btn4 = Button(master,text="Exit",width=50,command=master.destroy)
btn4.pack(pady = 10)


#btn1 = ttk.Button(window , text="Set",command=lambda:setTextInput("hi")).grid(row=5,column=1)


master.mainloop()
