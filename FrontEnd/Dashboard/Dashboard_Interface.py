#dashboard_interface.py

#imports
import os
import customtkinter as ctk
from PIL import Image

#module imports
from Assets.GradientBg import create_gradient_frame
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
    menuIcon = get_menuIcon()
    profileIcon = get_profileIcon()

    dashboardMainFrame = ctk.CTkFrame(container)
    dashboardMainFrame.pack(side="top", fill="both", expand=True)

    dashboardBg = create_gradient_frame(dashboardMainFrame)
    dashboardBg.pack(fill="both", expand=True)

    # Left frame (menu)
    leftFrame = ctk.CTkFrame(dashboardBg)
    leftFrame.pack_forget()  # Initially hidden

    # Center frame (main contents)
    centerFrame = ctk.CTkFrame(dashboardBg)
    centerBg = create_gradient_frame(centerFrame)
    centerBg.pack(fill="both", expand=True)
    centerFrame.pack(side="left", fill="both", expand=True)

    # Right frame (profile)
    rightFrame = ctk.CTkFrame(dashboardBg)
    rightFrame.pack_forget()  # Initially hidden

    # Header bar
    headerFrame = ctk.CTkFrame(centerBg)
    headerFrame.pack(side="top", fill="x")

    headerBg = create_gradient_frame(headerFrame)
    headerBg.pack(fill="both", expand=True)

    # Header buttons
    menuIconBtn = ctk.CTkButton(headerBg)
    profileIconBtn = ctk.CTkButton(headerBg)

    menuIconBtn.configure(
        text="",
        image=menuIcon,
        width=40, height=40,
        fg_color="transparent",
        hover_color="#000000",
        command=lambda: show_menu(leftFrame, menuIconBtn,
                                  centerFrame,
                                  rightFrame, profileIconBtn)
    )
    profileIconBtn.configure(
        text="",
        image=profileIcon,
        width=40, height=40,
        fg_color="transparent",
        hover_color="#000000",
        command=lambda: show_ProfileMenu(leftFrame, menuIconBtn,
                                        centerFrame,
                                        rightFrame, profileIconBtn,
                                        auth_callback, container,
                                        dashboardMainFrame
                                        )
    )

    menuIconBtn.pack(side="left", anchor="nw", pady=25, padx=25)
    profileIconBtn.pack(side="right", anchor="ne", pady=25, padx=25)

    # Main content frame
    contentFrame = ctk.CTkFrame(centerBg)
    contentFrame.pack(side="top", fill="both", expand=True)

    contentBg = create_gradient_frame(contentFrame)
    contentBg.pack(fill="both", expand=True)

    dContentsFrame = ctk.CTkFrame(contentBg, fg_color="#ffffff")
    dContentsFrame.pack(fill="both", expand=True, padx=25, pady=25)