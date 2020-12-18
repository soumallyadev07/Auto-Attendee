import time
from datetime import datetime
# from pynput.keyboard import Controller, Key
# from data import lst
import webbrowser
import calendar
import csv
from pynotifier import Notification
from playsound import playsound
my_date = datetime.today()

def labtutnotify():
    i = 1
    while i <= 4:
        try:
            Notification(
            title='You have have a LAB/TUT',
            description='Bro, Please Lab/Tut toh laga le!',
            icon_path='Media/winicon.ico', # On Windows .ico is required, on Linux - .png
            duration=10,                              # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
            ).send()
        except:
            Notification(
            title='You have have a LAB/TUT',
            description='Kuch toh sharam kro!',
            icon_path='Media/winicon.ico', # On Windows .ico is required, on Linux - .png
            duration=10,                              # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
            ).send()
        playsound('Media/Alien_Siren-KevanGC-610357990.mp3')
        time.sleep(5)
        i += 1

with open('Schedule.csv', newline='') as f:
    reader = csv.reader(f)
    lst = list(reader)
lst.remove(lst[0])
# for i in range(len(lst)):
#     lst[i].remove(lst[i][-1])
# for j in range(len(lst)):
#     if lst[j-1][0] == '':
#         lst.remove(lst[j-1])
#print(lst)


# keyboard = Controller()

isStarted = False

for i in lst:
    print(i)
    while True:
        #print('1')
        if isStarted == False:
            #print('2')
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[3]:
                #print('3')
                webbrowser.open(i[0])
                if i[-1] == "Yes":
                    #print('4')
                    labtutnotify()
                isStarted = True
            elif datetime.now().hour == int(i[1].split(':')[0]):
                #print('5')
                if datetime.now().minute > int(i[1].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[3]:
                    #print('6')
                    isStarted = False
                    break
            elif datetime.now().hour > int(i[1].split(':')[0]):
                if calendar.day_name[my_date.weekday()] == i[3]:
                    #print('10')
                    isStarted = False
                    break
            elif calendar.day_name[my_date.weekday()] != i[3]:
                isStarted = False
                break
        elif isStarted == True:
            #print('7')
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[3]:
                #print('8')
                #keyboard.press('w')
                time.sleep(1)
                #keyboard.press(Key.enter)
                isStarted = False
                break
    #print('9')
print('Day Complete')
