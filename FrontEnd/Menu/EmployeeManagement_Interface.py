
import customtkinter as ctk

from BackEnd.ReadfromFile import get_loggedIn_UsersId
from BackEnd.Dashboard.Dashboard_MenuContentsBackend import show_subwindow
from BackEnd.SQLiteQueries.MenuBarContentsQueries import (
    get_AllUsersId,
    get_AllUserCredentials
)

def load_EmployeeManagement(frame):
    userId = get_loggedIn_UsersId()

    managementFrame = ctk.CTkFrame(
        frame,
        fg_color="#d2fdff"
        )
    managementFrame.pack(side="top", fill="both", expand=True)

    # Header bar
    headerFrame = ctk.CTkFrame(
        managementFrame,
        fg_color="#d2fdff"
        )
    headerFrame.pack(side="top", anchor="nw")

    headerText = ctk.CTkLabel(
        headerFrame,
        text="ITicket : Employee Management",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        height=50,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
    )
    headerText.pack(side="left", anchor="nw", padx=50, pady=25)

    #main holder of everything
    contentsFrame = ctk.CTkScrollableFrame(
        managementFrame,
        width=600,
        height=750,
        fg_color="#e9feff",
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
        )
    contentsFrame.pack(side="top", anchor="nw", padx=50, pady=(0,50))

    # create filtering here

    userIds = get_AllUsersId()
    for (userId, ) in userIds:
        #another query here
        userContentHolder = get_AllUserCredentials(userId)
        username, email = userContentHolder

        mainRow = ctk.CTkFrame(
            contentsFrame,
            fg_color="#d2fdff"
        )
        mainRow.pack(side="top", anchor="w", padx=25, pady=(25,10))
        
        row1 = ctk.CTkFrame(
            mainRow,
            fg_color="#d2fdff"
        )
        row1.pack(side="left", anchor="w", padx=25)

        #row1 contents
        usernameLabel = ctk.CTkLabel(
            row1,
            text=username,
            font=("Arial", 25),
            text_color="#000000"
        )
        usernameLabel.pack(side="top", anchor="w", padx=5, pady=5)

        emailLabel = ctk.CTkLabel(
            row1,
            text=email,
            font=("Arial", 15),
            text_color="#000000"
        )
        emailLabel.pack(side="top", anchor="w", padx=5, pady=5)

        editAccount_Btn = ctk.CTkButton(
            row1,
            text="Edit",
            fg_color="#00c2cb",
            text_color="#000000",
            command=lambda uid=userId: show_subwindow("Edit", uid)
            )
        editAccount_Btn.pack(side="bottom", anchor="w", padx=10, pady=10)

        row2 = ctk.CTkFrame(
            mainRow,
            fg_color="#d2fdff"
        )
        row2.pack(side="left", anchor="w", padx=25, pady=(25,10))

        delAccount_Btn = ctk.CTkButton(
            row2,
            text="Delete Account",
            command=lambda uid=userId: show_subwindow("Delete Account", uid),
            width=125,
            height=40,
            font=("Arial", 16),
            fg_color="#00c2cb",
            text_color="#000000"
        )
        delAccount_Btn.pack(side="top", anchor="nw", pady=25)

        delTickets_Btn = ctk.CTkButton(
            row2,
            text="Delete Tickets",
            command=lambda uid=userId: show_subwindow("Delete Tickets", uid),
            width=125,
            height=40,
            font=("Arial", 16),
            fg_color="#00c2cb",
            text_color="#000000"
        )
        delTickets_Btn.pack(side="top", anchor="nw", pady=25)