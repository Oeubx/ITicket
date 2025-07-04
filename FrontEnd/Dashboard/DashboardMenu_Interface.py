
# combined menu and profile contents

import customtkinter as ctk
import os
from PIL import Image

#from BackEnd.Auth.LoggedIn_Acc import logoutUpdateFile
from BackEnd.ReadfromFile import logoutUpdateFile, get_userEmpType
from BackEnd.Dashboard.Dashboard_MenuBackend import (
    gotoProfile,
    gotoMyTickets,
    gotoEmployeeManagement
)

#will update to get_assets
def get_profileIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "profile.png")

    profile_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return profile_icon

def get_arrowBackIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "arrow back.png")

    arrowBack_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return arrowBack_icon

def get_ticketIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "ticket logo.png")

    ticket_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return ticket_icon

# --------------------------------------------------------- #
# functions for icons ^^^ |
# --------------------------------------------------------- #
def load_dashboardMenu(
        auth_callback,
        container, barFrame, mainFrame, headerFrame,
        toggle_callback
    ):

    
    if hasattr(barFrame, "loaded") and barFrame.loaded:
        return  # Already built

    profile_icon = get_profileIcon()
    ticket_icon = get_ticketIcon()

    mHome = ctk.CTkButton(
        barFrame,
        text="Home",
        #image=icon,
        compound="left",
        command=toggle_callback
    )
    mHome.pack(side="top", pady=(25, 0))

    pGoTo_Profile = ctk.CTkButton(
        barFrame,
        text="Profile",
        image=profile_icon,
        compound="left",
        command=lambda: gotoProfile(mainFrame, headerFrame) 
    )
    pGoTo_Profile.pack(side="top", padx=25, pady=(25, 0))

    pGoTo_MyTickets = ctk.CTkButton(
        barFrame,
        text="My Tickets",
        image=ticket_icon,
        compound="left",
        command=lambda: gotoMyTickets(mainFrame, headerFrame) 
    )
    pGoTo_MyTickets.pack(side="top", padx=25, pady=(25, 0))

    manageEmployees = ctk.CTkButton(
        barFrame,
        text="Employee Management",
        image=ticket_icon,
        compound="left",
        command=lambda: gotoEmployeeManagement(mainFrame, headerFrame) 
    )
    user_EmpType = get_userEmpType()
    if user_EmpType == 1 :
        manageEmployees.pack(side="top", padx=25, pady=(25, 0))
    else :
        manageEmployees.pack_forget()

    pLogOut_User = ctk.CTkButton(
        barFrame,
        text="Log Out",
        command=lambda: [
            logoutUpdateFile(),
            auth_callback(container, 0, container)
        ]
    )
    pLogOut_User.pack(side="bottom", anchor="e", padx=25, pady=25)

    barFrame.loaded = True  # Mark as initialized