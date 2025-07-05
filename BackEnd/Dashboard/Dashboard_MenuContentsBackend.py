
import customtkinter as ctk
import bcrypt
import re

from BackEnd.ReadfromFile import get_loggedIn_UsersId
from BackEnd.SQLiteQueries.MenuBarContentsQueries import  get_userDetails

from BackEnd.SQLiteQueries.MenuBarContentsQueries import (
    get_userName,
    get_userEmail,
    updateUserName,
    updateUserEmail,
    updateUserPass,
    del_AllRelatedToAcc,
    del_AllTicketsOfThisUser,
    del_SpecificTicketsOfThisUser,
    get_ThisUsersTickets
)

# --------------------------------------------------------- #
# for profile 
# --------------------------------------------------------- #
def show_TopLevelMessage(message, userId):
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
# for employee management
# --------------------------------------------------------- #
def show_subwindow(value, userId):
    managementWindow = ctk.CTkToplevel()
    managementWindow.title("Employee Management")
    managementWindow.grab_set()

    main_container_frame = ctk.CTkFrame(
        managementWindow,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    main_container_frame.pack(fill="both", expand=True)

    contentsHolder_Frame = ctk.CTkFrame(
        main_container_frame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
    )
    contentsHolder_Frame.pack(fill="both", expand=True, anchor="center", padx=25, pady=25)

    if value == "Edit":
        headerText = ctk.CTkLabel(
            contentsHolder_Frame,
            text="ITicket : Profile",
            text_color="#000000",
            font=("Arial", 32, "bold"),
            height=50,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
        )
        headerText.pack(side="top", anchor="nw", padx=50, pady=25)

        #userId = get_loggedIn_UsersId()
        userDetails = get_userDetails(userId)

        userId = userDetails[0]
        userName = userDetails[1]
        userEmail = userDetails[2]
        userPass = userDetails[3]

        #username frame
        epUsernameFrame = ctk.CTkFrame(
            contentsHolder_Frame,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
            )
        epUsernameFrame.pack(side="top", anchor="w")

        epUsername_Entry = ctk.CTkEntry(
            epUsernameFrame,
            width = 150,
            fg_color="#e9feff",
            placeholder_text_color="#000000",
            text_color="#000000"
            )
        epUsername_Entry.insert(0, userName)
        epUsername_Entry.configure(state="readonly")
        epUsername_Entry.pack(side="left", pady=25, padx=25)

        #email frame
        epEmailFrame = ctk.CTkFrame(
            contentsHolder_Frame,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
            )
        epEmailFrame.pack(side="top", anchor="w")

        epEmailEntry = ctk.CTkEntry(
            epEmailFrame,
            width = 150,
            fg_color="#e9feff",
            placeholder_text_color="#000000",
            text_color="#000000"
            )
        epEmailEntry.insert(0, userEmail)
        epEmailEntry.configure(state="readonly")
        epEmailEntry.pack(side="left", pady=25, padx=25)

        #password frame
        epPasswordFrame = ctk.CTkFrame(
            contentsHolder_Frame,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
            )
        #epPasswordFrame.pack(side="top", anchor="nw", padx=25, pady=25)
        epPasswordFrame.pack_forget()

        epPasswordEntry = ctk.CTkEntry(
            epPasswordFrame,
            show="*",
            placeholder_text="New Password",
            width = 150,
            fg_color="#e9feff",
            placeholder_text_color="#000000",
            text_color="#000000"
            )
        epPasswordEntry.pack(side="left", pady=25, padx=(25, 0))

        epConfirmPasswordEntry = ctk.CTkEntry(
            epPasswordFrame,
            show="*",
            placeholder_text="Confirm Password",
            width = 150,
            fg_color="#e9feff",
            placeholder_text_color="#000000",
            text_color="#000000"
            )
        epConfirmPasswordEntry.pack(side="left", pady=25, padx=25)

        #button
        epBtnFrame = ctk.CTkFrame(
            contentsHolder_Frame,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
            )
        epBtnFrame.pack(side="bottom")

        epCancelBtn = ctk.CTkButton(epBtnFrame)
        epUpdateProfileBtn = ctk.CTkButton(epBtnFrame)

        epCancelBtn.configure(
            text="Cancel",
            command = lambda: btnCancel(
                    headerText,
                    epCancelBtn, epUpdateProfileBtn,
                    epUsername_Entry, epEmailEntry,
                    epPasswordFrame, epPasswordEntry, epConfirmPasswordEntry
                ),
            text_color="#FFFFFF"
        )
        #epCancelBtn.pack(side="left", pady=25, padx=25)
        epCancelBtn.pack_forget()

        epUpdateProfileBtn.configure(
            text="Edit Profile", #and then change it to Save Profile
            command=lambda : btnAction(
                    headerText,
                    userId, userPass, 
                    epCancelBtn, epUpdateProfileBtn,
                    epUsername_Entry, epEmailEntry,
                    epPasswordFrame, epPasswordEntry, epConfirmPasswordEntry
                ),
            text_color="#FFFFFF"
            )
        epUpdateProfileBtn.pack(side="right", pady=25, padx=25)
    #
    elif value == "Delete Account":
        headerText = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Employee Account | Deletion",
            text_color="#000000",
            font=("Arial", 32, "bold"),
            height=50,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
        )
        headerText.pack(side="top", anchor="w", padx=50, pady=25)

        warningText1 = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Are you sure you want to delete this account?",
            text_color="#000000"
        )
        warningText1.pack(side="top", anchor="w", padx=25, pady=(25, 5))

        warningText2 = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Everything under this account will be deleted:",
            text_color="#000000"
        )
        warningText2.pack(side="top", anchor="w", padx=25, pady=(0, 5))

        warningText3 = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Account, Tickets, Ticket History (if applicable)",
            text_color="#000000"
        )
        warningText3.pack(side="top", anchor="w", padx=25, pady=(0, 15))

        buttonFrame = ctk.CTkFrame(
            contentsHolder_Frame,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
        )
        buttonFrame.pack(side="top", anchor="w", padx=25, pady=(10, 15))

        proceed_btn = ctk.CTkButton(
            buttonFrame,
            text="Proceed",
            command=lambda: del_AllRelatedToAcc(userId)
        )
        proceed_btn.pack(side="left", padx=5, pady=5)

        cancel_btn = ctk.CTkButton(
            buttonFrame,
            text="Cancel",
            command=managementWindow.destroy
        )
        cancel_btn.pack(side="left", padx=5, pady=5)
    #
    elif value == "Delete Tickets":
        headerText = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Employee's Ticket | Deletion",
            text_color="#000000",
            font=("Arial", 32, "bold"),
            height=50,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
        )
        headerText.pack(side="top", anchor="w", padx=50, pady=25)

        warningText = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Are you sure you want to delete tickets associated with this account?",
            text_color="#000000"
        )
        warningText.pack(side="top", anchor="w", padx=25, pady=(25, 5))

        warningText2 = ctk.CTkLabel(
            contentsHolder_Frame,
            text="Changes are irreversible once clicked. Proceed with caution.",
            text_color="#000000"
        )
        warningText2.pack(side="top", anchor="w", padx=25, pady=(0, 15))

        buttonFrame = ctk.CTkFrame(
            contentsHolder_Frame,
            fg_color="#a5fbff",
            bg_color="#a5fbff"
        )
        buttonFrame.pack(side="top", anchor="w", padx=25, pady=(10, 15))

        def load_ticket_option_buttons():
            buttonFrame2 = ctk.CTkFrame(
                contentsHolder_Frame,
                fg_color="#a5fbff",
                bg_color="#a5fbff"
            )
            buttonFrame2.pack(side="top", anchor="w", pady=(5, 15))

            def handle_all_tickets(userId):
                del_AllTicketsOfThisUser(userId)
                managementWindow.destroy()

            def show_specific_tickets(userId):
                scrollable_frame = ctk.CTkScrollableFrame(
                    contentsHolder_Frame,
                    width=400,
                    height=400,
                    fg_color="#e9feff",
                    scrollbar_fg_color="#b8f3fa",
                    scrollbar_button_color="#0097b2"
                )
                scrollable_frame.pack(side="top", padx=20, fill="both", expand=True)

                ticket_ContentsHolder = get_ThisUsersTickets(userId)

                if not ticket_ContentsHolder:
                    ctk.CTkLabel(scrollable_frame, text="No tickets found.", text_color="#000000").pack(pady=20)
                    return

                for row in ticket_ContentsHolder:
                    ticketId, title, status, level, created_at, submitterName = row

                    tContentFrame = ctk.CTkFrame(scrollable_frame, fg_color="#d2fdff")
                    tContentFrame.pack(side="top", fill="x", expand=True, padx=(0, 15), pady=15)

                    ticket_LeftFrame = ctk.CTkFrame(tContentFrame, fg_color="#d2fdff")
                    ticket_LeftFrame.pack(side="left", anchor="w", padx=25, pady=25)

                    ticket_frame = ctk.CTkFrame(tContentFrame, fg_color="#d2fdff")
                    ticket_frame.pack(side="right", anchor="e", padx=25, pady=25)

                    ticket_headerFrame = ctk.CTkFrame(ticket_LeftFrame, fg_color="#d2fdff")
                    ticket_headerFrame.pack(side="top", anchor="w")

                    ctk.CTkLabel(ticket_headerFrame, text=f"{submitterName} | ", font=("Arial", 16, "bold"), text_color="#000000").pack(side="left")
                    ctk.CTkLabel(ticket_headerFrame, text=f"{title} | ", font=("Arial", 16, "bold"), text_color="#000000").pack(side="left")
                    ctk.CTkLabel(ticket_headerFrame, text=f"{level}", font=("Arial", 16, "bold"), text_color="#000000").pack(side="left")

                    ticket_subFrame = ctk.CTkFrame(ticket_LeftFrame, fg_color="#d2fdff")
                    ticket_subFrame.pack(side="top", anchor="w")

                    ctk.CTkLabel(ticket_subFrame, text=f"Created at {created_at} | ", text_color="#000000").pack(side="left")

                    ctk.CTkLabel(ticket_frame, text=f"{status}", text_color="#000000", fg_color="#d2fdff").pack(side="top", pady=5)

                    del_thisTicket_Btn = ctk.CTkButton(
                        ticket_frame,
                        text="Delete Ticket",
                        text_color="#000000",
                        fg_color="#00c2cb",
                        command=lambda tid=ticketId: del_SpecificTicketsOfThisUser(tid)
                    )
                    del_thisTicket_Btn.pack(side="top")

            # Configure button options
            allTickets_btn = ctk.CTkButton(
                buttonFrame2,
                text="Delete All Tickets",
                command= lambda: handle_all_tickets(userId)
            )
            specificTicket_btn = ctk.CTkButton(
                buttonFrame2,
                text="Select Specific Tickets",
                command= lambda: show_specific_tickets(userId)
            )

            allTickets_btn.pack(side="left", padx=10, pady=5)
            specificTicket_btn.pack(side="left", padx=10, pady=5)

        # Proceed/Cancel buttons
        proceed_btn = ctk.CTkButton(
            buttonFrame,
            text="Proceed",
            command=load_ticket_option_buttons
        )
        proceed_btn.pack(side="left", padx=5, pady=5)

        cancel_btn = ctk.CTkButton(
            buttonFrame,
            text="Cancel",
            command=managementWindow.destroy
        )
        cancel_btn.pack(side="left", padx=5, pady=5)
