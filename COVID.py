from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import Moduledb
import numpy as np 
import cv2 
from matplotlib import pyplot as plt
import math

def openNewWindow(master):
    newWindow = Toplevel(master)
    newWindow.title("COVID 19 Detect")
    newWindow.geometry("1200x500")

    def file_opener():
       #input1 = filedialog.askopenfile(initialdir="/")
        input1 =filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("[PNG]","*.png*"),("[JPG]","*.jpg*"),("all files","*.*")))
        aa1.set(input1)

    def COVIDTEST():
        # Image operation using thresholding 
        img = cv2.imread(aa1.get()) 
        gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        test = ImageTk.PhotoImage(Image.fromarray(gray1))
        label1 = Label(newWindow,image=test)
        label1.image = test
        label1.grid(row = 3,column = 0,columnspan=3)

        #To Get Accuracy Highlight Dark and Light area
        light_val = (150, 150, 150)
        dark_val = (200, 200, 200)
        mask = cv2.inRange(gray1, light_val, dark_val)
        result = cv2.bitwise_and(gray1, gray1, mask=mask)

        #test = ImageTk.PhotoImage(Image.fromarray(mask))
        #label2 = Label(newWindow,image=test)
        #label2.image = test
        #label2.grid(row = 3,column = 3,columnspan=3)

        #To Again Convert Into Gray For threshold
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY) 

        #test = ImageTk.PhotoImage(Image.fromarray(gray))
        #label3 = Label(newWindow,image=test)
        #label3.image = test
        #label3.grid(row = 3,column = 6,columnspan=3)
        
        edges = cv2.Canny(mask,130,300)

        #test = ImageTk.PhotoImage(Image.fromarray(edges))
        #label4 = Label(newWindow,image=test)
        #label4.image = test
        #label4.grid(row = 4,column = 0,columnspan=3)


        # Marker labelling
        ret, markers = cv2.connectedComponents(mask)

        h, w = gray1.shape[:2]
        hue_markers = np.uint8(179*np.float32(markers)/np.max(markers))
        blank_channel = 255*np.ones((h, w), dtype=np.uint8)
        marker_img = cv2.merge([hue_markers, blank_channel, blank_channel])
        marker_img = cv2.cvtColor(marker_img, cv2.COLOR_HSV2BGR)
        
        test = ImageTk.PhotoImage(Image.fromarray(marker_img))
        label2 = Label(newWindow,image=test)
        label2.image = test
        label2.grid(row = 3,column = 3,columnspan=3)

        hsv = cv2.cvtColor(marker_img,cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        # Range for upper range
        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        #Generating the final mask to detect red color
        #mask1 = mask1+mask2   
        mask2 = cv2.bitwise_not(mask1)
        res1 = cv2.bitwise_and(marker_img,marker_img,mask=mask2)

        height,width = res1.shape[:2]
        for loop1 in range(height):
            for loop2 in range(width):
                r,g,b = res1[loop1,loop2]
                res1[loop1,loop2] = 0,g,0

        BROWN_MIN = np.array([0, 250, 0], np.uint8)
        BROWN_MAX = np.array([0, 255, 0], np.uint8)
        dst = cv2.inRange(res1, BROWN_MIN, BROWN_MAX)
        no_brown = cv2.countNonZero(dst)
        heartpix=(height*width)/3;
        perval=no_brown/(heartpix/100)
        perval=math.ceil(perval);
        cc1.set(str(perval))
        #print('The number of Green pixels is: ' + str(no_brown))
        #print('The number of pixels is: ' + str(height*width))
        #print('The number of %: ' + str(perval))

        res2 = cv2.bitwise_and(img, img, mask = mask1)
        final_output = cv2.addWeighted(res1,1,res2,1,0)

        test = ImageTk.PhotoImage(Image.fromarray(final_output))
        label3 = Label(newWindow,image=test)
        label3.image = test
        label3.grid(row = 3,column = 6,columnspan=3)
        Mess=""
        if perval>=10:
            Mess="High Risk"
        elif perval>=5 and perval<10:
            Mess="Min Risk"
        elif perval>=1 and perval<5:
            Mess="Low Risk"
        else:
            Mess="No Risk"
        messagebox.showinfo(title="COVID Test Result", message=Mess+", "+str(perval)+"% Infection Detected")

        
    #Til = Label(newWindow ,width=25,text = "COVID 19 Detect").grid(row = 0,column = 0)

    a = Label(newWindow ,width=25,text = "Select Image").grid(row = 1,column = 0,pady=(10, 10),padx=(5, 0))
    aa1 = StringVar()
    a1 = Entry(newWindow,width=30,textvariable=aa1).grid(row = 1,column = 1,pady=(10, 10))
    btn1 = Button(newWindow,text="File",width=20,command=lambda:file_opener()).grid(row = 1,column = 2,padx=(5, 0))
    btn2 = Button(newWindow,text="Start Test",width=20,command=COVIDTEST).grid(row = 1,column = 3,padx=(5, 0))
    btn3 = Button(newWindow,text="Cancel",width=20,command=newWindow.destroy).grid(row = 1,column = 4,padx=(5, 0))

    cc1 = StringVar()
    cc1.set("0")
    b = Label(newWindow ,width=25,text = "COVID 19 Result(%)").grid(row = 2,column = 0,pady=(10, 10),padx=(5, 0))
    c = Entry(newWindow ,width=25,textvariable=cc1).grid(row = 2,column = 1,pady=(10, 10),padx=(5, 0))
    
    
    def Saverrecord():
        if pid1.get()!='':
            Strval="update patient SET COVID='"+cc1.get()+"' where pid='"+pid1.get()+"'"
            a=Moduledb.Updatedata(Strval,Moduledb.mydb)
            messagebox.showinfo(title="Update", message="COVID 19 Test Result updated")
            newWindow.destroy()
        else:
            messagebox.showinfo(title="Alert", message="Enter patient id")
            
    u = Label(newWindow ,width=25,text = "Enter User ID").grid(row = 2,column = 2,pady=(10, 10),padx=(5, 0))
    pid1 = StringVar()
    pid = Entry(newWindow,width=30,textvariable=pid1).grid(row = 2,column = 3,pady=(10, 10))
    btnu1 = Button(newWindow,text="Update",width=20,command=Saverrecord).grid(row = 2,column = 4,padx=(5, 0))

    #canvas = Canvas(newWindow, width = 200, height = 200)  
    #canvas.grid(row = 2,column = 0)  
    #img = ImageTk.PhotoImage(Image.open("3.PNG"))  
    #canvas.create_image(20, 20, anchor=NW, image=img)
    
 

    
