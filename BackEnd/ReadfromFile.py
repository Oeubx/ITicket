
# new file | mainly will hold logic for reading file contents 

import os
from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall
from BackEnd.SQLiteQueries.LoggedInAcc_Queries import *

dbConn, pointer = SQLiteCall()

# file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
# new directory
filePointer = os.path.join(project_folder, "Auth", "previously_logged_in_details.txt")
# old directory
#filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"

# --------------------------------------------------------- #
# for authentication process
# --------------------------------------------------------- #
def read_AuthValue_fromFile():
    with open(filePointer, "r") as file:
        line1 = file.readline().strip()

    #returns an integer instead of default string
    return int(line1) 

# --------------------------------------------------------- #
# logging in and updating file contents with user credentials 
# --------------------------------------------------------- #
def loginUpdateFile(id):
    acc_details = fetch_all_user_credentials(id)
    emp_Id, emp_user, emp_email, emp_pw, emp_type = acc_details

    #writes it on file and automatically closes the file after
    with open(filePointer, "w") as file:
        #passes 3 automatically to direct user to dashboard n skips auth process
        file.write("3\n") 
        file.write(f"{emp_Id}\n")
        file.write(f"{emp_user}\n")
        file.write(f"{emp_email}\n")
        file.write(f"{emp_pw}\n")
        file.write(f"{emp_type}\n")

# --------------------------------------------------------- #
# logging out and updating file contents 
# --------------------------------------------------------- #
def logoutUpdateFile():
    # overwrites everything and 
    with open(filePointer, "w") as file:
        #passes 0 automatically to direct user to auth process
        file.write("0\n") 

# --------------------------------------------------------- #
# read from file logics
# --------------------------------------------------------- #

# --------------------------------------------------------- #
# get logged in users ID
# --------------------------------------------------------- #
# was used in ticket queries => moved here
# was used in ticket creation | line 18
# was used in ticket creation backend | line 57
# was used in tickets backend | line 38
def get_loggedIn_UsersId():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    #gets the first index (2nd item which is emp_Id)
    emp_Id = lines[1].strip() 

    user_id = fetch_user_id(emp_Id)
    
    return int(user_id)

# --------------------------------------------------------- #
# get logged in users employee type
# --------------------------------------------------------- #
def get_userEmpType():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    #gets the first index (2nd item which is emp_Id)
    emp_Id = lines[1].strip() 

    user_type = fetch_user_id(emp_Id)
    
    return int(user_type)