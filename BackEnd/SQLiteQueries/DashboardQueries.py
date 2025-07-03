
# new file

#auth queries.py
from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# --------------------------------------------------------- #
# queries for dashboard | dashboard interface .py
# --------------------------------------------------------- #
def get_pending_ticket_count():
    # usage of DISTINCT to avoid duplications
    get_query = """
        SELECT COUNT(DISTINCT t.ticket_Id)
        FROM Ticket t
        JOIN Ticket_History th ON t.ticket_Id = th.ticket_Id
        WHERE t.ticket_status = 'Open' AND th.ticket_Handler IS NOT NULL
    """

    pointer.execute(get_query)
    result = pointer.fetchone()

    return result[0] if result else 0

def get_open_ticket_count():
    get_query = """
        SELECT COUNT(*) FROM Ticket WHERE ticket_status = 'Open'
    """

    pointer.execute(get_query)
    result = pointer.fetchone()

    return result[0] if result else 0

def get_closed_ticket_count():
    get_query = """
        SELECT COUNT(*) FROM Ticket WHERE ticket_status = 'Close'
    """

    pointer.execute(get_query)
    result = pointer.fetchone()

    return result[0] if result else 0

def get_list_of_avail_ITemployees():
    # first query will get the names of it employees that are not on the second sub query
    # second sub query is the same as get pending tickets count
    get_query = """
        SELECT e.employee_username
        FROM Employee e
        WHERE e.employee_type = 1
        AND e.employee_Id NOT IN (
            SELECT th.ticket_Handler
            FROM Ticket t
            JOIN Ticket_History th ON t.ticket_Id = th.ticket_Id
            WHERE t.ticket_status = 'Open' AND th.ticket_Handler IS NOT NULL
        )
    """

    pointer.execute(get_query)
    result = pointer.fetchall()

    return result

def get_topClosers():
    # first query gets each employee's username and how many closed tickets they've handled
        # joins Ticket_History to Ticket to access ticket status
        # joins Employee to trace handler IDs back to usernames
    # second condition filters only the tickets with status 'Closed'
    # groups the results by employee_username and counts how many closed tickets each handled
    # orders the list descending to put the highest count first
    # limits the result to only the top employee (most closed tickets)

    query = """
        SELECT 
            E.employee_username,
            COUNT(*) AS closed_ticket_count
        FROM Ticket_History TH
        INNER JOIN Ticket T ON TH.ticket_Id = T.ticket_Id
        INNER JOIN Employee E ON TH.ticket_Handler = E.employee_Id
        WHERE T.ticket_status = 'Closed'
        GROUP BY E.employee_username
        ORDER BY closed_ticket_count DESC
        LIMIT 1
    """
    pointer.execute(query)
    result = pointer.fetchone()

    return result[0] if result else "No records yet"
