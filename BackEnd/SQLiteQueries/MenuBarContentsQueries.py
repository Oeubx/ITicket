
#
import os

from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"

# --------------------------------------------------------- #
# queries for profile | Signup_Backend.py
# --------------------------------------------------------- #
# read from file
def get_loggedIn_UsersId():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    getLogged_acc_details = "SELECT * FROM Employee WHERE employee_Id = ?"

    pointer.execute(getLogged_acc_details, (emp_Id,))
    acc_details = pointer.fetchone()
    # gets the id only
    user_id = acc_details[0]
    
    return int(user_id)
# --------------------------------------------------------- #
# get queries
# --------------------------------------------------------- #
def get_userDetails(id):
    get_query = """
        SELECT
            employee_Id
            ,employee_username
            ,employee_email
            ,employee_password
        FROM Employee WHERE employee_Id = ?
    """

    pointer.execute(get_query, (id,))
    user_details = pointer.fetchone()
    
    return user_details

def get_userName(id):
    get_query = """
        SELECT employee_username
        FROM Employee WHERE employee_Id = ?
    """

    pointer.execute(get_query, (id,))
    user_name = pointer.fetchone()
    
    return user_name

def get_userEmail(id):
    get_query = """
        SELECT employee_email
        FROM Employee WHERE employee_Id = ?
    """

    pointer.execute(get_query, (id,))
    user_email = pointer.fetchone()
    
    return user_email
# --------------------------------------------------------- #
# update queries
# --------------------------------------------------------- #
def updateUserName(id, newName):
    update_query = """
        UPDATE Employee
        SET employee_username = ?
        WHERE employee_Id = ?
    """
    
    try:
        pointer.execute(update_query, (newName, id))
        dbConn.commit()
        return True  # if success
    except Exception as e:
        #print("Failed to insert data:", e)
        return False
    
def updateUserEmail(id, newEmail):
    update_query = """
        UPDATE Employee
        SET employee_email = ?
        WHERE employee_Id = ?
    """
    
    try:
        pointer.execute(update_query, (newEmail, id))
        dbConn.commit()
        return True  # if success
    except Exception as e:
        #print("Failed to insert data:", e)
        return False

def updateUserPass(id, newPassword):
    update_query = """
        UPDATE Employee
        SET employee_password = ?
        WHERE employee_Id = ?
    """
    
    try:
        pointer.execute(update_query, (newPassword, id))
        dbConn.commit()
        return True  # if success
    except Exception as e:
        #print("Failed to insert data:", e)
        return False

# --------------------------------------------------------- #
#
# --------------------------------------------------------- #