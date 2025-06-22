
# profile queries.py
import sqlite3 as sql
import os

from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

# SQL stuffs
dbConn, pointer = SQLiteCall()

# file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"

# ------------------------------------------------------------------------------ #
# queries for => Edit Profile Interface and Dashboard Profile Backend | Profile
# ------------------------------------------------------------------------------ #
def get_loggedIn_UsersId():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    getLogged_acc_details = "SELECT * FROM Employee WHERE emp_Id = ?"

    pointer.execute(getLogged_acc_details, (emp_Id,))
    acc_details = pointer.fetchone()
    user_id = acc_details[0]
    
    return int(user_id)

def get_userDetails(id):
    get_query = """
        SELECT emp_Id, emp_username, emp_email, emp_password
        FROM Employee WHERE emp_Id = ?
    """

    pointer.execute(get_query, (id,))
    user_details = pointer.fetchone()
    
    return user_details

def updateUserCredentials(id, newPassword):
    update_query = """
        UPDATE Employee
        SET emp_password = ?
        WHERE emp_Id = ?
    """
    
    try:
        pointer.execute(update_query, (newPassword, id))
        dbConn.commit()
        return True  # if success
    except Exception as e:
        #print("Failed to insert data:", e)
        return False
    
# ------------------------------------------------------------------------------ #
# queries for => Edit Profile Interface and Dashboard Profile Backend | My Ticket
# ------------------------------------------------------------------------------ #