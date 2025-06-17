#signup backend.py
import os
from PIL import Image
import customtkinter as ctk
import bcrypt # to read passwords
import re # for email format

from Assets.GradientBg import create_gradient_frame
from BackEnd.SQLite_Calls import SQLiteCall, get_dbConn

_, pointer = SQLiteCall()
db = get_dbConn()

def show_TopLevelMessage(message):
    toplevelFrame = ctk.CTkToplevel()
    toplevelFrame.title("Sign Up Sub Window")
    toplevelFrame.grab_set()

    gradientFrame = create_gradient_frame(toplevelFrame)
    gradientFrame.pack(fill="both", expand=True)

    textFrame = ctk.CTkFrame(gradientFrame)
    textFrame.pack(side="top", padx=25, pady=(25,0))

    text = ctk.CTkLabel(
        textFrame,
        text=message
    )
    text.pack(padx=10, pady=10)

    CloseBtn = ctk.CTkButton(
        gradientFrame,
        text="Close",
        command=toplevelFrame.destroy  # just closes the top-level window
    )
    CloseBtn.pack(side="top", pady=25)

def hidePw(plain_password):
    # bcrypt requires bytes, so encode the string
    password_bytes = plain_password.encode('utf-8')
    
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # Store hashed as bytes or decode to string for SQLite TEXT column
    return hashed.decode('utf-8')

def signUpFunct(username_entry, password_entry, email_entry, emp_type_holder):
    user = username_entry.get().strip()
    email = email_entry.get().strip()
    pw = password_entry.get().strip()
    emp_type = emp_type_holder.get()

    # validation for empty fields
    empty_fields = []

    if user == "":
        empty_fields.append("Username")
    if email == "":
        empty_fields.append("Email")
    if pw == "":
        empty_fields.append("Password")
    if emp_type not in (0, 1):
        empty_fields.append("Employee Type")

    # Show error if any are empty
    if empty_fields:
        if len(empty_fields) == 1:
            message = f"{empty_fields[0]} field is empty!" if empty_fields[0] != "Employee Type" else "Please select an employee type!"
        else:
            message = f"{', '.join(empty_fields)} field(s) are empty!"
        show_TopLevelMessage(message)
        return False
    # end of validations

    # validates the email to have a <email name><@<any text>><.<.com or .net or anything>>
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        show_TopLevelMessage("Invalid email format!")
        return False
    
    # Check for duplicate email
    pointer.execute("SELECT emp_email FROM Employee WHERE emp_email = ?", (email,))
    if pointer.fetchone() is not None:
        show_TopLevelMessage("Email already exists!")
        return False
    
    # hashes the password
    hashed_password = hidePw(pw)

    # Proceed with sign-up
    signUpQuery = """
                    INSERT INTO Employee 
                        (
                        emp_username,
                        emp_email,
                        emp_password, 
                        emp_type
                        )
                    VALUES (?, ?, ?, ?)
                    """
    pointer.execute(signUpQuery, (user, email, hashed_password, emp_type))
    dbConn = get_dbConn()
    dbConn.commit()

    show_TopLevelMessage("Account successfully created!")
    return True

# --------------------------------------------------------- #
def get_showPassIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "showPW.png")

    showPassIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return showPassIcon

def get_unshowPassIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "unshowPW.png")

    unshowPassIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return unshowPassIcon

def signUpShowPass(entry, button):
    showPass_icon = get_showPassIcon()
    unshowPass_icon = get_unshowPassIcon()

    if entry.cget('show') == "":
        entry.configure(show="*")
        button.configure(image=unshowPass_icon)
    else:
        entry.configure(show="")
        button.configure(image=showPass_icon)
# --------------------------------------------------------- #

#default validation setup lol
"""
if user == "" and email == "" and pw == "" and emp_type not in (0, 1):
    show_TopLevelMessage("All fields are empty!!")
    return False
elif user == "" and email == "" and pw == "":
    show_TopLevelMessage("Username, Email, and Password are empty!")
    return False
elif user == "" and email == "" and emp_type not in (0, 1):
    show_TopLevelMessage("Username, Email, and Employee Type are empty!")
    return False
elif user == "" and pw == "" and emp_type not in (0, 1):
    show_TopLevelMessage("Username, Password, and Employee Type are empty!")
    return False
elif email == "" and pw == "" and emp_type not in (0, 1):
    show_TopLevelMessage("Email, Password, and Employee Type are empty!")
    return False
elif user == "" and email == "":
    show_TopLevelMessage("Username and Email fields are empty!")
    return False
elif user == "" and pw == "":
    show_TopLevelMessage("Username and Password fields are empty!")
    return False
elif user == "" and emp_type not in (0, 1):
    show_TopLevelMessage("Username and Employee Type are empty!")
    return False
elif email == "" and pw == "":
    show_TopLevelMessage("Email and Password fields are empty!")
    return False
elif email == "" and emp_type not in (0, 1):
    show_TopLevelMessage("Email and Employee Type are empty!")
    return False
elif pw == "" and emp_type not in (0, 1):
    show_TopLevelMessage("Password and Employee Type are empty!")
    return False
elif user == "":
    show_TopLevelMessage("Username field is empty!")
    return False
elif email == "":
    show_TopLevelMessage("Email field is empty!")
    return False
elif pw == "":
    show_TopLevelMessage("Password field is empty!")
    return False
elif emp_type not in (0, 1):
    show_TopLevelMessage("Please select an employee type!")
    return False
"""