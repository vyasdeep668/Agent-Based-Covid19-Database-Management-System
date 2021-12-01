import time
import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from AgentController import AgentCommunication
from AgentController import ApplicationData

from Application import ConnectDatabase

class DatabaseAdminAgentClass(Agent):
    class DatabaseAdminAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"DatabaseAdminAgentClass.DatabaseAdminAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            #print("DatabaseAdminAgent:DatabaseAdminAgentBehaviour:run")
            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print("DatabaseAdminAgentClass:DatabaseAdminAgentBehaviour:run:msg:request:\"{}\"".format(ReceivedMessage))

                ''' Check Agent Receiver ID'''
                if not ReceivedMessage[1] == AgentCommunication.SystemDatabaseAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.WebPortalAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                if commandID == AgentCommunication.UserDataCommandID:
                    ApplicationData.Name = ReceivedMessage[1]
                    ApplicationData.HCNo = ReceivedMessage[2]

                    '''Execute Find User Data Query'''
                    ErrorCode = ConnectDatabase(commandID)

                    # Send response to Webportal agent
                    msg.body = AgentCommunication.WebPortalAgentID + \
                               AgentCommunication.SystemDatabaseAgentID + \
                               commandID + \
                               ErrorCode + \
                               ':' + str(ApplicationData.Name) + \
                               ':' + str(ApplicationData.HCNo) + \
                               ':' + str(ApplicationData.DOB) + \
                               ':' + str(ApplicationData.Address) + \
                               ':' + str(ApplicationData.Contact)

                elif commandID == AgentCommunication.ReportDataCommandID:
                    ApplicationData.Name = ReceivedMessage[1]
                    ApplicationData.HCNo = ReceivedMessage[2]

                    '''Execute Find Vaccine Data Query'''
                    ErrorCode = ConnectDatabase(commandID)

                    # Send response to Webportal agent
                    msg.body = AgentCommunication.WebPortalAgentID + \
                               AgentCommunication.SystemDatabaseAgentID + \
                               commandID + \
                               ErrorCode + \
                               ':' + str(ApplicationData.Name) + \
                               ':' + str(ApplicationData.HCNo) + \
                               ':' + str(ApplicationData.Dose1Type) + \
                               ':' + str(ApplicationData.Dose1Date) + \
                               ':' + str(ApplicationData.Dose1Address) + \
                               ':' + str(ApplicationData.Dose2Type) + \
                               ':' + str(ApplicationData.Dose2Date) + \
                               ':' + str(ApplicationData.Dose2Address)

                elif (commandID == AgentCommunication.UserDataUpdateCommandID) or \
                        (commandID == AgentCommunication.UserDataAddCommandID) or \
                        (commandID == AgentCommunication.UserDataDeleteCommandID):

                    '''Update App Data'''
                    ApplicationData.Name = ReceivedMessage[1]
                    ApplicationData.HCNo = ReceivedMessage[2]
                    # Update DOB, Address, Contact only for below 2 commands
                    if (commandID == AgentCommunication.UserDataUpdateCommandID) or \
                            (commandID == AgentCommunication.UserDataAddCommandID):
                        ApplicationData.DOB = ReceivedMessage[3]
                        ApplicationData.Address = ReceivedMessage[4]
                        ApplicationData.Contact = ReceivedMessage[5]

                    '''Execute User Data Query according to commandID'''
                    ErrorCode = ConnectDatabase(commandID)

                    ''' Send response to Webportal agent '''
                    msg.body = AgentCommunication.WebPortalAgentID + \
                               AgentCommunication.SystemDatabaseAgentID + \
                               commandID + \
                               ErrorCode

                elif (commandID == AgentCommunication.VaccineDataUpdateCommandID) or \
                        (commandID == AgentCommunication.VaccineDataAddCommandID) or \
                        (commandID == AgentCommunication.VaccineDataDeleteCommandID):

                    '''Update App Data'''
                    ApplicationData.Name = ReceivedMessage[1]
                    ApplicationData.HCNo = ReceivedMessage[2]
                    # Update DOB, Address, Contact only for below 2 commands
                    if (commandID == AgentCommunication.VaccineDataUpdateCommandID) or \
                            (commandID == AgentCommunication.VaccineDataAddCommandID):
                        ApplicationData.Dose1Type = ReceivedMessage[3]
                        ApplicationData.Dose1Date = ReceivedMessage[4]
                        ApplicationData.Dose1Address = ReceivedMessage[5]
                        ApplicationData.Dose2Type = ReceivedMessage[6]
                        ApplicationData.Dose2Date = ReceivedMessage[7]
                        ApplicationData.Dose2Address = ReceivedMessage[8]

                    '''Execute User Data Query according to commandID'''
                    ErrorCode = ConnectDatabase(commandID)

                    ''' Send response to Webportal agent '''
                    msg.body = AgentCommunication.WebPortalAgentID + \
                               AgentCommunication.SystemDatabaseAgentID + \
                               commandID + \
                               ErrorCode

                print("DatabaseAdminAgentClass:DatabaseAdminAgentBehaviour:run:msg:response:\"{}\"".format(msg.body))
                await self.send(msg)


    async def setup(self):
        print("DatabaseAdminAgentClass:setup")
        b = self.DatabaseAdminAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def DatabaseAdminAgentStart():
    DatabaseAdminAgent = DatabaseAdminAgentClass(AgentCommunication.SystemDatabaseAgentUserID, AgentCommunication.SystemDatabaseAgentPassword)
    # wait for receiver agent to be prepared.
    DatabaseAdminAgent.start().result()
    DatabaseAdminAgent.web.start(hostname="127.0.0.3", port="10000")