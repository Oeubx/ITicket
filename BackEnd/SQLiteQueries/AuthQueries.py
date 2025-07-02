
# updated emp into employee

#auth queries.py
from BackEnd.SQLiteQueries.GeneralQueries import SQLiteCall

dbConn, pointer = SQLiteCall()

# --------------------------------------------------------- #
# queries for login | Login_Backend.py
# --------------------------------------------------------- #
def fetch_all_login_credentials():
    pointer.execute("""
                    SELECT
                        employee_Id 
                        ,employee_email 
                        ,employee_password 
                    FROM Employee
                    """
                    )
    userContentsHolder = pointer.fetchall()

    return userContentsHolder

# --------------------------------------------------------- #
# queries for forgot password | Forgotpw_Backend.py
# --------------------------------------------------------- #
def fetch_user_credentials_by_email(email_entry):
    query = "SELECT employee_email, employee_password FROM Employee WHERE employee_email = ?"

    pointer.execute(query, (email_entry.get().strip(), ) )
    # email_pass[0] to access the email
    # email_pass[1] to access the password
    email_pass = pointer.fetchone()

    return email_pass

def update_user_password_by_email(hashed_password, email):
    updatePassQuery = "UPDATE Employee SET employee_password = ? WHERE employee_email = ?"

    #short validation
    try:
        pointer.execute(updatePassQuery, (hashed_password, email) )
        dbConn.commit()
        return True     # if success
    except Exception as e:
        #for debugging
        #print("Failed to insert data:", e)
        return False

# --------------------------------------------------------- #
# queries for sign up | Signup_Backend.py
# --------------------------------------------------------- #
def check_emailDuplicates_by_email(email):
    pointer.execute("SELECT employee_email FROM Employee WHERE employee_email = ?", (email, ) )
    emailDuplicate_checket = pointer.fetchone()

    return emailDuplicate_checket

def sign_user_credentials(
        user, email, hashed_password, emp_type
    ):
    # Proceed with sign-up
    signUpQuery = """
                    INSERT INTO Employee 
                        (
                        employee_username
                        ,employee_email
                        ,employee_password
                        ,employee_type
                        )
                    VALUES (?, ?, ?, ?)
                    """
    
    #short validation
    try:
        pointer.execute(signUpQuery, (user, email, hashed_password, emp_type))
        dbConn.commit()
        return True     # if success
    except Exception as e:
        #for debugging
        #print("Failed to insert data:", e)
        return False
    
# --------------------------------------------------------- #
#
# --------------------------------------------------------- #