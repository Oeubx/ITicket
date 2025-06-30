import sqlite3 as sql
import os

from BackEnd.SQLite_Calls import SQLiteCall
_, pointer = SQLiteCall()

#file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
filePointer = os.path.join(project_folder, "previously_logged_in_details.txt")

def read_AuthValue_fromFile():
    with open(filePointer, "r") as file:
        line1 = file.readline().strip()

    return int(line1) #returns an integer instead of default string

#update file everytime user logs in
def loginUpdateFile(id):
    getLogged_acc_details = "SELECT * FROM Employee WHERE emp_Id = ?"

    #gets user data based on employee id
    pointer.execute(getLogged_acc_details, (id,))
    #saves it to acc_details
    acc_details = pointer.fetchone()
    emp_Id, emp_user, emp_email, emp_pw, emp_type = acc_details

    #writes it on file and automatically closes the file after
    with open(filePointer, "w") as file:
        file.write("3\n") #passes 3 automatically to direct user to dashboard n skips auth process
        file.write(f"{emp_Id}\n")
        file.write(f"{emp_user}\n")
        file.write(f"{emp_email}\n")
        file.write(f"{emp_pw}\n")
        file.write(f"{emp_type}\n")

#logout basic logic
def logoutUpdateFile():
    with open(filePointer, "w") as file:
        file.write("0\n") #passes 0 automatically to direct user auth process

def getUserDetails(): #read from database by reading logged in details on file
    #reads on file and automatically closes the file after
    with open(filePointer, "r") as file:
        lines = file.readlines()  # Reads all lines into a list

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    getLogged_acc_details = "SELECT * FROM Employee WHERE emp_Id = ?"

    #gets user data based on employee id
    pointer.execute(getLogged_acc_details, (emp_Id,))
    #saves it to acc_details
    acc_details = pointer.fetchone()
    return acc_details

def getUserID():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    #getLogged_acc_details = "SELECT * FROM Employee WHERE emp_Id = ?"
    getLogged_acc_details = "SELECT emp_Id FROM Employee WHERE emp_Id = ?"

    pointer.execute(getLogged_acc_details, (emp_Id,))
    acc_details = pointer.fetchone()
    user_id = acc_details[0]
    
    return int(user_id)

def getUserEmpType():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    getLogged_acc_details = "SELECT * FROM Employee WHERE emp_Id = ?"

    pointer.execute(getLogged_acc_details, (emp_Id,))
    acc_details = pointer.fetchone()
    user_type = acc_details[4]
    
    return int(user_type)

#def getTickets():


#def getTicketHistory():

#def fileCreation():
    #try:
    #    # Try creating the file (only if it doesn't exist)
    #    txtfile = open(filePointer, "x")
    #    txtfile.close()
    #    print("File created.")
    #except FileExistsError:
    #    print("File already exists.")

    #checks where the file is at
    #print("Data written to:", os.path.abspath(filePointer))

    #gets the value from the file
    #with open(filePointer, "r") as file:
    #    line1, line2, line3, line4, line5, line6 = [line.strip() for line in file]

    #print(line5)