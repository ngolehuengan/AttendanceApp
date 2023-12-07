from tkinter import *
from tkinter import messagebox
from BLL.account import AccountBLL
from DTO.account import AccountDTO
from GUI.main import Main_Form
class Login_Form(Tk):
    def __init__(self,):
        super().__init__()
        self.title("LOGIN")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"360x400+{(screen_width - 360) // 2}+{(screen_height - 400) // 2}")
        self.configure(bg="#333333")
        self.resizable(False, False)

        def login():
            if AccountBLL().checkAccount(AccountDTO(username_entry.get(), password_entry.get())):
                self.withdraw()
                Main_Form().lift()
            else:
                messagebox.showerror(title="Error", message="Đăng nhập không thành công")

        def on_enter_key(event):
            login()

        login_label = Label(
            self, text="ĐĂNG NHẬP", bg='#333333', fg="#FF3399", font=("Arial", 30, "bold"))
        username_label = Label(
            self, text="Tài khoản", bg='#333333', fg="#FFFFFF", font=("Arial", 16, "bold"))
        username_entry = Entry(self, font=("Arial", 16))
        password_entry = Entry(self, show="●", font=("Arial", 16))
        password_label = Label(
            self, text="Mật khẩu", bg='#333333', fg="#FFFFFF", font=("Arial", 16,"bold"))
        login_button = Button(
            self, text="Đăng nhập", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16,"bold"), command=login)

        self.bind('<Return>', on_enter_key)

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=20)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)