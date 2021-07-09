from tkinter import *
from utilities import *
from database_connection import read_table, drop_table, create_admin_table, insert_admin

window = Tk()
window.geometry("500x400")
window.title("Life Choices Online")


def sign_admin_in():
    try:
        name = name_entry.get()
        id_number = id_number_entry.get()

        if validate_min_entries(name, id_number):
            if admin_exists(name, id_number):
                window.destroy()
                import admin
            else:
                messagebox.showerror("Validation error", "User is not admin")
    except ValueError:
        messagebox.showerror("Validation Error", "Please check your inputs")


canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="ADMIN SIGN IN!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=150, y=150)

name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
name_label.place(x=10, y=200)
name_entry = Entry(window)
name_entry.place(x=10, y=220)

id_number_label = Label(window, text="Please enter ID Number!", fg="#8dc63f", font="Helvetica")
id_number_label.place(x=250, y=200)
id_number_entry = Entry(window)
id_number_entry.place(x=250, y=220)

sign_in_btn = Button(window, text="SIGN UP", width=50, bg="#8dc63f", fg="#ffffff", borderwidth=0, command=sign_admin_in)
sign_in_btn.place(x=10, y=300)

window.mainloop()