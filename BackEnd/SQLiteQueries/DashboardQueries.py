
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