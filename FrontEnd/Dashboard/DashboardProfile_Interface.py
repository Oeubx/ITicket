
#dashboard profile interface / frontend

import customtkinter as ctk
import os
from PIL import Image

from BackEnd.Auth.LoggedIn_Acc import logoutUpdateFile
from BackEnd.Dashboard.Dashboard_ProfileMenuBar import gotoProfile

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

def get_notificationIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "email.png")

    notification_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return notification_icon

def get_notificationUpdateIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "notification logo.png")

    notificationUpdate_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return notificationUpdate_icon

def load_dashboardProfile(
        profileFrame, profileIconBtn,
        toggle_callback,
        auth_callback, container,
        leftFrame, centerFrame,
        mainFrame
    ):

    if getattr(profileFrame, "loaded", False):
        return

    profile_icon = get_profileIcon()
    arrowBack_icon = get_arrowBackIcon()
    notification_icon = get_notificationIcon()
    notificationUpdate_icon = get_notificationUpdateIcon()

    # Close button
    pClose = ctk.CTkButton(
        profileFrame,
        text="",
        image=arrowBack_icon,
        width = 25,
        command=toggle_callback
    )
    pClose.pack(side="top", anchor="ne", padx=25, pady=(25, 0))

    # Username display (profile access)
    pGoTo_Profile = ctk.CTkButton(
        profileFrame,
        text="Profile",
        image=profile_icon,
        compound="left",
        command = lambda: gotoProfile(leftFrame, centerFrame,
                                      profileFrame, mainFrame)
    )
    pGoTo_Profile.pack(side="top", padx=25, pady=(25, 0))

    # Tickets navigation
    # need backend logic to check
    pGoTo_Tickets = ctk.CTkButton(
        profileFrame,
        text="Notifications",
        image=notification_icon,
        compound="left"
    )
    pGoTo_Tickets.pack(side="top", padx=25, pady=(25, 0))

    pGoTo_TicketHistory = ctk.CTkButton(
        profileFrame,
        text="My Tickets",
        image=profile_icon,
        compound="left"
    )
    pGoTo_TicketHistory.pack(side="top", padx=25, pady=(25, 0))

    # Log out
    pLogOut_User = ctk.CTkButton(
        profileFrame,
        text="Log Out",
        command=lambda: [
            logoutUpdateFile(),
            auth_callback(container, 0, container)
        ]
    )
    pLogOut_User.pack(side="bottom", anchor="e", padx=25, pady=25)

    profileFrame.loaded = True