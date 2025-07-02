
# new file

import os

#auth queries.py
from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# file stuffs
project_folder = os.path.dirname(os.path.abspath(__file__))
filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"

# --------------------------------------------------------- #
# read from file logic
# --------------------------------------------------------- #
def get_loggedIn_UsersId():
    with open(filePointer, "r") as file:
        lines = file.readlines()

    emp_Id = lines[1].strip() #gets the first index (2nd item which is emp_Id)

    getLogged_acc_details = "SELECT employee_Id FROM Employee WHERE employee_Id = ?"

    pointer.execute(getLogged_acc_details, (emp_Id,))
    acc_details = pointer.fetchone()
    # gets the id only
    user_id = acc_details[0]
    
    return int(user_id)

# --------------------------------------------------------- #
# get queries for ticket creation | ticket creation.py
# --------------------------------------------------------- #
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
            ticket_Id
            ,ticket_title
            --skip ticket descrption
            ,ticket_status
            ,ticket_level
            ,created_at
            ,submitted_by
        FROM Ticket
        ORDER BY created_at {sortOrder}
    """
    pointer.execute(getAll_query)
    allTickets = pointer.fetchall()

    return allTickets

def get_MyTickets(userId, sortOrder):
    getMyTickets_query = f"""
        SELECT 
            ticket_Id
            ,ticket_title
            --skip ticket descrption
            ,ticket_status
            ,ticket_level
            ,created_at
            ,submitted_by
        FROM Ticket
        WHERE submitted_by = {userId}
        ORDER BY created_at {sortOrder}
    """
    pointer.execute(getMyTickets_query)
    myTickets = pointer.fetchall()

    return myTickets

def get_TicketByLevel(level, sortOrder):
    get_TicketByLevel_query = f"""
        SELECT
            ticket_Id
            ,ticket_title
            --skip ticket descrption
            ,ticket_status
            ,ticket_level
            ,created_at
            ,submitted_by
        FROM Ticket
        WHERE ticket_level = {level}
        ORDER BY created_at {sortOrder}
    """
    pointer.execute(get_TicketByLevel_query)
    sortedTickets = pointer.fetchall()

    return sortedTickets

# is both used by functions
# reloadTicket and | line 75
# showFullTicket   | line 190
def get_TicketSubmitterName(userId):
    getSubmitterName_query = "SELECT employee_username FROM Employee WHERE employee_Id = ?"

    pointer.execute(getSubmitterName_query, (userId, ))
        
    submitterNameResult = pointer.fetchone()
    return submitterNameResult[0] if submitterNameResult else "Unkown Ticket Submitter | "

# is both used by functions
# reloadTicket and | line 109
# showFullTicket   | line 215
def get_LatestHandler(ticketId):
    latestHandlerQuery = """
            SELECT ticket_Handler
            FROM Ticket_History
            WHERE ticket_Id = ?
            ORDER BY "updatedAt" DESC
            LIMIT 1
        """
    #DESCENDING takes the latest history and the handler,
    # LIMIT 1 takes the first only

    pointer.execute(latestHandlerQuery, (ticketId,))
    latestHandlerResult = pointer.fetchone()

    return latestHandlerResult[0] if latestHandlerResult else "No Handler"

# --------------------------------------------------------- #
# queries for full ticket showing | --.py
# --------------------------------------------------------- #
def get_TicketDetails(ticketId):
    selectTicket = """
        SELECT
            ticket_Id
            ,ticket_title
            ,ticket_desc
            ,ticket_status
            ,ticket_level
            --skips created at
            ,submitted_by
        FROM Ticket
        WHERE ticket_Id = ?
    """
    pointer.execute(selectTicket, (ticketId,))
    ticketDetailsHolder = pointer.fetchone()

    return ticketDetailsHolder

def get_ThisTicketsHistory(ticketId):
    selectTicketHistory = """
        SELECT 
            ticket_Handler
            ,update_Description
        FROM Ticket_History
        WHERE ticket_Id = ?
        ORDER BY "updatedAt" ASC
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