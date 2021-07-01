from tkinter import END, messagebox


#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
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

