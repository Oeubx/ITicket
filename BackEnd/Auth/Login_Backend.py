
# updated top level message

import os
from PIL import Image
import customtkinter as ctk
import bcrypt #to read passwords

from BackEnd.Auth.LoggedIn_Acc import loginUpdateFile

# accesses the queries necessary
from BackEnd.SQLiteQueries.AuthQueries import fetch_all_login_credentials

def show_TopLevelMessage(message):
    #login error pop up widget
    toplevelFrame = ctk.CTkToplevel()
    toplevelFrame.title("Login Error")
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

def loginFunct(email_entry, password_entry):
    #receives it
    userContentsHolder = fetch_all_login_credentials()

    # simpler and shorter method of check validation
    if not userContentsHolder:
        show_TopLevelMessage("No user data found.")
        return False

    #is true if its empty
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
    
    emailCorrect = False
    pwCorrect = False

    #if not = if it has contents
    for id, email, hashed_password in userContentsHolder:
        if email == email_entry.get():
            emailCorrect = True

            # compare plain input with hashed password from db
            plain_pw = password_entry.get().strip().encode('utf-8')  # <-- bcrypt needs bytes
            hashed_pw = hashed_password.encode('utf-8')  # <-- convert db TEXT to bytes

            #returns true if equal
            if bcrypt.checkpw(plain_pw, hashed_pw):  # <-- bcrypt password check
                pwCorrect = True
                # saves the id of the user in the func
                loginUpdateFile(id)
                return True  # valid login

    # if email or password didn't match
    if not emailCorrect:
        show_TopLevelMessage("Wrong email!")
    elif not pwCorrect:
        show_TopLevelMessage("Wrong password!")
    else:
        show_TopLevelMessage("Unknown error!!?")

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

def loginShowPass(entry, button):
    showPass_icon = get_showPassIcon()
    unshowPass_icon = get_unshowPassIcon()

    if entry.cget('show') == "":
        entry.configure(show="*")
        button.configure(image=unshowPass_icon)
    else:
        entry.configure(show="")
        button.configure(image=showPass_icon)