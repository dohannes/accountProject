"""
--This is just a file for a crash course on MySQL within Python 3.** 

"""


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="dean7",
    passwd="Mymoneys123mm!",
    database="testdatabase"
    )

myCursor = db.cursor()

"""
# --below is an example of creating a DB, with table; User, and adding entries to it. 
# 
# #myCursor.execute(CREATE DATABASE testdatabase), creates a new database that can be accessed in .connector method
# # myCursor.execute("CREATE TABLE User(username VARCHAR(50), password VARCHAR(10), personID int PRIMARY KEY AUTO_INCREMENT)")
# # myCursor.execute("INSERT INTO User (username, password) VALUES (%s, %s)", ("dean7778", "password"))
# # db.commit()
# # myCursor.execute("INSERT INTO User(username, password) VALUES ()")
# #myCursor.execute("SELECT * FROM User")
"""

for i in myCursor:
    print(i)