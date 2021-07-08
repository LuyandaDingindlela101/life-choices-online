from tkinter import *
from tkinter import messagebox
from database_connection import read_table

window = Tk()
window.title("Life Choices Online")
window.geometry("500x550")


print(read_table("visitors"))


def sign_out():
    sign_out = messagebox.askquestion("Sign out?", "Are you sure you want to sign out?")

    if sign_out == "yes":
        window.destroy()
        import sign_in


canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="WELCOME BACK!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=100, y=150)

sign_out_btn = Button(window, text="SIGN OUT", width=55, bg="#8dc63f", fg="#ffffff", borderwidth=0, command=sign_out)
sign_out_btn.place(x=10, y=200)

window.mainloop()
