
import customtkinter as ctk
import os
from PIL import Image

from FrontEnd.Dashboard.DashboardMenu_Interface import load_dashboardMenu
from FrontEnd.Tickets.Tickets_Interface import load_ticketsInterface

from BackEnd.SQLiteQueries.DashboardQueries import (
    get_pending_ticket_count,
    get_open_ticket_count,
    get_closed_ticket_count,
    get_list_of_avail_ITemployees
)


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
# backend for menubar | Dashboard_Interface.py
# --------------------------------------------------------- #
def show_menu(
        auth_callback,
        container, barFrame, mainFrame, headerFrame, dContentsFrame
    ):

    if barFrame.winfo_ismapped():
        barFrame.pack_forget()

        # 🧽 Only clear widgets **below** headerFrame
        for widget in mainFrame.winfo_children():
            if widget != headerFrame:
                widget.destroy()

        # First: Clear everything except header
        for widget in mainFrame.winfo_children():
            if widget != headerFrame:
                widget.destroy()

        # Repack header
        headerFrame.pack(side="top", fill="x")

        # Then recreate content area
        contentFrame = ctk.CTkFrame(mainFrame, fg_color="#a5fbff")
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

        tempPendingTicketsIcon = get_backIcon()
        tempOpenTicketsIcon = get_backIcon()
        tempClosedTicketsIcon = get_forwardIcon()

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
            image=tempPendingTicketsIcon,
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

        avail_ITemployeesText = ctk.CTkLabel(
            dashboardContentsFrame,
            text="List of Available IT employees",
            text_color="#000000"
        )
        avail_ITemployeesText.pack(side="top", pady=5)

        row3 = ctk.CTkScrollableFrame(
            dashboardContentsFrame,
            corner_radius=18,
            width=375,
            height=125,
            fg_color="#d2fdff",
            bg_color="#d2fdff",
            scrollbar_fg_color="#b8f3fa",
            scrollbar_button_color="#0097b2"
        )
        row3.pack(side="top", anchor="center", padx=25, pady=10)

        for widget in row3.winfo_children():
            widget.destroy()

        list_of_avail_ITs = get_list_of_avail_ITemployees()

        if list_of_avail_ITs:
            for row in list_of_avail_ITs:
                ITname = ctk.CTkLabel(
                    row3,
                    text=row,
                    text_color="#000000"
                )
                ITname.pack(side="top", anchor="w", pady=(0,5))
        else:
            ITname = ctk.CTkLabel(
                row3,
                text="All IT Employees are currently handling a ticket"
            )
            ITname.pack(side="top", pady=(0,5))

        # Re-create fresh dContentsFrame
        newContentsFrame = ctk.CTkFrame(contentFrame, fg_color="#000000", bg_color="#ffffff")
        newContentsFrame.pack(fill="both", expand=True, padx=25, pady=25)

        # Load default content again
        load_ticketsInterface(newContentsFrame)
    else:
        # 🔵 Switch to sidebar
        headerFrame.pack_forget()  # ← HIDE the header when menu opens

        if not hasattr(barFrame, "loaded") or not barFrame.loaded:
            load_dashboardMenu(
                auth_callback,
                container, barFrame, mainFrame, headerFrame,  # ✅ INCLUDE headerFrame
                lambda: show_menu(
                    auth_callback,
                    container, barFrame, mainFrame, headerFrame, dContentsFrame)
            )
            barFrame.loaded = True

         # Reset main layout order
        barFrame.pack_forget()
        mainFrame.pack_forget()
        barFrame.pack(side="left", fill="y")  # LEFT
        mainFrame.pack(side="left", fill="both", expand=True)  # RIGHT

