
# new file
import customtkinter as ctk

# --------------------------------------------------------- #
# backend for menubar contents | DashboardMenu_Interface.py
# --------------------------------------------------------- #
from FrontEnd.Menu.Edit_Profile_Interface import load_Profile
from FrontEnd.Menu.MyTickets_Interface import load_MyTickets

def gotoProfile(mainFrame, headerFrame):
    for widget in mainFrame.winfo_children():
        if widget != headerFrame:
            widget.destroy()

    load_Profile(mainFrame)

def gotoMyTickets(mainFrame, headerFrame):
    for widget in mainFrame.winfo_children():
        if widget != headerFrame:
            widget.destroy()

    load_MyTickets(mainFrame)

# def go to users tickets
# def go to its ticket history
