
# updated top level message

import os
from PIL import Image
import customtkinter as ctk
import bcrypt #to read passwords

# accesses the queries necessary
from BackEnd.SQLiteQueries.AuthQueries import fetch_user_credentials_by_email, update_user_password_by_email

def show_TopLevelMessage(message):
    toplevelFrame = ctk.CTkToplevel()
    toplevelFrame.title("Forgot Password Sub Window")
    toplevelFrame.grab_set()

    main_container_frame = ctk.CTkFrame(
        toplevelFrame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    main_container_frame.pack(fill="both", expand=True)

    contentsHolder_Frame = ctk.CTkFrame(
        main_container_frame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
    )
    contentsHolder_Frame.pack(anchor="center", padx=25, pady=25)

    textFrame = ctk.CTkFrame(contentsHolder_Frame)
    textFrame.pack(side="top", padx=25, pady=(25,0))

    text = ctk.CTkLabel(
        textFrame,
        text=message
    )
    text.pack(padx=10, pady=10)

    CloseBtn = ctk.CTkButton(
        contentsHolder_Frame,
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

def forgotPassFunct(email_entry, password_entry):
    # validations if entry fields are empty
    userEntry_IsEmpty = email_entry.get().strip() == ""
    pwEntry_IsEmpty = password_entry.get().strip() == ""

    if userEntry_IsEmpty and pwEntry_IsEmpty:
        show_TopLevelMessage("Email and Password fields are empty!!")
        return False
    elif userEntry_IsEmpty:
        show_TopLevelMessage("Email field is empty!")
        return False
    elif pwEntry_IsEmpty:
        show_TopLevelMessage("Password field is empty!")
        return False

    #receives it while passing necessary widgets
    email_pass = fetch_user_credentials_by_email(email_entry)

    # returns None if there's no matching email in DB
    if email_pass is None:
        show_TopLevelMessage("Email not found!")
        return False

    plain_pw = password_entry.get().strip().encode('utf-8')
    hashed_pw = email_pass[1].encode('utf-8')

    # check if user entered the same old password
    if bcrypt.checkpw(plain_pw, hashed_pw):
        show_TopLevelMessage("That's your old password?!")
        return True
    else:
        # hash the new password and update it in DB
        hashed_password = hidePw(password_entry.get().strip())
        #receives it while passing necessary widgets
        pwUpdate_success = update_user_password_by_email(hashed_password, email_pass[0])

    # password update success
    if pwUpdate_success :
        show_TopLevelMessage("Password successfully updated!")
        return True
    else :
        # password update success
        show_TopLevelMessage("Error updating password!")
        return False

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

def forgotShowPass(entry, button):
    showPass_icon = get_showPassIcon()
    unshowPass_icon = get_unshowPassIcon()

    if entry.cget('show') == "":
        entry.configure(show="*")
        button.configure(image=unshowPass_icon)
    else:
        entry.configure(show="")
        button.configure(image=showPass_icon)