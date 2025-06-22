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

    ITicketLogo = ctk.CTkLabel(
        container,
        text="",
        image=iticket_icon,
        bg_color="#cdffd8"
        )
    ITicketLogo.pack(side="left", anchor="n", padx=(25, 0), pady=25)

    #awaiting design
    AboutUs = ctk.CTkButton(
        container,
        text="About Us",
        fg_color="#0059ff",
        bg_color="#94b9ff"
    )
    AboutUs.pack(side="right", anchor="n", padx=(0, 25), pady=25)

    #text
    textFrame = ctk.CTkFrame(container, fg_color="transparent")
    textFrame.pack(side="top", pady=(75, 25), anchor="n")

    welcomeTextLabel1 = ctk.CTkLabel(
        textFrame,
        text="Welcome to ",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        fg_color="#f0f0f0",
        height=50
    )
    welcomeTextLabel1.pack(side="left")

    welcomeTextLabel2 = ctk.CTkLabel(
        textFrame,
        text="ITicket",
        text_color="#6c6c6c",
        font=("Arial", 32, "bold"),
        fg_color="#f0f0f0",
        height=50
    )
    welcomeTextLabel2.pack(side="left")

    welcome_SubTextLabel1 = ctk.CTkLabel(
        container,
        text="A smart, simple way to report IT issues and get faster support"
        )
    welcome_SubTextLabel1.pack(side="top", pady=5)

    welcome_SubTextLabel1 = ctk.CTkLabel(
        container,
        text="—streamline your workflow with ITicket. "
    )
    welcome_SubTextLabel1.pack(side="top", pady=(0,50))

    #return ITicketLogo, AboutUs, welcomeTextLabel1, welcomeTextLabel2, welcome_SubTextLabel