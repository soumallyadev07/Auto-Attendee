import csv

import time
from datetime import datetime
# from pynput.keyboard import Controller, Key
# from data import lst
import webbrowser
import calendar
my_date = datetime.today()

# keyboard = Controller()

with open('Schedule.csv', newline='') as f:
    reader = csv.reader(f)
    lst = list(reader)
lst.remove(lst[0])
for i in range(len(lst)):
    lst[i].remove(lst[i][-1])
for j in range(len(lst)):
    if lst[j-1][0] == '':
        lst.remove(lst[j-1])



isStarted = False

for i in lst:
    print(i)
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[3]:
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[3]:
                #keyboard.press('w')
                time.sleep(1)
                #keyboard.press(Key.enter)
                isStarted = False
                break
print('Day Complete')