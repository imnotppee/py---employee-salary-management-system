from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title('Salary Management System') # Title program
root.iconbitmap('C:\PPPPP\project2024\icon.png') # icon porgram 
root.geometry("1000x800+500+50")    # size of windowed

# Open Image
my_logo = Image.open("icon.png")

# Resize Image
resized_logo = my_logo.resize((150, 150),Image.ANTIALIAS)

new_logopic = ImageTk.PhotoImage(resized_logo)

# Image size 512x512
LabelLogo = Label(root, image=new_logopic)
blanktext = Label(root, text="")
LabelLogo.pack()

LabelLogo.grid(row=10, column=10)
blanktext.grid(row=1, column=1)

root.mainloop()