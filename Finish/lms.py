from selenium import webdriver
from getpass import getpass
import time
from datetime import datetime
import calendar
import random
import csv
my_date = datetime.today()

#https://chromedriver.chromium.org/downloads
username = input("Enter in your username: ")
password = getpass("Enter your password: ")

lms = webdriver.Chrome(executable_path="ChromeDriver/chromedriver.exe")
lms.get("https://ada-lms.thapar.edu/moodle/login/index.php")

username_textbox = lms.find_element_by_id("username")
username_textbox.send_keys(username)

password_textbox = lms.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = lms.find_element_by_id("loginbtn")
login_button.submit()

with open('Schedule.csv', newline='') as f:
    reader = csv.reader(f)
    lst = list(reader)
lst.remove(lst[0])
for i in range(len(lst)):
    lst[i].remove(lst[i][0])
for j in range(len(lst)):
    if lst[j-1][0] == '':
        lst.remove(lst[j-1])
#print(lst)

isStarted = False

for i in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[0].split(':')[0]) and datetime.now().minute == int(i[0].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[2]:
                lms.get(i[3])
                time.sleep(10)
                isStarted = True
            elif datetime.now().hour == int(i[1].split(':')[0]):
                #print('1')
                if datetime.now().minute > int(i[1].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[2]:
                    #print('2')
                    isStarted = False
                    break
            elif datetime.now().hour > int(i[1].split(':')[0]):
                if calendar.day_name[my_date.weekday()] == i[2]:
                    #print('3')
                    isStarted = False
                    break
            elif calendar.day_name[my_date.weekday()] != i[2]:
                isStarted = False
                break
            else:
                num = random.randint(1, 3)
                if num == 1:
                    lms.get('https://ada-lms.thapar.edu/moodle/my/')
                    time.sleep(2)
                elif num == 2:
                    lms.get('https://ada-lms.thapar.edu/moodle/calendar/view.php?view=month')
                    time.sleep(2)
                else:
                    lms.get('https://ada-lms.thapar.edu/moodle/')
                    time.sleep(2)
        elif isStarted == True:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]) and calendar.day_name[my_date.weekday()] == i[2]:
                time.sleep(1)
                isStarted = False
                break