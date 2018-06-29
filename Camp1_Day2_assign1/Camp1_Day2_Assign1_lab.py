import json
def GetSessionFromFile(filename):
    file = open(filename, "r")
    data = json.load(file)
    session = data["sessions"]
    sessionArray = session.split(",")
    ##print(TempInputSession)
    return sessionArray
if __name__ == '__main__':
   AllSession = GetSessionFromFile("allsession.json")
   AttendSession = GetSessionFromFile("attended.json")
   numberSession = len(set(AllSession) & set(AttendSession))
   print ("I have attended " +str(numberSession)+ " sessions!!")
