from tkinter import *

window = Tk()
window.title("Life Choices Online")
window.geometry("500x350")


def admin_login(e):
    window.destroy()
    import admin_login


def navigate_to_sign_up():
    window.destroy()
    import sign_up


def navigate_to_sign_in():
    window.destroy()
    import sign_in


#   HERE WE BIND THE window WITH A <Control-Alt-a> KEYPRESS EVENT AND RUN THE admin_login FUNCTION
window.bind('<Control-a>', admin_login)

canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="Welcome to life choices online!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=80, y=150)

sign_in_btn = Button(window, text="SIGN IN", bg="#8dc63f", fg="#ffffff", borderwidth=0, height=2, width=20, command=navigate_to_sign_in)
sign_in_btn.place(x=10, y=200)

sign_up_btn = Button(window, text="SIGN UP", bg="#8dc63f", fg="#ffffff", borderwidth=0, height=2, width=20, command=navigate_to_sign_up)
sign_up_btn.place(x=300, y=200)

admin_label = Label(window, text="Ctrl + a for ADMIN", fg="#8dc63f", font=("Helvetica", 11))
admin_label.place(x=180, y=280)

mainloop()
