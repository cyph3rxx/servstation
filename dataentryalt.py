import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="toor",database="ssdata")
c=conn.cursor()
def dataentryalt():
    print("Enter the name")
    Name=input()
    print("Enter the type of vehicle")
    vehicle_type=input()
    print("Enter the vehicle number")
    vehicle_number=input()
    print("Enter the cost")
    service_cost=input()
    print("Enter the date")
    date=input()
    print(f" Name : {Name} \n Vehicle type : {vehicle_type} \n Vehicle No: {vehicle_number} \n Cost: {service_cost} \n Date: {date}")
    print("Is it correct?")
    correct_check=input()
    if correct_check=="yes" or correct_check=="y":
        query="""INSERT INTO servstation VALUES (%s,%s,%s,%s,%s)"""
        data=(Name,vehicle_type,vehicle_number,service_cost,date)
        c.execute(query,data)
        conn.commit()
        conn.close()
    elif correct_check=="no" or correct_check=="n":
        print("Do it again")
    else:
        print("Wrong input")