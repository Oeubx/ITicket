
# changed fg, bg color

import customtkinter as ctk
import os
from PIL import Image

from FrontEnd.AboutUs_Interface import load_AboutUs

def get_iticketIcon(): #no refresh icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "main logo.png")

    # Load and resize image
    original_image = Image.open(icon_path)
    resized_image = original_image.resize((150, 150))  # ← was 120x120, increased by 25%

    # Return CTkImage object
    iticketIcon = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(150, 150))  # ← updated size

    return iticketIcon

def load_authHeader(container):
    iticket_icon = get_iticketIcon()

    headerFrame = ctk.CTkFrame(container, fg_color="transparent")
    headerFrame.pack(side="top", anchor="n", fill="x")

    ITicketLogo = ctk.CTkLabel(
        headerFrame,
        text="",
        image=iticket_icon,
        bg_color= "#a5fbff",
        )
    ITicketLogo.pack(side="left", anchor="n", padx=(30, 0), pady=30)

    #awaiting design
    # needs command that will redirect to frontend about us
    AboutUs = ctk.CTkLabel(
        headerFrame,
        text="About Us",
        bg_color= "#a5fbff",
        width=125,
        height=40,
        font=("Arial", 16),
        cursor="hand2",
        text_color="#666666"
    )
    AboutUs.pack(side="right", anchor="n", padx=(0, 40), pady=(75, 0))  # ← was 30, added more right padding
    AboutUs.bind("<Button-1>", lambda event: load_AboutUs())

    #text
    textFrame1 = ctk.CTkFrame(container, fg_color="transparent")
    textFrame1.pack(side="top", anchor="n", pady=(30,0))

    textFrame2 = ctk.CTkFrame(container, fg_color="transparent")
    textFrame2.pack(side="top", anchor="n", pady=(0,30))

    welcomeTextLabel1 = ctk.CTkLabel(
        textFrame1,
        text="Welcome to ",
        text_color="#000000",
        font=("Arial", 50, "bold"),
        bg_color= "#a5fbff",
        height=60
    )
    welcomeTextLabel1.pack(side="left")

    welcomeTextLabel2 = ctk.CTkLabel(
        textFrame1,
        text="ITicket",
        text_color="#6c6c6c",
        font=("Arial", 50, "bold"), 
        fg_color= "#a5fbff",
        bg_color= "#a5fbff",
        height=60
    )
    welcomeTextLabel2.pack(side="left")

    welcome_SubTextLabel1 = ctk.CTkLabel(
        textFrame2,
        text="An efficient, simple way to report IT issues and get faster support",
        font=("Arial", 25),
        fg_color= "#a5fbff",
        bg_color= "#a5fbff",
        text_color="#666666"
        )
    welcome_SubTextLabel1.pack(side="top", pady=(15,6), padx=25)

    welcome_SubTextLabel2 = ctk.CTkLabel(
        textFrame2,
        text="—streamline your workflow with ITicket. ",
        font=("Arial", 25),
        text_color="#666666"
    )
    welcome_SubTextLabel2.pack(side="top")