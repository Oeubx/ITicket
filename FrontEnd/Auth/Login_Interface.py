
# updated comments

import customtkinter as ctk
import os
from PIL import Image

from BackEnd.Auth.Login_Backend import loginShowPass, loginFunct

def get_refreshIcon(): #no refresh icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "refresh arrow.png")

    refreshIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return refreshIcon

def get_unshowPassIcon(): #no unshow pass icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "unshowPW.png")

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

# --------------------------------------------------------- #
# functions for icons ^^^ | 
# --------------------------------------------------------- #
def load_loginpage(container, authValue, auth_callback):
    #collection of icons
    unshowPass_icon = get_unshowPassIcon()
    email_icon = get_emailIcon()
    pw_icon = get_pwIcon()

    #loginContainer Frame
    lContainerFrame = ctk.CTkFrame(
        container,
        corner_radius=0,
        fg_color="#ffffff"
        )
    lContainerFrame.pack(anchor="center", expand=True, pady=(0,50))

    Login_Text = ctk.CTkLabel(
        lContainerFrame,
        text="Log In",
        font=("Arial", 35), 
        text_color="#0097b2"
        )
    Login_Text.pack(side="top", pady=25)

    #emailframe
    lEmailFrame = ctk.CTkFrame(
        lContainerFrame,
        corner_radius = 15,
        fg_color = "#87CEEB"
        )
    lEmailFrame.pack(side="top", padx=25, pady=(0,25))

    lEmailIcon = ctk.CTkLabel(
        lEmailFrame,
        text="",
        image=email_icon
        )
    lEmailIcon.pack(side="left", padx=(10, 5))

    lEmailEntry = ctk.CTkEntry(
        lEmailFrame,
        width=240,
        border_width=0,
        placeholder_text="Email",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    lEmailEntry.pack(side="left", pady=10, padx=(0,10))

    #passwordframe
    lPasswordFrame = ctk.CTkFrame(
        lContainerFrame,
        corner_radius=15,
        fg_color = "#87CEEB"
        )
    lPasswordFrame.pack(side="top", padx=25, pady=(0,25))

    lPasswordIcon = ctk.CTkLabel(
        lPasswordFrame,
        text="",
        image=pw_icon
        )
    lPasswordIcon.pack(side="left", padx=(10, 5))

    lPasswordEntry = ctk.CTkEntry(
        lPasswordFrame,
        width=200,
        border_width=0,
        show="*",
        placeholder_text="Password",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    lPasswordEntry.pack(side="left", pady=10)

    lPasswordBtnShow = ctk.CTkButton(
        lPasswordFrame,
        text="",
        image=unshowPass_icon,
        width=5,        #update the image icon in the backend when clicked
        command=lambda: loginShowPass(lPasswordEntry, lPasswordBtnShow)
        )
    lPasswordBtnShow.pack(side="left", padx=(5, 10))

    #fp = forgot password
    fpLabelBtn = ctk.CTkLabel(
      lContainerFrame,
      text="Forgot Password?",
      text_color="#0097b2",
      font=("Arial", 12, "italic"),  # Optional: makes it look like a link
      cursor="hand2"  # Changes cursor to hand on hover
    )
    fpLabelBtn.pack(padx=5, pady=5)

    # Bind left-click to trigger the same callback
    fpLabelBtn.bind("<Button-1>", lambda event: auth_callback(container, 1, container))

    #l = login  #incomplete logic yet
    lButton = ctk.CTkButton(
        lContainerFrame,
        width=100,
        text="Login",
        text_color="white",
        command=lambda: auth_callback(container, 3, container)
            if loginFunct(lEmailEntry, lPasswordEntry)
            else None
        )
    lButton.pack(padx=5, pady=5)

    #su = sign up
    #no logic yet
    suLabel = ctk.CTkLabel(
      lContainerFrame,
      text="or Sign Up",
      text_color="#0097b2",
      font=("Arial", 12),  # Optional: underline to make it look like a link
      cursor="hand2"  # Hand cursor on hover
    )
    suLabel.pack(padx=5, pady=(5, 25))

    # Bind left-click to trigger the callback
    suLabel.bind("<Button-1>", lambda event: auth_callback(container, 2, container))

    return container