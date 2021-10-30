#Import Modules
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image

#Import Pages
import Database
import Application
from GUI import LoginPage
from GUI import UserPage
from GUI import AHSAdminPage
from GUI import AdminPage
from GUI import EditUserDataPage
from GUI import EditVaccineDataPage
from GUI import AddOnlyVaccineDataPage



AdminPageFrame = tk.Frame
class AdminPage(AdminPageFrame):
    #Callbacks Here
    def Button1_Callback(self, controller):
        print('AdminPage Button 1 Pressed')
        #self.Message1.configure(text = "Admin Page Message v1")
        #controller.show_frame(AdminPage.PageOne)

    def Button2_Callback(self, controller):
        print('AdminPage Button 2 Pressed')
        # controller.show_frame(AdminPage.PageOne)

    def Button3_Callback(self, controller):
        print('AdminPage Button 3 Pressed')
        self.UpdateEntryData()
        user = Database.FindRecord(Application.HCNo)
        if (user == 0):  # User Not Found
            tkinter.messagebox.showerror(title="Error", message="Data Not Found")
        else:
            print(user)
            self.UpdateUserData(user)
            self.RefreshDataListBox()
        #controller.show_frame(TestPage1.PageOne)

    def Button4_Callback(self, controller):
        print('AdminPage Button 4 Pressed')
        if ((tk.messagebox.askquestion('Logout', 'Are you sure you want to logout', icon='question')) == 'yes'):
            Curr_Frame = LoginPage.LoginPage
            print("LoginPage Initialized")
            controller.show_frame(LoginPage.LoginPage)

    def Button5_Callback(self, controller):
        print('AdminPage Button 5 Pressed')
        #controller.show_frame(TestPage1.PageOne)

    def Button6_Callback(self, controller):
        print('AdminPage Button 6 Pressed')
        Application.Curr_Frame = EditVaccineDataPage.EditVaccineDataPage
        print("EditVaccineDataPage Initialized")
        controller.show_frame(Application.Curr_Frame)

    def Button7_Callback(self, controller):
        print('AdminPage Button 7 Pressed')
        Application.Curr_Frame = EditUserDataPage.EditUserDataPage
        print("EditUserDataPage Initialized")
        controller.show_frame(Application.Curr_Frame)

    def UpdateEntryData(self):
        Application.Name = self.Entry1.get()
        Application.HCNo = self.Entry2.get()
        print("Name: " + Application.Name)
        print("HCNo: " + Application.HCNo)

    def RefreshDataListBox(self):
        self.ClearListBox()
        self.Listbox1.insert(1, "Database Entry")
        self.Listbox1.insert(3, "Name: " + Application.Name)
        self.Listbox1.insert(4, "HC No: " + Application.HCNo)
        self.Listbox1.insert(5, "DOB: " + Application.DOB)
        self.Listbox1.insert(6, "Address: " + Application.Address)
        self.Listbox1.insert(7, "Contact: " + Application.Contact)
        self.Listbox1.insert(8, "Dose 1 Type: " + Application.Dose1Type)
        self.Listbox1.insert(9, "Dose 1 Date: " + Application.Dose1Date)
        self.Listbox1.insert(10, "Dose 1 Location: " + Application.Dose1Address)
        self.Listbox1.insert(11, "Dose 2 Type: " + Application.Dose2Type)
        self.Listbox1.insert(12, "Dose 2 Date: " +Application.Dose2Date)
        self.Listbox1.insert(13, "Dose 2 Location: " +Application.Dose2Address)

    def UpdateUserData(self, user):
        Application.Name = user[0]
        Application.HCNo = user[1]
        Application.DOB = user[2]
        Application.Address = user[3]
        Application.Contact = user[4]
        Application.Dose1Type = user[5]
        Application.Dose1Date = user[6]
        Application.Dose1Address = user[7]
        Application.Dose2Type = user[8]
        Application.Dose1Date = user[9]
        Application.Dose1Address = user[10]

    def ClearListBox(self):
        self.Listbox1.delete('0', 'end')



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
        self.Message1.configure(text="Welcome Admin")
        self.Message1.configure(width=1538)

        #Name Entry Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.025, rely=0.3, height=64, width=207)
        self.Button1.configure(background="#f1ed43")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(command= lambda: AdminPage.Button1_Callback(self, controller))
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
        self.Button2.configure(command=lambda: AdminPage.Button2_Callback(self, controller))
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

        #Find Report Button
        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.25, rely=0.5, height=60, relwidth=0.150)
        self.Button3.configure(background="#1eee52")
        self.Button3.configure(borderwidth="3")
        self.Button3.configure(command=lambda: AdminPage.Button3_Callback(self, controller))
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text="Find")

        # Logout Button
        self.Button4 = tk.Button(self)
        self.Button4.place(relx=0.85, rely=0.06, height=64, width=207)
        self.Button4.configure(background="red")
        self.Button4.configure(borderwidth="3")
        self.Button4.configure(command=lambda: AdminPage.Button4_Callback(self, controller))
        self.Button4.configure(cursor="hand2")
        self.Button4.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(text="Logout")

        #Database List Box
        self.Listbox1 = tk.Listbox(self)
        self.Listbox1.place(relx=0.0, rely=0.627, relheight=0.377, relwidth = 0.999)
        self.Listbox1.configure(background="#c1f9f9")
        self.Listbox1.configure(borderwidth="3")
        self.Listbox1.configure(cursor="hand2")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {8514oem} -size 13")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.xview()
        #Default View


        # Generate Report Button
        self.Button5 = tk.Button(self)
        self.Button5.place(relx=0.7, rely=0.5, height=60, relwidth=0.200)
        self.Button5.configure(background="#1eee52")
        self.Button5.configure(borderwidth="3")
        self.Button5.configure(command=lambda: AdminPage.Button5_Callback(self, controller))
        self.Button5.configure(cursor="hand2")
        self.Button5.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(text="Generate Report")

        # Edit Vaccine Data
        self.Button6 = tk.Button(self)
        self.Button6.place(relx=0.7, rely=0.4, height=60, relwidth=0.200)
        self.Button6.configure(background="#1eee52")
        self.Button6.configure(borderwidth="3")
        self.Button6.configure(command=lambda: AdminPage.Button6_Callback(self, controller))
        self.Button6.configure(cursor="hand2")
        self.Button6.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(text="Edit Vaccine Data")

        # Edit User Data
        self.Button7 = tk.Button(self)
        self.Button7.place(relx=0.7, rely=0.3, height=60, relwidth=0.200)
        self.Button7.configure(background="#1eee52")
        self.Button7.configure(borderwidth="3")
        self.Button7.configure(command=lambda: AdminPage.Button7_Callback(self, controller))
        self.Button7.configure(cursor="hand2")
        self.Button7.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(text="Edit User Data")


