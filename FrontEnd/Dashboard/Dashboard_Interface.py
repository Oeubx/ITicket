
# updated comments, removed gradient frame, fixed packing errors

#imports
import os
import customtkinter as ctk
from PIL import Image

#module imports
from FrontEnd.Tickets.Tickets_Interface import load_ticketsInterface
from BackEnd.Dashboard.Dashboard_Backend import show_menu

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

# --------------------------------------------------------- #
# functions for icons ^^^
# --------------------------------------------------------- #
def load_dashboard(container, authValue, auth_callback):
    menuIcon = get_menuIcon()
    profileIcon = get_profileIcon()

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
    contentFrame = ctk.CTkFrame(
        mainFrame,
        fg_color= "#a5fbff",
        bg_color= "#a5fbff"
        )
    contentFrame.pack(side="top", fill="both", expand=True)

    # pass this for contents
    dContentsFrame = ctk.CTkFrame(
        contentFrame,
        fg_color= "#000000",
        bg_color= "#ffffff"
        )
    dContentsFrame.pack(fill="both", expand=True, padx=25, pady=25)

    load_ticketsInterface(dContentsFrame)