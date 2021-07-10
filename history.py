from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Style
from database_connection import select_from_table

window = Tk()
window.geometry("1000x1100")
window.title("Life Choices Online")

#   ADD STYLES TO TREEVIEW
style = Style()
#   CHANGE THE BODY FONT
style.configure("Treeview", highlightthickness=0, bd=0, bg="#fffffff", fieldbackground="#ffffff", fg="#8dc63f", font=('Helvetica', 11))
style.map("Treeview", background=[("selected", "#8dc63f")])


def populate_treeview():
    #   DELETE ALL THE CHILDREN OF THE TREEVIEW
    tree_view.delete(*tree_view.get_children())
    merged_data = select_from_table("SELECT history_table.id, visitor_table.name, visitor_table.surname, visitor_table.id_number, visitor_table.phone_number, history_table.timestamp_in, history_table.timestamp_out "
                      "FROM history AS history_table "
                      "INNER JOIN visitor AS visitor_table "
                      "ON history_table.visitor_id = visitor_table.id")

    for index, data in enumerate(merged_data):
        # CREATE A NEW INSERT INTO THE tree_view WITH EACH ENTRY IN THE DATABASE
        tree_view.insert(parent="", index="end", iid=index, open=True, values=data)


def return_to_admin():
    go_back = messagebox.askquestion("Confirmation", "Are you sure you want to continue?")

    if go_back == "yes":
        window.destroy()
        import admin


canvas = Canvas(window, width=450, height=100)
canvas.place(x=300, y=10)

img = PhotoImage(file="./images/logo.png")
canvas.create_image(20, 20, anchor=NW, image=img)

heading_label = Label(window, text="SIGN IN / SIGN OUT HISTORY!", fg="#8dc63f", font=("Helvetica", 18))
heading_label.place(x=400, y=150)

tree_view = Treeview(window, style="my_style.Treeview")
#   DEFINE COLUMNS HEADINGS
tree_view['columns'] = ("ID", "Name", "Surname", "ID Number", "Phone Number", "Timestamp In", "Timestamp Out")

#   FORMAT COLUMNS
tree_view.column("#0", width=0, stretch=NO)
tree_view.column("ID", anchor=CENTER, width=80)
tree_view.column("Name", anchor=CENTER, width=100)
tree_view.column("Surname", anchor=CENTER, width=100)
tree_view.column("ID Number", anchor=CENTER, width=150)
tree_view.column("Phone Number", anchor=CENTER, width=150)
tree_view.column("Timestamp In", anchor=CENTER, width=200)
tree_view.column("Timestamp Out", anchor=CENTER, width=200)

#   CREATE HEADINGS
tree_view.heading("#0")
tree_view.heading("ID", text="ID", anchor=CENTER)
tree_view.heading("Name", text="Name", anchor=CENTER)
tree_view.heading("Surname", text="Surname", anchor=CENTER)
tree_view.heading("ID Number", text="ID Number", anchor=CENTER)
tree_view.heading("Phone Number", text="Phone Number", anchor=CENTER)
tree_view.heading("Timestamp In", text="Timestamp In", anchor=CENTER)
tree_view.heading("Timestamp Out", text="Timestamp Out", anchor=CENTER)

# ADD DATA
populate_treeview()
tree_view.place(x=10, y=200)

return_btn = Button(window, text="RETURN", bg="#8dc63f", fg="#ffffff", borderwidth=0, width=30, command=return_to_admin)
return_btn.place(x=10, y=450)

window.mainloop()