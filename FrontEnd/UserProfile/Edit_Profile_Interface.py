
import customtkinter as ctk

from Assets.GradientBg import create_gradient_frame

from BackEnd.Dashboard.Dashboard_ProfileBackend import btnAction, btnCancel

from BackEnd.SQLiteQueries.DashboardProfileQueries import get_loggedIn_UsersId, get_userDetails

#pass root page
def load_Profile(frame):
    userId = get_loggedIn_UsersId()
    userDetails = get_userDetails(userId)

    userId = userDetails[0]
    userName = userDetails[1]
    userEmail = userDetails[2]
    userPass = userDetails[3]

    # Header bar
    headerFrame = ctk.CTkFrame(frame)
    headerFrame.pack(side="top", fill="x")

    headerBg = create_gradient_frame(headerFrame)
    headerBg.pack(fill="both", expand=True)

    headerText = ctk.CTkLabel(
        headerBg,
        text="ITicket : Profile",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        height=50,
        bg_color="#cdffd8",
        fg_color="#cdffd8"
    )
    headerText.pack(side="left", anchor="nw", padx=50, pady=(50,25))

    #main holder of everything
    epContentsFrame = ctk.CTkFrame(frame)
    epContentsFrame.pack(side="top", anchor="nw", padx=50, pady=(0,50))

    #username frame
    epUsernameFrame = ctk.CTkFrame(epContentsFrame)
    epUsernameFrame.pack(side="top", anchor="w", padx=25)

    epUsername_Entry = ctk.CTkEntry(
        epUsernameFrame,
        placeholder_text=f"{userName}",
        width = 150
        )
    epUsername_Entry.configure(state="readonly")
    epUsername_Entry.pack(side="left", pady=25, padx=25)

    #email frame
    epEmailFrame = ctk.CTkFrame(epContentsFrame)
    epEmailFrame.pack(side="top", anchor="w", padx=25, pady=25)

    epEmailEntry = ctk.CTkEntry(
        epEmailFrame,
        placeholder_text=f"{userEmail}",
        width = 150
        )
    epEmailEntry.configure(state="readonly")
    epEmailEntry.pack(side="left", pady=25, padx=25)

    #password frame
    epPasswordFrame = ctk.CTkFrame(epContentsFrame)
    #epPasswordFrame.pack(side="top", anchor="nw",padx=25, pady=25)
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
    epBtnFrame = ctk.CTkFrame(epContentsFrame)
    epBtnFrame.pack(side="bottom")

    epCancelBtn = ctk.CTkButton(epBtnFrame)
    epUpdateProfileBtn = ctk.CTkButton(epBtnFrame)

    epCancelBtn.configure(
        text="Cancel",
        command = lambda: btnCancel(
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
                userId, userPass, 
                epCancelBtn, epUpdateProfileBtn,
                epUsername_Entry, epEmailEntry,
                epPasswordFrame, epPasswordEntry, epConfirmPasswordEntry
            )
        )
    epUpdateProfileBtn.pack(side="right", pady=25, padx=25)