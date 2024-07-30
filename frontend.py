from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title('Salary Management System')
root.iconbitmap('C:\PPPPP\project2024\icon.png')
root.geometry("800x800+700+60")

# Open Image
my_logo = Image.open("icon.png")

# Resize Image
resized_logo = my_logo.resize((150, 150),Image.ANTIALIAS)

new_logopic = ImageTk.PhotoImage(resized_logo)

# Image size 512x512
LabelLogo = Label(root, image=new_logopic)
text = Label(root, text="")
LabelLogo.pack()

LabelLogo.grid(row=10, column=10)
text.grid(row=1, column=1)

root.mainloop()