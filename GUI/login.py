from tkinter import *
from tkinter import messagebox

class Login_Form:
    def __init__(self,root):
        self.root = root
        self.root.title("LOGIN")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"360x400+{(screen_width - 360) // 2}+{(screen_height - 400) // 2}")
        self.root.configure(bg="#333333")
        self.root.resizable(False, False)

        def login():
            username = "johnsmith"
            password = "12345"
            if username_entry.get()==username and password_entry.get()==password:
                messagebox.showinfo(title="Login Success", message="Đăng nhập thành công")
            else:
                messagebox.showerror(title="Error", message="Đăng nhập không thành công")

        login_label = Label(
            self.root, text="ĐĂNG NHẬP", bg='#333333', fg="#FF3399", font=("Arial", 30))
        username_label = Label(
            self.root, text="Tài khoản", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        username_entry = Entry(self.root, font=("Arial", 16))
        password_entry = Entry(self.root, show="●", font=("Arial", 16))
        password_label = Label(
            self.root, text="Mật khẩu", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        login_button = Button(
            self.root, text="Đăng nhập", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=20)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)