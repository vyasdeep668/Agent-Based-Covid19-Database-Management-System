#Main Application

#Imports
import tkinter as tk
import AgentController
from AgentController import AgentCommunication
from AgentController import ApplicationData
from Agents import Webportal_Agent
from mysql.connector import connection

#Import Pages
from GUI import LoginPage
from GUI import UserPage
from GUI import AHSAdminPage
from GUI import AdminPage
from GUI import EditUserDataPage
from GUI import EditVaccineDataPage
from GUI import AddOnlyVaccineDataPage


#Application Data
Curr_Frame = LoginPage.LoginPage
Username = ""  # "deep.vyas"
Password = ""  # "1997"
Name = ""  # "Deep Vyas"
HCNo = ""  # "12345"
DOB = ""  # "10/14/1997"
Contact = ""  # "5879689120"
Address = ""  # "3843, Charleswood Dr. NW, Calgary"
Dose1Type = ""  # "Covishield"
Dose1Date = ""  # "07/25/2021"
Dose1Address = ""  # "University Pharmacy"
Dose2Type = ""  # "Covishield"
Dose2Date = ""  # "08/29/2021"
Dose2Address = ""  # "University Pharmacy"



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

def ConnectDatabase(Command_ID):
    try:
        cnx = connection.MySQLConnection(user='root', password='admin',
                                         host='localhost',
                                         database='covid19_database')
        cursor = cnx.cursor()
        cursor.execute("USE covid19_database")
        print('covid19_database Connection success')

        if (Command_ID == AgentCommunication.UserDataCommandID):
            try:
                query = "SELECT * FROM covid19_database.userdata WHERE Name='{Name}' AND HCNo={HCNo}".format\
                    (Name=ApplicationData.Name, HCNo=ApplicationData.HCNo)
                print(query)
                # query = "SELECT * FROM PatientData WHERE PatientName='Sudarsini Tekkam' AND HCNo=344225"
                cursor.execute(query)
                databases = cursor.fetchall()
                print(databases)

                if not databases:
                    ErrorCode = AgentCommunication.DataNotFoundAckID
                    return ErrorCode
                else:
                    # Update the App data
                    ApplicationData.Name = databases[0][0]
                    ApplicationData.HCNo = databases[0][1]
                    ApplicationData.DOB = databases[0][2]
                    ApplicationData.Address = databases[0][4]
                    ApplicationData.Contact = databases[0][3]
                    ErrorCode = AgentCommunication.SuccessAckID
                    return ErrorCode

            except Exception:
                ErrorCode = AgentCommunication.DatabaseConnectionFailureAckID
                return ErrorCode

        elif (Command_ID == AgentCommunication.ReportDataCommandID):
            try:
                query = "SELECT * FROM covid19_database.reportdata WHERE Name='{Name}' AND HCNo={HCNo}".format \
                    (Name=ApplicationData.Name, HCNo=ApplicationData.HCNo)
                print(query)
                # query = "SELECT * FROM EditVaccineData WHERE Name='Deep Vyas' AND HCNo=344225"
                cursor.execute(query)
                databases = cursor.fetchall()
                print(databases)

                if not databases:
                    ErrorCode = AgentCommunication.DataNotFoundAckID
                    #Clear Application Data #Patch: When Find button is pressed data was shown even if its deleted. Corrected
                    ApplicationData.Dose1Type = ""
                    ApplicationData.Dose1Date = ""
                    ApplicationData.Dose1Address = ""
                    ApplicationData.Dose2Type = ""
                    ApplicationData.Dose2Date = ""
                    ApplicationData.Dose2Address = ""
                    print("Database Empty")
                    return ErrorCode
                else:
                    # Update the App data
                    ApplicationData.Name = databases[0][0]
                    ApplicationData.HCNo = databases[0][1]
                    ApplicationData.Dose1Type = databases[0][2]
                    ApplicationData.Dose1Date = databases[0][3]
                    ApplicationData.Dose1Address = databases[0][4]
                    ApplicationData.Dose2Type = databases[0][5]
                    ApplicationData.Dose2Date = databases[0][6]
                    ApplicationData.Dose2Address = databases[0][7]
                    ErrorCode = AgentCommunication.SuccessAckID
                    return ErrorCode

                # print(databases)
            except Exception:
                ErrorCode = AgentCommunication.DatabaseConnectionFailureAckID
                return ErrorCode

        elif (Command_ID == AgentCommunication.UserDataAddCommandID):
            try:
                sql = "INSERT INTO covid19_database.userdata (Name, HCNo, DOB, Address, Contact) VALUES('{Name}', {HCNo}, '{DOB}', '{Address}', '{Contact}')".format(
                    Name=ApplicationData.Name,
                    HCNo=ApplicationData.HCNo, DOB=ApplicationData.DOB, Address=ApplicationData.Address,
                    Contact=ApplicationData.Contact)
                print(sql)
                cursor.execute(sql)
                cnx.commit()
                print(cursor.rowcount, "record inserted.")

                if cursor.rowcount == 0:
                    ErrorCode = AgentCommunication.DataAddFailedAckID
                else:
                    ErrorCode = AgentCommunication.SuccessAckID

                return ErrorCode
            except Exception:
                ErrorCode = AgentCommunication.DataAddFailedAckID
                print('Failure in User Add')
                return ErrorCode

        elif (Command_ID == AgentCommunication.UserDataUpdateCommandID):
            try:
                query = "Update covid19_database.userdata set Name='{Name}', DOB= '{DOB}', Address= '{Address}', Contact= '{Contact}' WHERE HCNo={HCNo}".format(
                    Name=ApplicationData.Name,
                    HCNo=ApplicationData.HCNo, DOB=ApplicationData.DOB, Address=ApplicationData.Address,
                    Contact=ApplicationData.Contact)
                print(query)
                cursor.execute(query)
                cnx.commit()
                # databases = cursor.fetchall()
                print(cursor.rowcount, "record updated.")
                if cursor.rowcount == 0:
                    ErrorCode = AgentCommunication.DataUpdateFailedAckID
                else:
                    ErrorCode = AgentCommunication.SuccessAckID
                return ErrorCode
            except Exception:
                ErrorCode = AgentCommunication.DataUpdateFailedAckID
                print('Failure in update')
                return ErrorCode

        elif (Command_ID == AgentCommunication.UserDataDeleteCommandID):
            try:
                # query="DELETE FROM covid19_database.userdata WHERE Name = 'Tuan Trang' AND HCNo = 12345
                query = "DELETE FROM covid19_database.userdata WHERE Name='{Name}' AND HCNo={HCNo}".format(
                    Name=ApplicationData.Name, HCNo=ApplicationData.HCNo)

                # query = "DELETE FROM PatientData WHERE PatientName='Sudarsini Tekkam' AND HCNo=344225"
                cursor.execute(query)
                cnx.commit()
                # databases = cursor.fetchall()
                print(cursor.rowcount, "record deleted.")
                if cursor.rowcount == 0:
                    ErrorCode = AgentCommunication.DataDeleteFailedAckID
                else:
                    ErrorCode = AgentCommunication.SuccessAckID
                return ErrorCode
            except Exception:
                ErrorCode = AgentCommunication.DataDeleteFailedAckID
                print('Failure in delete')
                return ErrorCode

        elif (Command_ID == AgentCommunication.VaccineDataAddCommandID):
            try:
                query = "INSERT INTO covid19_database.reportdata (Name, HCNo, Dose1Type, Dose1Date, Dose1Address, Dose2Type, Dose2Date, Dose2Address) \
                VALUES('{Name}', {HCNo}, '{Dose1Type}', '{Dose1Date}', '{Dose1Address}', '{Dose2Type}', '{Dose2Date}', '{Dose2Address}')"\
                    .format(Name=ApplicationData.Name, HCNo=ApplicationData.HCNo,
                            Dose1Type=ApplicationData.Dose1Type, Dose1Date=ApplicationData.Dose1Date, Dose1Address=ApplicationData.Dose1Address,
                            Dose2Type=ApplicationData.Dose2Type, Dose2Date=ApplicationData.Dose2Date, Dose2Address=ApplicationData.Dose2Address)
                print(query)
                cursor.execute(query)
                cnx.commit()
                print(cursor.rowcount, "record inserted.")
                if cursor.rowcount == 0:
                    ErrorCode = AgentCommunication.DataAddFailedAckID
                else:
                    ErrorCode = AgentCommunication.SuccessAckID
                return ErrorCode
            except Exception:
                ErrorCode = AgentCommunication.DataAddFailedAckID
                print('Failure in report data Add')
                return ErrorCode

        elif (Command_ID == AgentCommunication.VaccineDataUpdateCommandID):
            try:
                query = "Update covid19_database.reportdata set Name='{Name}', Dose1Type= '{Dose1Type}', Dose1Date= '{Dose1Date}', Dose1Address= '{Dose1Address}',\
                 Dose2Type= '{Dose2Type}', Dose2Date= '{Dose2Date}', Dose2Address= '{Dose2Address}' WHERE HCNo={HCNo}" \
                    .format(Name=ApplicationData.Name, HCNo=ApplicationData.HCNo,
                            Dose1Type=ApplicationData.Dose1Type, Dose1Date=ApplicationData.Dose1Date, Dose1Address=ApplicationData.Dose1Address,
                            Dose2Type=ApplicationData.Dose2Type, Dose2Date=ApplicationData.Dose2Date, Dose2Address=ApplicationData.Dose2Address)

                print(query)
                cursor.execute(query)
                cnx.commit()
                # databases = cursor.fetchall()
                print(cursor.rowcount, "record updated.")
                if cursor.rowcount == 0:
                    ErrorCode = AgentCommunication.DataUpdateFailedAckID
                else:
                    ErrorCode = AgentCommunication.SuccessAckID
                return ErrorCode

            except Exception:
                ErrorCode = AgentCommunication.DataUpdateFailedAckID
                print('Failure in report data Update')
                return ErrorCode

        elif (Command_ID == AgentCommunication.VaccineDataDeleteCommandID):
            try:
                # query="DELETE FROM covid19_database.reportdata WHERE Name = 'Tuan Trang' AND HCNo = 12345
                query = "DELETE FROM covid19_database.reportdata WHERE Name='{Name}' AND HCNo={HCNo}".format(
                    Name=ApplicationData.Name, HCNo=ApplicationData.HCNo)

                # query = "DELETE FROM PatientData WHERE PatientName='Sudarsini Tekkam' AND HCNo=344225"
                cursor.execute(query)
                cnx.commit()
                # databases = cursor.fetchall()
                print(cursor.rowcount, "record deleted.")
                if cursor.rowcount == 0:
                    ErrorCode = AgentCommunication.DataDeleteFailedAckID
                else:
                    ErrorCode = AgentCommunication.SuccessAckID
                return ErrorCode
            except Exception:
                ErrorCode = AgentCommunication.DataDeleteFailedAckID
                print('Failure in delete')
                return ErrorCode


    except Exception:
        ErrorCode = AgentCommunication.DatabaseConnectionFailureAckID
        return ErrorCode



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
        for F in (LoginPage.LoginPage, UserPage.UserPage, AHSAdminPage.AHSAdminPage,
                  AdminPage.AdminPage, EditUserDataPage.EditUserDataPage,
                  EditVaccineDataPage.EditVaccineDataPage,
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
    AgentController.StartAgents()
    Webportal_Agent.WebPortalAgentStart()
    app = Application()
    app.mainloop()








