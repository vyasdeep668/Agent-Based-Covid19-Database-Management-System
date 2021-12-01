from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from AgentController import AgentCommunication
from AgentController import ApplicationData
from ReportGeneration.Encoder_Decoder import encode_file_to_str
from ReportGeneration import ReportGeneration


class UserAgentClass(Agent):
    class UserAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"UserAgentClass.UserAgentBehaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            #print("UserAgent:UserAgentBehaviour:run")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body

                ''' Check Agent Receiver ID'''
                if not ReceivedMessage[1] == AgentCommunication.UserAgentID:
                    return

                commandID = ReceivedMessage[2]
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.WebPortalAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                if commandID == AgentCommunication.GenerateReportCommandID:
                    'Get Data from Message body'
                    ApplicationData.Name = ReceivedMessage[1]
                    ApplicationData.HCNo = ReceivedMessage[2]
                    ApplicationData.DOB = ReceivedMessage[3]
                    ApplicationData.Dose1Type = ReceivedMessage[4]
                    ApplicationData.Dose1Date = ReceivedMessage[5]
                    ApplicationData.Dose1Address = ReceivedMessage[6]
                    ApplicationData.Dose2Type = ReceivedMessage[7]
                    ApplicationData.Dose2Date = ReceivedMessage[8]
                    ApplicationData.Dose2Address = ReceivedMessage[9]

                    ReportGeneration.GenerateReport(ApplicationData.Name, ApplicationData.HCNo, ApplicationData.DOB,
                                                    ApplicationData.Dose1Type, ApplicationData.Dose1Date, ApplicationData.Dose1Address,
                                                    ApplicationData.Dose2Type, ApplicationData.Dose2Date, ApplicationData.Dose2Address)

                    file_str = encode_file_to_str("CovidReport.pdf")
                    ErrorCode = AgentCommunication.SuccessAckID

                    # Send response to Webportal agent
                    msg.body = AgentCommunication.WebPortalAgentID + \
                               AgentCommunication.UserAgentID + \
                               commandID + \
                               ErrorCode + \
                               ':' + file_str

                print("UserAgentClass:UserAgentBehaviour:run:msg:response:{CovidReport.pdf Sent}")
                await self.send(msg)


    async def setup(self):
        print("UserAgentClass:setup")
        b = self.UserAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def UserAgentStart():
    UserAgent = UserAgentClass(AgentCommunication.UserAgentUserID, AgentCommunication.UserAgentPassword)
    # wait for receiver agent to be prepared.
    UserAgent.start().result()
    UserAgent.web.start(hostname="127.0.0.4", port="10000")