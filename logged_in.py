from tkinter import *
from tkinter import messagebox
from duplicity.dup_time import curtime
from database_connection import select_from_table, update_table

window = Tk()
window.title("Life Choices Online")
window.geometry("500x550")

message = StringVar()


def sign_out():
    sign_out = messagebox.askquestion("Sign out?", "Are you sure you want to sign out?")

    if sign_out == "yes":
        #   FIRST, WE HAVE TO FIND OUT WHO IS LOGGED IN BY QUERYING THE DATABASE FOR WHERE logged_inn = 1
        visitor = select_from_table("SELECT * FROM visitors WHERE logged_in = 1")[0]
        #   CHANGE THEIR logged_in VALUE TO 0
        update_table("UPDATE visitors SET logged_in = 0, time_out = " + curtime() + " WHERE id = " + str(visitor[0]))
        window.destroy()
        import sign_in


def greet_user():
    visitor = select_from_table("SELECT name FROM visitors WHERE logged_in = 1")[0]
    name = visitor[0]
    message.set("WELCOME BACK " + name.upper() + "!!!")


greet_user()
canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, textvariable=message, fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=100, y=150)

sign_out_btn = Button(window, text="SIGN OUT", width=55, bg="#8dc63f", fg="#ffffff", borderwidth=0, command=sign_out)
sign_out_btn.place(x=10, y=200)

window.mainloop()
