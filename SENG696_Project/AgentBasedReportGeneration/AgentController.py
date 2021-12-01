# ------------------------------Protocol Related Defines ##Don't Change##-----------------------------------
class ApplicationData:
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

class AgentCommunication:

    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    WebPortalAgentUserID = "professor14@jabbim.com"
    WebPortalAgentPassword = "BelaDeep@1964"
    AHSAdminAgentUserID = "professor15@jabbim.com"
    AHSAdminAgentPassword = "BelaDeep@1964"
    SystemDatabaseAgentUserID = "professor16@jabbim.com"
    SystemDatabaseAgentPassword = "BelaDeep@1964"
    UserAgentUserID = "professor17@jabbim.com"
    UserAgentPassword = "BelaDeep@1964"

    # Command IDs
    UserDataCommandID = "1"
    ReportDataCommandID = "2"
    UserDataUpdateCommandID = "3"
    UserDataAddCommandID = "4"
    UserDataDeleteCommandID = "5"
    VaccineDataUpdateCommandID = "6"
    VaccineDataAddCommandID = "7"
    VaccineDataDeleteCommandID = "8"
    GenerateReportCommandID = "9"

    # Agent IDs
    WebPortalAgentID = "1"
    SystemDatabaseAgentID = "2"
    AHSAdminAgentID = "3"
    UserAgentID = "4"

    # Error Codes
    SuccessAckID = "0"
    DataNotFoundAckID = "1"
    DatabaseConnectionFailureAckID = "2"
    DataUpdateFailedAckID = "3"
    DataAddFailedAckID = "4"
    DataDeleteFailedAckID = "5"

    # Protocol Format
    SenderAgentIDIndex = 0
    ReceiverAgentIDIndex = 1
    CommandIDIndex = 2
    ErrorCodeIndex = 3
    # index reserved for :
    DataIndex = 5
# ------------------------------------------------------------------------------------------
from Agents import User_Agent, AHSAdmin_Agent, DatabaseAdmin_Agent


def StartAgents():
    DatabaseAdmin_Agent.DatabaseAdminAgentStart()
    User_Agent.UserAgentStart()
    AHSAdmin_Agent.AHSAdminAgentStart()

