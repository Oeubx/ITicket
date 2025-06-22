
import customtkinter as ctk
import bcrypt
import re

from Assets.GradientBg import create_gradient_frame
from BackEnd.SQLiteQueries.DashboardProfileQueries import updateUserCredentials

# --------------------------------------------------------- #
# for profile 
# --------------------------------------------------------- #
def show_TopLevelMessage(message):
    toplevelFrame = ctk.CTkToplevel()
    toplevelFrame.title("Profile Sub Window")
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

def btnAction(
        userId, userPass,
        CancelBtn, btn,
        usernameEntry, emailEntry,
        pwFrame, passwordEntry, confirmPassEntry
    ):

    # if edit profile
    # change their state to normal and the text
    if btn.cget("text") == "Edit Profile":
        usernameEntry.configure(state="normal")
        emailEntry.configure(state="normal")

        pwFrame.pack(side="top", anchor="nw", padx=25, pady=(0, 25))

        CancelBtn.pack(side="left", pady=25, padx=25)
        btn.configure(text="Save Profile")
    else:
        email = emailEntry.get().strip()

        # validates the email to have a <email name><@<any text>><.<.com or .net or anything>>
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            show_TopLevelMessage("Invalid email format!")
            return False

        newPw = passwordEntry.get().strip()
        confirmPw = confirmPassEntry.get().strip()

        # pw validation
        if bcrypt.checkpw(newPw.encode('utf-8'), userPass.encode('utf-8')):
            show_TopLevelMessage("Same Password as your old Password")
        else:
            # Check if either pw field has input
            if newPw and confirmPw:
                if newPw == confirmPw:
                    hashed_pw = hidePw(newPw)
                    successUpdate = updateUserCredentials(userId, hashed_pw)

                    if successUpdate:
                        usernameEntry.configure(state="disabled")
                        emailEntry.configure(state="disabled")

                        passwordEntry.delete(0, 'end')
                        confirmPassEntry.delete(0, 'end')
                        pwFrame.pack_forget()

                        CancelBtn.pack_forget()
                        btn.configure(text="Edit Profile")

                        show_TopLevelMessage("Update Successful")
                    else:
                        show_TopLevelMessage("Update Failed")
                else:
                    show_TopLevelMessage("New password and confirm password do not match.")
            else:
                show_TopLevelMessage("Please enter both password fields.")

def btnCancel(
        CancelBtn, btn,
        usernameEntry, emailEntry,
        pwFrame, passwordEntry, confirmPassEntry,
    ):
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
