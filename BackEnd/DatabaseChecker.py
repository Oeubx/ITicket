
#run this to double check db
from BackEnd.SQLiteQueries.GeneralQueries import (
    SQLiteCall,
    employee_table_creation,
    ticket_table_creation,
    ticket_history_table_creation
)

def check_if_db_exists():
    #runs all this
    SQLiteCall()

    # dw, there will be no duplication
    # added validation
    # IF NOT EXISTS
    # table searcher
    employee_table_creation()
    ticket_table_creation()
    ticket_history_table_creation()

# other stuffs
#insertion_inEmployees()
#insertion_inTicket()
#insertion_inTicketHistory()

#SQLitePrinting_of_employees()
#SQLitePrinting_of_tickets()
#SQLitePrinting_of_ticket_history()

#employees | pls insert newly created accs below

#Prince Amorsolo Remo, remorat@gmail.com, remorat, 1 = IT
#Oeubx, oeubxwaa@gmail.com, oeubxwaa, 0 = non IT