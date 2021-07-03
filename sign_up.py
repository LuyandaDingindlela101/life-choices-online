from tkinter import *

window = Tk()
window.title("Life Choices Online")
window.geometry("500x550")

canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="Your details!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=150, y=150)

name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
name_label.place(x=10, y=200)
name_entry = Entry(window)
name_entry.place(x=10, y=220)

surname_label = Label(window, text="Please enter surname!", fg="#8dc63f", font="Helvetica")
surname_label.place(x=250, y=200)
surname_entry = Entry(window)
surname_entry.place(x=250, y=220)

id_number_label = Label(window, text="Please enter id number!", fg="#8dc63f", font="Helvetica")
id_number_label.place(x=10, y=250)
id_number_entry = Entry(window)
id_number_entry.place(x=10, y=270)

phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
phone_number_label.place(x=250, y=250)
phone_number_entry = Entry(window)
phone_number_entry.place(x=250, y=270)

heading_label = Label(window, text="Your next of kin details!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=80, y=350)

nok_name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
nok_name_label.place(x=10, y=400)
nok_name_entry = Entry(window)
nok_name_entry.place(x=10, y=420)

nok_surname_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
nok_surname_label.place(x=250, y=400)
nok_surname_entry = Entry(window)
nok_surname_entry.place(x=250, y=420)

sign_in_btn = Button(window, text="SIGN UP", width=50, bg="#8dc63f", fg="#ffffff", borderwidth=0)
sign_in_btn.place(x=10, y=470)

window.mainloop()