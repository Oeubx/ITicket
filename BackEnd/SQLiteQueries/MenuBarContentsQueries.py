
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

# --------------------------------------------------------- #
# get queries for employee management
# --------------------------------------------------------- #
def get_AllUsersId():
    pointer.execute("SELECT employee_Id FROM Employee")
    return pointer.fetchall()

#except type
def get_AllUserCredentials(userId):
    query = f"""
            SELECT 
                employee_username
                ,employee_email
            FROM Employee
            WHERE employee_Id = ?
        """
    pointer.execute(query, (userId,))
    return pointer.fetchone()

# --------------------------------------------------------- #
# deletion of accounts n everything in that
# --------------------------------------------------------- #
def del_AllRelatedToAcc(userId):
    try:
        # Step 1: Delete all tickets and their history
        pointer.execute("SELECT ticket_Id FROM Ticket WHERE submitted_by = ?", (userId,))
        ticket_ids = [row[0] for row in pointer.fetchall()]

        if ticket_ids:
            pointer.executemany(
                "DELETE FROM Ticket_History WHERE ticket_Id = ?",
                [(ticket_id,) for ticket_id in ticket_ids]
            )
        
        pointer.execute("DELETE FROM Ticket WHERE submitted_by = ?", (userId,))

        # Step 2: Delete the user from the Employee table
        pointer.execute("DELETE FROM Employee WHERE employee_Id = ?", (userId,))

        dbConn.commit()
        #print(f"[✓] Successfully deleted employee ID {userId}, their tickets, and ticket history.")
    except Exception as e:
        #undoes any committed stuff if error
        dbConn.rollback()
        #print("[!] Error during account deletion:", e)

# --------------------------------------------------------- #
# deletion of all tickets under that user
# --------------------------------------------------------- #
def del_AllTicketsOfThisUser(userId):
    try:
        # Step 1: Get all ticket IDs submitted by this user
        pointer.execute("SELECT ticket_Id FROM Ticket WHERE submitted_by = ?", (userId,))
        ticket_ids = [row[0] for row in pointer.fetchall()]

        # Step 2: Delete associated Ticket_History records
        if ticket_ids:
            pointer.executemany(
                "DELETE FROM Ticket_History WHERE ticket_Id = ?",
                [(ticket_id,) for ticket_id in ticket_ids]
            )

        # Step 3: Delete tickets from the Ticket table
        pointer.execute("DELETE FROM Ticket WHERE submitted_by = ?", (userId,))

        dbConn.commit()
        #print(f"[✓] Deleted {len(ticket_ids)} tickets and their history for user ID {userId}")
    except Exception as e:
        #undoes any committed stuff if error
        dbConn.rollback()
        #print("[!] Error during deletion:", e)

# --------------------------------------------------------- #
# deletion of specific ticket under that user
# --------------------------------------------------------- #
def get_ThisUsersTickets(userId):
    getThisTickets_query = f"""
        SELECT 
            T.ticket_Id
            ,T.ticket_title
            ,T.ticket_status
            ,T.ticket_level
            ,T.created_at
            ,E.employee_username
        FROM Ticket T
        INNER JOIN Employee E ON T.submitted_by = E.employee_Id
        WHERE T.submitted_by = ?
        ORDER BY T.created_at DESC
    """
    pointer.execute(getThisTickets_query, (userId,))
    return pointer.fetchall()

def del_SpecificTicketsOfThisUser(ticketId):
    try:
        # Step 1: Delete any related ticket history
        pointer.execute("DELETE FROM Ticket_History WHERE ticket_Id = ?", (ticketId,))

        # Step 2: Delete the ticket itself
        pointer.execute("DELETE FROM Ticket WHERE ticket_Id = ?", (ticketId,))

        dbConn.commit()
        #print(f"[✓] Deleted ticket ID {ticketId} and its history.")
    except Exception as e:
        #undoes any committed stuff if error
        dbConn.rollback()
        #print("[!] Error deleting specific ticket:", e)