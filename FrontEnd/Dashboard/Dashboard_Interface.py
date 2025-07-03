
# updated comments, removed gradient frame, fixed packing errors

#imports
import os
import customtkinter as ctk
from PIL import Image

#module imports
from FrontEnd.Tickets.Tickets_Interface import load_ticketsInterface
from BackEnd.Dashboard.Dashboard_Backend import show_menu
from BackEnd.SQLiteQueries.DashboardQueries import (
    get_pending_ticket_count,
    get_open_ticket_count,
    get_closed_ticket_count,
    get_list_of_avail_ITemployees,
    get_topClosers
)

###########################################################################
#icons
def get_menuIcon():
    # Get the absolute path to the icon
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "menu.png")
    # Load image and wrap it in CTkImage

    icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return icon

def get_backIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "arrow back.png")

    backIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return backIcon

def get_forwardIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "arrow forward.png")

    backIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return backIcon

# --------------------------------------------------------- #
# functions for icons ^^^
# --------------------------------------------------------- #
def load_dashboard(container, authValue, auth_callback):
    menuIcon = get_menuIcon()

    tempPendingTicketsIcon = get_backIcon()
    tempOpenTicketsIcon = get_backIcon()
    tempClosedTicketsIcon = get_forwardIcon()

    dashboardMainFrame = ctk.CTkFrame(container)
    dashboardMainFrame.pack(fill="both", expand=True)

    # bar frame (menu)
    barFrame = ctk.CTkFrame(
        dashboardMainFrame,
        fg_color= "white",
        bg_color= "white"
        )
    barFrame.pack_forget()  # Initially hidden

    # Center frame (main contents)
    mainFrame = ctk.CTkFrame(
        dashboardMainFrame,
        fg_color= "#a5fbff",
        bg_color= "#a5fbff"
        )
    mainFrame.pack(side="left", fill="both", expand=True)

    # Header frame for menu button
    headerFrame = ctk.CTkFrame(
        mainFrame,
        fg_color= "#a5fbff",
        bg_color= "#a5fbff"
        )
    headerFrame.pack(side="top", fill="x")

    # Header button
    menuIconBtn = ctk.CTkButton(headerFrame)

    menuIconBtn.configure(
        text="",
        image=menuIcon,
        width=40, height=40,
        fg_color="transparent",
        hover_color="#000000",
        # dashboard backend
        command=lambda: show_menu(
            auth_callback,
            container, barFrame, mainFrame,
            headerFrame, dContentsFrame  # ✅ INCLUDE headerFrame
        )
    )

    menuIconBtn.pack(side="left", anchor="nw", pady=25, padx=25)

    # Main content frame
    contentFrame =  ctk.CTkScrollableFrame(
        mainFrame,
        width=400,
        height=400,
        fg_color= "#a5fbff",
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
        )
    contentFrame.pack(side="top", fill="both", expand=True)

    dashboardContentsFrame = ctk.CTkFrame(
        contentFrame,
        fg_color= "#a5fbff"
    )
    dashboardContentsFrame.pack(fill="both", expand=True, padx=25, pady=25)

    row1 = ctk.CTkFrame(
        dashboardContentsFrame
    )
    row1.pack(side="top", padx=25)

    welcomeTextLabel1 = ctk.CTkLabel(
        row1,
        text="Welcome to ",
        text_color="#000000",
        font=("Arial", 50, "bold"),
        bg_color= "#a5fbff",
        height=60
    )
    welcomeTextLabel1.pack(side="left")

    welcomeTextLabel2 = ctk.CTkLabel(
        row1,
        text="ITicket",
        text_color="#6c6c6c",
        font=("Arial", 50, "bold"), 
        fg_color= "#a5fbff",
        bg_color= "#a5fbff",
        height=60
    )
    welcomeTextLabel2.pack(side="left")

    # Container frame for ticket stats
    row2 = ctk.CTkFrame(
        dashboardContentsFrame,
        fg_color="#a5fbff"
    )
    row2.pack(side="top", padx=25, pady=10)

    pendingTickets_Count = get_pending_ticket_count()
    openTickets_Count = get_open_ticket_count()
    closedTickets_Count = get_closed_ticket_count()

    pendingTickets = ctk.CTkLabel(
        row2,
        text=f"Pending Tickets : {pendingTickets_Count}",
        image=tempClosedTicketsIcon,
        compound="left",
        text_color="#000000"
    )
    pendingTickets.pack(side="left", anchor="n", padx=(0,25))

    openTickets = ctk.CTkLabel(
        row2,
        text=f"Open Tickets : {openTickets_Count}",
        image=tempOpenTicketsIcon,
        compound="left",
        text_color="#000000"
    )
    openTickets.pack(side="left", anchor="n", padx=(0,25))

    closedTickets = ctk.CTkLabel(
        row2,
        text=f"Closed Tickets : {closedTickets_Count}",
        image=tempClosedTicketsIcon,
        compound="left",
        text_color="#000000"
    )
    closedTickets.pack(side="left", anchor="n", padx=(0,25))

    row3 = ctk.CTkFrame(
        dashboardContentsFrame,
        fg_color="#a5fbff"
    )
    row3.pack(side="top", padx=25, pady=10)

    closedTickets_Count = get_topClosers()

    mostTicketsClosed = ctk.CTkLabel(
        row3,
        text=f"Employee with most tickets handled and closed : {closedTickets_Count}",
        image=tempClosedTicketsIcon,
        compound="left",
        text_color="#000000"
    )
    mostTicketsClosed.pack(side="left", anchor="n", padx=(0,25))

    avail_ITemployeesText = ctk.CTkLabel(
        dashboardContentsFrame,
        text="List of Available IT employees",
        text_color="#000000"
    )
    avail_ITemployeesText.pack(side="top", pady=5)

    row4 = ctk.CTkScrollableFrame(
        dashboardContentsFrame,
        corner_radius=18,
        width=375,
        height=125,
        fg_color="#d2fdff",
        bg_color="#d2fdff",
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
    )
    row4.pack(side="top", anchor="center", padx=25, pady=10)

    for widget in row4.winfo_children():
        widget.destroy()

    list_of_avail_ITs = get_list_of_avail_ITemployees()

    if list_of_avail_ITs:
        for row in list_of_avail_ITs:
            ITname = ctk.CTkLabel(
                row4,
                text=row,
                text_color="#000000"
            )
            ITname.pack(side="top", anchor="w", pady=(0,5))
    else:
        ITname = ctk.CTkLabel(
            row4,
            text="All IT Employees are currently handling a ticket"
        )
        ITname.pack(side="top", pady=(0,5))

    # pass this for contents
    dContentsFrame = ctk.CTkFrame(
        contentFrame,
        fg_color= "#000000",
        bg_color= "#ffffff"
        )
    dContentsFrame.pack(fill="both", expand=True, padx=25, pady=25)

    # ticketing system
    load_ticketsInterface(dContentsFrame)