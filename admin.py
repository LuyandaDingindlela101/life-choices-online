from tkinter import *
from utilities import *
from datetime import datetime
from tkinter import messagebox
from database_connection import *
from tkinter.ttk import Style, Treeview


window = Tk()
window.geometry("1100x550")
window.title("Life Choices Online")

#   ADD STYLES TO TREEVIEW
style = Style()
#   CHANGE THE BODY FONT
style.configure("Treeview", highlightthickness=0, bd=0, bg="#fffffff", fieldbackground="#ffffff", fg="#8dc63f", font=('Helvetica', 11))
style.map("Treeview", background=[("selected", "#8dc63f")])


#   FUNCTION WILL POPULATE THE TREEVIEW WITH ALL THE USERS
def populate_treeview():
    #   DELETE ALL THE CHILDREN OF THE TREEVIEW
    tree_view.delete(*tree_view.get_children())
    #   Index WILL KEEP TRACK OF EACH TREEVIEW ITEM
    index = 0
    #   GET ALL THE RECORDS IN THE visitors TABLE
    database_list = read_table("visitors")
    #   LOOP THROUGH THE database_list
    for database_item in database_list:
        #   CREATE A NEW INSERT INTO THE tree_view WITH EACH ENTRY IN THE DATABASE
        tree_view.insert(parent='', index=index, iid=index, values=database_item)
        #   INCREASE index BY 1 ON EACH ITERATION
        index = index + 1


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
            delete_entry("visitors", "id", visitor[0])
            #   REPOPULATE THE TREEVIEW
            populate_treeview()

    #     IF THE delete_btn IS CLICKED WITHOUT ANY ENTRY SELECTED, TELL THE USER TO CHOOSE AN ENTRY
    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


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
            if validate_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):
                    #   QUERY TO UPDATE THE visitors TABLE
                    query = "UPDATE visitors SET name = '" + name + "', surname = '" + surname + "', id_number = '" + id_number + "', phone_number = '" + phone_number + "' WHERE id = " + visitor_id
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


def show_hidden_entries():
    #   MAKE SPACE FOR THE NEW WIDGETS BY INCREASING THE WINDOWS LENGTH
    window.geometry("1100x1000")
    #   PLACE THE WIDGETS SO THEY CAN BE SEEN
    hr_label.place(x=10, y=500)
    edit_label.place(x=400, y=550)
    name_label.place(x=10, y=600)
    name_entry.place(x=10, y=620)
    surname_label.place(x=250, y=600)
    surname_entry.place(x=250, y=620)
    id_number_label.place(x=500, y=600)
    id_number_entry.place(x=500, y=620)

    phone_number_label.place(x=750, y=600)
    phone_number_entry.place(x=750, y=620)
    nok_label.place(x=400, y=700)
    nok_name_label.place(x=10, y=750)
    nok_name_entry.place(x=10, y=780)

    nok_phone_number_label.place(x=250, y=750)
    nok_phone_number_entry.place(x=250, y=780)


#   FUNCTION WILL EDIT A SELECTED ENTRY IN THE DATABASE
def edit_row():
    show_hidden_entries()
    edit_visitor_btn.place(x=10, y=850)
    cancel_btn.place(x=500, y=850)

    #   CALL THE populate_entries FUNCTION TO POPULATE THE ENTRIES WITH THE VISITOR AND NEXT OF KIN DETAILS
    populate_entries()


def create_row():
    #   CLEAR THE ENTRIES BEFORE UPDATING THERE VALUES
    clear_entries()

    visitor_id = IntVar
    show_hidden_entries()
    create_visitor_btn.place(x=10, y=850)
    cancel_btn.place(x=500, y=850)


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
            if validate_entries(name, surname, id_number, phone_number, nok_name, nok_phone_number):
                if not user_exists(name, id_number):
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
tree_view.column('#0', width=0, stretch=NO)
tree_view.column('ID', anchor=CENTER, width=80)
tree_view.column('Name', anchor=CENTER, width=100)
tree_view.column('Surname', anchor=CENTER, width=100)
tree_view.column('ID Number', anchor=CENTER, width=150)
tree_view.column('Phone Number', anchor=CENTER, width=150)
tree_view.column('Logged In', anchor=CENTER, width=150)
tree_view.column('Time In', anchor=CENTER, width=150)
tree_view.column('Time Out', anchor=CENTER, width=150)
#   CREATE HEADINGS
tree_view.heading('#0')
tree_view.heading('ID', text="ID", anchor=CENTER)
tree_view.heading('Name', text="Name", anchor=CENTER)
tree_view.heading('Surname', text="Surname", anchor=CENTER)
tree_view.heading('ID Number', text="ID Number", anchor=CENTER)
tree_view.heading('Phone Number', text="Phone Number", anchor=CENTER)
tree_view.heading('Logged In', text="Logged In", anchor=CENTER)
tree_view.heading('Time In', text="Time In", anchor=CENTER)
tree_view.heading('Time Out', text="Time Out", anchor=CENTER)
# ADD DATA
populate_treeview()
tree_view.place(x=10, y=200)

create_btn = Button(window, text="CREATE NEW VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=create_row)
create_btn.place(x=10, y=450)

edit_btn = Button(window, text="EDIT VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=edit_row)
edit_btn.place(x=380, y=450)

delete_btn = Button(window, text="DELETE VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=delete_row)
delete_btn.place(x=775, y=450)

hr_label = Label(window, text="____________________________________________________________________________________________________________________________________________________", fg="#8dc63f")

edit_label = Label(window, text="Edit entry!", fg="#8dc63f", font=("Helvetica", 18))

name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
name_entry = Entry(window)

surname_label = Label(window, text="Please enter surname!", fg="#8dc63f", font="Helvetica")
surname_entry = Entry(window)

id_number_label = Label(window, text="Please enter ID Number!", fg="#8dc63f", font="Helvetica")
id_number_entry = Entry(window)

phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
phone_number_entry = Entry(window)

nok_label = Label(window, text="Next of kin details!", fg="#8dc63f", font=("Helvetica", 18))

nok_name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
nok_name_entry = Entry(window)

nok_phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
nok_phone_number_entry = Entry(window)

edit_visitor_btn = Button(window, text="UPDATE VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=edit_visitor)

create_visitor_btn = Button(window, text="ADD NEW VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=add_visitor)


cancel_btn = Button(window, text="CANCEL", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=cancel)
window.mainloop()
