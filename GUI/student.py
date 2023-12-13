import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from BLL.department import DepartmentBLL
from BLL.student import StudentBLL
from BLL.subject import SubjectBLL
from DTO.student import StudentDTO
import cv2

class Student_Form(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1530x790+0+0")
        self.title("Phần mềm điểm danh SGU")
        self.state('zoomed')

        #values
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_class=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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
        l_course_frame.place(x=10,y=10,width=(new_width-60)/2-25,height=(self.winfo_screenheight()-new_height-145)/3-100)

        # Chuyên ngành
        dep_lbl=Label(l_course_frame,text="Chuyên Ngành:",font=("Arial", 13, "bold"),bg="white")
        dep_lbl.grid(row=0,column=0,padx=10,sticky="W")
        self.dep_combo=ttk.Combobox(l_course_frame,textvariable=self.var_dep,font=("Arial", 13),width=18,state="readonly")
        self.dep_combo["values"]=tuple([item[0] for item in DepartmentBLL().getAll()])
        self.dep_combo.current(0)
        self.dep_combo.grid(row=0,column=1,padx=2,pady=20,sticky="W")
        self.dep_combo.bind("<<ComboboxSelected>>", self.update_subjects)

        # Mã môn
        subj_lbl=Label(l_course_frame,text="Mã môn:",font=("Arial", 13, "bold"),bg="white")
        subj_lbl.grid(row=0,column=2,padx=10,sticky="W")
        self.subj_combo=ttk.Combobox(l_course_frame,textvariable=self.var_course,font=("Arial", 13),width=7)
        self.subj_combo['values'] = ['-'] + [row[0] for row in SubjectBLL().getId(1)]
        self.subj_combo.current(0)
        self.subj_combo.grid(row=0,column=3,padx=2,pady=20,sticky="W")
        self.subj_combo.bind("<<ComboboxSelected>>", self.update_subj_name)
        self.subj_combo.bind("<KeyRelease>", self.update_subj_name)

        # Tên môn
        subj_lbl=Label(l_course_frame,text="Môn:",font=("Arial", 13, "bold"),bg="white")
        subj_lbl.grid(row=0,column=4,padx=10,sticky="W")
        self.subj_name_var = StringVar()
        self.subj_name_var.set('-')
        self.subj_name = ttk.Entry(l_course_frame,font=("Arial", 13), width=33, state="readonly", textvariable=self.subj_name_var)
        self.subj_name.grid(row=0, column=5, padx=2, pady=20, sticky="W")

        # Năm học
        year_lbl=Label(l_course_frame,text="Năm học:",font=("Arial", 13, "bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky="W")
        self.year_combo=ttk.Combobox(l_course_frame,textvariable=self.var_year,font=("Arial", 13),width=10,state="readonly")
        self.year_combo["values"]=("Chọn năm", "2021-2022", "2022-2023", "2023-2024", "2025-2026")
        self.year_combo.current(0)
        self.year_combo.grid(row=1,column=1,padx=2,pady=20,sticky="W")

        # Học kỳ
        semester_lbl=Label(l_course_frame,text="Học kỳ:",font=("Arial", 13, "bold"),bg="white")
        semester_lbl.grid(row=1,column=2,padx=10,sticky="W")
        self.semester_combo=ttk.Combobox(l_course_frame,textvariable=self.var_sem,font=("Arial", 13),width=12,state="readonly")
        self.semester_combo["values"]=("Chọn học kỳ", "Học kỳ 1", "Học kỳ 2", "Học kỳ 3")
        self.semester_combo.current(0)
        self.semester_combo.grid(row=1,column=3,columnspan=2,padx=2,pady=20,sticky="W")

        l_class_frame=LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Thông tin Nhóm lớp học",font=("Arial", 15, "bold"))
        l_class_frame.place(x=10,y=(self.winfo_screenheight()-new_height-145)/3-80,width=(new_width-60)/2-25,height=(self.winfo_screenheight()-new_height-145)*2/3+60)

        # MSSV
        id_lbl=Label(l_class_frame,text="MSSV:",font=("Arial", 13, "bold"),bg="white")
        id_lbl.grid(row=0,column=0,padx=10,sticky="W")
        self.id_entry = ttk.Entry(l_class_frame,textvariable=self.var_id,font=("Arial", 13), width=35)
        self.id_entry.grid(row=0, column=1, padx=2, pady=30, sticky="W")

        # Họ và tên
        name_lbl=Label(l_class_frame,text="Họ và tên:",font=("Arial", 13, "bold"),bg="white")
        name_lbl.grid(row=0,column=2,padx=10,sticky="W")
        self.name_entry = ttk.Entry(l_class_frame,textvariable=self.var_name,font=("Arial", 13), width=35)
        self.name_entry.grid(row=0, column=3, padx=2, pady=30, sticky="W")

        # Nhóm lớp
        class_lbl=Label(l_class_frame,text="Nhóm lớp:",font=("Arial", 13, "bold"),bg="white")
        class_lbl.grid(row=1,column=0,padx=10,sticky="W")
        self.class_combo=ttk.Combobox(l_class_frame,textvariable=self.var_class,font=("Arial", 13),width=33,state="readonly")
        self.class_combo["values"]=("Chọn nhóm","01", "02", "03", "04", "05", "06", "07", "09", "10")
        self.class_combo.current(0)
        self.class_combo.grid(row=1,column=1,padx=2,pady=20,sticky="W")

        # STT
        no_lbl=Label(l_class_frame,text="STT:",font=("Arial", 13, "bold"),bg="white")
        no_lbl.grid(row=1,column=2,padx=10,sticky="W")
        self.no_entry = ttk.Entry(l_class_frame,textvariable=self.var_roll,font=("Arial", 13), width=35)
        self.no_entry.config(state='readonly')
        self.no_entry.grid(row=1, column=3, padx=2, pady=30, sticky="W")

        # Giới tính
        gender_lbl=Label(l_class_frame,text="Giới tính:",font=("Arial", 13, "bold"),bg="white")
        gender_lbl.grid(row=2,column=0,padx=10,sticky="W")
        self.gender_combo=ttk.Combobox(l_class_frame,textvariable=self.var_gender,font=("Arial", 13),width=33,state="readonly")
        self.gender_combo["values"]=("Nam", "Nữ")
        self.gender_combo.current(0)
        self.gender_combo.grid(row=2,column=1,padx=2,pady=20,sticky="W")

        # Ngày sinh
        dob_lbl=Label(l_class_frame,text="Ngày sinh:",font=("Arial", 13, "bold"),bg="white")
        dob_lbl.grid(row=2,column=2,padx=10,sticky="W")
        self.dob_entry = ttk.Entry(l_class_frame,textvariable=self.var_dob,font=("Arial", 13), width=35)
        self.dob_entry.grid(row=2, column=3, padx=2, pady=30, sticky="W")

        # email
        email_lbl=Label(l_class_frame,text="Email:",font=("Arial", 13, "bold"),bg="white")
        email_lbl.grid(row=3,column=0,padx=10,sticky="W")
        self.email_entry = ttk.Entry(l_class_frame,textvariable=self.var_email,font=("Arial", 13), width=35)
        self.email_entry.grid(row=3, column=1, padx=2, pady=30, sticky="W")

        # sđt
        contact_lbl=Label(l_class_frame,text="SĐT:",font=("Arial", 13, "bold"),bg="white")
        contact_lbl.grid(row=3,column=2,padx=10,sticky="W")
        self.contact_entry = ttk.Entry(l_class_frame,textvariable=self.var_phone,font=("Arial", 13), width=35)
        self.contact_entry.grid(row=3, column=3, padx=2, pady=30, sticky="W")

        # địa chỉ
        address_lbl=Label(l_class_frame,text="Địa chỉ:",font=("Arial", 13, "bold"),bg="white")
        address_lbl.grid(row=4,column=0,padx=10,sticky="W")
        self.address_entry = ttk.Entry(l_class_frame,textvariable=self.var_address,font=("Arial", 13), width=35)
        self.address_entry.grid(row=4, column=1, padx=2, pady=30, sticky="W")

        # giảng viên
        teacher_lbl=Label(l_class_frame,text="Giảng viên:",font=("Arial", 13, "bold"),bg="white")
        teacher_lbl.grid(row=4,column=2,padx=10,sticky="W")
        self.teacher_entry = ttk.Entry(l_class_frame,textvariable=self.var_teacher,font=("Arial", 13), width=35)
        self.teacher_entry.grid(row=4, column=3, padx=2, pady=30, sticky="W")

        # radio
        self.var_radio = StringVar()
        radiobtn = ttk.Radiobutton(l_class_frame,variable=self.var_radio,text="Chụp ảnh mẫu", value="Yes")
        radiobtn.grid(row=6, column=0, padx=10)
        radiobtn1= ttk.Radiobutton(l_class_frame,variable=self.var_radio,text="Không có ảnh mẫu", value="No")
        radiobtn1.grid(row=6, column=1)

        btn_frame=Frame(l_class_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=485,width=(new_width-60)/2-30,height=40)
        save_btn=Button(btn_frame,command=self.add_data,text="Thêm",width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,command=self.update_data,text="Sửa",width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)
        delete_btn=Button(btn_frame,command=self.delete_data,text="Xóa",width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)
        create_btn=Button(btn_frame,command=self.reset_data,text="Nhập lại",width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        create_btn.grid(row=0,column=3)

        btn1_frame=Frame(l_class_frame,bd=2,relief=RIDGE,bg='white')
        btn1_frame.place(x=0,y=525,width=(new_width-60)/2-30,height=40)
        add_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Thêm ảnh mẫu",width=37,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        add_photo_btn.grid(row=0,column=0)
        update_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Cập nhật ảnh mẫu",width=37,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_btn.grid(row=0,column=1)

        r_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Chi tiết Sinh viên",font=("Arial", 15, "bold"))
        r_frame.place(x=(new_width-60)/2+10,y=10,width=(new_width-60)/2-5,height=self.winfo_screenheight()-new_height-125)

        r_search_frame=LabelFrame(r_frame,bd=2,bg="white",relief=RIDGE,text="Tìm kiếm",font=("Arial", 15, "bold"))
        r_search_frame.place(x=10,y=10,width=(new_width-60)/2-25,height=75)

        search_lbl=Label(r_search_frame,text="Tìm kiếm:",font=("Arial", 14, "bold"),bg="red",fg="white")
        search_lbl.grid(row=0,column=0,padx=10,sticky="W")

        self.search_combo=ttk.Combobox(r_search_frame,font=("Arial", 13),width=8,state="readonly")
        self.search_combo["values"]=("Chọn","MSSV","Nhóm lớp")
        self.search_combo.current(0)
        self.search_combo.grid(row=0,column=1,padx=2,sticky="W")

        self.search_entry = ttk.Entry(r_search_frame,font=("Arial", 14), width=35)
        self.search_entry.grid(row=0, column=2, padx=10, sticky="W")

        search_btn=Button(r_search_frame,text="Tìm kiếm",width=10,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        search_btn.grid(row=0,column=3)
        show_btn=Button(r_search_frame,text="Tất cả",width=10,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        show_btn.grid(row=0,column=4)

        r_table_frame=LabelFrame(r_frame,bd=2,bg="white",relief=RIDGE)
        r_table_frame.place(x=10,y=95,width=(new_width-60)/2-25,height=690)

        scroll_x=ttk.Scrollbar(r_table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(r_table_frame,orient=VERTICAL)
        self.table=ttk.Treeview(r_table_frame,columns=("roll","course","year","sem","id","name","class","gender","dob","email","contact","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        columns_with_width = {
            "roll": "STT",
            "course": "Mã môn",
            "year": "Năm học",
            "sem": "Học kỳ",
            "id": "MSSV",
            "name": "Họ và tên",
            "class": "Nhóm lớp",
            "gender": "Giới tính",
            "dob": "Ngày sinh",
            "email": "Email",
            "contact": "SĐT",
            "address": "Địa chỉ",
            "teacher": "Giảng viên",
            "photo": "Ảnh"
        }
        for column, heading in columns_with_width.items():
            self.table.heading(column, text=heading)
            self.table.column(column, width=100)
        self.table.column("roll", width=50)
        self.table["show"]="headings"
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def back(self):
        self.destroy()
        from GUI.main import Main_Form
        form = Main_Form()
        form.lift()
        form.mainloop()

    def update_subjects(self, event):
        selected_dep = self.dep_combo.current()+1
        subjects = ['Chọn môn học'] + [row[0] for row in SubjectBLL().getId(selected_dep)]
        if subjects:
            self.subj_combo['values'] = subjects
            self.subj_combo.current(0)
            self.subj_name_var.set('-')
        else:
            self.subj_combo.set('-')
            self.subj_combo['values'] = []

    def update_subj_name(self, event):
        selected_subj_id = self.subj_combo.get()
        if selected_subj_id != '-':
            subj_values_list = SubjectBLL().getName(selected_subj_id)
            if subj_values_list:
                cleaned_values = [str(value[0]).strip('{} ') for value in subj_values_list]
                cleaned_value = cleaned_values[0] if cleaned_values else '-'
                self.subj_name_var.set(cleaned_value)
        else:
            self.subj_name_var.set('-')

    def add_data(self):
        if self.var_course.get()=="-" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","Bắt buộc đủ thông tin")
        else:
            try:
                StudentBLL().insert(StudentDTO(self.var_course,self.var_year,self.var_sem,self.var_class,self.var_id,self.var_name,self.var_gender,self.var_dob,self.var_email,self.var_phone,self.var_address,self.var_teacher,self.var_radio))
                self.fetch_data()
                messagebox.showinfo("Success","Lưu thành công")
            except Exception as e:
                messagebox.showerror("Error",f"Đã xảy ra lỗi: {str(e)}")

    def fetch_data(self):
        data=StudentBLL().show()
        self.table.delete(*self.table.get_children())
        if data != 0:
            for i in data:
                self.table.insert("",END,values=i)

    def get_cursor(self, event):
        cursor_focus=self.table.focus()
        content=self.table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set([str(value[0]).strip('{} ') for value in DepartmentBLL().getName(data[1])][0] if [str(value[0]).strip('{} ') for value in DepartmentBLL().getName(data[1])] else '-'),
        self.var_course.set(data[1]),
        self.subj_name_var.set([str(value[0]).strip('{} ') for value in SubjectBLL().getName(data[1])][0] if [str(value[0]).strip('{} ') for value in SubjectBLL().getName(data[1])] else '-')
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_roll.set(data[0]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio.set(data[13])

    def update_data(self):
        if self.var_course.get()=="-" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","Bắt buộc đủ thông tin")
        else:
            try:
                update=messagebox.askyesno("Update","Bạn có muốn chỉnh sửa thông tin của học sinh này?",parent=self)
                if update>0:
                    StudentBLL().update(StudentDTO(
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_class.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get()
                    ))
                else:
                    if not update:
                        return
                self.fetch_data()
                messagebox.showinfo("Success","Chỉnh sửa thành công",parent=self)
            except Exception as e:
                messagebox.showerror("Error",f"Đã xảy ra lỗi: {str(e)}")

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error","Chưa chọn sinh viên",parent=self)
        else:
            try:
                delete=messagebox.askyesno("Delete","Xác nhận xóa sinh viên này?",parent=self)
                if delete>0:
                    StudentBLL().delete(self.var_id.get())
                else:
                    if not delete:
                        return
                self.fetch_data()
                messagebox.showinfo("Success","Xóa thành công",parent=self)
            except Exception as e:
                messagebox.showerror("Error",f"Đã xảy ra lỗi: {str(e)}")

    def reset_data(self):
        self.var_dep.set('Chọn chuyên ngành'),
        self.var_course.set('Chọn môn'),
        self.subj_name_var.set('-')
        self.var_year.set('Chọn năm'),
        self.var_sem.set('Chọn học kỳ'),
        self.var_roll.set(''),
        self.var_id.set(''),
        self.var_name.set(''),
        self.var_class.set('Chọn nhóm'),
        self.var_gender.set('Nam'),
        self.var_dob.set(''),
        self.var_email.set(''),
        self.var_phone.set(''),
        self.var_address.set(''),
        self.var_teacher.set(''),
        self.var_radio.set('')

    def generate_dataset(self):
        if self.var_course.get()=="-" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","Bắt buộc đủ thông tin")
        else:
            try:
                data=StudentBLL().show()
                id=0
                for i in data:
                    id+=1
                StudentBLL().update(StudentDTO(
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_class.get(),
                    str(id + 1),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio.get()
                ))
                self.fetch_data()
                self.reset_data()

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame = cap.read(cv2.IMREAD_GRAYSCALE)
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Chụp mặt",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Tạo dữ liệu thành công!")
            except Exception as e:
                messagebox.showerror("Error",f"Đã xảy ra lỗi: {str(e)}", parent=self)