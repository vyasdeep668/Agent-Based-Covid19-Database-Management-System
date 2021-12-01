#Sender Agent: "professor14@jabbim.com", "BelaDeep@1964"
#Reciever Agent: "professor15@jabbim.com", "BelaDeep@1964"
import time
import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template


# ------------------------------Protocol Related Defines ##Don't Change##-----------------------------------
class AgentCommunication:

    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    WebPortalAgentUserID = "professor14@jabbim.com"
    WebPortalAgentPassword = "BelaDeep@1964"
    AHSAdminAgentUserID = "professor15@jabbim.com"
    SystemDatabaseAgentUserID = "professor16@jabbim.com"  # "professor16@jabbim.com"
    UserAgentUserID = "professor17@jabbim.com"

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


class WebPortalAgentClass(Agent):
    class WebPortalAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"WebPortalAgentClass.WebPortalAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            #print("SenderAgent:WebPortalAgentBehaviour:run")
            if AgentCommunication.CommunicationFlag:
                if AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.WebPortalAgentID:
                    msg = Message(to=AgentCommunication.WebPortalAgentUserID)  # Instantiate the message

                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.AHSAdminAgentID:
                    msg = Message(to=AgentCommunication.AHSAdminAgentUserID)  # Instantiate the message

                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.UserAgentID:
                    msg = Message(to=AgentCommunication.UserAgentUserID)  # Instantiate the message

                else:
                    msg = Message(to=AgentCommunication.SystemDatabaseAgentUserID)  # Instantiate the message

                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")

                # Set the message content
                msg.body = AgentCommunication.CommunicationTxBuffer

                # Send Message
                await self.send(msg)
                print("WebPortalAgentClass:WebPortalAgentBehaviour:run:msg:request:\"{}\"".format(msg.body))

                # wait for a message for 5 seconds
                msg = await self.receive(timeout=5)

                if msg:
                    # Copy Received to Communication RX Buffer
                    AgentCommunication.CommunicationRxBuffer = msg.body
                    print("WebPortalAgentClass:WebPortalAgentBehaviour:run:msg:response:\"{}\"".format(msg.body))
                    AgentCommunication.CommunicationError = False
                    AgentCommunication.CommunicationFlag = False

                else:
                    AgentCommunication.CommunicationFlag = False
                    AgentCommunication.CommunicationError = True
                    print("WebPortalAgentClass:WebPortalAgentBehaviour:run:msg:response:\"No Response\"")

            # else:
                # No Messages to be sent
            #await asyncio.sleep(2)

    async def setup(self):
        print("WebPortalAgentClass:setup")
        b = self.WebPortalAgentBehaviour()
        self.add_behaviour(b)


def RequestData(SenderAgentID, ReceiverAgentID, CommandID, ErrorCode, Data):

    AgentCommunication.CommunicationTxBuffer = SenderAgentID + ReceiverAgentID + CommandID + ErrorCode + Data
    AgentCommunication.CommunicationFlag = True
    while AgentCommunication.CommunicationFlag:
        pass

    # if Slave Agent is not responding
    if AgentCommunication.CommunicationError:
        AgentCommunication.CommunicationRxBuffer = ""

    return AgentCommunication.CommunicationRxBuffer

def WebPortalAgentStart():
    AgentCommunication.CommunicationTxBuffer = "Deep"
    WebPortalAgent = WebPortalAgentClass(AgentCommunication.WebPortalAgentUserID, AgentCommunication.WebPortalAgentPassword)
    # wait for receiver agent to be prepared.
    WebPortalAgent.start().result()
    WebPortalAgent.web.start(hostname="127.0.0.1", port="10000")

