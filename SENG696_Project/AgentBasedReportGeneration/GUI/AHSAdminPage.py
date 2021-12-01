#Import Modules
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
from Agents import Webportal_Agent
from Agents.Webportal_Agent import AgentCommunication
from ReportGeneration.Encoder_Decoder import decode_str_to_file

#Import Pages
import Application
from GUI import LoginPage
from GUI import AHSAdminPage
from GUI import AddOnlyVaccineDataPage



AHSAdminPageFrame = tk.Frame
class AHSAdminPage(AHSAdminPageFrame):
    #Callbacks Here
    def Button1_Callback(self, controller):
        print('AHSAdminPage Button 1 Pressed')
        #self.Message1.configure(text = "AHSAdmin Page Message v1")
        #controller.show_frame(AHSAdminPage.PageOne)

    def Button2_Callback(self, controller):
        print('AHSAdminPage Button 2 Pressed')
        # controller.show_frame(AHSAdminPage.PageOne)

    def Button3_Callback(self, controller):
        print('AHSAdminPage Button 3 Pressed')
        self.UpdateEntryData()

        # Check Data Integrity If HCNo is not entered give error msg
        if not Application.HCNo:
            tkinter.messagebox.showerror(title="Error", message="Please Enter HC No.")
            return

        CommData = ':' + Application.Name + ':' + Application.HCNo
        ReceivedData = Webportal_Agent.RequestData(AgentCommunication.WebPortalAgentID,
                                                   AgentCommunication.AHSAdminAgentID,
                                                   AgentCommunication.UserDataCommandID,
                                                   AgentCommunication.SuccessAckID,
                                                   CommData)

        # No Message received from Slave Agent
        if not ReceivedData:
            tkinter.messagebox.showerror(title="Error", message="AHS Admin Agent is not Responding!")
            return

        # If Nack Error Received from Slave Agent
        if ReceivedData[AgentCommunication.ErrorCodeIndex] == AgentCommunication.DataNotFoundAckID:
            tkinter.messagebox.showerror(title="Error", message="User Data not found!")
            return

        userData = ReceivedData[AgentCommunication.DataIndex:]

        ReceivedData = Webportal_Agent.RequestData(AgentCommunication.WebPortalAgentID,
                                                   AgentCommunication.AHSAdminAgentID,
                                                   AgentCommunication.ReportDataCommandID,
                                                   AgentCommunication.SuccessAckID,
                                                   CommData)
        # No Message received from Slave Agent
        if not ReceivedData:
            tkinter.messagebox.showerror(title="Error", message="AHS Admin Agent is not Responding!")
            return

        vaccineData = ReceivedData[AgentCommunication.DataIndex:]

        # Get data in list elements
        userData = userData.split(":")
        vaccineData = vaccineData.split(":")

        self.UpdateUserData(userData, vaccineData)
        self.RefreshDataListBox()

    def Button4_Callback(self, controller):
        print('AHSAdminPage Button 4 Pressed')
        if ((tk.messagebox.askquestion('Logout', 'Are you sure you want to logout', icon='question')) == 'yes'):
            Curr_Frame = LoginPage.LoginPage
            print("LoginPage Initialized")
            controller.show_frame(LoginPage.LoginPage)

    def Button5_Callback(self, controller):
        print('AHSAdminPage Button 5 Pressed')
        # Check Data Integrity If HCNo is not entered give error msg
        if not Application.HCNo:
            tkinter.messagebox.showerror(title="Error", message="Please Enter HC No.")
            return

        # Check Data Integrity If Name is not entered give error msg
        if not Application.Name:
            tkinter.messagebox.showerror(title="Error", message="Please Enter Name")
            return

        CommData = ':' + Application.Name + ':' + Application.HCNo + ':' + Application.DOB + \
                   ':' + Application.Dose1Type + ':' + Application.Dose1Date + ':' + Application.Dose1Address + \
                   ':' + Application.Dose2Type + ':' + Application.Dose2Type + ':' + Application.Dose2Address

        ReceivedData = Webportal_Agent.RequestData(AgentCommunication.WebPortalAgentID,
                                                   AgentCommunication.UserAgentID,
                                                   AgentCommunication.GenerateReportCommandID,
                                                   AgentCommunication.SuccessAckID,
                                                   CommData)

        # No Message received from Slave Agent
        if not ReceivedData:
            tkinter.messagebox.showerror(title="Error", message="User Agent is not Responding!")
            return

        # If Nack Error Received from Slave Agent
        if ReceivedData[AgentCommunication.ErrorCodeIndex] == AgentCommunication.DataNotFoundAckID:
            tkinter.messagebox.showerror(title="Error", message="User Data not found!")
            return
        if ReceivedData[AgentCommunication.ErrorCodeIndex] == AgentCommunication.DatabaseConnectionFailureAckID:
            tkinter.messagebox.showerror(title="Error", message="Database connection failure!")
            return

        # decode file string to actual file
        file_str = ReceivedData[AgentCommunication.DataIndex:]
        decode_str_to_file(file_str, "CovidReportDecoded.pdf")
        tkinter.messagebox.showinfo(title="Success", message="File Successfully Saved!")

    def Button6_Callback(self, controller):
        print('AHSAdminPage Button 6 Pressed')
        Curr_Frame = AddOnlyVaccineDataPage.AddOnlyVaccineDataPage
        print("AddOnlyVaccineDataPage Initialized")
        controller.show_frame(AddOnlyVaccineDataPage.AddOnlyVaccineDataPage)
        #controller.show_frame(TestPage1.PageOne)

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
        self.Listbox1.insert(12, "Dose 2 Date: " + Application.Dose2Date)
        self.Listbox1.insert(13, "Dose 2 Location: " + Application.Dose2Address)

    def UpdateUserData(self, userData, vaccineData):
        Application.Name = userData[0]
        Application.HCNo = userData[1]
        Application.DOB = userData[2]
        Application.Address = userData[3]
        Application.Contact = userData[4]
        Application.Dose1Type = vaccineData[2]
        Application.Dose1Date = vaccineData[3]
        Application.Dose1Address = vaccineData[4]
        Application.Dose2Type = vaccineData[5]
        Application.Dose2Date = vaccineData[6]
        Application.Dose2Address = vaccineData[7]

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

        #AHSAdmin Webportal Message
        self.Message1 = tk.Message(self)
        self.Message1.place(relx=0.0, rely=0.0, relheight=0.203, relwidth=1.001)
        self.Message1.configure(background="#0E86D4")
        self.Message1.configure(borderwidth="5")
        self.Message1.configure(cursor="hand2")
        self.Message1.configure(font="-family {Segoe UI} -size 34 -weight bold -underline 1")
        self.Message1.configure(justify='left')
        self.Message1.configure(relief="groove")
        self.Message1.configure(text="Welcome AHS Admin")
        self.Message1.configure(width=1538)

        #Name Entry Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.025, rely=0.3, height=64, width=207)
        self.Button1.configure(background="#f1ed43")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(command= lambda: AHSAdminPage.Button1_Callback(self, controller))
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
        self.Button2.configure(command=lambda: AHSAdminPage.Button2_Callback(self, controller))
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
        self.Button3.configure(command=lambda: AHSAdminPage.Button3_Callback(self, controller))
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(font="-family {Segoe UI} -size 23 -weight bold")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text="Find")

        # Logout Button
        self.Button4 = tk.Button(self)
        self.Button4.place(relx=0.85, rely=0.06, height=64, width=207)
        self.Button4.configure(background="red")
        self.Button4.configure(borderwidth="3")
        self.Button4.configure(command=lambda: AHSAdminPage.Button4_Callback(self, controller))
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

        # Generate Report Button
        self.Button5 = tk.Button(self)
        self.Button5.place(relx=0.7, rely=0.5, height=60, relwidth=0.200)
        self.Button5.configure(background="#1eee52")
        self.Button5.configure(borderwidth="3")
        self.Button5.configure(command=lambda: AHSAdminPage.Button5_Callback(self, controller))
        self.Button5.configure(cursor="hand2")
        self.Button5.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(text="Generate Report")

        # Add Vaccine Data
        self.Button6 = tk.Button(self)
        self.Button6.place(relx=0.7, rely=0.4, height=60, relwidth=0.200)
        self.Button6.configure(background="#1eee52")
        self.Button6.configure(borderwidth="3")
        self.Button6.configure(command=lambda: AHSAdminPage.Button6_Callback(self, controller))
        self.Button6.configure(cursor="hand2")
        self.Button6.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(text="Add Vaccine Data")


