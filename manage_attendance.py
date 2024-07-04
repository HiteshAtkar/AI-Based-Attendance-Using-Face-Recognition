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

class manage_attendance:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1710x1112+0+0")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root.title("Face Recognition System")

         #Variable Declaration------------------------------->
         self.var_atten_id=StringVar()
         self.var_atten_roll=StringVar()
         self.var_atten_name=StringVar()
         self.var_atten_dep=StringVar()
         self.var_atten_time=StringVar()
         self.var_atten_date=StringVar()
         self.var_atten_attendance=StringVar()

    
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
         l_frame_name=Label(l_frame,text="Manage Attendance Details",font=("times new roman",17,"bold"),fg="white",bg="#636E72")
         l_frame_name.place(x=300,y=3,width=200,height=20)

        #Manage Attendance details Frame------------------------------------->
         mad_frame=Frame(l_frame,bd=2,relief=RIDGE,bg="white")
         mad_frame.place(x=-2,y=32,width=843,height=834)


         #Background Image 6------------------------------------------------------------------------------------------------------------------------------>
         background_image6=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg5.png")
         background_image6=background_image6.resize((640,450))
         self.photoimage6=ImageTk.PhotoImage(background_image6)
         bg_img6=Label(mad_frame,image=self.photoimage6)
         bg_img6.place(x=70,y=0,width=640,height=450)


         #Student ID Entryfield----------------------------->
         att_id_lbl=Label(mad_frame,text="Student ID:",font=("times new roman",17,"bold"),fg="black",bg="White")
         att_id_lbl.place(x=30,y=500,width=100,height=20)

         att_id_ent=ttk.Entry(mad_frame,textvariable=self.var_atten_id,width=50,font=("times new roman",17))
         att_id_ent.place(x=190,y=500,width=220,height=35)

         #Student Roll Entryfield----------------------------->
         roll_lbl=Label(mad_frame,text="Roll No:",font=("times new roman",17,"bold"),fg="black",bg="White")
         roll_lbl.place(x=432,y=500,width=120,height=20)

         roll_ent=ttk.Entry(mad_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",17))
         roll_ent.place(x=590,y=500,width=220,height=35)


         #Student name Entryfield----------------------------->
         name_lbl=Label(mad_frame,text="Name:",font=("times new roman",17,"bold"),fg="black",bg="White")
         name_lbl.place(x=30,y=565,width=100,height=20)

         name_ent=ttk.Entry(mad_frame,textvariable=self.var_atten_name,width=50,font=("times new roman",17))
         name_ent.place(x=190,y=565,width=220,height=35)


         #department combobox------------------------------->
         dep_lbl=Label(mad_frame,text="Department:",font=("times new roman",17,"bold"),fg="black",bg="white")
         dep_lbl.place(x=432,y=565,width=120,height=20)

         dep_cmb=ttk.Combobox(mad_frame,textvariable=self.var_atten_dep,font=("times new roman",17,),width=15,state="readonly")
         dep_cmb["values"]=("Select Department","IT","Computer","Civil","Mechanical")
         dep_cmb.current(0)
         dep_cmb.place(x=590,y=565,width=220,height=35)


         #time Entryfield----------------------------->
         time_id_lbl=Label(mad_frame,text="Time:",font=("times new roman",17,"bold"),fg="black",bg="White")
         time_id_lbl.place(x=30,y=630,width=100,height=20)

         time_id_ent=ttk.Entry(mad_frame,textvariable=self.var_atten_time,width=50,font=("times new roman",17))
         time_id_ent.place(x=190,y=630,width=220,height=35)

         #Date Entryfield----------------------------->
         date_lbl=Label(mad_frame,text="Date:",font=("times new roman",17,"bold"),fg="black",bg="White")
         date_lbl.place(x=432,y=630,width=120,height=20)

         date_ent=ttk.Entry(mad_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",17))
         date_ent.place(x=590,y=630,width=220,height=35)



         #attendance combobox------------------------------->
         att_lbl=Label(mad_frame,text="Department:",font=("times new roman",17,"bold"),fg="black",bg="white")
         att_lbl.place(x=30,y=695,width=120,height=20)

         att_cmb=ttk.Combobox(mad_frame,textvariable=self.var_atten_attendance,font=("times new roman",17,),width=15,state="readonly")
         att_cmb["values"]=("Select Status","Present","Absent")
         att_cmb.current(0)
         att_cmb.place(x=190,y=695,width=220,height=35)



         #Import CSV Button---------------------->
         imp_btn=Button(mad_frame,text="Import CSV",command=self.importCsv,font=("times new roman",20),fg="white",bg="#6a951f",)
         imp_btn.place(x=30,y=770,width=180,height=40)

         #Export CSV Button------------------------>
         exp_btn=Button(mad_frame,text="Export CSV",command=self.exportCsv,font=("times new roman",20),fg="white",bg="#eda946",)
         exp_btn.place(x=231,y=770,width=180,height=40)

         #Reset Button------------------------>
         update_btn=Button(mad_frame,text="Reset",command=self.reset_data,font=("times new roman",20),fg="white",bg="#d45836",)
         update_btn.place(x=633,y=770,width=180,height=40)

         #Update Button------------------------>
         reset_btn=Button(mad_frame,text="Update",font=("times new roman",20),fg="white",bg="#2977b7",)
         reset_btn.place(x=432,y=770,width=180,height=40)


         #Right Frame-------------------------------------------------------------------------------------->
         r_frame=Frame(bg_img3,bd=2,relief=RIDGE,bg="white")
         r_frame.place(x=850,y=1,width=853,height=867)

         #student frame name Background image------------------------------------------------------------------------------------------------------------------------------>
         background_image9=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg4.png")
         background_image9=background_image9.resize((1710,44))
         self.photoimage9=ImageTk.PhotoImage(background_image9)
         bg_img9=Label(r_frame,image=self.photoimage9)
         bg_img9.place(x=0,y=0,width=1710,height=30)

         #right Frame Name------------------------------------->
         student_frame_name=Label(bg_img9,text="Attendance Details",font=("times new roman",17,"bold"),fg="white",bg="#636E72")
         student_frame_name.place(x=353,y=0,width=180,height=20)

         #Right table Frame-------------------------------------------------------------------------------------->
         table_frame=Frame(bg_img3,bd=2,relief=RIDGE,bg="white")
         table_frame.place(x=850,y=35,width=853,height=832)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #scrollbars
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x.config(command=self.AttendanceReportTable.xview)
         scroll_y.config(command=self.AttendanceReportTable.yview)

         self.AttendanceReportTable.heading("id",text="ID")
         self.AttendanceReportTable.heading("roll",text="Roll No")
         self.AttendanceReportTable.heading("name",text="Name")
         self.AttendanceReportTable.heading("department",text="Department")
         self.AttendanceReportTable.heading("time",text="Time")
         self.AttendanceReportTable.heading("date",text="Date")
         self.AttendanceReportTable.heading("attendance",text="Attendance")

         self.AttendanceReportTable["show"]="headings"

         self.AttendanceReportTable.column("#0",width=-10)
         self.AttendanceReportTable.column("id",width=30)
         self.AttendanceReportTable.column("roll",width=30)
         self.AttendanceReportTable.column("name",width=150)
         self.AttendanceReportTable.column("department",width=100)
         self.AttendanceReportTable.column("time",width=100)
         self.AttendanceReportTable.column("date",width=100)
         self.AttendanceReportTable.column("attendance",width=100)

         self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    #attendance Import CSV-------------------------------------------------> 
    def fetchData(self,rows):
         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
         for i in rows:
             self.AttendanceReportTable.insert("",END,values=i)
         

    def importCsv(self):
         global mydata
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
         with open(fln) as myfile:
             csvread=csv.reader(myfile,delimiter=",")
             for i in csvread:
                 mydata.append(i)
             self.fetchData(mydata)


    #attendance Export CSV------------------------------------------------>
    def exportCsv(self):
         try:
             if len(mydata)<1:
                 messagebox.showerror("Error","No Data Found In File")
                 return False
             else:
                 fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                 with open(fln,mode="w",newline="") as myfile:
                     exp_write=csv.writer(myfile,delimiter=",")
                     for i in mydata:
                         exp_write.writerow(i)
                     messagebox.showinfo("Resukt","Data Exported to "+os.path.basename(fln)+" Successfully")
         
         except Exception as es:
                messagebox.showerror("Error",f"Data Not Exported Due to {str(es)}")


    
    #Attendance Data to variable function
    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])
         self.var_atten_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_date.set(rows[5])
         self.var_atten_attendance.set(rows[6])


    
    def reset_data(self):
         self.var_atten_id.set("")
         self.var_atten_roll.set("")
         self.var_atten_name.set("")
         self.var_atten_dep.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance.set("")
         

                     

                 












             
         


        
                 










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
    obj=manage_attendance(root)
    root.mainloop()