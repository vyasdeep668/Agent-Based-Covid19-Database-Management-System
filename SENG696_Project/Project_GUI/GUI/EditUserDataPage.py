#Import Modules
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image

#Import Pages
import Application
from GUI import LoginPage
from GUI import UserPage
from GUI import AHSAdminPage
from GUI import AdminPage
from GUI import EditUserDataPage
from GUI import EditVaccineDataPage
from GUI import AddOnlyVaccineDataPage

#from Application import Application


EditUserDataPageFrame = tk.Frame
class EditUserDataPage(EditUserDataPageFrame):
    #Callbacks Here
    def Button1_Callback(self, controller):
        print('EditUserDataPage Button 1 Pressed')
        #self.Message1.configure(text = "EditUserData Page Message v1")
        #controller.show_frame(EditUserDataPage.PageOne)

    def Button2_Callback(self, controller):
        print('EditUserDataPage Button 2 Pressed')
        # controller.show_frame(EditUserDataPage.PageOne)

    def Button3_Callback(self, controller):
        print('EditUserDataPage Button 3 Pressed')
        #controller.show_frame(TestPage1.PageOne)

    def Button4_Callback(self, controller):
        print('EditUserDataPage Button 4 Pressed')
        #Curr_Frame = LoginPage.LoginPage
        #print("LoginPage Initialized")
        #controller.show_frame(LoginPage.LoginPage)

    def Button5_Callback(self, controller):
        print('EditUserDataPage Button 5 Pressed')
        #controller.show_frame(TestPage1.PageOne)

    def Button6_Callback(self, controller):
        print('EditUserDataPage Button 6 Pressed')
        if(Application.UserAccessLevel == 0):
            #Go back to Admin Portal
            print("AdminPage Initialized")
            Application.Curr_Frame = AdminPage.AdminPage
            controller.show_frame(Application.Curr_Frame)


        #controller.show_frame(TestPage1.PageOne)

    def Button7_Callback(self, controller):
        print('EditUserDataPage Button 7 Pressed')
        self.UpdateEntryData()
        #controller.show_frame(TestPage1.PageOne)

    def Button8_Callback(self, controller):
        print('EditUserDataPage Button 8 Pressed')
        self.UpdateEntryData()
        #controller.show_frame(TestPage1.PageOne)

    def Button9_Callback(self, controller):
        print('EditUserDataPage Button 9 Pressed')
        self.UpdateEntryData()
        #controller.show_frame(TestPage1.PageOne)

    def UpdateEntryData(self):
        Application.Name = self.Entry1.get()        #Name
        Application.HCNo = self.Entry2.get()        #HC No
        Application.DOB = self.Entry3.get()         #DOB
        Application.Address = self.Entry4.get()     #Address
        Application.Contact = self.Entry5.get()     #Contact
        print("Name: " + Application.Name)
        print("HC No: " + Application.HCNo)
        print("DOB: " + Application.DOB)
        print("Address: " + Application.Address)
        print("Contact: " + Application.Contact)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Adding Image to frame
        # BgImage = Image.open("Images\BackgroundImage.png")
        BgImage = Image.open("Images\Image3.jpg")
        BgImage = ImageTk.PhotoImage(BgImage.resize((1920, 1080), Image.ANTIALIAS))
        self.Label1 = tk.Label(self, image = BgImage)
        self.Label1.image = BgImage
        self.Label1.pack()

        #Admin Webportal Message
        self.Message1 = tk.Message(self)
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.203, relwidth=1.001)
        self.Message1.configure(background="#0E86D4")
        self.Message1.configure(borderwidth="5")
        self.Message1.configure(cursor="hand2")
        self.Message1.configure(font="-family {Segoe UI} -size 34 -weight bold -underline 1")
        self.Message1.configure(justify='left')
        self.Message1.configure(relief="groove")
        self.Message1.configure(text="Edit User Data")
        self.Message1.configure(width=1538)

        #Name Entry Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.025, rely=0.3, height=64, width=207)
        self.Button1.configure(background="#f1ed43")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(command= lambda: EditUserDataPage.Button1_Callback(self, controller))
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text="Name")

        #Name Entry
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.2, rely=0.3, height=60, relwidth=0.257)
        self.Entry1.configure(background="#ecd1ca")
        self.Entry1.configure(borderwidth="5")
        self.Entry1.configure(cursor="hand2")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 20")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable="Name")

        # HC No. Entry Button
        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.025, rely=0.4, height=64, width=207)
        self.Button2.configure(background="#f1ed43")
        self.Button2.configure(borderwidth="3")
        self.Button2.configure(command=lambda: EditUserDataPage.Button2_Callback(self, controller))
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text="HC No.")

        # HCNo. Entry
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.2, rely=0.4, height=60, relwidth=0.257)
        self.Entry2.configure(background="#ecd1ca")
        self.Entry2.configure(borderwidth="5")
        self.Entry2.configure(cursor="hand2")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 20")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(text="Enter HCNo.")

        # DOB. Entry
        self.Entry3 = tk.Entry(self)
        self.Entry3.place(relx=0.2, rely=0.5, height=60, relwidth=0.257)
        self.Entry3.configure(background="#ecd1ca")
        self.Entry3.configure(borderwidth="5")
        self.Entry3.configure(cursor="hand2")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Courier New} -size 20")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(text="Enter DOB")

        # DOB Entry Button
        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.025, rely=0.5, height=64, width=207)
        self.Button3.configure(background="#f1ed43")
        self.Button3.configure(borderwidth="3")
        self.Button3.configure(command=lambda: EditUserDataPage.Button3_Callback(self, controller))
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text="DOB")

        # Address. Entry
        self.Entry4 = tk.Entry(self)
        self.Entry4.place(relx=0.2, rely=0.6, height=60, relwidth=0.257)
        self.Entry4.configure(background="#ecd1ca")
        self.Entry4.configure(borderwidth="5")
        self.Entry4.configure(cursor="hand2")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="-family {Courier New} -size 20")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(text="Enter Address")

        # Address Entry Button
        self.Button4 = tk.Button(self)
        self.Button4.place(relx=0.025, rely=0.6, height=64, width=207)
        self.Button4.configure(background="#f1ed43")
        self.Button4.configure(borderwidth="3")
        self.Button4.configure(command=lambda: EditUserDataPage.Button4_Callback(self, controller))
        self.Button4.configure(cursor="hand2")
        self.Button4.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(text="Address")

        # Contact No. Entry
        self.Entry5 = tk.Entry(self)
        self.Entry5.place(relx=0.2, rely=0.7, height=60, relwidth=0.257)
        self.Entry5.configure(background="#ecd1ca")
        self.Entry5.configure(borderwidth="5")
        self.Entry5.configure(cursor="hand2")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="-family {Courier New} -size 20")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(text="Enter ContactNo..")

        # Contact No Entry Button
        self.Button5 = tk.Button(self)
        self.Button5.place(relx=0.025, rely=0.7, height=64, width=207)
        self.Button5.configure(background="#f1ed43")
        self.Button5.configure(borderwidth="3")
        self.Button5.configure(command=lambda: EditUserDataPage.Button5_Callback(self, controller))
        self.Button5.configure(cursor="hand2")
        self.Button5.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(text="Contact")

        # Back Button
        self.Button6 = tk.Button(self)
        self.Button6.place(relx=0.85, rely=0.06, height=64, width=207)
        self.Button6.configure(background="yellow")
        self.Button6.configure(borderwidth="3")
        self.Button6.configure(command=lambda: EditUserDataPage.Button6_Callback(self, controller))
        self.Button6.configure(cursor="hand2")
        self.Button6.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(text="Back")


        # Update User Data Button
        self.Button7 = tk.Button(self)
        self.Button7.place(relx=0.7, rely=0.5, height=60, relwidth=0.200)
        self.Button7.configure(background="#1eee52")
        self.Button7.configure(borderwidth="3")
        self.Button7.configure(command=lambda: EditUserDataPage.Button7_Callback(self, controller))
        self.Button7.configure(cursor="hand2")
        self.Button7.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(text="Update")

        # Delete User Data Data
        self.Button8 = tk.Button(self)
        self.Button8.place(relx=0.7, rely=0.4, height=60, relwidth=0.200)
        self.Button8.configure(background="#1eee52")
        self.Button8.configure(borderwidth="3")
        self.Button8.configure(command=lambda: EditUserDataPage.Button8_Callback(self, controller))
        self.Button8.configure(cursor="hand2")
        self.Button8.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(text="Delete")

        # Add User Data
        self.Button9 = tk.Button(self)
        self.Button9.place(relx=0.7, rely=0.3, height=60, relwidth=0.200)
        self.Button9.configure(background="#1eee52")
        self.Button9.configure(borderwidth="3")
        self.Button9.configure(command=lambda: EditUserDataPage.Button9_Callback(self, controller))
        self.Button9.configure(cursor="hand2")
        self.Button9.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(text="Add")


