# Agent-Based-Covid19-Database-Management-System

## Prject Description
----------------------
COVID-19 vaccines help prevent us from getting infected and protect us from getting severely sick if we do get it. Albertans may wish to prove vaccination status if accessing businesses, other facilities, or travelling. Alberta vaccine reports will be the only valid Alberta proof of vaccination accepted by operators participating in the Restrictions Exemption Program as of November 15. Valid Alberta vaccine record will show name, birthdate, and vaccination type and date. Our project explains how to use Agent-based model to access and retrieve Covid-19 vaccination reports from the database for people who resides in Alberta. 

  
## Objectives
----------------------
Multi-agent systems technology allows for the development of autonomous software entities (intelligent agents) which are designed to communicate with each other. In our project, we are aiming to have a multi-agent system with the following agents: 

**User agent**: Responsible for generating covid report. 

**AHS admin agent**: Responsible for find user data/vaccine data and adding vaccine data.

**System database agent**: Responsible for find user data/vaccine data and add/delete/update user/vaccine data.

**Web portal Agent**: Responsible for connecting to other backend agents and get information from them.
The above agents will communicate and send messages to each other using Message Protocol. The Gaia Methodology which includes roles, permissions, rights, protocols, and transmission between agents is  used for the analysis and design of our application. 


![image](https://user-images.githubusercontent.com/24715827/144364233-30d846d7-9967-4438-b648-ff8d87c433f6.png)

## Multi Agent System
----------------------
An agent is a software entity that functions continuously and autonomously in a particular environment, often inhabited by other agents and process. In our system there are four agents as follows:
•	Web portal Agent
•	User Agent
•	System Database Agent
•	AHS Admin Agent

![image](https://user-images.githubusercontent.com/24715827/144363821-1bffb706-38a5-42cd-b3d6-179982966de3.png)


## Software Requirements
----------------------
Please Use requirements.txt file to install all dependencies on your machine
1) Python 3.7
2) Tkinter (For GUI)
3) Spade (Multi Agent System Framework)
4) mysql (Database Management)
5) fpdf (PDF Report Generation)
6) qrcode (QR Code Generation)
7) Pillow (Documents Operation)


