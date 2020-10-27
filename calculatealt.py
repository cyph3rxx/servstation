import sqlite3
conn = sqlite3.connect("ssdata.db")
c=conn.cursor()
def calculatealt():
	print("Enter the date")
	calculate_date=input()
	calculate_query="""SELECT SUM(cost) FROM servstation WHERE dateofservice=(?,?,?,?,?,?,?,?,?,?)"""
	x=c.execute(calculate_query,calculate_date)
	x=c.fetchall()
	print(x)
