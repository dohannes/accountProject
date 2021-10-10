#import necessary modules
from tkinter import *

import mysql.connector
import dotenv, os

"""
CREATION OF DATABASE 
--USE OF MYSQL, OS, DOTENV
"""
dotenv.load_dotenv('.env')
root_password = os.getenv('USER_PASSWORD')

db = mysql.connector.connect(
    host="localhost",
    user="dean7",
    passwd=root_password,
    database="Userdata"
)

myCursor = db.cursor()
# myCursor.execute("CREATE DATABASE Userdata") #create the database to be used within the SQL workbench
#myCursor.execute("CREATE TABLE users(username VARCHAR(20), password VARCHAR(16), userID int PRIMARY KEY AUTO_INCREMENT)") #create table to hold certain values

"""
CREATION OF THE GUI FOR THE PROJECT
--USE OF TKINTER
"""

#define app setting, title, geo, etc.
root = Tk()
root.title("INSULATE")
root.geometry("250x180")
root.resizable(False, False)
root.iconbitmap("logo.ico")

class app(Frame):
    def __init__(self, **kwargs):
        super(app, self).__init__(**kwargs) #inherit the module
        self.utils() #import utils (apart of class, defines widgets)

    def create_user(self):
        #get username and password from entry fields
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        #insert them into db with appropriate userID's
        myCursor.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (f"{username}", f"{password}"))
        db.commit()
        myCursor.execute("SELECT * FROM users")
        for i in myCursor:
            print(f"//\n{i}")

        #delete strings within entry fields
        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)

        #create 'account created' label
        self.creationLabel = Label(master=self.mainFrame, text=f"Account {username} created", font=("Verdana", 10))
        self.creationLabel.place(relx=0.5, rely=0.85, anchor=CENTER)

    #creation of widgets is below
    def utils(self):
        #creation of title mainFrame
        self.mainFrame = Frame().grid(row=1, column=0)

        #creation of labels
        self.mainLabel = Label(master=root, text="INSULATE", font=("Verdana", 10)).place(relx=0.47, rely=0.03, anchor=N)
        self.usernameLabel = Label(master=self.mainFrame, text="username: ", font=("Verdana", 10)).place(relx=0.01, rely=0.24, anchor=W)
        self.passwordLabel = Label(master=self.mainFrame, text="password: ", font=("Verdana", 10)).place(relx=0.01, rely=0.45, anchor=W)

        #creation of Entries
        self.usernameEntry = Entry(master=self.mainFrame, font=("Verdana", 10))
        self.usernameEntry.place(relx=0.31, rely=0.25, anchor=W) #have to do seperately to allow myself to get users information
        self.passwordEntry = Entry(master=self.mainFrame, font=("Verdana", 10), show="*")
        self.passwordEntry.place(relx=0.31, rely=0.44, anchor=W) #follow the same procedure

        #creation of buttons
        self.loginBttn = Button(master=self.mainFrame,text="login", font=("Verdana", 10)).place(relx=0.35, rely=0.65, anchor=CENTER)
        self.signupBttn = Button(master=self.mainFrame, text="sign-up", font=("Verdana", 10), command=self.create_user).place(relx=0.6, rely=0.65, anchor=CENTER)

#executes this files code
if __name__ == '__main__':
    root = app()
    root.mainloop()