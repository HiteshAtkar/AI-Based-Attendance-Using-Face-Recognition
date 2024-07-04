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


class register_window:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1710x1112+0+0")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root.title("Face Recognition System")



         #Variable declaration--------------------------------------------->
         self.var_fname=StringVar()
         self.var_lname=StringVar()
         self.var_contact=StringVar()
         self.var_email=StringVar()
         self.var_securityQ=StringVar()
         self.var_securityA=StringVar()
         self.var_pass=StringVar()
         self.var_confpass=StringVar()
         self.var_check=IntVar()


    
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

         #Background Image 3------------------------------------------------------------------------------------------------------------------------------>
         background_image3=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg6.png")
         background_image3=background_image3.resize((1710,1112))
         self.photoimage2=ImageTk.PhotoImage(background_image3)
         bg_img3=Label(self.root,image=self.photoimage2)
         bg_img3.place(x=0,y=83,width=1710,height=880)



         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image5=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg7.jpg")
         background_image5=background_image5.resize((690,570))
         self.photoimage5=ImageTk.PhotoImage(background_image5)
         bg_img5=Label(self.root,image=self.photoimage5)
         bg_img5.place(x=505,y=225,width=690,height=570)

         login_name=Label(bg_img5,text="Register New User",font=("roboto",30,"bold"),fg="#592a9c",bg="White")
         login_name.place(x=50,y=45,width=280,height=40)

        #firstname---------------------------------------->
         f_name=Label(bg_img5,text="Firstname",font=("roboto",15,"bold"),fg="Black",bg="White")
         f_name.place(x=58,y=100,width=83,height=30)

         self.f_name_ent=ttk.Entry(bg_img5,textvariable=self.var_fname,width=50,font=("times new roman",17))
         self.f_name_ent.place(x=60,y=133,width=240,height=35)

         #lastname---------------------------------------->
         l_name=Label(bg_img5,text="Lastname",font=("roboto",15,"bold"),fg="Black",bg="White")
         l_name.place(x=375,y=100,width=83,height=30)

         self.l_name_ent=ttk.Entry(bg_img5,textvariable=self.var_lname,width=50,font=("times new roman",17))
         self.l_name_ent.place(x=380,y=133,width=240,height=35)



         #Contact No---------------------------------------->
         c_no=Label(bg_img5,text="Contact No.",font=("roboto",15,"bold"),fg="Black",bg="White")
         c_no.place(x=60,y=180,width=90,height=30)

         self.c_no_ent=ttk.Entry(bg_img5,textvariable=self.var_contact,width=50,font=("times new roman",17))
         self.c_no_ent.place(x=60,y=213,width=240,height=35)

         #Email---------------------------------------->
         mail=Label(bg_img5,text="E-Mail",font=("roboto",15,"bold"),fg="Black",bg="White")
         mail.place(x=370,y=180,width=70,height=30)

         self.mail_ent=ttk.Entry(bg_img5,textvariable=self.var_email,width=50,font=("times new roman",17))
         self.mail_ent.place(x=380,y=213,width=240,height=35)

         #security question combobox------------------------------->
         sec_que_lbl=Label(bg_img5,text="Security Question",font=("roboto",15,"bold"),fg="Black",bg="White")
         sec_que_lbl.place(x=58,y=260,width=140,height=30)

         sec_que_cmb=ttk.Combobox(bg_img5,textvariable=self.var_securityQ,font=("roboto",15,"bold"),width=20,state="readonly")
         sec_que_cmb["values"]=("Select Security Question","What Is Your Birth Place?","What Is Your Father's Name?","What Is Your Mother Name?")
         sec_que_cmb.current(0)
         sec_que_cmb.place(x=60,y=296,width=240,height=25)

         #security Answer---------------------------------------->
         sec_ans=Label(bg_img5,text="Security Answer",font=("roboto",15,"bold"),fg="Black",bg="White")
         sec_ans.place(x=380,y=260,width=128,height=30)

         self.sec_ans_ent=ttk.Entry(bg_img5,textvariable=self.var_securityA,width=50,font=("times new roman",17))
         self.sec_ans_ent.place(x=380,y=293,width=240,height=35)


         #password---------------------------------------->
         c_no=Label(bg_img5,text="Password",font=("roboto",15,"bold"),fg="Black",bg="White")
         c_no.place(x=60,y=340,width=75,height=30)

         self.c_no_ent=ttk.Entry(bg_img5,textvariable=self.var_pass,width=50,font=("times new roman",17))
         self.c_no_ent.place(x=60,y=373,width=240,height=35)

         #confirm password---------------------------------------->
         mail=Label(bg_img5,text="Confirm Password",font=("roboto",15,"bold"),fg="Black",bg="White")
         mail.place(x=380,y=340,width=140,height=30)

         self.mail_ent=ttk.Entry(bg_img5,textvariable=self.var_confpass,width=50,font=("times new roman",17))
         self.mail_ent.place(x=380,y=373,width=240,height=35)
        

        #agree terms checkbox------------------------------------->
         Chk_btn=Checkbutton(bg_img5,variable=self.var_check,text="I agree the terms and conditions",font=("roboto",15,"bold"),fg="Black",bg="White",onvalue=1,offvalue=0)
         Chk_btn.place(x=60,y=425,width=280,height=35)

         #register Button---------------------->
         register_btn=Button(bg_img5,text="Register",command=self.register_data,font=("roboto",15,"bold"),fg="white",bg="#6a951f",)
         register_btn.place(x=60,y=480,width=560,height=35)






    #Register function button------------------------------------------>
         
    def register_data(self):
         if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_securityQ.get()=="Select Security Question" or self.var_securityA.get()=="":
             messagebox.showerror("Error","All Field Are Required")

         elif( self.var_pass.get()!= self.var_confpass.get()):
             messagebox.showerror("Error","Password and confirm Password Must be Same")
         
         elif self.var_check.get()==0:
             messagebox.showerror("Error","Please,Agree and Terms and Conditions")
        
         else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox("Error","User Already Exist")
             else:
                 my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                            self.var_pass.get()     
                                                                                      ))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success","User Added Successfully!")



         
             

         
         




        





































         #Background Image 4------------------------------------------------------------------------------------------------------------------------------->
         background_image4=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg2.png")
         background_image4=background_image4.resize((1710,1112))
         self.photoimage4=ImageTk.PhotoImage(background_image4)
         bg_img4=Label(self.root,image=self.photoimage4)
         bg_img4.place(x=0,y=958,width=1710,height=30)

         #devloper name------------------->
         collage_name=Label(bg_img4,text="Copyright @ 2024 Hitesh Atkar. All Rights Reserved",font=("times new roman",13),fg="black",bg="#faa500")
         collage_name.place(x=1350,y=0,width=400,height=20)





                 

















































if __name__ == "__main__":
    root=Tk()
    obj=register_window(root)
    root.mainloop()