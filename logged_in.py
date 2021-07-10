from tkinter import *
from tkinter import messagebox
from database_connection import select_from_table, update_table, insert_history_out

window = Tk()
window.geometry("500x550")
window.title("Life Choices Online")

message = StringVar()


def sign_out():
    sign_out = messagebox.askquestion("Sign out?", "Are you sure you want to sign out?")

    if sign_out == "yes":
        #   FIRST, WE HAVE TO FIND OUT WHO IS LOGGED IN BY QUERYING THE DATABASE FOR WHERE logged_in = true BUT is_admin = false, SO WE CANT SELECT THE ADMIN
        visitor_id = select_from_table("SELECT * FROM visitor WHERE logged_in = 'true' AND is_admin = 'false'")[0][0]
        #   UPDATE THEIR logged_in AND time_out VALUES
        update_table(f"UPDATE visitor SET logged_in = 'false', time_in = NULL, time_out = curtime() WHERE id = {str(visitor_id)}")
        #   RECORD THE SIGN IN AND INSERT IT INTO THE history TABLE
        insert_history_out(visitor_id)
        window.destroy()
        import sign_in


canvas = Canvas(window, width=450, height=100)
canvas.place(x=10, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="Welcome Back", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=100, y=150)

sign_out_btn = Button(window, text="SIGN OUT", width=55, bg="#8dc63f", fg="#ffffff", borderwidth=0, command=sign_out)
sign_out_btn.place(x=10, y=200)

window.mainloop()
