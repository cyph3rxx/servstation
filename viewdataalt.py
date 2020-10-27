import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="toor",database="ssdata")
c=conn.cursor()
def viewdataalt():
    x=c.execute("""SELECT * FROM servstation""")
    for row in x:
        print(row)