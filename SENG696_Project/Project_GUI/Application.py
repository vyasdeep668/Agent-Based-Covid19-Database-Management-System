#Main Application

#Imports

import tkinter as tk
from tkinter import ttk

#Import Pages
import Database
from GUI import LoginPage
from GUI import UserPage
from GUI import AHSAdminPage
from GUI import AdminPage
from GUI import EditUserDataPage
from GUI import EditVaccineDataPage
from GUI import AddOnlyVaccineDataPage

#Application Data
Curr_Frame = LoginPage.LoginPage
Username = "deep.vyas"
Password = "1997"
Name = "Deep Vyas"
HCNo = "12345"
DOB = "10/14/1997"
Contact = "5879689120"
Address = "3843, Charleswood Dr. NW, Calgary"
Dose1Type = "Covishield"
Dose1Date = "07/25/2021"
Dose1Address = "University Pharmacy"
Dose2Type = "Covishield"
Dose2Date = "08/29/2021"
Dose2Address = "University Pharmacy"

#Dummy Database for Unit Testing Change it to actual Database when integrating
#Admin
User1_Username = "user1"
User1_Password = "user1"
#AHS Admin
User2_Username = "user2"
User2_Password = "user2"
#User Admin
User3_Username = "user3"
User3_Password = "user3"


#UserAccessLevel: 0->Admin, 1->AHSAdmin, 2->User
UserAccessLevel = 0




class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "BTC")

        self.geometry("1536x801+-8+-8")
        self.minsize(120, 1)
        self.maxsize(3844, 1071)
        self.resizable(1, 1)
        self.title("Agent Based Covid 19 Vaccine Report Generation")
        self.configure(background="#a6a6a6")
        self.configure(highlightbackground="#efcefd")
        self.configure(highlightcolor="#fff7c6")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LoginPage.LoginPage, UserPage.UserPage, AHSAdminPage.AHSAdminPage,\
                  AdminPage.AdminPage, EditUserDataPage.EditUserDataPage,\
                  EditVaccineDataPage.EditVaccineDataPage,\
                  AddOnlyVaccineDataPage.AddOnlyVaccineDataPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #1st Page Show
        #self.show_frame(LoginPage.LoginPage)

        Curr_Frame = LoginPage.LoginPage
        #Curr_Frame = UserPage.UserPage
        #Curr_Frame = AHSAdminPage.AHSAdminPage
        #Curr_Frame = AdminPage.AdminPage
        #Curr_Frame = EditUserDataPage.EditUserDataPage
        #Curr_Frame =  EditVaccineDataPage.EditVaccineDataPage
        #Curr_Frame =  AddOnlyVaccineDataPage.AddOnlyVaccineDataPage
        #print("UserPage Initialized")
        self.show_frame(Curr_Frame)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == '__main__':
    #print(Database.UserDatabase[0])
    #Database.UserDatabase.append(Database.listtoappend)
    #print(Database.UserDatabase[3])
    #user = Database.FindRecord("00001")
    #print(user)
    app = Application()
    app.mainloop()