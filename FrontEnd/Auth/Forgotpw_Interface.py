
# updated comments

import customtkinter as ctk
import os
from PIL import Image

from BackEnd.Auth.Forgotpw_Backend import show_TopLevelMessage, forgotPassFunct, forgotShowPass

#takes the icons
def get_backIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "arrow back.png")

    backIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return backIcon

def get_unshowPassIcon(): #no unshow pass icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "refresh arrow.png")

    unshowPassIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return unshowPassIcon

def get_emailIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "email.png")

    emailIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return emailIcon

def get_pwIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "password.png")

    pwIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return pwIcon
#end of functions for the icons

# --------------------------------------------------------- #
# functions for icons ^^^ | 
# --------------------------------------------------------- #
def load_forgotpwpage(container, authValue, auth_callback):
    #collection of icons
    back_icon = get_backIcon()
    unshowPass_icon = get_unshowPassIcon()
    email_icon = get_emailIcon()
    pw_icon = get_pwIcon()

    #forgot password Container Frame
    fpContainerFrame = ctk.CTkFrame(
        container,
        corner_radius=15,
        fg_color="#ffffff"
        )
    fpContainerFrame.pack(anchor="center", expand=True, pady=(0,50))

    #auth passing frame
    fpCloseBtn = ctk.CTkButton(
        fpContainerFrame,
        text="Back to Login Page ?",
        image=back_icon,
        compound="left",
        width=20,
        command=lambda: auth_callback(container, 0, container)
    )
    fpCloseBtn.pack(side="top", anchor="n", pady=(15,0))

    ForgotPw_Text = ctk.CTkLabel(
        fpContainerFrame,
        text="Forgot Password",
        font=("Arial", 35), 
        text_color="#0097b2"
        )
    ForgotPw_Text.pack(side="top", pady=25)

    #email frame
    fpEmailFrame = ctk.CTkFrame(
        fpContainerFrame,
        corner_radius=15,
        fg_color = "#87CEEB"
        )
    fpEmailFrame.pack(side="top", padx=25, pady=(0,25))

    fpEmailIcon = ctk.CTkLabel(
        fpEmailFrame,
        text="",
        image=email_icon
        )
    fpEmailIcon.pack(side="left", padx=(10, 5))

    fpEmailEntry = ctk.CTkEntry(
        fpEmailFrame,
        width=240,
        border_width=0,
        placeholder_text="Email",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    fpEmailEntry.pack(side="left", pady=10)

    #password frame
    fpPasswordFrame = ctk.CTkFrame(
        fpContainerFrame,
        corner_radius=15,
        fg_color = "#87CEEB"
        )
    fpPasswordFrame.pack(side="top", padx=25, pady=(0,25))

    fpPasswordIcon = ctk.CTkLabel(
        fpPasswordFrame,
        text="",
        image=pw_icon
        )
    fpPasswordIcon.pack(side="left", padx=(10, 5))

    fpPasswordEntry = ctk.CTkEntry(
        fpPasswordFrame,
        width=200,
        border_width=0,
        show="*",
        placeholder_text="Password",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    fpPasswordEntry.pack(side="left", pady=10)

    fpPasswordBtnToShow = ctk.CTkButton(
        fpPasswordFrame,
        text="",
        image=unshowPass_icon,
        width=5,        #update the image icon in the backend when clicked
        command=lambda: forgotShowPass(fpPasswordEntry, fpPasswordBtnToShow)
        )
    fpPasswordBtnToShow.pack(side="left", padx=(5, 10))

    #forgot pw button
    fpButton = ctk.CTkButton(
        fpContainerFrame,
        text="Update Password",
        command=lambda: auth_callback(container, 0, container)
            if forgotPassFunct(fpEmailEntry, fpPasswordEntry)
            else None
    )
    fpButton.pack(side="bottom", anchor="e", padx=25, pady=25)

    return container
#end of main page ----------------------------------------------- #