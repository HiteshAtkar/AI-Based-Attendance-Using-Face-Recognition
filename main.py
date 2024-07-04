from tkinter import *
from tkmacosx import Button
from tkinter import ttk
from tkinter import PhotoImage
import tkinter
import os
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime 
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from manage_student import manage_student
from manage_attendance import manage_attendance
from help import help
import csv


class Face_Recognition_System:
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
         lbl.place(x=15,y=5,width=230,height=24)
         time()

         #logout Button------------------------>
         lg_btn=Button(bg_img1,text="Logout",font=("times new roman",15),command=self.iexit,fg="white",bg="#cf3017",)
         lg_btn.place(x=1600,y=-2,width=70,height=38)

         #help Button-------------------------->
         hlp_btn=Button(bg_img1,text="Help",command=self.help_window,font=("times new roman",15),fg="white",bg="#012a4a")
         hlp_btn.place(x=1530,y=-2,width=70,height=38)

         #New Admin Button--------------------->
         nar_btn=Button(bg_img1,text="New Admin Register",command=self.register,font=("times new roman",15),fg="white",bg="#636e72")
         nar_btn.place(x=1380,y=-2,width=150,height=38)

         #Background Image 3------------------------------------------------------------------------------------------------------------------------------>
         background_image3=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg.jpeg")
         background_image3=background_image3.resize((1710,1112))
         self.photoimage2=ImageTk.PhotoImage(background_image3)
         bg_img3=Label(self.root,image=self.photoimage2)
         bg_img3.place(x=0,y=83,width=1710,height=880)

         #Collage Logo Image------------------->
         collage_logo=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/collage_logo.png")
         collage_logo=collage_logo.resize((150,75))
         self.photoimage5=ImageTk.PhotoImage(collage_logo)
         first_label=Label(bg_img3,image=self.photoimage5)
         first_label.place(x=7,y=2,width=150,height=75)


         #container1---------------------------------------------------------------------->
         container1=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/container2.png")
         container1=container1.resize((250,800))
         self.photoimage6=ImageTk.PhotoImage(container1)
         cont1_label=Label(bg_img3,image=self.photoimage6)
         cont1_label.place(x=1480,y=-2,width=200,height=800)

         #train Image------------------------->
         train_image=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/train.png")
         train_image=train_image.resize((200,200))
         self.photoimage10=ImageTk.PhotoImage(train_image)
         trn_img=Button(bg_img3,command=self.train_classifier,image=self.photoimage10)
         trn_img.place(x=1480,y=301,width=200,height=200)

         #train Button------------------------>
         train_btn=Button(bg_img3,text="Train Model",command=self.train_classifier,font=("times new roman",20),fg="black",bg="#ebebeb")
         train_btn.place(x=1480,y=500,width=200,height=40)


         #container2---------------------------------------------------------------------->
         container2=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/container1.png")
         container2=container2.resize((200,800))
         self.photoimage7=ImageTk.PhotoImage(container2)
         cont2_label=Label(bg_img3,image=self.photoimage7)
         cont2_label.place(x=1250,y=73,width=200,height=800)

         #attendance Image-------------------->
         attendance_image=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/attendance.png")
         attendance_image=attendance_image.resize((200,200))
         self.photoimage11=ImageTk.PhotoImage(attendance_image)
         atd_img=Button(bg_img3,command=self.manage_att,image=self.photoimage11)
         atd_img.place(x=1250,y=301,width=200,height=200)

         #attendance Button------------------->
         atd_btn=Button(bg_img3,text="Manage Attendance",command=self.manage_att,font=("times new roman",20),fg="black",bg="#ebebeb")
         atd_btn.place(x=1250,y=500,width=200,height=40)


         #container3---------------------------------------------------------------------->
         container3=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/container2.png")
         container3=container3.resize((200,800))
         self.photoimage8=ImageTk.PhotoImage(container3)
         cont1_label=Label(bg_img3,image=self.photoimage8)
         cont1_label.place(x=1020,y=-2,width=200,height=800)

         #student Image----------------------->
         student_image=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/student.png")
         student_image=student_image.resize((200,200))
         self.photoimage12=ImageTk.PhotoImage(student_image)
         std_img=Button(bg_img3,command=self.manage_stud,image=self.photoimage12)
         std_img.place(x=1020,y=301,width=200,height=200)

         #student Button------------------->
         atd_btn=Button(bg_img3,command=self.manage_stud,text="Manage Student",font=("times new roman",20),fg="black",bg="#ebebeb")
         atd_btn.place(x=1020,y=500,width=200,height=40)


         #container4---------------------------------------------------------------------->
         container4=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/container1.png")
         container4=container4.resize((200,800))
         self.photoimage9=ImageTk.PhotoImage(container4)
         cont2_label=Label(bg_img3,image=self.photoimage9)
         cont2_label.place(x=790,y=73,width=200,height=800)

         #face Image--------------------------->
         face_image=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/face.png")
         face_image=face_image.resize((200,200))
         self.photoimage13=ImageTk.PhotoImage(face_image)
         fac_img=Button(bg_img3,command=self.face_recog,image=self.photoimage13)
         fac_img.place(x=790,y=301,width=200,height=200)

         #face Button--------------------->
         fac_btn=Button(bg_img3,text="Recognise Face",command=self.face_recog,font=("times new roman",20),fg="black",bg="#ebebeb")
         fac_btn.place(x=790,y=500,width=200,height=40)

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
    def manage_stud(self):
        self.new_window=Toplevel(self.root)
        self.app=manage_student(self.new_window)

    def manage_att(self):
        self.new_window=Toplevel(self.root)
        self.app=manage_attendance(self.new_window)

    def help_window(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)

    



    #Train data function---------------------------------->
    def train_classifier(self):
         try:
             
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ]
            faces=[]
            ids=[]

            for image in path:
                try:
                    img = Image.open(image).convert('L')  # Convert image to grayscale
                    image_np = np.array(img, 'uint8')
                    id = int(os.path.split(image)[1].split('.')[1])

                    faces.append(image_np)
                    ids.append(id)
                    cv2.imshow("Training Dataset", image_np)
                    cv2.waitKey(100)  # Adjust the delay time to display images (100ms here)
                except Exception as e:
                    print(f"Error loading image {image}: {e}")
            
            ids=np.array(ids)

            #train and save dataset
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Dataset Completed!")
         
         except Exception as es:
                messagebox.showerror("Error",f"Data Not Trained Due to {str(es)}")

    #Attendace marking----------------------------------------------------->
    def mark_attendance(self,i,r,n,d):  
         try:
             with open("attendance.csv","r+",newline="\n") as f:
                 myDataList=f.readlines()
                 name_list=[]
                 for line in myDataList:
                     entry=line.split(",")
                     name_list.append(entry[0])
                 
                 if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                     now=datetime.now()
                     d1=now.strftime("%d/%m/%Y")
                     dtString=now.strftime("%H:%M:%S")
                     f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
         except Exception as es:
                 messagebox.showerror("Error",f"Attendance Not Marked Due to {str(es)}")

                     
                     

    #face Recognition function-------------------------------------------------->
    def face_recog(self):
         try:
            def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                 gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                 features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                 coord=[]

                 for (x,y,w,h) in features:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                     id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                     confidence=int((100*(1-predict/300)))

                     conn=mysql.connector.connect(host="localhost",username="root",password="Hitesh@123",database="face_recognizer")
                     my_cursor=conn.cursor()

                     n = None
                     r = None
                     d = None
                     i = None

                     my_cursor.execute("select Name from student where Student_id=" + str(id))
                     n_row = my_cursor.fetchone()
                     if n_row:
                         n = "+".join(n_row)

                     my_cursor.execute("select Roll from student where Student_id=" + str(id))
                     r_row = my_cursor.fetchone()
                     if r_row:
                         r = "+".join(r_row)

                     my_cursor.execute("select Dep from student where Student_id=" + str(id))
                     d_row = my_cursor.fetchone()
                     if d_row:
                         d = "+".join(d_row)

                     my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                     i_row = my_cursor.fetchone()
                     if i_row:
                        i = "+".join(i_row)



                     if confidence>85:
                         cv2.putText(img,f"Id: {i}",(x,y-140),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                         cv2.putText(img,f"Roll: {r}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                         cv2.putText(img,f"Name: {n}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                         cv2.putText(img,f"Dep: {d}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                         self.mark_attendance(i,r,n,d)
                        
                     else:
                         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                         cv2.putText(img,"Unknown Face",(x,y-23),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                     coord=[x,y,w,h]

                 return coord
            
            def recognize(img,clf,faceCascade):
                 coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                 return img
            
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break
                
            video_cap.release()
            cv2.destroyAllWindows()
        
         except Exception as es:
                messagebox.showerror("Error",f"Face not reognized Due to {str(es)}")


    #Register Function----------------------------------->
    def register(self):
         self.root2=Toplevel()
         self.root2.geometry("690x570+515+250")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root2.title("Register New User")

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


         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image10=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg7.jpg")
         background_image10=background_image10.resize((690,570))
         self.photoimage10=ImageTk.PhotoImage(background_image10)
         bg_img10=Label(self.root2,image=self.photoimage10)
         bg_img10.place(x=0,y=0,width=690,height=570)

         login_name=Label(bg_img10,text="Register New User",font=("roboto",30,"bold"),fg="#592a9c",bg="White")
         login_name.place(x=50,y=45,width=280,height=40)

        #firstname---------------------------------------->
         f_name=Label(bg_img10,text="Firstname",font=("roboto",15,"bold"),fg="Black",bg="White")
         f_name.place(x=58,y=100,width=83,height=30)

         self.f_name_ent=ttk.Entry(bg_img10,textvariable=self.var_fname,width=50,font=("times new roman",17))
         self.f_name_ent.place(x=60,y=133,width=240,height=35)

         #lastname---------------------------------------->
         l_name=Label(bg_img10,text="Lastname",font=("roboto",15,"bold"),fg="Black",bg="White")
         l_name.place(x=375,y=100,width=83,height=30)

         self.l_name_ent=ttk.Entry(bg_img10,textvariable=self.var_lname,width=50,font=("times new roman",17))
         self.l_name_ent.place(x=380,y=133,width=240,height=35)

         #Contact No---------------------------------------->
         c_no=Label(bg_img10,text="Contact No.",font=("roboto",15,"bold"),fg="Black",bg="White")
         c_no.place(x=60,y=180,width=90,height=30)

         self.c_no_ent=ttk.Entry(bg_img10,textvariable=self.var_contact,width=50,font=("times new roman",17))
         self.c_no_ent.place(x=60,y=213,width=240,height=35)

         #Email---------------------------------------->
         mail=Label(bg_img10,text="E-Mail",font=("roboto",15,"bold"),fg="Black",bg="White")
         mail.place(x=370,y=180,width=70,height=30)

         self.mail_ent=ttk.Entry(bg_img10,textvariable=self.var_email,width=50,font=("times new roman",17))
         self.mail_ent.place(x=380,y=213,width=240,height=35)

         #security question combobox------------------------------->
         sec_que_lbl=Label(bg_img10,text="Security Question",font=("roboto",15,"bold"),fg="Black",bg="White")
         sec_que_lbl.place(x=58,y=260,width=140,height=30)

         sec_que_cmb=ttk.Combobox(bg_img10,textvariable=self.var_securityQ,font=("roboto",15,"bold"),width=20,state="readonly")
         sec_que_cmb["values"]=("Select Security Question","What Is Your Birth Place?","What Is Your Father's Name?","What Is Your Mother Name?")
         sec_que_cmb.current(0)
         sec_que_cmb.place(x=60,y=296,width=240,height=25)

         #security Answer---------------------------------------->
         sec_ans=Label(bg_img10,text="Security Answer",font=("roboto",15,"bold"),fg="Black",bg="White")
         sec_ans.place(x=380,y=260,width=128,height=30)

         self.sec_ans_ent=ttk.Entry(bg_img10,textvariable=self.var_securityA,width=50,font=("times new roman",17))
         self.sec_ans_ent.place(x=380,y=293,width=240,height=35)


         #password---------------------------------------->
         c_no=Label(bg_img10,text="Password",font=("roboto",15,"bold"),fg="Black",bg="White")
         c_no.place(x=60,y=340,width=75,height=30)

         self.c_no_ent=ttk.Entry(bg_img10,textvariable=self.var_pass,width=50,font=("times new roman",17))
         self.c_no_ent.place(x=60,y=373,width=240,height=35)

         #confirm password---------------------------------------->
         mail=Label(bg_img10,text="Confirm Password",font=("roboto",15,"bold"),fg="Black",bg="White")
         mail.place(x=380,y=340,width=140,height=30)

         self.mail_ent=ttk.Entry(bg_img10,textvariable=self.var_confpass,width=50,font=("times new roman",17))
         self.mail_ent.place(x=380,y=373,width=240,height=35)
        

        #agree terms checkbox------------------------------------->
         Chk_btn=Checkbutton(bg_img10,variable=self.var_check,text="I agree the terms and conditions",font=("roboto",15,"bold"),fg="Black",bg="White",onvalue=1,offvalue=0)
         Chk_btn.place(x=60,y=425,width=280,height=35)

         #register Button---------------------->
         register_btn=Button(bg_img10,text="Register",command=self.register_data,font=("roboto",15,"bold"),fg="white",bg="#6a951f",)
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

    #devloper Function----------------------------------->
    def devloper(self):
         self.root3=Toplevel()
         self.root3.geometry("690x500+515+320")
         #Application Name-------------------------------------------------------------------------------------------------------------------------------->
         self.root3.title("Devlopers")

         #Background Image 5------------------------------------------------------------------------------------------------------------------------------>
         background_image10=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg7.jpg")
         background_image10=background_image10.resize((690,570))
         self.photoimage10=ImageTk.PhotoImage(background_image10)
         bg_img10=Label(self.root3,image=self.photoimage10)
         bg_img10.place(x=0,y=0,width=690,height=570)

         login_name=Label(self.root3,text="Devlopers",font=("roboto",30,"bold"),fg="#592a9c",bg="White")
         login_name.place(x=15,y=15,width=180,height=40)

          #Background Image 11------------------------------------------------------------------------------------------------------------------------------>
         background_image11=Image.open("/Users/hiteshatkar/Downloads/Face Recognition/Images/bg6.png")
         background_image11=background_image11.resize((180,200))
         self.photoimage11=ImageTk.PhotoImage(background_image11)
         bg_img11=Label(self.root3,image=self.photoimage11)
         bg_img11.place(x=35,y=75,width=180,height=200)

         dev_name=Label(self.root3,text="Hitesh Atkar",font=("roboto",30,"bold"),fg="#592a9c",bg="White")
         dev_name.place(x=30,y=285,width=180,height=40)

         dev_info1=Label(self.root3,text="TY  B.Tech (IT) Student At",font=("roboto",15),fg="black",bg="White")
         dev_info1.place(x=30,y=320,width=190,height=40)

         dev_info2=Label(self.root3,text="DY Patil SOET,Ambi",font=("roboto",15,"bold"),fg="black",bg="White")
         dev_info2.place(x=30,y=350,width=150,height=40)




    





    #Exit Function--------------------------------------------->
    def iexit(self):
         self.iexit=messagebox.askyesno("Face Recognition","Do You want to Exit?")
         if self.iexit>0:
              self.root.destroy()
         else:
              return 


             

                     

                      
                     
        



         




        
        




       








        
    


        









        














if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()