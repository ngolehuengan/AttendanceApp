import os
from tkinter import *
from PIL import Image, ImageTk

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
        btn.place(x=self.winfo_screenwidth()/2-850,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn_lbl = Button(canvas,text="Thông tin Sinh Viên",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"),command=self.student)
        btn_lbl.place(x=self.winfo_screenwidth()/2-850,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Teacher
        img1 = Image.open(os.path.join(script_directory, "images", "teacher.png"))
        img1 = img1.resize((300,300),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        btn1 = Button(canvas,image=self.photoImg1,cursor="hand2",bg="#FFB6C1")
        btn1.place(x=self.winfo_screenwidth()/2-500,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn1_lbl = Button(canvas,text="Thông tin Giảng Viên",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"))
        btn1_lbl.place(x=self.winfo_screenwidth()/2-500,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Training data
        img2 = Image.open(os.path.join(script_directory, "images", "business-presentation.png"))
        img2 = img2.resize((300,300),Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        btn2 = Button(canvas,image=self.photoImg2,cursor="hand2",bg="#FFB6C1")
        btn2.place(x=self.winfo_screenwidth()/2-150,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn2_lbl = Button(canvas,text="Traning Data",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"))
        btn2_lbl.place(x=self.winfo_screenwidth()/2-150,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Face Recognition
        img3 = Image.open(os.path.join(script_directory, "images", "face-id.png"))
        img3 = img3.resize((300,300),Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        btn3 = Button(canvas,image=self.photoImg3,cursor="hand2",bg="#FFB6C1")
        btn3.place(x=self.winfo_screenwidth()/2+200,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn3_lbl = Button(canvas,text="Nhận diện gương mặt",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"))
        btn3_lbl.place(x=self.winfo_screenwidth()/2+200,y=self.winfo_screenheight()/2+125,width=300,height=50)

        # Attendance
        img4 = Image.open(os.path.join(script_directory, "images", "checked.png"))
        img4 = img4.resize((300,300),Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        btn4 = Button(canvas,image=self.photoImg4,cursor="hand2",bg="#FFB6C1")
        btn4.place(x=self.winfo_screenwidth()/2+550,y=self.winfo_screenheight()/2-175,width=300,height=300)
        btn4_lbl = Button(canvas,text="Danh sách điểm danh",cursor="hand2",bg='#aa4d73', fg="white", font=("Arial", 15, "bold"))
        btn4_lbl.place(x=self.winfo_screenwidth()/2+550,y=self.winfo_screenheight()/2+125,width=300,height=50)

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