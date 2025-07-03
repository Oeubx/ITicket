
# new file

import os

#auth queries.py
from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
filePointer = os.path.join(project_folder, "BackEnd", "Auth", "previously_logged_in_details.txt")
#filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"

# --------------------------------------------------------- #
# read from file logic
# --------------------------------------------------------- #

# ticket creation | line 18 | is commented => passed to read from file
# ticket creation backend | line 57 | is commented => passed to read from file
# tickets backend | line 38 | is commented => passed to read from file
# def get_loggedIn_UsersId():

# --------------------------------------------------------- #
# get queries for ticket creation | ticket creation.py
# --------------------------------------------------------- #
# ticket creation | line 21
def get_userName(id):
    get_query = """
        SELECT employee_username
        FROM Employee WHERE employee_Id = ?
    """

    pointer.execute(get_query, (id,))
    user_name = pointer.fetchone()

    # returns the first string (username, <null>)
    return user_name[0] if user_name else None 

def createTicket( title, desc, level, id ):
    ticketInserter = """
            INSERT INTO Ticket (
                ticket_title
                ,ticket_desc
                ,ticket_level
                ,submitted_by
                )
            VALUES (?, ?, ?, ?)    
        """
    
    #short validation
    try:
        pointer.execute( ticketInserter, (title, desc, level, id) )
        dbConn.commit()
        return True     # if success
    except Exception as e:
        #for debugging
        #print("Failed to insert data:", e)
        return False

# --------------------------------------------------------- #
# queries for ticket reloading | --.py
# --------------------------------------------------------- #

#select_AllTickets = "SELECT * FROM Ticket"
#select_LoggedUsersTickets = "SELECT * FROM Ticket WHERE submitted_by = ?"
#select_TicketLevel = "SELECT * FROM Ticket WHERE ticket_level = ?"

def get_AllTickets(sortOrder):
    getAll_query = f"""
        SELECT 
            T.ticket_Id,
            T.ticket_title,
            T.ticket_status,
            T.ticket_level,
            T.created_at,
            E.employee_username
        FROM Ticket T
        INNER JOIN Employee E ON T.submitted_by = E.employee_Id
        ORDER BY T.created_at {sortOrder}
    """
    pointer.execute(getAll_query)
    return pointer.fetchall()

def get_MyTickets(userId, sortOrder):
    getMyTickets_query = f"""
        SELECT 
            T.ticket_Id,
            T.ticket_title,
            T.ticket_status,
            T.ticket_level,
            T.created_at,
            E.employee_username
        FROM Ticket T
        INNER JOIN Employee E ON T.submitted_by = E.employee_Id
        WHERE T.submitted_by = ?
        ORDER BY T.created_at {sortOrder}
    """
    pointer.execute(getMyTickets_query, (userId,))
    return pointer.fetchall()

def get_TicketByLevel(level, sortOrder):
    get_TicketByLevel_query = f"""
        SELECT 
            T.ticket_Id,
            T.ticket_title,
            T.ticket_status,
            T.ticket_level,
            T.created_at,
            E.employee_username
        FROM Ticket T
        INNER JOIN Employee E ON T.submitted_by = E.employee_Id
        WHERE T.ticket_level = ?
        ORDER BY T.created_at {sortOrder}
    """
    pointer.execute(get_TicketByLevel_query, (level,))
    return pointer.fetchall()

# is both used by functions
# reloadTicket and | line 122
# showFullTicket   | line 215
def get_LatestHandler(ticketId):
    latestHandlerQuery = """
        SELECT E.employee_username
        FROM Ticket_History TH
        INNER JOIN Employee E ON TH.ticket_Handler = E.employee_Id
        WHERE TH.ticket_Id = ?
        ORDER BY TH.update_Date DESC
        LIMIT 1
    """
    pointer.execute(latestHandlerQuery, (ticketId,))
    latestHandlerResult = pointer.fetchone()

    return latestHandlerResult[0] if latestHandlerResult else "No Handler"

# --------------------------------------------------------- #
# queries for full ticket showing | --.py
# --------------------------------------------------------- #
def get_FullTicketDetails(ticketId):
    selectTicket = """
        SELECT
            T.ticket_Id,
            T.ticket_title,
            T.ticket_desc,
            T.ticket_status,
            T.ticket_level,
            E.employee_username
        FROM Ticket T
        INNER JOIN Employee E ON T.submitted_by = E.employee_Id
        WHERE T.ticket_Id = ?
    """
    pointer.execute(selectTicket, (ticketId,))
    ticketDetailsHolder = pointer.fetchone()

    return ticketDetailsHolder

# query for update ticket history backend line 82
def get_TicketDescription(ticketId):
    query = """
        SELECT T.ticket_desc
        FROM Ticket T
        WHERE T.ticket_Id = ?
    """
    pointer.execute(query, (ticketId,))
    result = pointer.fetchone()

    return result[0] if result else "No Description Found"

def get_ThisTicketsHistory(ticketId):
    selectTicketHistory = """
        SELECT 
            ticket_Handler
            ,update_Description
        FROM Ticket_History
        WHERE ticket_Id = ?
        ORDER BY "update_" DESC
    """
    pointer.execute(selectTicketHistory, (ticketId,))
    ticketHistoryDetailsHolder = pointer.fetchall()

    return ticketHistoryDetailsHolder

# is both used by functions
# in Update ticket history backend > render ticket history | line 99
# in Update ticket history backend > render ticket history | line 165
# and in tickets backend > show full ticket | line 215
def get_TicketHandlers_Name(handlerId):
    getHandlerName_query = "SELECT employee_username FROM Employee WHERE employee_Id = ?"

    pointer.execute(getHandlerName_query, (handlerId, ))
    handlerNameResult = pointer.fetchone()

    return handlerNameResult[0] if handlerNameResult else "Unkown Ticket Handler"

# ---------------------------------------------------------------------------- #
# query for updating ticket history | update ticket history backend .py
# ---------------------------------------------------------------------------- #
def update_thisTicket(ticketId, handlerId, updateDesc):
    insert_TH_query = """
            INSERT INTO Ticket_History (
                ticket_id
                ,ticket_Handler
                ,update_Description
                )
            VALUES (?, ?, ?)    
        """
    
    #short validation
    try:
        pointer.execute(insert_TH_query,
                        (ticketId, handlerId, updateDesc)
                        )
        dbConn.commit()
    except Exception as e:
        #for debugging
        #print("Failed to insert data:", e)
        return

def update_thisTicketsStatus(status, ticketId):
    update_Ticket_query = """
                    UPDATE Ticket
                    SET
                        ticket_status = ?
                    WHERE ticket_Id = ?
                """
                
    #short validation
    try:
        # 1 default value to re open the ticket
        pointer.execute(update_Ticket_query, (status, ticketId))
        dbConn.commit()
    except Exception as e:
        #for debugging
        #print("Failed to insert data:", e)
        return