import mysql.connector
from calculatealt import calculatealt
from viewdataalt import viewdataalt
from dataentryalt import dataentryalt
conn=mysql.connector.connect(host="localhost",user="root",password="toor",database="ssdata")
c=conn.cursor()
print("Welcome, what do you need?")
print("1. Enter data")
print("2. View entries")
print("3. Calculate")
userchoice=input()
if userchoice=="1":
    dataentryalt()
elif userchoice=="2":
    viewdataalt()
elif userchoice=="3":
    calculatealt()
else:
    print("Wrong input")
conn.close()