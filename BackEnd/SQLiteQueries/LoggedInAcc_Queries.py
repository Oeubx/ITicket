
# new file

import os

from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall
dbConn, pointer = SQLiteCall()

# file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
# new directory
filePointer = os.path.join(project_folder, "BackEnd", "Auth", "previously_logged_in_details.txt")
# old directory
#filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"

# --------------------------------------------------------- #
# queries for Logged in Account | LoggedIn_Acc.py
# --------------------------------------------------------- #
def fetch_all_user_credentials(id):
    pointer.execute("SELECT * FROM Employee WHERE employee_Id = ?", (id, ) )
    userContentsHolder = pointer.fetchone()

    return userContentsHolder

def fetch_user_id(id):
    get_Id_query = "SELECT employee_Id FROM Employee WHERE employee_Id = ?"

    pointer.execute(get_Id_query, (id,))
    acc_details = pointer.fetchone()
    
    # passed the id only
    # ( id, <null>)
    return acc_details[0]

def fetch_user_type(id):
    get_type_query = "SELECT employee_type FROM Employee WHERE employee_Id = ?"

    pointer.execute(get_type_query, (id,))
    acc_details = pointer.fetchone()
    
    # passed the type only
    # ( type, <null>)
    return acc_details[0]

def get_userEmpType():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    getLogged_acc_details = """
        SELECT employee_type
        FROM Employee
        WHERE employee_Id = ?
    """

    pointer.execute(getLogged_acc_details, (emp_Id,))
    user_type = pointer.fetchone()
    
    return int(user_type[0])