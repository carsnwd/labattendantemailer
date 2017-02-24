from tkinter import *  # GUI library
import tkinter.messagebox
import smtplib #SMTP library
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# @author: Carson Wood
# Email: carsnwd@gmail.com
# Sends automated emails out for lab attendant job

###
# Object to store student info gathered
# from GUI input (name, email, item left)
###
class Student:
    def __init__(self, name, email, item):
        self.name = name
        self.email = email
        self.item = item

    @property
    def semail(self):
        return self.email

    @semail.setter
    def semail(self, email):
        self.email = email

    @property
    def sname(self):
        return self.name

    @sname.setter
    def sname(self, name):
        self.name = name

    @property
    def sitem(self):
        return self.item

    @sitem.setter
    def sitem(self, item):
        self.item = item

###
# Object for lab attendant email.
# Semi-useless object, may consider removing and
# just hard coding this in.
###
class LabAttendant:
    def __init__(self, email, password, lab):
        self.email = email 
        self.password = password
        self.lab = lab

    @property
    def lemail(self):
        return self.email

    @lemail.setter
    def lemail(self, email):
        self.email = email

    @property
    def lpassword(self):
        return self.password

    @lpassword.setter
    def lpassword(self, password):
        self.password = password

    @property
    def llab(self):
        return self.lab

    @llab.setter
    def llab(self, password):
        self.password = password
###
# Method to send out the emails
# utilizing SMTPlib
###
def SendEmail(labattendant, student):
    message = MIMEMultipart() 
    message['From'] = labattendant.email
    message['To'] = student.email
    message['Subject'] = student.item + " left in " + labattendant.lab + " computer lab."
    
    #Grove has different hours than other labs, so seperate condition. 
    #Refactor to seperate method?
    if(labattendant.lab == "GRH106"): 
        #Various wordings of the email for different situations
        if "id" == student.item: #Left ID in Grove
            body = "Hello " + student.name + ",\nI believe you left your " + student.item + " in the " + labattendant.lab\
                   + " computer lab. If so, please stop by the " + labattendant.lab\
                   + " computer lab, and ask the lab attendant to return your " + student.item + " to you.\n\n"\
                   + "Lab attendants should be in the " + labattendant.lab + " computer lab Monday through Thursday 8AM-10PM and Friday 8AM-4PM.\n\n"+ "Thank you!\n-Lab Attendant"
        else: #Left other item in Grove
            body = "Hello " + student.name + ",\nI believe you left your " + student.item + " in the " + labattendant.lab\
                   + " computer lab. If so, please stop by the " + labattendant.lab\
                   + " computer lab, with your ID, and ask the lab " + "attendant to return your " + student.item + " to you.\n\n"\
                   + "Lab attendants should be in the " + labattendant.lab + " computer lab Monday through Thursday 8AM-10PM and Friday 8AM-4PM.\n\n"+ "Thank you!\n-Lab Attendant"
    else: #Left ID in MCT/CUB
        if "id" == student.item:
            body = "Hello " + student.name + ",\nI believe you left your " + student.item + " in the " + labattendant.lab\
                   + " computer lab. If so, please stop by the " + labattendant.lab\
                   + " computer lab, and ask the lab attendant to return your " + student.item +" to you."\
                   + "\n\n" + "Lab attendants should be in the " + labattendant.lab + " computer lab Monday through Thursday 8AM-10PM, Friday 8AM-4PM, and weekends 12PM-6PM.\n\n"+ "Thank you!\n-Lab Attendant"
        else: #Left other item in MCT/CUB
            body = "Hello " + student.name + ",\nI believe you left your " + student.item + " in the " + labattendant.lab\
                   + " computer lab. If so, please stop by the " + labattendant.lab\
                   + " computer lab, with your ID, and ask the lab " + "attendant to return your " + student.item +""\
                   + " to you.\n\n" + "Lab attendants should be in the " + labattendant.lab + " computer lab Monday through Thursday 8AM-10PM, Friday 8AM-4PM, and weekends 12PM-6PM.\n\n"+ "Thank you!\n-Lab Attendant"
    message.attach(MIMEText(body, 'plain'))

    #Send email
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(labattendant.email, labattendant.password)
    text = message.as_string()
    server.sendmail(labattendant.email, student.email, text)

###
# The mess that is writing a GUI.
###
class GUI:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        student_info_frame = Frame(frame)
        student_info_frame.pack(side=TOP)
        labattendant_info_frame = Frame(frame)
        labattendant_info_frame.pack(side=TOP)

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
        labattendant_email_entry.insert(END, 'shiplabattendant@gmail.com')
        labattendant_email_entry.grid(row=3, column=1)
        labattendant_password_label = Label(labattendant_info_frame, text="Email password: ")
        labattendant_password_label.grid(row=4, column=0)
        labattendant_password_entry = Entry(labattendant_info_frame, show='*')
        labattendant_password_entry.insert(END, 'labsthataremicro')
        labattendant_password_entry.grid(row=4, column=1)
        labattendant_lab_label = Label(labattendant_info_frame, text="Current lab: ")
        labattendant_lab_label.grid(row=5, column=0)
        lab_defualt = StringVar(labattendant_info_frame)
        labattendant_lab_menu = OptionMenu(labattendant_info_frame, lab_defualt, "MCT054", "CUB124", "GRH106")
        labattendant_lab_menu.grid(row=5, column=1)

        # Button handler for the submit button
        def submit_on_click():
            #if "@ship.edu" not in labattendant_email_entry.get():
             #   tkinter.messagebox.showwarning("Error", "Please use your @ship.edu email.")
              #  labattendant_email_entry.delete(0, 'end')
            #else:
                labattendant = LabAttendant(labattendant_email_entry.get(), labattendant_password_entry.get(),
                                            labattendant_lab_menu.cget("text"))
                student = Student(student_name_entry.get(), student_email_entry.get(), student_item_entry.get().lower())
                SendEmail(labattendant, student)


        # Collects data and sends it
        submit_button = Button(frame, text="Send Email", command=submit_on_click)
        submit_button.pack(side=BOTTOM)

root = Tk()
GUI = GUI(root)
root.mainloop()
