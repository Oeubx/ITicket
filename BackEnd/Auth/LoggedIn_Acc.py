
import os

from BackEnd.SQLiteQueries.LoggedInAcc_Queries import fetch_all_user_credentials

#file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
filePointer = os.path.join(project_folder, "previously_logged_in_details.txt")

def read_AuthValue_fromFile():
    with open(filePointer, "r") as file:
        line1 = file.readline().strip()

    #returns an integer instead of default string
    return int(line1) 

#update file everytime user logs in
def loginUpdateFile(id):

    #moved the query to the query file
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

#logout basic logic
def logoutUpdateFile():
    # overwrites everything and 
    with open(filePointer, "w") as file:
        #passes 0 automatically to direct user to auth process
        file.write("0\n") 
