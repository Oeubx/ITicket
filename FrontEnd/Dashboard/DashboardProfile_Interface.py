import customtkinter as ctk
import os
from PIL import Image

from BackEnd.Auth.LoggedIn_Acc import logoutUpdateFile, getUserDetails

#will update to get_assets
def get_profileIcon():
    # Get the absolute path to the icon
    current_dir = os.path.dirname(__file__)  # = /path/to/frontend/dashboard
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "profile.png")
    # Load image and wrap it in CTkImage

    profile_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return profile_icon

def load_dashboardProfile(
        profileFrame, profileIconBtn,
        toggle_callback, auth_callback,
        container):
    #collection of icons
    profile_icon = get_profileIcon()

    # Prevent double creation
    if getattr(profileFrame, "loaded", False):
        return
    
    userDetails = getUserDetails() 
    emp_username = userDetails[1]

    #contents of profile frame
    pClose = ctk.CTkButton(
        profileFrame,
        text="Close",
        image=profile_icon, #temp icon
        compound="left",  # image on the left, text on the right
        command=toggle_callback
    )
    pClose.pack(side="top", padx=25, pady=(25,0))

    #p = profile
    #pUser = ctk.CTkButton(
    #    profileFrame,
    #    text="<username>",
    #    image=profile_icon, #temp icon
    #    compound="left"  # image on the left, text on the right
    #)
    #pUser.pack(side="top", padx=25, pady=(25,0))

    pGoTo_Profile = ctk.CTkButton(
        profileFrame,
        text=emp_username,
        image=profile_icon, #temp icon
        compound="left"  # image on the left, text on the right
    )
    pGoTo_Profile.pack(side="top", padx=25, pady=(25,0))

    pGoTo_Tickets = ctk.CTkButton(
        profileFrame,
        text="Tickets",
        image=profile_icon, #temp icon
        compound="left"  # image on the left, text on the right
    )
    pGoTo_Tickets.pack(side="top", padx=25, pady=(25,0))

    pGoTo_TicketHistory = ctk.CTkButton(
        profileFrame,
        text="Ticket History",
        image=profile_icon, #temp icon
        compound="left"  # image on the left, text on the right
    )
    pGoTo_TicketHistory.pack(side="top", padx=25, pady=(25,0))

    #
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