from tkinter import *
from utilities import *
from database_connection import update_table, insert_history_in

window = Tk()
window.title("Life Choices Online")
window.geometry("500x400")


def admin_login(e):
    window.destroy()
    import admin_login


#   FUNCTION WILL SIGN A USER IN IF ENTRIES PASS VALIDATION AND USER EXISTS IN DATABASE
def sign_user_in():
    try:
        #   GET THE VALUES OF THE INPUTS
        name = name_entry.get()
        id_number = id_number_entry.get()

        #   CALL THE validate_entries FUNCTION AND PASS IN THE name AND id_number ENTRIES
        if validate_min_entries(name, id_number):
            #   IF VALIDATION PASSES, CALL THE user_exists FUNCTION AND PASS IN THE name AND id_number ENTRIES
            if user_exists(name, id_number):
                #   IF USER EXISTS, GET THE USER AND CHANGE THEIR logged_in STATUS
                visitor = select_from_table(f"SELECT * FROM visitor WHERE name='{name}' AND id_number= '{id_number}';")[0]
                #   UPDATE THE visitor TABLE AND SET THE CURRENT VISITORS logged_in VALUE TO true
                update_table(f"UPDATE visitor SET logged_in = 'true' WHERE id = {str(visitor[0])}")
                #   RECORD THE SIGN IN AND INSERT IT INTO THE history TABLE
                insert_history_in(visitor[0])
                messagebox.showinfo("Login successful", "You have successfully logged in")
                #   DESTROY THE CURRENT WINDOW AND LOG THEM IN
                window.destroy()
                import logged_in
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


#   HERE WE BIND THE window WITH A <Control-Alt-a> KEYPRESS EVENT AND RUN THE admin_login FUNCTION
window.bind('<Control-a>', admin_login)

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

admin_label = Label(window, text="Ctrl + a for ADMIN", fg="#8dc63f", font=("Helvetica", 11))
admin_label.place(x=150, y=350)

window.mainloop()
