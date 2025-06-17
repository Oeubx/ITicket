#sqlite calls file

import sqlite3 as sql
import bcrypt
from datetime import datetime   #for date n time

_dbConn = None
_pointer = None

curr_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def SQLiteCall():
    global _dbConn, _pointer
    if _dbConn is None:
        db_path = "C:/BIBOYstuffs/CODES/PYTHON CODES/ITicket/BackEnd/ITicket.db"
        _dbConn = sql.connect(db_path)
        _pointer = _dbConn.cursor()
        _dbConn.commit()
    return _dbConn, _pointer

def get_dbConn():
    db, _ = SQLiteCall()
    return db

import bcrypt

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
    getDetails = "SELECT emp_username FROM Employee WHERE emp_Id = ?"

    pointer.execute(getDetails, (id,))
    empUsername = pointer.fetchone()
    
    return empUsername[0]

##############################################################################
#for table creation
def employee_table_creation():
    dbConn, pointer = SQLiteCall()

    # changed sequence id - uname - email - pass - type //0, 1 for IT
    creation="""
        CREATE TABLE IF NOT EXISTS Employee (
            emp_Id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_username TEXT,
            emp_email TEXT,
            emp_password TEXT,
            emp_type INTEGER
        )
    """
    pointer.execute(creation)
    dbConn.commit()

    print("employee table creation test")

def ticket_table_creation():
    dbConn, pointer = SQLiteCall()

    # ticket status = closed or open
    # ticket level = 0 for inquiry, 1 for non urgent, 2 for urgent
    creation="""
        CREATE TABLE IF NOT EXISTS Ticket (
            ticket_Id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_title TEXT,
            ticket_desc TEXT,
            ticket_status INTEGER,
            ticket_level INTEGER,
            created_at TEXT,
            submitted_by INTEGER,
            FOREIGN KEY (submitted_by) REFERENCES Employee(emp_Id)
        );
    """
    pointer.execute(creation)
    dbConn.commit()

    print("ticket table creation test")

def ticket_history_table_creation():
    dbConn, pointer = SQLiteCall()

    creation="""
        CREATE TABLE IF NOT EXISTS Ticket_History (
            ticket_history_Id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_Id INTEGER,
            ticket_Handler INTEGER,
            update_Description TEXT,
            update_Date TEXT,
            FOREIGN KEY (ticket_Id) REFERENCES Ticket(ticket_Id),
            FOREIGN KEY (ticket_Handler) REFERENCES Employee(emp_Id)
        );
    """
    pointer.execute(creation)
    dbConn.commit()

    print("ticket history table creation test")

##############################################################################
#insertion of values
def insertion_inEmployees():
    dbConn, pointer = SQLiteCall()

    # have to update this goddamn it
    insertion = """
        INSERT INTO Employee (
        emp_username,
        emp_email,
        emp_password,
        emp_type
        )
        VALUES (?, ?, ?, ?)    
    """
    
    #values to insert
    value1 = "Oeubx"
    value2 = "oeubxwaa@gmail.com"
    value3 = hidePw("oeubxwaa")
    value4 = 0    #0 for non IT, #1 for IT

    pointer.execute(insertion,
                    (value1, value2, value3, value4)
                    )
    dbConn.commit()

    print("success insertion in employee")

def insertion_inTicket():#
    dbConn, pointer = SQLiteCall()

    insertion = """
        INSERT INTO Ticket (
            ticket_title,
            ticket_desc,
            ticket_status,
            ticket_level,
            created_at,
            submitted_by
            )
        VALUES (?, ?, ?, ?, ?, ?)    
    """
    
    #values to insert
    value0 = "TICKET TITLE 1"
    value1 = "DESCRIPTION for id insertion1"
    value2 = 0 #0 for open, 1 for close
    value3 = 1 #0 for inquiry, 1 for nonurgent, 2 for urgent
    value4 = curr_dateTime
    value5 = 1 #emp id of user who submitted the tix

    pointer.execute(insertion, (
        value0, value1, value2, value3, value4, value5)
        )
    dbConn.commit()

    print("success insertion in ticket")

def insertion_inTicketHistory():
    dbConn, pointer = SQLiteCall()

    insertion = """
        INSERT INTO Ticket_History (
            ticket_id,
            ticket_Handler,
            update_Description,
            update_Date           
            )
        VALUES (?, ?, ?, ?)    
    """
    
    #values to insert
    value1 = 1 #ticket id
    value2 = None
    value3 = "no updated desc yet"
    value4 = None #passes None so db will read it as NULL

    pointer.execute(insertion,
                    (value1, value2, value3, value4)
                    )
    dbConn.commit()

    print("success insertion in ticket history")

##############################################################################
#printing of contents
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