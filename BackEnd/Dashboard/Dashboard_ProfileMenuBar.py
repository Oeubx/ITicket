
import customtkinter as ctk

from Assets.GradientBg import create_gradient_frame

from FrontEnd.UserProfile.Edit_Profile_Interface import load_Profile
from FrontEnd.UserProfile.MyTickets_Interface import load_MyTickets

def gotoProfile(leftFrame, centerFrame, rightFrame, mainFrame):
    rightFrame.pack(side="left", fill="y", expand=True)
    leftFrame.pack_forget()
    centerFrame.pack_forget()

    ProfileFrame = ctk.CTkFrame(mainFrame)
    ProfileFrame.pack(side="top", fill="both", expand=True)

    ProfileBg = create_gradient_frame(ProfileFrame)
    ProfileBg.pack(fill="both", expand=True)

    load_Profile(ProfileBg)

def gotoMyTickets(leftFrame, centerFrame, rightFrame, mainFrame):
    rightFrame.pack(side="left", fill="y", expand=True)
    leftFrame.pack_forget()
    centerFrame.pack_forget()

    MyTicketsFrame = ctk.CTkFrame(mainFrame)
    MyTicketsFrame.pack(side="top", fill="both", expand=True)

    MyTicketsBg = create_gradient_frame(MyTicketsFrame)
    MyTicketsBg.pack(fill="both", expand=True)

    load_MyTickets(MyTicketsBg)