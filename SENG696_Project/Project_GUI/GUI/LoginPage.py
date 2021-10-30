#Import Modules
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image

#Import Pages
from GUI import LoginPage
from GUI import UserPage
from GUI import AHSAdminPage
from GUI import AdminPage
from GUI import EditVaccineDataPage
from GUI import AddOnlyVaccineDataPage

import Application




LoginPageFrame = tk.Frame
class LoginPage(LoginPageFrame):

    #Callbacks Here
    def Button1_Callback(self, controller):
        print('LoginPage Button 1 Pressed')
        #controller.show_frame(TestPage1.PageOne)

    def Button2_Callback(self, controller):
        print('LoginPage Button 2 Pressed')
        # controller.show_frame(TestPage1.PageOne)

    def Button3_Callback(self, controller):
        print('LoginPage Button 3 Pressed')
        self.UpdateEntryData()
        #Validation Checks
        if((not Application.Username) or (not Application.Password)):
            tkinter.messagebox.showerror(title="Error", message="Enter Username or Password")
        else:
            #Check Username in Database if matches
            if((Application.Username == Application.User3_Username) and (Application.Password == Application.User3_Password)):
                Curr_Frame = UserPage.UserPage
                print("UserPage Initialized")
                controller.show_frame(Curr_Frame)
            elif((Application.Username == Application.User2_Username) and (Application.Password == Application.User2_Password)):
                Curr_Frame = AHSAdminPage.AHSAdminPage
                print("AHSAdminPage Initialized")
                controller.show_frame(Curr_Frame)
            elif ((Application.Username == Application.User1_Username) and (Application.Password == Application.User1_Password)):
                Curr_Frame = AdminPage.AdminPage
                print("AdminPage Initialized")
                controller.show_frame(Curr_Frame)
            else:
                tkinter.messagebox.showerror(title="Error", message="Wrong Username or Password")

    def UpdateEntryData(self):
        Application.Username = self.Entry1.get()
        Application.Password = self.Entry2.get()
        print("Username: " + Application.Username)
        print("Password: " + Application.Password)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Adding Image to frame
        #BgImage = Image.open("Images\BackgroundImage.png")
        BgImage = Image.open("Images\Image1.jpg")
        BgImage = ImageTk.PhotoImage(BgImage.resize((1920, 1080), Image.ANTIALIAS))
        self.Label1 = tk.Label(self, image = BgImage)
        self.Label1.image = BgImage
        self.Label1.pack()

        #Title of the Project
        self.Message1 = tk.Message(self)
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.203, relwidth=1.001)
        self.Message1.configure(background="#0E86D4") #0E86D4 #abcbf1
        self.Message1.configure(borderwidth="5")
        self.Message1.configure(cursor="fleur")
        self.Message1.configure(font="-family {Segoe UI} -size 34 -weight bold -underline 1")
        self.Message1.configure(justify='center')
        self.Message1.configure(relief="groove")
        self.Message1.configure(text='''Agent Based Covid19 Vaccine Report Generation''')
        self.Message1.configure(width=1538)

        #Username Textbox Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.250, rely=0.389, height=64, width=207)
        self.Button1.configure(background="#f1ed43")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(command= lambda: LoginPage.Button1_Callback(self, controller))
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text="Username")

        #Username Entry
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.400, rely=0.389, height=60, relwidth=0.257)
        self.Entry1.configure(background="#ecd1ca")
        self.Entry1.configure(borderwidth="5")
        self.Entry1.configure(cursor="arrow")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 20")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable="Username")

        # Password TextBox Button
        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.250, rely=0.503, height=64, width=207)
        self.Button2.configure(background="#f1ed43")
        self.Button2.configure(borderwidth="3")
        self.Button2.configure(command=lambda: LoginPage.Button2_Callback(self, controller))
        self.Button2.configure(cursor="fleur")
        self.Button2.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text="Password")

        # Username Entry
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.400, rely=0.503, height=60, relwidth=0.257)
        self.Entry2.configure(background="#ecd1ca")
        self.Entry2.configure(borderwidth="5")
        self.Entry2.configure(cursor="arrow")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 20")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable="Password")
        self.Entry2.configure(show="*")

        #Login Button
        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.461, rely=0.628, height=64, width=207)
        self.Button3.configure(background="#1eee52")
        self.Button3.configure(borderwidth="3")
        self.Button3.configure(command=lambda: LoginPage.Button3_Callback(self, controller))
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text="Login")


