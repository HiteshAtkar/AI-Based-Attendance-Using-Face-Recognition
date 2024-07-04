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


class login_window:
    def __init__(self,root2):
         self.root2=root2
         self.root2.geometry("690x400+515+330")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root2.title("Forgot Password")


         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image5=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg7.jpg")
         background_image5=background_image5.resize((320,400))
         self.photoimage5=ImageTk.PhotoImage(background_image5)
         bg_img5=Label(self.root2,image=self.photoimage5)
         bg_img5.place(x=400,y=0,width=320,height=400)

          #Background forgot password------------------------------------------------------------------------------------------------------------------------------>
         background_image6=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/fp.png")
         background_image6=background_image6.resize((400,400))
         self.photoimage6=ImageTk.PhotoImage(background_image6)
         bg_img6=Label(self.root2,image=self.photoimage6)
         bg_img6.place(x=0,y=0,width=400,height=400)

        #forgot password name------------------------->
         fp_name=Label(bg_img5,text="Forgot Password",font=("roboto",22,"bold"),fg="#592a9c",bg="White")
         fp_name.place(x=30,y=20,width=180,height=40)

         #security question combobox------------------------------->
         sec_que_lbl=Label(bg_img5,text="Security Question",font=("roboto",15,"bold"),fg="Black",bg="White")
         sec_que_lbl.place(x=0,y=80,width=140,height=30)

         sec_que_cmb=ttk.Combobox(bg_img5,font=("roboto",15,"bold"),width=20,state="readonly")
         sec_que_cmb["values"]=("Select Security Question","What Is Your Birth Place?","What Is Your Father's Name?","What Is Your Mother Name?")
         sec_que_cmb.current(0)
         sec_que_cmb.place(x=0,y=110,width=240,height=25)

         #security Answer---------------------------------------->
         sec_ans=Label(bg_img5,text="Security Answer",font=("roboto",15,"bold"),fg="Black",bg="White")
         sec_ans.place(x=0,y=150,width=128,height=30)

         self.sec_ans_ent=ttk.Entry(bg_img5,width=50,font=("times new roman",17))
         self.sec_ans_ent.place(x=0,y=180,width=240,height=35)

         #password---------------------------------------->
         n_pass=Label(bg_img5,text="New Password",font=("roboto",15,"bold"),fg="Black",bg="White")
         n_pass.place(x=0,y=230,width=120,height=30)

         self.n_pass_ent=ttk.Entry(bg_img5,width=50,font=("times new roman",17))
         self.n_pass_ent.place(x=0,y=260,width=240,height=35)

         #register Button---------------------->
         register_btn=Button(bg_img5,text="Reset Password",font=("roboto",15,"bold"),fg="white",bg="#6a951f",)
         register_btn.place(x=0,y=325,width=240,height=35)


        
             
             





    





         















       




                 

















































if __name__ == "__main__":
    root2=Tk()
    obj=login_window(root2)
    root2.mainloop()