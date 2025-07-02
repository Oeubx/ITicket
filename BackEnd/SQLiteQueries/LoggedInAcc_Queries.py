
# new file

# queries for logged in user.py
from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# --------------------------------------------------------- #
# queries for Logged in Account | LoggedIn_Acc.py
# --------------------------------------------------------- #
def fetch_all_user_credentials(id):
    pointer.execute("SELECT * FROM Employee WHERE employee_Id = ?", (id, ) )
    userContentsHolder = pointer.fetchone()

    return userContentsHolder