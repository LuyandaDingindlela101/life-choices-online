from tkinter import *
from utilities import *
from datetime import datetime
from tkinter import messagebox
from database_connection import *
from tkinter.ttk import Style, Treeview, Combobox

window = Tk()
window.geometry("1100x1000")
window.title("Life Choices Online")


#   ADD STYLES TO TREEVIEW
style = Style()
#   CHANGE THE BODY FONT
style.configure("Treeview", highlightthickness=0, bd=0, bg="#fffffff", fieldbackground="#ffffff", fg="#8dc63f", font=('Helvetica', 11))
style.map("Treeview", background=[("selected", "#8dc63f")])


signed_status = StringVar()
admin_privileges = StringVar()


#   FUNCTION WILL POPULATE THE TREEVIEW WITH ALL THE USERS
def populate_treeview():
    #   DELETE ALL THE CHILDREN OF THE TREEVIEW
    tree_view.delete(*tree_view.get_children())
    #   GET ALL THE RECORDS IN THE visitor TABLE
    visitors_list = read_table("visitor")
    #   LOOP THROUGH THE database_list
    for index in range(len(visitors_list)):
        # CREATE A NEW INSERT INTO THE tree_view WITH EACH ENTRY IN THE DATABASE
        tree_view.insert(parent="", index="end", iid=index, open=True, values=visitors_list[index])

def populate_entries():
    try:
        #   CLEAR THE ENTRIES BEFORE UPDATING THERE VALUES
        clear_entries()

        #   GET THE ID OF THE SELECTED ITEM
        selected_id = tree_view.focus()
        #   GET THE ACTUAL ITEMS VALUES
        visitor = tree_view.item(selected_id, 'values')
        #   GET THE visitor NEXT OF KIN
        nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
        nok = select_from_table(nok_query)[0]

        #   POPULATE THE ENTRIES WITH THE visitor DETAILS
        name_entry.insert(0, visitor[1])
        surname_entry.insert(0, visitor[2])
        id_number_entry.insert(0, visitor[3])
        phone_number_entry.insert(0, visitor[4])

        #   POPULATE THE ENTRIES WITH THE NEXT OF KIN DETAILS
        nok_name_entry.insert(0, nok[0])
        nok_phone_number_entry.insert(0, nok[1])

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def edit_visitor():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":
            #   GET THE ID OF THE SELECTED ITEM
            selected_id = tree_view.focus()
            #   GET THE ACTUAL ITEMS VALUES
            visitor = tree_view.item(selected_id, 'values')
            #   GET THE visitor NEXT OF KIN
            nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
            nok = select_from_table(nok_query)[0]

            #   GET THE visitor DETAILS FROM THE ENTRIES
            name = name_entry.get()
            surname = surname_entry.get()
            id_number = id_number_entry.get()
            phone_number = phone_number_entry.get()
            visitor_id = visitor[0]

            #   GET THE nok DETAILS FROM THE ENTRIES
            nok_name = nok_name_entry.get()
            nok_phone_number = nok_phone_number_entry.get()

            #   CALL THE validate_entries FUNCTION AND PASS IN ALL THE ENTRIES
            if validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):
                    #   QUERY TO UPDATE THE visitor TABLE
                    query = "UPDATE visitor SET name = '" + name + "', surname = '" + surname + "', id_number = '" + id_number + "', phone_number = '" + phone_number + "' WHERE id = " + visitor_id
                    update_table(query)

                    #   QUERY TO UPDATE THE next_of_kin TABLE
                    nok_query = "UPDATE next_of_kin SET name = '" + nok_name + "', phone_number = '" + nok_phone_number + "' WHERE visitor_id = " + visitor_id
                    update_table(nok_query)
                    #   REPOPULATE THE TREEVIEW
                    populate_treeview()
                    #   RESIZE THE WINDOW
                    window.geometry("1100x500")
                #     IF THE USER EXISTS IN THE DATABASE, ALLOW THEM TO TRY AGAIN
                else:
                    #   SHOW THE USER THE ERROR MESSAGE BOX
                    messagebox.showinfo("User exists", "Please try again.")

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def create_row():
    #   CLEAR THE ENTRIES BEFORE UPDATING THERE VALUES
    clear_entries()
    cancel_btn.place(x=650, y=750)
    create_visitor_btn.place(x=350, y=750)


#   FUNCTION WILL EDIT A SELECTED ENTRY IN THE DATABASE
def edit_row():
    #   CALL THE populate_entries FUNCTION TO POPULATE THE ENTRIES WITH THE VISITOR AND NEXT OF KIN DETAILS
    populate_entries()

    cancel_btn.place(x=650, y=750)
    edit_visitor_btn.place(x=350, y=750)


#   FUNCTION WILL DELETE AN ENTRY FROM THE DATABASE
def delete_row():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":
            #   GET THE ID OF THE SELECTED ITEM
            selected_id = tree_view.focus()
            #   GET THE ACTUAL ITEMS VALUES
            visitor = tree_view.item(selected_id, 'values')
            #   DELETE THE ENTRY IN THE next_of_kin TABLE FIRST BY USING THE visitor_id
            delete_entry("next_of_kin", "visitor_id", visitor[0])
            #   DELETE THE ACTUAL visitor
            delete_entry("visitor", "id", visitor[0])
            #   REPOPULATE THE TREEVIEW
            populate_treeview()

    #     IF THE delete_btn IS CLICKED WITHOUT ANY ENTRY SELECTED, TELL THE USER TO CHOOSE AN ENTRY
    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def add_visitor():
    try:
        permission = messagebox.askquestion("Add new user", "Are you sure you want to continue?")

        if permission == "yes":
            #   GET THE visitor DETAILS FROM THE ENTRIES
            name = name_entry.get()
            surname = surname_entry.get()
            id_number = id_number_entry.get()
            phone_number = phone_number_entry.get()

            #   GET THE nok DETAILS FROM THE ENTRIES
            nok_name = nok_name_entry.get()
            nok_phone_number = nok_phone_number_entry.get()

            #   CALL THE validate_entries FUNCTION AND PASS IN ALL THE ENTRIES
            if validate_max_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):
                    time_in = datetime.now()
                    #   CALL THE insert_visitor FUNCTION AND PASS IN THE NEEDED PARAMETERS
                    insert_visitor(name, surname, id_number, phone_number)
                    # SELECT STATEMENT TO GET A DATABASE ENTRY THAT MEETS THE WHERE CLAUSE SO WE KNOW WHICH visitor TO ASSIGN THE NEXT OF KIN TO
                    query = "SELECT id FROM visitor WHERE name='" + name + "' AND id_number='" + id_number + "';"
                    #   CALL THE select_from_table AND PASS IN THE QUERY, WHICH RETURNS A LIST
                    db_rows = select_from_table(query)
                    #   HERE, WE LOOP THROUGH THE SET AT THE 0 INDEX TO GET THE VALUE OF THE id
                    for i in db_rows[0]:
                        visitor_id = i

                    #   SAVE THE NEXT OF KIN WITH THE CORRECT visitor_id
                    insert_nok(nok_name, nok_phone_number, visitor_id)
                    #   REPOPULATE THE TREEVIEW WITH THE NEW VISITOR
                    populate_treeview()
                    #   AFTER ADDING THE NEW visitor, CLEAR THE ENTRIES
                    clear_entries()

                #     IF THE USER EXISTS IN THE DATABASE, ALLOW THEM TO TRY AGAIN
                else:
                    #   SHOW THE USER THE ERROR MESSAGE BOX
                    messagebox.showinfo("User exists", "Please try again.")
    except ValueError:
        messagebox.showerror("Validation", "Please check your inputs")


def clear_entries():
    clear_entry(name_entry)
    clear_entry(surname_entry)
    clear_entry(phone_number_entry)
    clear_entry(id_number_entry)
    clear_entry(nok_name_entry)
    clear_entry(nok_phone_number_entry)


def cancel():
    permission = messagebox.askquestion("Cancel operation", "Are you sure you want to continue?")

    if permission == "yes":
        clear_entries()
        window.geometry("1100x500")


canvas = Canvas(window, width=450, height=100)
canvas.place(x=300, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="WELCOME BACK ADMIN!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=400, y=150)

tree_view = Treeview(window, style="my_style.Treeview")
#   DEFINE COLUMNS HEADINGS
tree_view['columns'] = ('ID', 'Name', 'Surname', "ID Number", "Phone Number", "Logged In", "Time In", "Time Out")
#   FORMAT COLUMNS
tree_view.column("#0", width=0, stretch=NO)
tree_view.column("ID", anchor=CENTER, width=80)
tree_view.column("Name", anchor=CENTER, width=100)
tree_view.column("Surname", anchor=CENTER, width=100)
tree_view.column("ID Number", anchor=CENTER, width=150)
tree_view.column("Phone Number", anchor=CENTER, width=150)
tree_view.column("Logged In", anchor=CENTER, width=150)
tree_view.column("Time In", anchor=CENTER, width=150)
tree_view.column("Time Out", anchor=CENTER, width=150)
#   CREATE HEADINGS
tree_view.heading("#0")
tree_view.heading("ID", text="ID", anchor=CENTER)
tree_view.heading("Name", text="Name", anchor=CENTER)
tree_view.heading("Surname", text="Surname", anchor=CENTER)
tree_view.heading("ID Number", text="ID Number", anchor=CENTER)
tree_view.heading("Phone Number", text="Phone Number", anchor=CENTER)
tree_view.heading("Logged In", text="Logged In", anchor=CENTER)
tree_view.heading("Time In", text="Time In", anchor=CENTER)
tree_view.heading("Time Out", text="Time Out", anchor=CENTER)
# ADD DATA
populate_treeview()
tree_view.place(x=10, y=200)

create_btn = Button(window, text="CREATE VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=create_row)
create_btn.place(x=10, y=450)

edit_btn = Button(window, text="EDIT VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=edit_row)
edit_btn.place(x=10, y=500)

delete_btn = Button(window, text="DELETE VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=delete_row)
delete_btn.place(x=10, y=550)

report_btn = Button(window, text="DAILY REPORT", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=delete_row)
report_btn.place(x=10, y=600)

logout_btn = Button(window, text="LOG OUT", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=delete_row)
logout_btn.place(x=10, y=650)





name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
name_label.place(x=350, y=450)
name_entry = Entry(window)
name_entry.place(x=350, y=480)

surname_label = Label(window, text="Please enter surname!", fg="#8dc63f", font="Helvetica")
surname_label.place(x=650, y=450)
surname_entry = Entry(window)
surname_entry.place(x=650, y=480)

id_number_label = Label(window, text="Please enter ID Number!", fg="#8dc63f", font="Helvetica")
id_number_label.place(x=350, y=520)
id_number_entry = Entry(window)
id_number_entry.place(x=350, y=550)

phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
phone_number_label.place(x=650, y=520)
phone_number_entry = Entry(window)
phone_number_entry.place(x=650, y=550)

admin_label = Label(window, text="Allow admin privilege", fg="#8dc63f", font="Helvetica")
admin_label.place(x=350, y=590)
admin_combobox = Combobox(window, textvariable=admin_privileges, state="readonly")
admin_combobox["values"] = ("Grant", "Revoke")
admin_combobox.place(x=350, y=620)

status_label = Label(window, text="Sign user in / out", fg="#8dc63f", font="Helvetica")
status_label.place(x=650, y=590)
status_combobox = Combobox(window, textvariable=signed_status, state="readonly")
status_combobox["values"] = ("Sign out", "Sign in")
status_combobox.place(x=650, y=620)

# nok_label = Label(window, text="Next of kin details!", fg="#8dc63f", font=("Helvetica", 18))

nok_name_label = Label(window, text="Please enter next of kin name!", fg="#8dc63f", font="Helvetica")
nok_name_label.place(x=350, y=690)
nok_name_entry = Entry(window)
nok_name_entry.place(x=350, y=710)
nok_phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
nok_phone_number_label.place(x=650, y=690)
nok_phone_number_entry = Entry(window)
nok_phone_number_entry.place(x=650, y=710)

create_visitor_btn = Button(window, text="ADD NEW VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=add_visitor)

edit_visitor_btn = Button(window, text="UPDATE VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=edit_visitor)

cancel_btn = Button(window, text="CANCEL", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=cancel)

window.mainloop()
