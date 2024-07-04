from tkinter import *
from turtle import update
from tkmacosx import Button
from tkinter import ttk
from tkinter import PhotoImage
import os
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime 
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import numpy as np


class manage_student:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1710x1112+0+0")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root.title("Face Recognition System")

         #Variables------------------------------------------------------------------------------->
         self.var_dep=StringVar()
         self.var_course=StringVar()
         self.var_year=StringVar()
         self.var_semester=StringVar()
         self.var_std_id=StringVar()
         self.var_std_name=StringVar()
         self.var_div=StringVar()
         self.var_roll=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_email=StringVar()
         self.var_phone=StringVar()
         self.var_address=StringVar()
         self.var_teacher=StringVar()

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

         #left Frame-------------------------------->
         l_frame=Frame(bg_img3,bd=2,relief=RIDGE,bg="white")
         l_frame.place(x=1,y=1,width=843,height=868)

         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image5=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg4.png")
         background_image5=background_image5.resize((1710,44))
         self.photoimage5=ImageTk.PhotoImage(background_image5)
         bg_img5=Label(l_frame,image=self.photoimage5)
         bg_img5.place(x=0,y=0,width=1710,height=30)

         #Frame Name------------------------------------->
         l_frame_name=Label(l_frame,text="Add / Edit Student",font=("times new roman",17,"bold"),fg="white",bg="#636E72")
         l_frame_name.place(x=353,y=3,width=140,height=20)

        #Couse Frame------------------------------------->
         course_frame=Frame(l_frame,bd=2,relief=RIDGE,bg="#eeeeee")
         course_frame.place(x=-2,y=32,width=843,height=280)

        #course frame name Background image------------------------------------------------------------------------------------------------------------------------------>
         background_image6=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg3.png")
         background_image6=background_image6.resize((1710,44))
         self.photoimage6=ImageTk.PhotoImage(background_image6)
         bg_img6=Label(course_frame,image=self.photoimage6)
         bg_img6.place(x=0,y=0,width=1710,height=20)

         #course Frame Name------------------------------------->
         course_frame_name=Label(bg_img6,text="Course Details",font=("times new roman",15,"bold"),fg="Black",bg="#aaaaaa")
         course_frame_name.place(x=0,y=0,width=100,height=13)

         #course frame Background Image 7------------------------------------------------------------------------------------------------------------------------------>
         background_image7=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/course_image.jpeg")
         background_image7=background_image7.resize((500,394))
         self.photoimage7=ImageTk.PhotoImage(background_image7)
         bg_img7=Label(course_frame,image=self.photoimage7)
         bg_img7.place(x=0,y=20,width=500,height=257)


         #department combobox------------------------------->
         dep_lbl=Label(course_frame,text="Department:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         dep_lbl.place(x=500,y=59,width=150,height=25)

         dep_cmb=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",15,),width=15,state="readonly")
         dep_cmb["values"]=("Select Department","IT","Computer","Civil","Mechanical")
         dep_cmb.current(0)
         dep_cmb.place(x=640,y=59,width=170,height=25)


         #Academic year combobox------------------------------->
         ayr_lbl=Label(course_frame,text="Academic year:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         ayr_lbl.place(x=490,y=109,width=150,height=25)

         ayr_cmb=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",15,),width=15,state="readonly")
         ayr_cmb["values"]=("Select Academic Year","2022-2023","2023-2024","2024-2025","2025-2026")
         ayr_cmb.current(0)
         ayr_cmb.place(x=640,y=109,width=170,height=25)


         #year combobox------------------------------->
         yer_lbl=Label(course_frame,text="Year:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         yer_lbl.place(x=525,y=159,width=150,height=25)

         yer_cmb=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",15,),width=15,state="readonly")
         yer_cmb["values"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
         yer_cmb.current(0)
         yer_cmb.place(x=640,y=159,width=170,height=25)


         #semester combobox------------------------------->
         sem_lbl=Label(course_frame,text="Semester:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         sem_lbl.place(x=508,y=209,width=150,height=25)

         sem_cmb=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",15,),width=15,state="readonly")
         sem_cmb["values"]=("Select Semester","1st Semester","2nd Semester")
         sem_cmb.current(0)
         sem_cmb.place(x=640,y=209,width=170,height=25)
         
         #Student Frame------------------------------------->
         student_frame=Frame(l_frame,bd=2,relief=RIDGE,bg="#eeeeee")
         student_frame.place(x=-2,y=315,width=843,height=654)

         #Student frame name Background image------------------------------------------------------------------------------------------------------------------------------>
         background_image8=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg3.png")
         background_image8=background_image8.resize((1710,44))
         self.photoimage8=ImageTk.PhotoImage(background_image8)
         bg_img8=Label(student_frame,image=self.photoimage8)
         bg_img8.place(x=0,y=0,width=1710,height=20)

         #Student Frame Name------------------------------------->
         student_frame_name=Label(student_frame,text="Student Details",font=("times new roman",15,"bold"),fg="Black",bg="#aaaaaa")
         student_frame_name.place(x=5,y=2,width=100,height=13)

        

         #Student ID Entryfield----------------------------->
         sid_lbl=Label(student_frame,text="Student ID:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         sid_lbl.place(x=30,y=60,width=100,height=20)

         std_ent=ttk.Entry(student_frame,textvariable=self.var_std_id,width=50,font=("times new roman",17))
         std_ent.place(x=190,y=60,width=220,height=35)

         #Student Name Entryfield----------------------------->
         sname_lbl=Label(student_frame,text="Student Name:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         sname_lbl.place(x=432,y=60,width=120,height=20)

         sname_ent=ttk.Entry(student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",17))
         sname_ent.place(x=590,y=60,width=220,height=35)

         #Division Entryfield----------------------------->
         div_lbl=Label(student_frame,text="Division:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         div_lbl.place(x=20,y=120,width=100,height=30)

         div_cmb=ttk.Combobox(student_frame,textvariable=self.var_div,font=("times new roman",17,),width=20,state="readonly")
         div_cmb["values"]=("Select Division","A","B")
         div_cmb.current(0)
         div_cmb.place(x=190,y=120,width=220,height=35)

         #Student Rno Entryfield----------------------------->
         srno_lbl=Label(student_frame,text="Roll No:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         srno_lbl.place(x=432,y=120,width=80,height=30)

         srno_ent=ttk.Entry(student_frame,textvariable=self.var_roll,width=20,font=("times new roman",17))
         srno_ent.place(x=590,y=120,width=220,height=35)

         #Gender combobox------------------------------->
         gen_lbl=Label(student_frame,text="Gender:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         gen_lbl.place(x=20,y=180,width=100,height=35)

         gen_cmb=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("times new roman",17,),width=20,state="readonly")
         gen_cmb["values"]=("Select Gender","Male","Female","Other")
         gen_cmb.current(0)
         gen_cmb.place(x=190,y=180,width=220,height=35)

         #Student DOB Entryfield----------------------------->
         sdob_lbl=Label(student_frame,text="Date of Birth:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         sdob_lbl.place(x=442,y=180,width=100,height=30)

         sdob_ent=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",17))
         sdob_ent.place(x=590,y=180,width=220,height=35)

         #Student Email Entryfield----------------------------->
         seml_lbl=Label(student_frame,text="Email:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         seml_lbl.place(x=20,y=240,width=100,height=30)

         seml_ent=ttk.Entry(student_frame,textvariable=self.var_email,width=20,font=("times new roman",17))
         seml_ent.place(x=190,y=240,width=220,height=35)

         #Student Mobile No Entryfield----------------------------->
         smno_lbl=Label(student_frame,text="Mobile No:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         smno_lbl.place(x=440,y=240,width=90,height=30)

         smno_ent=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",17))
         smno_ent.place(x=590,y=240,width=220,height=35)

         #Student Address Entryfield----------------------------->
         sadd_lbl=Label(student_frame,text="Address:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         sadd_lbl.place(x=25,y=300,width=100,height=30)

         sadd_ent=ttk.Entry(student_frame,textvariable=self.var_address,width=20,font=("times new roman",17))
         sadd_ent.place(x=190,y=300,width=220,height=35)

         #Student Teachers Entryfield----------------------------->
         stnm_lbl=Label(student_frame,text="Teacher Name:",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         stnm_lbl.place(x=432,y=300,width=125,height=30)

         stnm_ent=ttk.Entry(student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",17))
         stnm_ent.place(x=590,y=300,width=220,height=35)

        #Take Photo Sample----------------------------------->
         tps_lbl=Label(student_frame, text="Take Photo Sample?    Yes",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         tps_lbl.place(x=37,y=365,width=200,height=35)

         self.var_radio1=StringVar()
         tps_rbt=ttk.Radiobutton(student_frame,variable=self.var_radio1,value="Yes")
         tps_rbt.place(x=240,y=365,width=20,height=35)

         #No Photo Sample----------------------------------->
         nps_lbl=Label(student_frame,text="No",font=("times new roman",17,"bold"),fg="black",bg="#eeeeee")
         nps_lbl.place(x=280,y=365,width=20,height=35)

         nps_rbt=ttk.Radiobutton(student_frame,variable=self.var_radio1,value="No")
         nps_rbt.place(x=305,y=365,width=20,height=35)

         #save Button---------------------->
         save_btn=Button(student_frame,text="Save",command=self.add_data,font=("times new roman",20),fg="white",bg="#6a951f",)
         save_btn.place(x=30,y=480,width=180,height=35)

         #update Button------------------------>
         update_btn=Button(student_frame,text="Update",command=self.update_data,font=("times new roman",20),fg="white",bg="#eda946",)
         update_btn.place(x=231,y=480,width=180,height=35)

         #delete Button------------------------>
         delete_btn=Button(student_frame,text="Delete",command=self.delete_data,font=("times new roman",20),fg="white",bg="#d45836",)
         delete_btn.place(x=633,y=480,width=180,height=35)

         #reset Button------------------------>
         reset_btn=Button(student_frame,text="Reset",command=self.reset_data,font=("times new roman",20),fg="white",bg="#2977b7",)
         reset_btn.place(x=432,y=480,width=180,height=35)

         #Take Photo Sample Button------------------------>
         tps_btn=Button(student_frame,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",20),fg="white",bg="#765465",)
         tps_btn.place(x=30,y=440,width=381,height=35)

         #Update Photo Sample Button------------------------>
         ups_btn=Button(student_frame,text="Update Photo Sample",font=("times new roman",20),fg="white",bg="#009698",)
         ups_btn.place(x=432,y=440,width=381,height=35)



 


         #Right Frame-------------------------------------------------------------------------------------->
         r_frame=Frame(bg_img3,bd=2,relief=RIDGE,bg="#eeeeee")
         r_frame.place(x=850,y=1,width=853,height=867)

         #student frame name Background image------------------------------------------------------------------------------------------------------------------------------>
         background_image9=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg4.png")
         background_image9=background_image9.resize((1710,44))
         self.photoimage9=ImageTk.PhotoImage(background_image9)
         bg_img9=Label(r_frame,image=self.photoimage9)
         bg_img9.place(x=0,y=0,width=1710,height=30)

         #right Frame Name------------------------------------->
         student_frame_name=Label(bg_img9,text="Manage Details",font=("times new roman",17,"bold"),fg="white",bg="#636E72")
         student_frame_name.place(x=353,y=0,width=120,height=20)

         #right frame name Background image------------------------------------------------------------------------------------------------------------------------------>
         background_image10=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg3.png")
         background_image10=background_image10.resize((850,27))
         self.photoimage10=ImageTk.PhotoImage(background_image10)
         bg_img10=Label(r_frame,image=self.photoimage10)
         bg_img10.place(x=0,y=31,width=850,height=24)

         #search Frame Name------------------------------------->
         search_frame_name=Label(bg_img10,text="Search details",font=("times new roman",15,"bold"),fg="Black",bg="#aaaaaa")
         search_frame_name.place(x=5,y=0,width=100,height=19)

         #Search Frame------------------------------------->
         search_frame=Frame(r_frame,bd=2,relief=RIDGE,bg="#eeeeee")
         search_frame.place(x=-2,y=56,width=853,height=95)



         #Search Label----------------------------->
         search_lbl=Label(search_frame,text="Search By:",font=("times new roman",20,"bold"),fg="REd",bg="#eeeeee")
         search_lbl.place(x=30,y=30,width=100,height=24)

         #search combobox------------------------------->
         sem_cmb=ttk.Combobox(search_frame,font=("times new roman",20,),width=15,state="readonly")
         sem_cmb["values"]=("Select","Student ID","Student Name","Class Division","Roll No","Gender","Date of Birth","E-Mail","Mobile No","Address")
         sem_cmb.current(0)
         sem_cmb.place(x=155,y=25,width=160,height=38)

         #Seach Entryfield--------------------------------->
         search_ent=ttk.Entry(search_frame,width=20,font=("times new roman",17))
         search_ent.place(x=340,y=25,width=200,height=38)

         #search Button------------------------>
         search_btn=Button(search_frame,text="Search",font=("times new roman",20),fg="white",bg="#2977b7",)
         search_btn.place(x=560,y=25,width=120,height=35)

         #Show All Button------------------------>
         show_btn=Button(search_frame,text="Show All",font=("times new roman",20),fg="white",bg="#6a951f",)
         show_btn.place(x=700,y=25,width=120,height=35)



        #Table Frame------------------------------------->
         table_frame=Frame(r_frame,bd=2,relief=RIDGE,bg="white")
         table_frame.place(x=-2,y=150,width=853,height=715)

         #scroll Bars
         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        

         self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","Student ID","Student Name","Division","Roll No","Gender","DOB","Email","Mobile No","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("Department",text="Department")
         self.student_table.heading("Course",text="Course")
         self.student_table.heading("Year",text="Year")
         self.student_table.heading("Semester",text="Semester")
         self.student_table.heading("Student ID",text="Student ID")
         self.student_table.heading("Student Name",text="Student Name")
         self.student_table.heading("Division",text="Division")
         self.student_table.heading("Roll No",text="Roll No")
         self.student_table.heading("Gender",text="Gender")
         self.student_table.heading("DOB",text="DOB")
         self.student_table.heading("Email",text="Email")
         self.student_table.heading("Mobile No",text="Mobile No")
         self.student_table.heading("Address",text="Address")

         self.student_table.column("#0",width=-10)
         self.student_table.column("Department",width=200)
         self.student_table.column("Course",width=100)
         self.student_table.column("Year",width=100)
         self.student_table.column("Semester",width=100)
         self.student_table.column("Student ID",width=100)
         self.student_table.column("Student Name",width=250)
         self.student_table.column("Division",width=80)
         self.student_table.column("Roll No",width=80)
         self.student_table.column("Gender",width=80)
         self.student_table.column("DOB",width=100)
         self.student_table.column("Email",width=250)
         self.student_table.column("Mobile No",width=120)
         self.student_table.column("Address",width=300)

         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()


         #Background Image 4------------------------------------------------------------------------------------------------------------------------------->
         background_image4=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg2.png")
         background_image4=background_image4.resize((1710,1112))
         self.photoimage4=ImageTk.PhotoImage(background_image4)
         bg_img4=Label(self.root,image=self.photoimage4)
         bg_img4.place(x=0,y=958,width=1710,height=30)

         #devloper name------------------->
         collage_name=Label(bg_img4,text="Copyright @ 2024 Hitesh Atkar. All Rights Reserved",font=("times new roman",13),fg="black",bg="#faa500")
         collage_name.place(x=1350,y=0,width=400,height=20)


#functions declaration------------------------------------------------------------------------------------------------------------------------------>
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Field are required",)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(  
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data Added Successfully")
            except Exception as es:
                messagebox.showerror("Erroe",f"Data not added Due to {str(es)}")

#Fetch Function----------------------------------->
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()

#get cursor--------------------------------------->
    def get_cursor(self,event=""):
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]

         self.var_dep.set(data[0]),
         self.var_course.set(data[1]),
         self.var_year.set(data[2]),
         self.var_semester.set(data[3]),
         self.var_std_id.set(data[4]),
         self.var_std_name.set(data[5]),
         self.var_div.set(data[6]),
         self.var_roll.set(data[7]),
         self.var_gender.set(data[8]),
         self.var_dob.set(data[9]),
         self.var_email.set(data[10]),
         self.var_phone.set(data[11]),
         self.var_address.set(data[12]),
         self.var_teacher.set(data[13]),
         self.var_radio1.set(data[14])

#Update Function---------------------------------->
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Field are required",)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update Student Details?")
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                 ))

                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details Updated Successfully!")
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Data Not Updated Due to {str(es)}")


#Delete Fumtion-------------------------------->
    def delete_data(self):
        if self.var_std_id.get()=="":
             messagebox.showerror("Error","Student id Must required")
        else:
            try:
                delete=messagebox.askyesno("Delete Details","Do You Want to Delete Details?")
                if delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
                     my_cursor=conn.cursor()
                     sql="delete from student where Student_id=%s"
                     val=(self.var_std_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Details Deleted Successfully")

            except Exception as es:
                messagebox.showerror("Error",f"Data Not Deleted Due to {str(es)}")

#Reset Function
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("")
         self.var_gender.set("Select Gender")
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")


    #generate Dataset and take sample------------------------->
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Field are required",)
        else:
            try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=self.var_std_id.get()
    
                 my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                                                 ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()


                 #load predefined data on frontal from opencv

                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(gray,2,5) #2 is Scaling factor and 5 is minimum neighbour
                     for (x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return face_cropped
                     
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                     ret,my_frame=cap.read()
                     if face_cropped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(my_frame),(500,500))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                         cv2.imshow("Cropped Face",face)

                     if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                     
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("Result","Dataset Generated Successfully")
            
            except Exception as es:
                messagebox.showerror("Error",f"Data Not Generated Due to {str(es)}")
    
    #Exit Function--------------------------------------------->
    def iexit(self):
              self.root.destroy()




                 






















































if __name__ == "__main__":
    root=Tk()
    obj=manage_student(root)
    root.mainloop()