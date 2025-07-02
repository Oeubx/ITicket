
import customtkinter as ctk
import bcrypt
import re

from Assets.GradientBg import create_gradient_frame
from BackEnd.SQLiteQueries.MenuBarContentsQueries import *

# --------------------------------------------------------- #
# for profile 
# --------------------------------------------------------- #
def show_TopLevelMessage(message):
    toplevelFrame = ctk.CTkToplevel()
    toplevelFrame.title("Profile Sub Window")
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

def btnAction(
        headerText,
        userId, userPass,
        CancelBtn, btn,
        usernameEntry, emailEntry,
        pwFrame, passwordEntry, confirmPassEntry
    ):
    headerText.configure(text="ITicket : Edit Profile")

    # if edit profile
    # change their state to normal and the text
    if btn.cget("text") == "Edit Profile":
        usernameEntry.configure(state="normal")
        emailEntry.configure(state="normal")

        pwFrame.pack(side="top", anchor="nw")

        CancelBtn.pack(side="left", pady=25, padx=25)
        btn.configure(text="Save Profile")
    else:
        #necessary queries
        user_Name = get_userName(userId)[0].strip()
        user_Email = get_userEmail(userId)[0].strip()

        username = usernameEntry.get().strip()
        email = emailEntry.get().strip()
        newPw = passwordEntry.get().strip()
        confirmPw = confirmPassEntry.get().strip()

        # Track what changed
        usernameIsChanged = username.lower() != user_Name.lower()
        emailIsChanged = email.lower() != user_Email.lower()
        pwIsChanged = newPw and newPw != "" and not bcrypt.checkpw(newPw.encode('utf-8'), userPass.encode('utf-8'))

        # Validate username if changed
        if usernameIsChanged:
            if not username.isalpha():
                show_TopLevelMessage("Username must contain only letters.")
                return
            if len(username) > 25:
                show_TopLevelMessage("Username must not exceed 25 characters.")
                return

        # Validate email if changed
        if emailIsChanged:
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, email):
                show_TopLevelMessage("Invalid email format!")
                return

        # Validate password if attempted
        if newPw or confirmPw:
            if not pwIsChanged:
                show_TopLevelMessage("Newly Inputted Password is your old Password")
                return
            if newPw != confirmPw:
                show_TopLevelMessage("New password and confirm password do not match.")
                return

        # Update only what changed
        if usernameIsChanged:
            updateUserName(userId, username)

        if emailIsChanged:
            updateUserEmail(userId, email)

        if pwIsChanged:
            hashed_pw = hidePw(newPw)
            successUpdate = updateUserPass(userId, hashed_pw)
            if not successUpdate:
                show_TopLevelMessage("Password update failed.")
                return

        # If any update occurred, reflect UI changes
        if usernameIsChanged or emailIsChanged or pwIsChanged:
            usernameEntry.configure(state="disabled")
            emailEntry.configure(state="disabled")
            passwordEntry.delete(0, 'end')
            confirmPassEntry.delete(0, 'end')
            pwFrame.pack_forget()
            CancelBtn.pack_forget()
            btn.configure(text="Edit Profile")
            show_TopLevelMessage("Update Successful")
        else:
            show_TopLevelMessage("No changes detected.")

def btnCancel(
        headerText,
        CancelBtn, btn,
        usernameEntry, emailEntry,
        pwFrame, passwordEntry, confirmPassEntry,
    ):
    headerText.configure(text="ITicket : Profile")

    usernameEntry.configure(state="disabled")
    emailEntry.configure(state="disabled")

    passwordEntry.delete(0, 'end')
    confirmPassEntry.delete(0, 'end')
    pwFrame.pack_forget()

    CancelBtn.pack_forget()
    btn.configure(text="Edit Profile")

# --------------------------------------------------------- #
# for password verification
# --------------------------------------------------------- #

# --------------------------------------------------------- #
# for email verification 
# --------------------------------------------------------- #

# --------------------------------------------------------- #
# for button 
# --------------------------------------------------------- #
