import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student_Form(Toplevel):
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
        title_lbl=Label(canvas, text="QUẢN LÝ SINH VIÊN", bg='#aa4d73', fg="white", font=("Arial", 25, "bold"))
        title_lbl.place(x=0,y=new_height,width=new_width,height=45)
        b_lbl = Button(canvas, text="Trở về", cursor="hand2", bg='#333333', fg="white", font=("Arial", 15, "bold"),command=self.back)
        b_lbl.place(x=new_width-120,y=new_height,width=120,height=45)

        #Form
        frame=Frame(canvas, bd=2,bg="white")
        frame.place(x=20,y=new_height+65,width=new_width-40,height=self.winfo_screenheight()-new_height-105)

        l_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Thông tin Sinh viên",font=("Arial", 15, "bold"))
        l_frame.place(x=10,y=10,width=(new_width-60)/2-5,height=self.winfo_screenheight()-new_height-125)

        l_course_frame=LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Thông tin Khóa học",font=("Arial", 15, "bold"))
        l_course_frame.place(x=10,y=10,width=(new_width-60)/2-25,height=(self.winfo_screenheight()-new_height-145)/3-30)

        dep_lbl=Label(l_course_frame,text="Chuyên Ngành",font=("Arial", 15, "bold"))
        dep_lbl.grid(row=0,column=0)
        dep_combo=ttk.Combobox(l_course_frame,font=("Arial", 15, "bold"),width=17)
        dep_combo["values"]=("Chọn Chuyên Ngành")
        dep_combo.grid(row=0,column=1)

        # l_class_frame=LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Thông tin Lớp học",font=("Arial", 15, "bold"))
        # l_class_frame.place(x=10,y=(self.winfo_screenheight()-new_height-145)/3-20,width=(new_width-60)/2-25,height=(self.winfo_screenheight()-new_height-145)*2/3)

        r_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Chi tiết Sinh viên",font=("Arial", 15, "bold"))
        r_frame.place(x=(new_width-60)/2+10,y=10,width=(new_width-60)/2-5,height=self.winfo_screenheight()-new_height-125)

    def back(self):
        self.destroy()
        from GUI.main import Main_Form
        form = Main_Form()
        form.lift()
        form.mainloop()