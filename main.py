from tkinter import *
from PIL import Image, ImageTk

class Attendance_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Phần mềm điểm danh SGU")

        img = Image.open(r"images/IMG_7238.PNG")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImg)
        f_lbl.place(x = 0, y = 0, width=500, height=130)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance_App(root)
    root.mainloop()