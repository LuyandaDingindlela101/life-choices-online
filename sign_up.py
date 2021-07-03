from tkinter import *
from utilities import *
from tkinter import messagebox


window = Tk()
window.title("Life Choices Online")
window.geometry("500x550")


#   FUNCTION WILL VALIDATE ALL ENTRIES BY CHECKING CONTENTS AND DATA TYPES
def validate_entries():
    try:
        name = name_entry.get()
        surname = surname_entry.get()
        id_number = id_number_entry.get()
        phone_number = int(phone_number_entry.get())
        nok_name = nok_name_entry.get()
        nok_phone_number = int(nok_phone_number_entry.get())

        #   CHECK IF ALL THE ENTRIES ARE EMPTY
        if not_empty(name) and not_empty(surname) and not_empty(id_number) and not_empty(phone_number) and not_empty(nok_name) and not_empty(nok_phone_number):
            #   CHECK IF THE id_number_entry AND phone_number_entry ARE NUMBERS
            if len(id_number) == 13 and len(str(phone_number)) == 10 and len(str(nok_phone_number)) == 10:
                #   CHECK IF THE ID NUMBER IS VALID
                if not id_valid(id_number):
                    messagebox.showerror("Validation Error", "Your ID Number is invalid")
                    return False
                else:
                    return True
            else:
                messagebox.showerror("Validation Error", "Please check ID Number or phone numbers")
                return False
    except ValueError:
        messagebox.showerror("Validation Error", "Please check your inputs")
    except TypeError:
        messagebox.showerror("Validation Error", "Please check your ID Number")


def sign_user_up():
    if validate_entries():
        print("values are correct")


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

id_number_label = Label(window, text="Please enter ID Number!", fg="#8dc63f", font="Helvetica")
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

nok_phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
nok_phone_number_label.place(x=250, y=400)
nok_phone_number_entry = Entry(window)
nok_phone_number_entry.place(x=250, y=420)

sign_in_btn = Button(window, text="SIGN UP", width=50, bg="#8dc63f", fg="#ffffff", borderwidth=0, command=sign_user_up)
sign_in_btn.place(x=10, y=470)

window.mainloop()
