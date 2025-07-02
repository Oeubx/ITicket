
import customtkinter as ctk

from Assets.GradientBg import create_gradient_frame

#from BackEnd.Dashboard.Dashboard_ProfileBackend import btnAction, btnCancel

#from BackEnd.SQLiteQueries.DashboardProfileQueries import get_loggedIn_UsersId

#pass root page
def load_MyTickets(frame):
    # queries here

    #header frame TEXT
    # Header bar
    headerFrame = ctk.CTkFrame(frame)
    headerFrame.pack(side="top", fill="x")

    headerBg = create_gradient_frame(headerFrame)
    headerBg.pack(fill="both", expand=True)

    headerText = ctk.CTkLabel(
        headerBg,
        text="ITicket : My Tickets",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        height=50,
        bg_color="#cdffd8",
        fg_color="#cdffd8"
    )
    headerText.pack(side="top", anchor="w", padx=50, pady=(50,25))

    #main holder of everything
    tContentsFrame = ctk.CTkFrame(frame)
    tContentsFrame.pack(side="top", anchor="nw", padx=50, pady=(0,50))

    