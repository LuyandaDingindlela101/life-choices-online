from tkinter import END, messagebox

#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
from database_connection import select_from_table


def clear_entry(test_entry):
    test_entry.delete(0, END)


#   FUNCTION WILL DETERMINE IF PARAMETER IS A VALID ID OR NOT
def id_valid(id_number):
    #   IMPORT THE rsaidnumber MODULE
    import rsaidnumber

    try:
        id_number = rsaidnumber.parse(id_number)
        #   .valid RETURNS TRUE OR FALSE BASED ON id_number
        return id_number.valid
    except ValueError:
        return False


#   FUNCTION WILL DETERMINE IF PARAMETER IS EMPTY OR NOT
def not_empty(test_entry):
    try:
        #   IF THE test_entry IS EMPTY, RAISE THE ValueError
        if test_entry == "":
            raise ValueError()
        #   IF THE test_entry IS NOT EMPTY, RETURN True
        else:
            return True
    except ValueError:
        return False


#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program(window):
    exit = messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')

    if exit == 'yes':
        window.destroy()

    #   ELSE, JUST GO BACK TO THE APPLICATION SCREEN


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