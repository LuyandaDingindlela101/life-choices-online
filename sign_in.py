from tkinter import *
from utilities import *
from tkinter import messagebox
from database_connection import *

window = Tk()
window.title("Life Choices Online")
window.geometry("500x400")


#   FUNCTION WILL VALIDATE ALL ENTRIES BY CHECKING CONTENTS AND DATA TYPES
def validate_entries(name, id_number):
    try:
        name = name_entry.get()
        id_number = id_number_entry.get()

        #   CHECK IF ALL THE ENTRIES ARE NOT EMPTY
        if not_empty(name) and not_empty(id_number):
            #   CHECK IF THE id_number_entry AND phone_number_entry ARE NUMBERS
            if len(id_number) == 13:
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


#   FUNCTION WILL CHECK IF USER EXISTS IN THE DATABASE
def user_exists(name, id_number):
    # SELECT STATEMENT TO GET A DATABASE ENTRY THAT MEETS THE WHERE CLAUSE
    query = "SELECT * FROM visitors WHERE name='" + name + "' AND id_number='" + id_number + "';"
    #   CALL THE select_from_table AND PASS IN THE QUERY, WHICH RETURNS A LIST
    db_rows = select_from_table(query)

    #   CHECK IF THE LENGTH OF db_rows IS MORE THAN 0, IF YES THEN THE USER EXISTS
    if len(db_rows) > 0:
        return True
    #   IF NO, THEN THE USER DOESNT EXIST
    else:
        return False


#   FUNCTION WILL SIGN A USER IN IF ENTRIES PASS VALIDATION AND USER EXISTS IN DATABASE
def sign_user_in():
    try:
        #   GET THE VALUES OF THE INPUTS
        name = name_entry.get()
        id_number = id_number_entry.get()

        #   CALL THE validate_entries FUNCTION AND PASS IN THE name AND id_number ENTRIES
        if validate_entries(name, id_number):
            #   IF VALIDATION PASSES, CALL THE user_exists FUNCTION AND PASS IN THE name AND id_number ENTRIES
            if user_exists(name, id_number):
                messagebox.showinfo("Login successful", "You have successfully logged in")
                #   IF USER EXISTS, DESTROY THE CURRENT WINDOW AND LOG THEM IN
                window.destroy()
                # import logged_in
            #     IF USER DOESNT EXIST...
            else:
                #   ASK IF THEY WANT TO REGISTER
                register = messagebox.askquestion('User not found', "Would you like to register an account")

                #   IF THEY WANT TO REGISTER...
                if register == "yes":
                    #   DESTROY THE CURRENT WINDOW AND IMPORT THE sign_up WINDOW
                    window.destroy()
                    import sign_up
                else:
                    #   CLOSE THE MESSAGEBOX
                    pass
        else:
            messagebox.showerror("Validation error", "Entries are not valid, please check your inputs")
    except ValueError:
        messagebox.showerror("Validation error", "Please check your entries")


canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="SIGN IN!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=150, y=150)

name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
name_label.place(x=10, y=200)
name_entry = Entry(window)
name_entry.place(x=10, y=220)

id_number_label = Label(window, text="Please enter ID Number!", fg="#8dc63f", font="Helvetica")
id_number_label.place(x=250, y=200)
id_number_entry = Entry(window)
id_number_entry.place(x=250, y=220)

sign_in_btn = Button(window, text="SIGN UP", width=50, bg="#8dc63f", fg="#ffffff", borderwidth=0, command=sign_user_in)
sign_in_btn.place(x=10, y=300)

window.mainloop()
