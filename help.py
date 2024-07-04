from tkinter import *
from turtle import update
from tkmacosx import Button
from tkinter import ttk
from tkinter import PhotoImage
import os
import csv
from tkinter import filedialog
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime 
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import numpy as np

mydata=[]

class help:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1710x1112+0+0")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root.title("Face Recognition System")

    
         #Background Image 1------------------------------------------------------------------------------------------------------------------------------>
         background_image1=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg1.png")
         background_image1=background_image1.resize((1710,1112))
         self.photoimage1=ImageTk.PhotoImage(background_image1)
         bg_img=Label(self.root,image=self.photoimage1)
         bg_img.place(x=0,y=0,width=1710,height=42)

         #App Name----------------------------->
         collage_name=Label(bg_img,text="AI Based Attendance Using Facial Recognition System",font=("times new roman",17),fg="white",bg="black")
         collage_name.place(x=10,y=0,width=400,height=32)
 
         #Background Image 2------------------------------------------------------------------------------------------------------------------------------>
         background_image2=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg2.png")
         background_image2=background_image2.resize((1710,44))
         self.photoimage3=ImageTk.PhotoImage(background_image2)
         bg_img1=Label(self.root,image=self.photoimage3)
         bg_img1.place(x=0,y=44,width=1710,height=38)

         #date & time-------------------------->
         def time():
             string = strftime('Time: %H:%M | Date: %A,%d %B')
             lbl.config(text=string)
             lbl.after(1000,time)

         lbl=Label(bg_img1,font=("times new roman",15,),background="#faa500",fg="black")
         lbl.place(x=15,y=5,width=250,height=24)
         time()

         #home Button------------------------>
         lg_btn=Button(bg_img1,text="Home",font=("times new roman",15),command=self.iexit,fg="white",bg="#6a951f",)
         lg_btn.place(x=1620,y=-2,width=80,height=38)

         #Background Image 3------------------------------------------------------------------------------------------------------------------------------>
         background_image3=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg.jpeg")
         background_image3=background_image3.resize((1710,1112))
         self.photoimage2=ImageTk.PhotoImage(background_image3)
         bg_img3=Label(self.root,image=self.photoimage2)
         bg_img3.place(x=0,y=83,width=1710,height=880)

         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image5=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/b.jpg")
         background_image5=background_image5.resize((550,350))
         self.photoimage5=ImageTk.PhotoImage(background_image5)
         bg_img5=Label(self.root,image=self.photoimage5)
         bg_img5.place(x=15,y=145,width=550,height=350)

        #help 1----------------------------->
         help1=Label(root,text="Step 1: Click Here To Register Student",font=("times new roman",17,"bold"),fg="Black",bg="white")
         help1.place(x=15,y=100,width=300,height=32)


         #Background Image 6------------------------------------------------------------------------------------------------------------------------------>
         background_image6=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/d.jpg")
         background_image6=background_image6.resize((550,350))
         self.photoimage6=ImageTk.PhotoImage(background_image6)
         bg_img6=Label(self.root,image=self.photoimage6)
         bg_img6.place(x=578,y=145,width=550,height=350)

         #help 2----------------------------->
         help2=Label(root,text="Step 2: Click Here To Train Model With New Student Data",font=("times new roman",17,"bold"),fg="Black",bg="white")
         help2.place(x=578,y=100,width=450,height=32)

         #Background Image 7------------------------------------------------------------------------------------------------------------------------------>
         background_image7=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/a.jpg")
         background_image7=background_image7.resize((550,350))
         self.photoimage7=ImageTk.PhotoImage(background_image7)
         bg_img7=Label(self.root,image=self.photoimage7)
         bg_img7.place(x=1146,y=145,width=550,height=350)

         #help 3----------------------------->
         help3=Label(root,text="Step 3: Click Here To Take Attendance",font=("times new roman",17,"bold"),fg="Black",bg="white")
         help3.place(x=1146,y=100,width=300,height=32)


         #Background Image 8------------------------------------------------------------------------------------------------------------------------------>
         background_image8=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/c.jpg")
         background_image8=background_image8.resize((550,350))
         self.photoimage8=ImageTk.PhotoImage(background_image8)
         bg_img8=Label(self.root,image=self.photoimage8)
         bg_img8.place(x=15,y=580,width=550,height=350)

         #help 4----------------------------->
         help4=Label(root,text="Step 4: Click Here To Manage Attendance",font=("times new roman",17,"bold"),fg="Black",bg="white")
         help4.place(x=15,y=535,width=330,height=32)


         #Background Image 6------------------------------------------------------------------------------------------------------------------------------>
         background_image9=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/e.jpg")
         background_image9=background_image9.resize((550,350))
         self.photoimage9=ImageTk.PhotoImage(background_image9)
         bg_img9=Label(self.root,image=self.photoimage9)
         bg_img9.place(x=578,y=580,width=550,height=350)

         #help 5----------------------------->
         help5=Label(root,text="Step 5: Click Here To Register New Admin User",font=("times new roman",17,"bold"),fg="Black",bg="white")
         help5.place(x=575,y=535,width=380,height=45)

         #Background Image 7------------------------------------------------------------------------------------------------------------------------------>
         background_image10=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/f.jpg")
         background_image10=background_image10.resize((550,350))
         self.photoimage10=ImageTk.PhotoImage(background_image10)
         bg_img10=Label(self.root,image=self.photoimage10)
         bg_img10.place(x=1146,y=580,width=550,height=350)

         #help 5----------------------------->
         help5=Label(root,text="Step 6: Click Here To Quit",font=("times new roman",17,"bold"),fg="Black",bg="white")
         help5.place(x=1135,y=535,width=230,height=45)

        





















         #Background Image 4------------------------------------------------------------------------------------------------------------------------------->
         background_image4=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg2.png")
         background_image4=background_image4.resize((1710,1112))
         self.photoimage4=ImageTk.PhotoImage(background_image4)
         bg_img4=Label(self.root,image=self.photoimage4)
         bg_img4.place(x=0,y=958,width=1710,height=30)

         #devloper name------------------->
         collage_name=Label(bg_img4,text="Copyright @ 2024 Hitesh Atkar. All Rights Reserved",font=("times new roman",13),fg="black",bg="#faa500")
         collage_name.place(x=1350,y=0,width=400,height=20)

    #Exit Function--------------------------------------------->
    def iexit(self):
              self.root.destroy()






                 

















































if __name__ == "__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()