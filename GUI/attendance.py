import csv
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

data=[]
class Attendance_Form(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1530x790+0+0")
        self.title("Phần mềm điểm danh SGU")
        self.state('zoomed')

        #values
        self.var_roll=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

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
        title_lbl=Label(canvas, text="DANH SÁCH ĐIỂM DANH", bg='#aa4d73', fg="white", font=("Arial", 25, "bold"))
        title_lbl.place(x=0,y=new_height,width=new_width,height=45)
        b_lbl = Button(canvas, text="Trở về", cursor="hand2", bg='#333333', fg="white", font=("Arial", 15, "bold"),command=self.back)
        b_lbl.place(x=new_width-120,y=new_height,width=120,height=45)

        frame=Frame(canvas, bd=2,bg="white")
        frame.place(x=20,y=new_height+65,width=new_width-40,height=self.winfo_screenheight()-new_height-105)

        l_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Thông tin Sinh viên",font=("Arial", 15, "bold"))
        l_frame.place(x=10,y=10,width=(new_width-60)/2-5,height=self.winfo_screenheight()-new_height-125)

        # STT
        roll_lbl=Label(l_frame,text="STT:",font=("Arial", 13, "bold"),bg="white")
        roll_lbl.grid(row=0,column=0,padx=15,sticky="W")
        self.roll_entry = ttk.Entry(l_frame,textvariable=self.var_roll,font=("Arial", 13), width=35)
        self.roll_entry.grid(row=0, column=1, padx=2, pady=30, sticky="W")

        # MSSV
        id_lbl=Label(l_frame,text="MSSV:",font=("Arial", 13, "bold"),bg="white")
        id_lbl.grid(row=0,column=2,padx=15,sticky="W")
        self.id_entry = ttk.Entry(l_frame,textvariable=self.var_id,font=("Arial", 13), width=35)
        self.id_entry.grid(row=0, column=3, padx=2, pady=30, sticky="W")

        # Họ và tên
        name_lbl=Label(l_frame,text="Họ và tên:",font=("Arial", 13, "bold"),bg="white")
        name_lbl.grid(row=1,column=0,padx=15,sticky="W")
        self.name_entry = ttk.Entry(l_frame,textvariable=self.var_name,font=("Arial", 13), width=35)
        self.name_entry.grid(row=1, column=1, padx=2, pady=30, sticky="W")

        # Thời gian
        time_lbl=Label(l_frame,text="Thời gian:",font=("Arial", 13, "bold"),bg="white")
        time_lbl.grid(row=1,column=2,padx=15,sticky="W")
        self.time_entry = ttk.Entry(l_frame,textvariable=self.var_time,font=("Arial", 13), width=35)
        self.time_entry.grid(row=1, column=3, padx=2, pady=30, sticky="W")

        # Ngày
        date_lbl=Label(l_frame,text="Ngày:",font=("Arial", 13, "bold"),bg="white")
        date_lbl.grid(row=2,column=0,padx=15,sticky="W")
        self.date_entry = ttk.Entry(l_frame,textvariable=self.var_date,font=("Arial", 13), width=35)
        self.date_entry.grid(row=2, column=1, padx=2, pady=30, sticky="W")

        # Điểm danh
        status_lbl=Label(l_frame,text="Điểm danh:",font=("Arial", 13, "bold"),bg="white")
        status_lbl.grid(row=2,column=2,padx=15,sticky="W")
        self.gender_combo=ttk.Combobox(l_frame,textvariable=self.var_status,font=("Arial", 13),width=33,state="readonly")
        self.gender_combo["values"]=("Vắng mặt", "Có mặt")
        self.gender_combo.current(0)
        self.gender_combo.grid(row=2,column=3,padx=2,pady=20,sticky="W")

        btn_frame=Frame(l_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=485,width=(new_width-60)/2-10,height=40)
        import_btn=Button(btn_frame,text="Nhập csv",command=self.import_csv,width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        import_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame,text="Xuất csv",command=self.export_csv,width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        export_btn.grid(row=0,column=1)
        update_btn=Button(btn_frame,text="Sửa",command=self.update_data,width=18,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Nhập lại",command=self.reset_data,width=19,font=("Arial", 14, "bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        r_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Chi tiết Sinh viên",font=("Arial", 15, "bold"))
        r_frame.place(x=(new_width-60)/2+10,y=10,width=(new_width-60)/2-5,height=self.winfo_screenheight()-new_height-125)

        scroll_x=ttk.Scrollbar(r_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(r_frame,orient=VERTICAL)
        self.table=ttk.Treeview(r_frame,columns=("id","roll","name","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        columns_with_width = {
            "id": "MSSV",
            "roll": "STT",
            "name": "Họ và tên",
            "time": "Thời gian",
            "date": "Ngày",
            "status": "Điểm danh"
        }
        for column, heading in columns_with_width.items():
            self.table.heading(column, text=heading)
            self.table.column(column, width=100)
        self.table.column("roll", width=50)
        self.table["show"]="headings"
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)

    def back(self):
        self.destroy()
        from GUI.main import Main_Form
        form = Main_Form()
        form.lift()
        form.mainloop()

    def fetch_data(self,rows):
        self.table.delete(*self.table.get_children())
        for i in rows:
            self.table.insert("",END,values=i)

    def import_csv(self):
        global data
        data.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self)
        with open(fln, encoding='utf-8') as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                if len(i)!=0:
                    data.append(i)
            self.fetch_data(data)

    def export_csv(self):
        try:
            if len(data)<1:
                messagebox.showerror("Error","Không có dữ liệu để xuất",parent=self)
                return False
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self)
            with open(fln,mode='w',newline="", encoding='utf-8') as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in data:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Xuất csv thành công "+os.path.basename(fln),parent=self)
        except Exception as e:
                messagebox.showerror("Error",f"Đã xảy ra lỗi: {str(e)}")

    def get_cursor(self, event):
        cursor_focus = self.table.focus()
        content = self.table.item(cursor_focus)
        rows = content["values"]

        if rows:
            if len(rows) >= 6:
                self.var_roll.set(rows[1])
                self.var_id.set(rows[2])
                self.var_name.set(rows[2])
                self.var_time.set(rows[3])
                self.var_date.set(rows[4])
                self.var_status.set(rows[5])

    def reset_data(self):
        self.var_roll.set(''),
        self.var_id.set(''),
        self.var_name.set(''),
        self.var_time.set(''),
        self.var_date.set(''),
        self.var_status.set('Vắng mặt')

    def update_data(self):
        pass
