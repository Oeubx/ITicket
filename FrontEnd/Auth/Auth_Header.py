
# changed fg, bg color

import customtkinter as ctk
import os
from PIL import Image

def get_iticketIcon(): #no refresh icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "main logo.png")

        # Load and resize image
    original_image = Image.open(icon_path)
    resized_image = original_image.resize((120, 120))  # Adjust size as needed

    # Return CTkImage object
    iticketIcon = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(120, 120))

    #iticketIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
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
    ITicketLogo.pack(side="left", anchor="n", padx=(25, 0), pady=25)

    #awaiting design
    # needs command that will redirect to frontend about us
    AboutUs = ctk.CTkButton(
        headerFrame,
        text="About Us",
        fg_color= "#0059ff",
        bg_color= "#a5fbff"
    )
    AboutUs.pack(side="right", anchor="n", padx=(0, 25), pady=(65,0))

    #text
    textFrame1 = ctk.CTkFrame(container, fg_color="transparent")
    textFrame1.pack(side="top", anchor="n", pady=(25,0))

    textFrame2 = ctk.CTkFrame(container, fg_color="transparent")
    textFrame2.pack(side="top", anchor="n", pady=(0,25))

    welcomeTextLabel1 = ctk.CTkLabel(
        textFrame1,
        text="Welcome to ",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        fg_color= "#a5fbff",
        bg_color= "#a5fbff",
        height=50
    )
    welcomeTextLabel1.pack(side="left")

    welcomeTextLabel2 = ctk.CTkLabel(
        textFrame1,
        text="ITicket",
        text_color="#6c6c6c",
        font=("Arial", 32, "bold"),
        fg_color= "#a5fbff",
        bg_color= "#a5fbff",
        height=50
    )
    welcomeTextLabel2.pack(side="left")

    welcome_SubTextLabel1 = ctk.CTkLabel(
        textFrame2,
        text="An efficient, simple way to report IT issues and get faster support",
        fg_color= "#a5fbff",
        bg_color= "#a5fbff",
        )
    welcome_SubTextLabel1.pack(side="top", pady=5)

    welcome_SubTextLabel1 = ctk.CTkLabel(
        textFrame2,
        text="—streamline your workflow with ITicket. "
    )
    welcome_SubTextLabel1.pack(side="top")