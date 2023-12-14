from datetime import datetime
import os
from time import strftime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from unidecode import unidecode
from BLL.face import FaceBLL

class Main_Form(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1530x790+0+0")
        self.title("Phần mềm điểm danh SGU")
        self.state('zoomed')

        #banner
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, "images", "banner.png")

        image = Image.open(image_path)
        new_width = self.winfo_screenwidth()
        aspect_ratio = image.width / image.height
        new_height = int(new_width / aspect_ratio)

        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)

        canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), highlightthickness=0)
        canvas.pack(fill=BOTH, expand=YES)
        canvas.create_image(0, 0, image=photo, anchor=NW)

        #container
        bg_color = "#FFFFCC"
        canvas.create_rectangle(0, new_height, new_width, self.winfo_screenheight(), fill=bg_color, outline=bg_color)
        canvas.photo = photo

        #title
        title_lbl=Label(canvas, text="PHẦN MỀM ĐIỂM DANH SAIGON UNIVERSITY", bg='#aa4d73', fg="white", font=("Arial", 25, "bold"))
        title_lbl.place(x=0,y=new_height,width=new_width,height=45)
        b_lbl = Button(canvas, text="Đăng xuất", cursor="hand2", bg='red', fg="white", font=("Arial", 15, "bold"),command=self.logout)
        b_lbl.place(x=new_width-120,y=new_height,width=120,height=45)

        # Students
        img = Image.open(os.path.join(script_directory, "images", "presentation.png"))
        img = img.resize((300,300),Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)
        btn = Button(canvas,image=self.photoImg,cursor="hand2",bg="#FFB6C1",command=self.student)
        btn.place(x=self.winfo_screenwidth()/2-25-600-50,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn_lbl = Button(canvas,text="Thông tin Sinh Viên",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"),command=self.student)
        btn_lbl.place(x=self.winfo_screenwidth()/2-25-600-50,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Training data
        img2 = Image.open(os.path.join(script_directory, "images", "business-presentation.png"))
        img2 = img2.resize((300,300),Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        btn2 = Button(canvas,image=self.photoImg2,cursor="hand2",bg="#FFB6C1",command=self.train)
        btn2.place(x=self.winfo_screenwidth()/2-25-300,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn2_lbl = Button(canvas,text="Traning Data",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"),command=self.train)
        btn2_lbl.place(x=self.winfo_screenwidth()/2-25-300,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Face Recognition
        img3 = Image.open(os.path.join(script_directory, "images", "face-id.png"))
        img3 = img3.resize((300,300),Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        btn3 = Button(canvas,image=self.photoImg3,cursor="hand2",bg="#FFB6C1",command=self.face)
        btn3.place(x=self.winfo_screenwidth()/2+25,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn3_lbl = Button(canvas,text="Nhận diện gương mặt",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"),command=self.face)
        btn3_lbl.place(x=self.winfo_screenwidth()/2+25,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Attendance
        img4 = Image.open(os.path.join(script_directory, "images", "checked.png"))
        img4 = img4.resize((300,300),Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        btn4 = Button(canvas,image=self.photoImg4,cursor="hand2",bg="#FFB6C1",command=self.attendance)
        btn4.place(x=self.winfo_screenwidth()/2+375,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn4_lbl = Button(canvas,text="Danh sách điểm danh",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"),command=self.attendance)
        btn4_lbl.place(x=self.winfo_screenwidth()/2+375,y=self.winfo_screenheight()/2+125,width=300,height=50)

    def logout(self):
        self.destroy()
        from GUI.login import Login_Form
        form = Login_Form()
        form.lift()
        form.mainloop()

    def student(self):
        self.destroy()
        from GUI.student import Student_Form
        form = Student_Form()
        form.lift()
        form.mainloop()

    def train(self):
        data_dir=("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNP = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)

            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Hoàn thành!")

    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n",encoding="utf-8",errors="ignore") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{dtString},{d1},Có mặt")

    def face(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors,text,color, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)
                id,predict =clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                i = FaceBLL().select_id(id)
                n = FaceBLL().select_name(id)
                r = FaceBLL().select_roll(id)

                if confidence > 77:
                    cv2.putText(img, f"MSSV: {unidecode(str(i))}", (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2)
                    cv2.putText(img, f"STT: {unidecode(str(r))}", (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2)
                    cv2.putText(img, f"Name: {unidecode(str(n))}", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2)
                    self.mark_attendance(i, r, n)

                else:
                    cv2.rectangle(img,(x,y), (x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

                coord = [x,y,w,h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade,1.1,10,(255,25,255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def attendance(self):
        self.destroy()
        from GUI.attendance import Attendance_Form
        form = Attendance_Form()
        form.lift()
        form.mainloop()