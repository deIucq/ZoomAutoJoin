import subprocess
import datetime

def startZoom(meetingid, password):
    res = subprocess.call(f"start zoommtg:\"//zoom.us/join?action=join&confno={meetingid}&pwd={password}\"", shell=True)
    return None

def extractMeetingidAndPassword(url):
    if url.startswith("https://us06web.zoom.us/j/"):
        passindex = url.find("?pwd=")
        meetingid = url[26:passindex]
        password = url[passindex+5:]
        return meetingid, password
    else:
        print("invalid URL")
        return None,None

def extractYMDHM(date):
    if len(date) == 16:
        if date[4] == date[7] == date[10] == date[13] == "/" and date[0:4].isdecimal() and date[5:7].isdecimal() and date[8:10].isdecimal() and date[11:13].isdecimal() and date[14:].isdecimal():
            return datetime.datetime(year=int(date[0:4]),month=int(date[5:7]),day=int(date[8:10]),hour=int(date[11:13]),minute=int(date[14:]))
        else:
            print("invalid date")
            return None
    else:
        print("invalid date")
        return None

inputURL = input("URL:")
inputDate = input("date(YYYY/MM/DD/HH/MM):")

meetingid, password = extractMeetingidAndPassword(inputURL)
meetingtime = extractYMDHM(inputDate)

if meetingid==None or password==None or meetingtime==None:
    exit()
print(inputURL)
while meetingtime - datetime.datetime.now() > datetime.timedelta():
    sec = int((meetingtime - datetime.datetime.now()).total_seconds())
    days = sec//(60*60*24)
    hours = (sec//(60*60))%24
    minutes = (sec//60)%60
    if(days > 1):
        print("\r"+str(days)+"days "+str(hours)+":"+str(minutes)+":"+str(sec%60),end="")
    elif(days == 1):
        print("\r"+str(days)+"day "+str(hours)+":"+str(minutes)+":"+str(sec%60),end="")
    else:
        print("\r"+str(hours)+":"+str(minutes)+":"+str(sec%60),end="")
startZoom(meetingid, password)