from datetime import datetime
from tkinter import *
from utilities import *
from tkinter import messagebox
from database_connection import *


window = Tk()
window.title("Life Choices Online")
window.geometry("500x550")


def sign_user_up():
    try:
        #   GET THE VALUES OF THE INPUTS
        name = name_entry.get()
        surname = surname_entry.get()
        id_number = id_number_entry.get()
        phone_number = phone_number_entry.get()
        nok_name = nok_name_entry.get()
        nok_phone_number = nok_phone_number_entry.get()

        #   CALL THE validate_entries FUNCTION AND PASS IN ALL THE ENTRIES
        if validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
            #   IF VALIDATION PASSES, CALL THE id_valid FUNCTION AND PASS IN THE id_number
            if id_valid(id_number):
                #       ONCE THE id_number IS VALID, WE CHECK IF THE USER DOESNT EXIST ALREADY IN THE DATABASE
                if not user_exists(name, id_number):
                    visitor_id = ""
                    time_in = datetime.now()
                    #   CALL THE insert_visitor FUNCTION AND PASS IN THE NEEDED PARAMETERS
                    insert_visitor(name, surname, id_number, phone_number, 1, time_in)

                    # SELECT STATEMENT TO GET A DATABASE ENTRY THAT MEETS THE WHERE CLAUSE SO WE KNOW WHICH visitor TO ASSIGN THE NEXT OF KIN TO
                    query = "SELECT id FROM visitors WHERE name='" + name + "' AND id_number='" + id_number + "';"
                    #   CALL THE select_from_table AND PASS IN THE QUERY, WHICH RETURNS A LIST
                    db_rows = select_from_table(query)
                    #   HERE, WE LOOP THROUGH THE SET AT THE 0 INDEX TO GET THE VALUE OF THE id
                    for i in db_rows[0]:
                        visitor_id = i

                    #   SAVE THE NEXT OF KIN WITH THE CORRECT visitor_id
                    insert_nok(nok_name, nok_phone_number, visitor_id)

                    #   DESTROY THE CURRENT WINDOW AND LOG THEM IN
                    window.destroy()
                    import logged_in
                #     IF THE USER EXISTS IN THE DATABASE, ALLOW THEM TO GO SIGN IN
                else:
                    #   DESTROY THE CURRENT WINDOW AND IMPORT THE sign_in WINDOW
                    messagebox.showinfo("User exists", "Please go login.")
                    window.destroy()
                    import sign_in
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
