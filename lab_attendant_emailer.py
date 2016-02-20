from tkinter import *

class gui:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        student_info_frame = Frame(frame)
        student_info_frame.pack(side=TOP)
        labattendant_info_frame = Frame(frame)
        labattendant_info_frame.pack(side=BOTTOM)

        # Student name, email, item
        student_name_label = Label(student_info_frame, text="Student name: ")
        student_name_label.grid(row=0, column=0)
        student_name_entry = Entry(student_info_frame)
        student_name_entry.grid(row=0, column=1)
        student_email_label = Label(student_info_frame, text="Student email: ")
        student_email_label.grid(row=1, column=0)
        student_email_entry = Entry(student_info_frame)
        student_email_entry.insert(END, '@ship.edu')
        student_email_entry.grid(row=1, column=1)
        student_item_label = Label(student_info_frame, text="Item left behind: ")
        student_item_label.grid(row=2, column=0)
        student_item_entry = Entry(student_info_frame)
        student_item_entry.grid(row=2, column=1)

        # Lab attendant email, password, lab working in
        labattendant_email_label = Label(labattendant_info_frame, text="Your email: ")
        labattendant_email_label.grid(row=3, column=0)
        labattendant_email_entry = Entry(labattendant_info_frame)
        labattendant_email_entry.insert(END, '@ship.edu')
        labattendant_email_entry.grid(row=3, column=1)
        labattendant_password_label = Label(labattendant_info_frame, text="Email password: ")
        labattendant_password_label.grid(row=4, column=0)
        labattendant_password_entry = Entry(labattendant_info_frame, show='*')
        labattendant_password_entry.grid(row=4, column=1)
        labattendant_lab_label = Label(labattendant_info_frame, text="Current lab: ")
        labattendant_lab_label.grid(row=5, column=0)
        lab_defualt = StringVar(labattendant_info_frame)
        labattendant_lab_menu = OptionMenu(labattendant_info_frame, lab_defualt, "MCT054", "CUB124", "GRH106")
        labattendant_lab_menu.grid(row=5, column=1)

        # Collects data and sends it
        # submit_button = Button(self, text="Send Email", command=self.button_handle)
        # submit_button.pack(side=BOTTOM)

root = Tk()
gui = gui(root)
root.mainloop()