from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style, Treeview
from database_connection import read_table, delete_entry, select_from_table

window = Tk()
window.geometry("1100x550")
window.title("Life Choices Online")


#   FUNCTION WILL POPULATE THE TREEVIEW WITH ALL THE USERS
def populate_treeview():
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
        #   GET THE ID OF THE SELECTED ITEM
        selected_id = tree_view.focus()
        #   GET THE ACTUAL ITEMS VALUES
        visitor = tree_view.item(selected_id, 'values')
        #   DELETE THE ENTRY IN THE next_of_kin TABLE FIRST BY USING THE visitor_id
        delete_entry("next_of_kin", "visitor_id", visitor[0])
        #   DELETE THE ACTUAL visitor
        delete_entry("visitors", "id", visitor[0])
    #     IF THE delete_btn IS CLICKED WITHOUT ANY ENTRY SELECTED, TELL THE USER TO CHOOSE AN ENTRY
    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def populate_entries(name_entry, surname_entry, id_number_entry, phone_number_entry, nok_name_entry, nok_phone_number_entry):
    try:
        #   GET THE ID OF THE SELECTED ITEM
        selected_id = tree_view.focus()
        #   GET THE ACTUAL ITEMS VALUES
        visitor = tree_view.item(selected_id, 'values')
        #   GET THE visitor NEXT OF KIN
        nok_query = "SELECT name, phone_number FROM next_of_kin WHERE visitor_id = " + visitor[0]
        nok = select_from_table(nok_query)[0]
        print(nok)
        print(visitor)

        #   POPULATE THE ENTRIES WITH THE visitor DETAILS
        name_entry.insert(0, visitor[1])
        surname_entry.insert(0, visitor[2])
        id_number_entry.insert(0, visitor[3])
        phone_number_entry.insert(0, visitor[4])

        #   POPULATE THE ENTRIES WITH THE NEXT OF KIN DETAILS
        nok_name_entry.insert(0, visitor[0])
        nok_phone_number_entry.insert(0, visitor[1])

    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


def edit_visitor(name, surname, id_number, phone_number):
    pass


#   FUNCTION WILL EDIT A SELECTED ENTRY IN THE DATABASE
def edit_row():
    try:
        #   MAKE SPACE FOR THE NEW WIDGETS BY INCREASING THE WINDOWS LENGTH
        window.geometry("1100x1000")
        #   CRETE THE NEW WIDGETS
        hr_label = Label(window,
                         text="____________________________________________________________________________________________________________________________________________________",
                         fg="#8dc63f")
        hr_label.place(x=10, y=500)

        edit_label = Label(window, text="Edit entry!", fg="#8dc63f", font=("Helvetica", 18))
        edit_label.place(x=400, y=550)

        name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
        name_label.place(x=10, y=600)
        name_entry = Entry(window)
        name_entry.place(x=10, y=620)

        surname_label = Label(window, text="Please enter surname!", fg="#8dc63f", font="Helvetica")
        surname_label.place(x=250, y=600)
        surname_entry = Entry(window)
        surname_entry.place(x=250, y=620)

        id_number_label = Label(window, text="Please enter ID Number!", fg="#8dc63f", font="Helvetica")
        id_number_label.place(x=500, y=600)
        id_number_entry = Entry(window)
        id_number_entry.place(x=500, y=620)

        phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
        phone_number_label.place(x=750, y=600)
        phone_number_entry = Entry(window)
        phone_number_entry.place(x=750, y=620)

        nok_label = Label(window, text="Next of kin details!", fg="#8dc63f", font=("Helvetica", 18))
        nok_label.place(x=400, y=700)

        nok_name_label = Label(window, text="Please enter name!", fg="#8dc63f", font="Helvetica")
        nok_name_label.place(x=10, y=750)
        nok_name_entry = Entry(window)
        nok_name_entry.place(x=10, y=780)

        nok_phone_number_label = Label(window, text="Please enter phone number!", fg="#8dc63f", font="Helvetica")
        nok_phone_number_label.place(x=250, y=750)
        nok_phone_number_entry = Entry(window)
        nok_phone_number_entry.place(x=250, y=780)

        edit_visitor_btn = Button(window, text="Update visitor", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30,
                                  command=edit_visitor)
        edit_visitor_btn.place(x=10, y=850)

        #   CALL THE populate_entries FUNCTION TO POPULATE THE ENTRIES WITH THE VISITOR AND NEXT OF KIN DETAILS
        populate_entries(name_entry, surname_entry, id_number_entry, phone_number_entry, nok_name_entry,
                         nok_phone_number_entry)
    except IndexError:
        messagebox.showerror("Entry not chosen", "Please select an entry above")


style = Style()
#   CHANGE THE BODY FONT
style.configure("my_style.Treeview", highlightthickness=0, bd=0, font=('Helvetica', 11))
#   CHANGE THE HEADING FONT
style.configure("my_style.Treeview.Heading", font=('Helvetica', 13, 'bold'))
#   REMOVE THE BORDERS
style.layout("my_style.Treeview", [('my_style.Treeview.treearea', {'sticky': 'nswe'})])

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

create_btn = Button(window, text="CREATE NEW VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30)
create_btn.place(x=10, y=450)

edit_btn = Button(window, text="EDIT VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=edit_row)
edit_btn.place(x=380, y=450)

delete_btn = Button(window, text="DELETE VISITOR", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=delete_row)
delete_btn.place(x=775, y=450)

window.mainloop()
