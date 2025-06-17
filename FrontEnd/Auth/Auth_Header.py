import customtkinter as ctk
import os
from PIL import Image

def get_iticketIcon(): #no refresh icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "main logo.png")

    iticketIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return iticketIcon

def load_authHeader(container):
    iticket_icon = get_iticketIcon()

    ITicketLogo = ctk.CTkLabel(
        container,
        text="",
        image=iticket_icon
        )
    ITicketLogo.pack(side="left", anchor="n", padx=(25, 0), pady=25)

    #awaiting design
    AboutUs = ctk.CTkButton(container, text="About Us")
    AboutUs.pack(side="right", anchor="n", padx=(0, 25), pady=25)

    #text
    textFrame = ctk.CTkFrame(container, fg_color="transparent")
    textFrame.pack(side="top", pady=(75, 25), anchor="n")

    welcomeTextLabel1 = ctk.CTkLabel(
        textFrame,
        text="Welcome to ",
        text_color="#000000"
    )
    welcomeTextLabel1.pack(side="left")

    welcomeTextLabel2 = ctk.CTkLabel(
        textFrame,
        text="ITicket",
        text_color="#6c6c6c"
    )
    welcomeTextLabel2.pack(side="left")

    welcome_SubTextLabel = ctk.CTkLabel(container, text="subtext")
    welcome_SubTextLabel.pack(side="top", pady=(0,50))

    #return ITicketLogo, AboutUs, welcomeTextLabel1, welcomeTextLabel2, welcome_SubTextLabel