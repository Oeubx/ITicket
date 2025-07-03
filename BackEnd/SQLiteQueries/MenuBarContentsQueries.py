
#

from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# --------------------------------------------------------- #
# get queries for edit profile interface
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
# update queries for edit profile interface
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
# get queries for my tickets interface
# --------------------------------------------------------- #
def get_MyTickets(userId, sortOrder):
    query = f"""
            SELECT ticket_Id
            FROM Ticket
            WHERE submitted_by = ?
            ORDER BY created_at {sortOrder}
        """
    pointer.execute(query, (userId,))
    return pointer.fetchall()