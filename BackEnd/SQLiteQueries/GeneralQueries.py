
# fixed comments
# updated emp to employee

#general queries.py

import sqlite3 as sql
import bcrypt

_dbConn = None
_pointer = None

#from datetime import datetime   #for date n time of ticket
#curr_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# file stuffs
#project_folder = os.path.dirname(os.path.abspath(__file__))
#filePointer = r"C:\BIBOYstuffs\\CODES\\PYTHON CODES\\ITicket\BackEnd\Auth\\previously_logged_in_details.txt"


def SQLiteCall():
    global _dbConn, _pointer
    if _dbConn is None:
        db_path = "C:/BIBOYstuffs/CODES/PYTHON CODES/ITicket/BackEnd/ITicket.db"
        _dbConn = sql.connect(db_path)
        _pointer = _dbConn.cursor()
        _dbConn.commit()
    return _dbConn, _pointer

#optimized selection
def get_dbConn():
    return SQLiteCall()[0]  # get db connection for commits

def get_pointer():
    return SQLiteCall()[1]  # get db pointer
    
# --------------------------------------------------------- #
# queries for others
# --------------------------------------------------------- #
def hidePw(plain_password):
    # bcrypt requires bytes, so encode the string
    password_bytes = plain_password.encode('utf-8')
    
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # Store hashed as bytes or decode to string for SQLite TEXT column
    return hashed.decode('utf-8')

def getEmpName_fromDb(id): #id of the passed employee
    _, pointer = SQLiteCall()
    getDetails = "SELECT employee_username FROM Employee WHERE employee_Id = ?"

    pointer.execute(getDetails, (id,))
    empUsername = pointer.fetchone()
    
    return empUsername[0]

# --------------------------------------------------------- #
# validation for db commits
"""
    try:
        pointer.execute(query_string, (values, othervalues... ) )
        dbConn.commit()
        return True     # if success
    except Exception as e:
        #for debugging
        #print("Failed to insert data:", e)
        return False
"""
# --------------------------------------------------------- #

# --------------------------------------------------------- #
# queries for table creation
# --------------------------------------------------------- #
def employee_table_creation():
    dbConn, pointer = SQLiteCall()

    # changed sequence id - uname - email - pass - type //0, 1 for IT
    creation="""
        CREATE TABLE IF NOT EXISTS Employee (
            employee_Id INTEGER PRIMARY KEY AUTOINCREMENT
            ,employee_username TEXT NOT NULL
            ,employee_email TEXT NOT NULL
            ,employee_password TEXT NOT NULL
            ,employee_type INTEGER NOT NULL
        )
    """
    pointer.execute(creation)
    dbConn.commit()

    print("employee table creation test")

def ticket_table_creation():
    dbConn, pointer = SQLiteCall()

    # ticket status = closed or open
    # ticket level = Inquiry, Non-Urgent, Urgent
    creation="""
        CREATE TABLE IF NOT EXISTS Ticket (
            ticket_Id INTEGER PRIMARY KEY AUTOINCREMENT
            ,ticket_title TEXT NOT NULL
            ,ticket_desc TEXT NOT NULL
            ,ticket_status TEXT NOT NULL DEFAULT 'Open'
            ,ticket_level TEXT NOT NULL
            ,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            ,submitted_by INTEGER NOT NULL
            ,FOREIGN KEY (submitted_by) REFERENCES Employee(employee_Id)
        );
    """
    pointer.execute(creation)
    dbConn.commit()

    print("ticket table creation test")

def ticket_history_table_creation():
    dbConn, pointer = SQLiteCall()

    creation="""
        CREATE TABLE IF NOT EXISTS Ticket_History (
            ticket_history_Id INTEGER PRIMARY KEY AUTOINCREMENT
            ,ticket_Id INTEGER NOT NULL
            ,ticket_Handler INTEGER NULL
            ,update_Description TEXT NOT NULL
            ,update_Date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            ,FOREIGN KEY (ticket_Id) REFERENCES Ticket(ticket_Id)
            ,FOREIGN KEY (ticket_Handler) REFERENCES Employee(employee_Id)
        );
    """
    pointer.execute(creation)
    dbConn.commit()

    print("ticket history table creation test")

# --------------------------------------------------------- #
# queries for insertion of values
# --------------------------------------------------------- #
def insertion_inEmployees():
    dbConn, pointer = SQLiteCall()

    insertion = """
        INSERT INTO Employee (
            employee_username
            ,employee_email
            ,employee_password
            ,employee_type
        )
        VALUES (?, ?, ?, ?)    
    """

    # First account
    value1a = "Prince Amorsolo Remo"
    value2a = "remorat@gmail.com"
    value3a = hidePw("remorat")
    value4a = 1  # IT

    # Second account
    value1b = "Oeubx"
    value2b = "oeubxwaa@gmail.com"
    value3b = hidePw("oeubxwaa")
    value4b = 0  # non-IT

    # Insert both
    pointer.execute(insertion, (value1a, value2a, value3a, value4a))
    pointer.execute(insertion, (value1b, value2b, value3b, value4b))

    dbConn.commit()
    print("Successfully inserted 2 employee accounts")

def insertion_inTicket():#
    dbConn, pointer = SQLiteCall()

    insertion = """
        INSERT INTO Ticket (
            ticket_title
            ,ticket_desc
            ,ticket_level
            ,submitted_by
            )
        VALUES (?, ?, ?, ?, ?, ?)    
    """
    
    #values to insert
    value0 = "TICKET TITLE 1"
    value1 = "DESCRIPTION for id insertion1"
    value2 = "Inquiry"
    value3 = 1 #emp id of user who submitted the tix

    pointer.execute(insertion, (
        value0, value1, value2, value3)
        )
    dbConn.commit()

    print("success insertion in ticket")

def insertion_inTicketHistory():
    dbConn, pointer = SQLiteCall()

    insertion = """
        INSERT INTO Ticket_History (
            ticket_id
            ,ticket_Handler
            ,update_Description   
            )
        VALUES (?, ?, ?, ?)    
    """
    
    #values to insert
    value1 = 1 #ticket id
    value2 = None
    value3 = "no updated desc yet"

    pointer.execute(insertion,
                    (value1, value2, value3)
                    )
    dbConn.commit()

    print("success insertion in ticket history")

# --------------------------------------------------------- #
# queries printing of contents
# --------------------------------------------------------- #
def SQLitePrinting_of_employees():
    _, pointer = SQLiteCall()
    #should change this later
    pointer.execute("SELECT * FROM Employee")
    tableContentHolder = pointer.fetchall()

    for row in tableContentHolder:
        print(f"{row}")

def SQLitePrinting_of_tickets():
    _, pointer = SQLiteCall()
    pointer.execute("SELECT * FROM Ticket")
    ticket_table_contentHolder = pointer.fetchall()

    for row in ticket_table_contentHolder:
        print(f"{row}")

def SQLitePrinting_of_ticket_history():
    _, pointer = SQLiteCall()
    pointer.execute("SELECT * FROM Ticket_History")
    ticketHistory_table_contentHolder = pointer.fetchall()

    for row in ticketHistory_table_contentHolder:
        print(f"{row}") 