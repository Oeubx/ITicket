
import customtkinter as ctk

from Assets.GradientBg import create_gradient_frame

from BackEnd.Dashboard.Dashboard_MenuContentsBackend import btnAction, btnCancel

from BackEnd.SQLiteQueries.MenuBarContentsQueries import get_loggedIn_UsersId, get_userDetails

def load_Profile(frame):
    userId = get_loggedIn_UsersId()
    userDetails = get_userDetails(userId)

    userId = userDetails[0]
    userName = userDetails[1]
    userEmail = userDetails[2]
    userPass = userDetails[3]

    profileFrame = ctk.CTkFrame(
        frame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    profileFrame.pack(side="top", fill="both", expand=True)

    # Header bar
    headerFrame = ctk.CTkFrame(
        profileFrame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    headerFrame.pack(side="top", anchor="nw")

    headerText = ctk.CTkLabel(
        headerFrame,
        text="ITicket : Profile",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        height=50,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
    )
    headerText.pack(side="left", anchor="nw", padx=50, pady=25)

    #main holder of everything
    epContentsFrame = ctk.CTkFrame(
        profileFrame,
        fg_color="#a5fbff"
        )
    epContentsFrame.pack(side="top", anchor="nw", padx=50, pady=(0,50))

    #username frame
    epUsernameFrame = ctk.CTkFrame(
        epContentsFrame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    epUsernameFrame.pack(side="top", anchor="w")

    epUsername_Entry = ctk.CTkEntry(
        epUsernameFrame,
        width = 150
        )
    epUsername_Entry.insert(0, userName)
    epUsername_Entry.configure(state="readonly")
    epUsername_Entry.pack(side="left", pady=25, padx=25)

    #email frame
    epEmailFrame = ctk.CTkFrame(
        epContentsFrame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    epEmailFrame.pack(side="top", anchor="w")

    epEmailEntry = ctk.CTkEntry(
        epEmailFrame,
        width = 150
        )
    epEmailEntry.insert(0, userEmail)
    epEmailEntry.configure(state="readonly")
    epEmailEntry.pack(side="left", pady=25, padx=25)

    #password frame
    epPasswordFrame = ctk.CTkFrame(
        epContentsFrame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    #epPasswordFrame.pack(side="top", anchor="nw", padx=25, pady=25)
    epPasswordFrame.pack_forget()

    epPasswordEntry = ctk.CTkEntry(
        epPasswordFrame,
        show="*",
        placeholder_text="New Password",
        width = 150
        )
    epPasswordEntry.pack(side="left", pady=25, padx=(25, 0))

    epConfirmPasswordEntry = ctk.CTkEntry(
        epPasswordFrame,
        show="*",
        placeholder_text="Confirm Password",
        width = 150
        )
    epConfirmPasswordEntry.pack(side="left", pady=25, padx=25)

    #button
    epBtnFrame = ctk.CTkFrame(
        epContentsFrame,
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
            )
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
            )
        )
    epUpdateProfileBtn.pack(side="right", pady=25, padx=25)