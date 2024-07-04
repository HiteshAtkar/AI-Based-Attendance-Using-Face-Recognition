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
from main import Face_Recognition_System


class login_window:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1710x1112+0+0")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root.title("Face Recognition System")

         #Variable declaration-------------------------------->
         self.txtuser=StringVar()
         self.txtpass=StringVar()
         self.username=StringVar()
         self.password=StringVar()
         self.var_securityQ=StringVar()
         self.var_securityA=StringVar()
         self.var_newpass=StringVar()
    
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
         lg_btn=Button(bg_img1,text="Quit",font=("times new roman",15),command=self.iexit,fg="white",bg="#6a951f",)
         lg_btn.place(x=1620,y=-2,width=80,height=38)

         #Background Image 3------------------------------------------------------------------------------------------------------------------------------>
         background_image3=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg6.png")
         background_image3=background_image3.resize((1710,1112))
         self.photoimage2=ImageTk.PhotoImage(background_image3)
         bg_img3=Label(self.root,image=self.photoimage2)
         bg_img3.place(x=0,y=83,width=1710,height=880)

         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image5=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg7.jpg")
         background_image5=background_image5.resize((800,450))
         self.photoimage5=ImageTk.PhotoImage(background_image5)
         bg_img5=Label(self.root,image=self.photoimage5)
         bg_img5.place(x=450,y=270,width=800,height=450)

        #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image6=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/login_image.png")
         background_image6=background_image6.resize((400,400))
         self.photoimage6=ImageTk.PhotoImage(background_image6)
         bg_img6=Label(bg_img5,image=self.photoimage6)
         bg_img6.place(x=20,y=30,width=400,height=400)

         login_name=Label(bg_img5,text="Admin Login",font=("roboto",30,"bold"),fg="#592a9c",bg="White")
         login_name.place(x=485,y=55,width=180,height=40)

        #Username---------------------------------------->
         user_name=Label(bg_img5,text="Username",font=("roboto",15,"bold"),fg="Black",bg="White")
         user_name.place(x=455,y=125,width=83,height=30)

         self.user_ent=ttk.Entry(bg_img5,textvariable=self.username,width=50,font=("times new roman",17))
         self.user_ent.place(x=455,y=157,width=240,height=35)


        #password---------------------------------------->
         pass_name=Label(bg_img5,text="Password",font=("roboto",15,"bold"),fg="Black",bg="White")
         pass_name.place(x=455,y=205,width=80,height=30)

         self.pass_ent=ttk.Entry(bg_img5,textvariable=self.password,width=50,font=("times new roman",17))
         self.pass_ent.place(x=455,y=237,width=240,height=35)


         #login Button------------------------>
         login_btn=Button(bg_img5,text="login",command=self.login,font=("times new roman",20),fg="white",bg="#2977b7",)
         login_btn.place(x=455,y=295,width=240,height=40)

         
         forgot_name=Label(bg_img5,text="Forgot Your Password?",font=("roboto",14,),fg="Black",bg="White")
         forgot_name.place(x=456,y=350,width=150,height=20)

         #forgot Button------------------------>
         fp_btn=Button(bg_img5,text="Get it Back!",command=self.forgot_password_window,font=("times new roman",14,"underline"),fg="black",bg="#dddddd",)
         fp_btn.place(x=610,y=350,width=80,height=22)


    #login function------------------------------------------------------->
    def login(self):
        if self.user_ent.get() == "" or self.pass_ent.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        else:
            try:
                 conn = mysql.connector.connect(host="localhost", username="root", password="Hitesh@123", database="face_recognizer")
                 my_cursor = conn.cursor()

                 my_cursor.execute("select email, password from register where email=%s", (self.username.get(),))
                 fetched_data = my_cursor.fetchone()

                 if fetched_data is not None:
                    db_username, db_password = fetched_data
                    if self.username.get() == db_username and self.password.get() == db_password:
                         self.main_window()
                    else:
                         messagebox.showerror("Error","Incorrect credentials")
                 else:
                     messagebox.showerror("Error","User not found")
            except Error as e:
                 print(f"Error connecting to database: {e}")

            finally: 
                if conn.is_connected():
                     my_cursor.close()
                     conn.close()


    #reset password--------------------------------------------->
    def reset_pass(self):
        if self.var_securityQ.get() == "Select Security Question":
            messagebox.showerror("Error", "Select Security Question")
        elif self.var_securityA.get() == "":
            messagebox.showerror("Error", "Enter Security Answer")
        elif self.var_newpass.get() == "":
            messagebox.showerror("Error", "Enter New Password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Hitesh@123", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email = %s AND securityQ = %s AND securityA = %s"
                value = (self.username.get(), self.var_securityQ.get(), self.var_securityA.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Enter Correct Answer")
                else:
                    query = "UPDATE register SET password = %s WHERE email = %s"
                    value = (self.var_newpass.get(), self.username.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    messagebox.showinfo("Success", "Password Has Successfully Changed")
            except Error as e:
                print(f"Error: {e}")
                messagebox.showerror("Error", "An error occurred while resetting the password")
            finally:
                if conn.is_connected():
                    my_cursor.close()
                    conn.close()


    #Forgot password Function---------------------------------------------------------> 
    def  forgot_password_window(self):
        if self.username.get()=="":
            messagebox.showerror("Erroe","Enter Email to Reset Password")
           
        else:
             conn = mysql.connector.connect(host="localhost", username="root", password="Hitesh@123", database="face_recognizer")
             my_cursor = conn.cursor()

             my_cursor.execute("select email from register where email=%s", (self.username.get(),))
             fetched_data = my_cursor.fetchone()

             if fetched_data is not None:
                 db_username= fetched_data
                 print(db_username)
                 conn.close()

                 #Forgot Password window-------------------------------->
                 self.root2=Toplevel()
                 self.root2.geometry("690x400+500+350")
                 #Application Name-------------------------------------------------------------------------------------------------------------------------------->
                 self.root2.title("Forgot Password")

                 #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
                 background_image7=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg7.jpg")
                 background_image7=background_image7.resize((320,400))
                 self.photoimage7=ImageTk.PhotoImage(background_image7)
                 bg_img7=Label(self.root2,image=self.photoimage7)
                 bg_img7.place(x=400,y=0,width=320,height=400)

                 #Background forgot password------------------------------------------------------------------------------------------------------------------------------>
                 background_image8=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/fp.png")
                 background_image8=background_image8.resize((400,400))
                 self.photoimage8=ImageTk.PhotoImage(background_image8)
                 bg_img8=Label(self.root2,image=self.photoimage8)
                 bg_img8.place(x=0,y=0,width=400,height=400)
                 #forgot password name------------------------->
                 fp_name=Label(bg_img7,text="Forgot Password",font=("roboto",22,"bold"),fg="#592a9c",bg="White")
                 fp_name.place(x=30,y=20,width=180,height=40)

                 #security question combobox------------------------------->
                 sec_que_lbl=Label(bg_img7,text="Security Question",font=("roboto",15,"bold"),fg="Black",bg="White")
                 sec_que_lbl.place(x=0,y=80,width=140,height=30)

                 sec_que_cmb=ttk.Combobox(bg_img7,textvariable=self.var_securityQ,font=("roboto",15,"bold"),width=20,state="readonly")
                 sec_que_cmb["values"]=("Select Security Question","What Is Your Birth Place?","What Is Your Father's Name?","What Is Your Mother Name?")
                 sec_que_cmb.current(0)
                 sec_que_cmb.place(x=0,y=110,width=240,height=25)

                 #security Answer---------------------------------------->
                 sec_ans=Label(bg_img7,text="Security Answer",font=("roboto",15,"bold"),fg="Black",bg="White")
                 sec_ans.place(x=0,y=150,width=128,height=30)

                 self.sec_ans_ent=ttk.Entry(bg_img7,textvariable=self.var_securityA,width=50,font=("times new roman",17))
                 self.sec_ans_ent.place(x=0,y=180,width=240,height=35)

                 #password---------------------------------------->
                 n_pass=Label(bg_img7,text="New Password",font=("roboto",15,"bold"),fg="Black",bg="White")
                 n_pass.place(x=0,y=230,width=120,height=30)

                 self.n_pass_ent=ttk.Entry(bg_img7,textvariable=self.var_newpass,width=50,font=("times new roman",17))
                 self.n_pass_ent.place(x=0,y=260,width=240,height=35)

                 #register Button---------------------->
                 register_btn=Button(bg_img7,text="Reset Password",command=self.reset_pass,font=("roboto",15,"bold"),fg="white",bg="#6a951f",)
                 register_btn.place(x=0,y=325,width=240,height=35)

             else:
                 messagebox.showerror("Error","Enter Valid Username")

        #Background Image 4------------------------------------------------------------------------------------------------------------------------------->
        background_image4=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg2.png")
        background_image4=background_image4.resize((1710,1112))
        self.photoimage4=ImageTk.PhotoImage(background_image4)
        bg_img4=Label(self.root,image=self.photoimage4)
        bg_img4.place(x=0,y=958,width=1710,height=30)

        #devloper name------------------->
        collage_name=Label(bg_img4,text="Copyright @ 2024 Hitesh Atkar. All Rights Reserved",font=("times new roman",13),fg="black",bg="#faa500")
        collage_name.place(x=1350,y=0,width=400,height=20)


    #Function Buttons
    def main_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)
    
    #Exit Function--------------------------------------------->
    def iexit(self):
              self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=login_window(root)
    root.mainloop()