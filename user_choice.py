from tkinter import *

window = Tk()
window.title("Life Choices Online")
window.geometry("500x300")

canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)


def navigate_to_sign_in():
    import sign_in


def navigate_to_sign_up():
    import sign_up


img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="Welcome to life choices online!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=80, y=150)

sign_in_btn = Button(window, text="SIGN IN", bg="#8dc63f", fg="#ffffff", borderwidth=0, height=2, width=20)
sign_in_btn.place(x=10, y=200)

sign_up_btn = Button(window, text="SIGN UP", bg="#8dc63f", fg="#ffffff", borderwidth=0, height=2, width=20)
sign_up_btn.place(x=300, y=200)

mainloop()
