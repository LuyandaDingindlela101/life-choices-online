from datetime import datetime
from tkinter import *
from utilities import *
from tkinter import messagebox
from database_connection import *


window = Tk()
window.title("Life Choices Online")
window.geometry("500x550")


#   FUNCTION WILL VALIDATE ALL ENTRIES BY CHECKING CONTENTS AND DATA TYPES
def validate_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
    try:
        #   CHECK IF ALL THE ENTRIES ARE EMPTY
        if not_empty(name) and not_empty(surname) and not_empty(id_number) and not_empty(phone_number) and not_empty(nok_name) and not_empty(nok_phone_number):
            #   CHECK IF THE id_number_entry AND phone_number_entry ARE NUMBERS
            if len(id_number) == 13 and len(phone_number) == 10 and len(nok_phone_number) == 10:
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
    try:
        name = name_entry.get()
        surname = surname_entry.get()
        id_number = id_number_entry.get()
        phone_number = phone_number_entry.get()
        nok_name = nok_name_entry.get()
        nok_phone_number = nok_phone_number_entry.get()

        if validate_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
            if id_valid(id_number):
                visitor_id = ""
                time_in = datetime.now()
                insert_visitor(name, surname, id_number, phone_number, 1, time_in)

                # SELECT STATEMENT TO GET A DATABASE ENTRY THAT MEETS THE WHERE CLAUSE
                query = "SELECT id FROM visitors WHERE name='" + name + "' AND id_number='" + id_number + "';"
                #   CALL THE select_from_table AND PASS IN THE QUERY, WHICH RETURNS A LIST
                db_rows = select_from_table(query)
                for i in db_rows[0]:
                    visitor_id = i

                insert_nok(nok_name, nok_phone_number, visitor_id)

                # import logged_in
    except ValueError:
        messagebox.showerror("Validation error", "Please check your entries")


canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="SIGN UP!", fg="#8dc63f", font=("Helvetica", 18))
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
