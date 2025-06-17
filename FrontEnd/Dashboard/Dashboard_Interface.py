#dashboard_interface.py

#imports
import os
import customtkinter as ctk
from PIL import Image

#module imports
from FrontEnd.Tickets.Tickets_Interface import load_ticketsInterface
from BackEnd.Dashboard.Dashboard_Backend import show_menu, show_ProfileMenu

###########################################################################
#icons
def get_menuIcon():
    # Get the absolute path to the icon
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "menu.png")
    # Load image and wrap it in CTkImage

    icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return icon

def get_profileIcon():
    # Get the absolute path to the icon
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "profile.png")
    # Load image and wrap it in CTkImage

    icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return icon

###########################################################################
#main
def load_dashboard(container, authValue, auth_callback):
    #collection of icons
    menuIcon = get_menuIcon()
    profileIcon = get_profileIcon()

    #menu frame
    menuFrame = ctk.CTkFrame(container)
    menuFrame.pack(side="left", fill="y")
    menuFrame.pack_forget()

    #contents of menu frame
    menuIconBtn = ctk.CTkButton(container)

    #frame for whatever the contents is
    dContentsFrame = ctk.CTkFrame(
        container,
        fg_color="#ffffff"
        )
    load_ticketsInterface(dContentsFrame)
    dContentsFrame.pack()
    dContentsFrame.pack_forget()

    #mini profile frame
    profileFrame = ctk.CTkFrame(container)
    profileFrame.pack(side="left", fill="y")
    profileFrame.pack_forget()

    #contents of profile frame
    profileIconBtn = ctk.CTkButton(container)

    #configuring the contents
    menuIconBtn.configure(
        text="", 
        image=menuIcon,
        width=40, 
        height=40,
        fg_color="transparent",
        hover_color="#000000",
        command=lambda: show_menu(menuFrame, menuIconBtn,
                                  dContentsFrame,
                                  profileFrame, profileIconBtn)
    )
    
    profileIconBtn.configure(
        text="", 
        image=profileIcon,
        width=40, 
        height=40,
        fg_color="transparent",
        hover_color="#000000",
        command=lambda: show_ProfileMenu(
            profileFrame, profileIconBtn, auth_callback, container
            )
    )
    
    #printing the three
    menuIconBtn.pack(side="left", anchor="nw", pady=25, padx=25)
    dContentsFrame.pack(side="left", fill="both", expand=True, pady=25, padx=25)
    profileIconBtn.pack(side="left", anchor="ne", pady=25, padx=25)