
# new file
import customtkinter as ctk

# --------------------------------------------------------- #
# backend for menubar contents | DashboardMenu_Interface.py
# --------------------------------------------------------- #
from FrontEnd.Menu.Edit_Profile_Interface import load_Profile
#from FrontEnd.Menu.MyTickets_Interface import load_MyTickets

def gotoProfile(barFrame, mainFrame):
    for widget in mainFrame.winfo_children():
        widget.destroy()

    #mainFrame.pack(side="left", fill="both", expand=True)
    load_Profile(mainFrame)

# def go to users tickets
# def go to its ticket history
