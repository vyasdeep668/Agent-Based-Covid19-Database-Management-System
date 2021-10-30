#Database

#Dataset Format
#["Name", "HC No", "DOB", "Address", "Contact", "Dose1Type", "Dose1Date", "Dose1Loc", "Dose2Type", "Dose2Date", "Dose2Loc"]
import Application


def FindRecord(HC_No):
    for user in UserDatabase:
        if(user[1] == HC_No):
            return user
    return 0



UserDatabase= [
    ["Deep Vyas", "00001", "10/14/1997", "3843 Charleswood Dr.", "5879689120", "Covishield", "07/25/2021", "University", "Covishield", "28/08/2021", "University"],
    ["Manan Shah", "00002", "11/28/1997", "604 Waterlily NE", "4039665230", "Pfizer", "07/25/2021", "London Drugs", "Pfizer", "28/08/2021", "London Drugs"],
    ["Harsh Vyas", "00003", "09/27/1997", "1102 Meadows NW", "4039688659", "Moderna", "07/25/2021", "North Hill", "Moderna", "28/08/2021", "North Hill"]
]


UserList = [""]
