#sign up UI
import customtkinter as ctk
import os
from PIL import Image

from BackEnd.Auth.Signup_Backend import signUpFunct, signUpShowPass

def get_backIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "arrow back.png")

    backIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return backIcon

def get_showPassIcon(): #no show pass icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "showPW.png")

    showPassIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return showPassIcon

def get_unshowPassIcon(): #no unshow pass icon yet
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "unshowPW.png")

    unshowPassIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return unshowPassIcon

def get_userIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "blue profile.png")

    userIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return userIcon

def get_emailIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "email.png")

    emailIcon = ctk.CTkImage(Image.open(icon_path), size=(30, 30))
    return emailIcon

def get_pwIcon():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "password.png")

    pwIcon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))
    return pwIcon

def load_signuppage(container, authValue, auth_callback):
    #collection of icons
    back_icon = get_backIcon()
    showPass_icon = get_showPassIcon()
    unshowPass_icon = get_unshowPassIcon()
    user_icon = get_userIcon()
    email_icon = get_emailIcon()
    pw_icon = get_pwIcon()

    #signupContainer Frame
    suContainerFrame = ctk.CTkFrame(
        container,
        corner_radius=0,
        fg_color="#ffffff"
        )
    suContainerFrame.pack(expand=True, pady=(0,50))

    #auth passing frame
    suCloseBtn = ctk.CTkButton(
        suContainerFrame,
        text="Back to Login Page ?",
        image=back_icon,
        compound="left",
        width=20,
        command=lambda: auth_callback(container, 0, container)
    )
    suCloseBtn.pack(side="top", anchor="n", pady=(15,0))

    SignUp_Text = ctk.CTkLabel(
        suContainerFrame,
        text="Sign Up",
        font=("Arial", 35), 
        text_color="#0097b2"
        )
    SignUp_Text.pack(side="top", pady=25)

    #username frame
    suUsernameFrame = ctk.CTkFrame(
        suContainerFrame,
        corner_radius=15,
        fg_color = "#87CEEB"
        )
    suUsernameFrame.pack(side="top", padx=25, pady=(0,25))

    suUsernameIcon = ctk.CTkLabel(
        suUsernameFrame,
        text="",
        image=user_icon
        )
    suUsernameIcon.pack(side="left", padx=(10, 5))

    suUsernameEntry = ctk.CTkEntry(
        suUsernameFrame,
        width=240,
        border_width=0,
        placeholder_text="Username",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    suUsernameEntry.pack(side="left", pady=10)

    #employee frame
    suEmailFrame = ctk.CTkFrame(
        suContainerFrame,
        corner_radius=15,
        fg_color = "#87CEEB"
        )
    suEmailFrame.pack(side="top", padx=25, pady=(0,25))

    suEmployeeEmailIcon = ctk.CTkLabel(
        suEmailFrame,
        text="",
        image=email_icon
        )
    suEmployeeEmailIcon.pack(side="left", padx=(10, 5))

    suEmployeeEmailEntry = ctk.CTkEntry(
        suEmailFrame,
        width=225,
        border_width=0,
        placeholder_text="Email",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    suEmployeeEmailEntry.pack(side="left", pady=10, padx=(5,10))

    #password frame
    suPasswordFrame = ctk.CTkFrame(
        suContainerFrame,
        corner_radius=15,
        fg_color = "#87CEEB"
        )
    suPasswordFrame.pack(side="top", padx=25, pady=(0,25))

    suPasswordIcon = ctk.CTkLabel(
        suPasswordFrame,
        text="",
        image=pw_icon
        )
    suPasswordIcon.pack(side="left", padx=(10, 5))

    suPasswordEntry = ctk.CTkEntry(
        suPasswordFrame,
        width=200,
        border_width=0,
        show="*",
        placeholder_text="Password",
        text_color="#000000",
        placeholder_text_color="#0097b2",
        fg_color = "#87CEEB"
        )
    suPasswordEntry.pack(side="left", pady=10)

    suPasswordBtnToShow = ctk.CTkButton(
        suPasswordFrame,
        text="",
        image=unshowPass_icon,
        width=5,        #update the image icon in the backend when clicked
        command=lambda: signUpShowPass(suPasswordEntry, suPasswordBtnToShow)
        )
    suPasswordBtnToShow.pack(side="left", padx=(5,10))

    #employee type frame
    suEmployeeTypeFrame = ctk.CTkFrame(
        suContainerFrame,
        corner_radius = 15,
        fg_color = "#87CEEB"
        )
    suEmployeeTypeFrame.pack(side="top", padx=10, pady=10)

    suEmployeeTypeVarHolder = ctk.IntVar()
    suEmployeeTypeVarHolder.set(value=-1)

    suEmployeeTypeText = ctk.CTkLabel(
        suEmployeeTypeFrame,
        text="Employee Type : ",
        text_color= "#0097b2"
        )
    suEmployeeTypeText.pack(side="top", padx=10, pady=(10,5))

    suEmployeeTypeButton0 = ctk.CTkRadioButton(
        suEmployeeTypeFrame,
        text="Employee",
        variable=suEmployeeTypeVarHolder,
        value=0,
        text_color= "#0097b2",
        fg_color="#0097b2",           # main circle color (when selected)
        hover_color="#00788f",        # circle color on hover
        border_color="#0097b2"        # circle outline when not selected
        )
    suEmployeeTypeButton1 = ctk.CTkRadioButton(
        suEmployeeTypeFrame,
        text="IT Employee",
        variable=suEmployeeTypeVarHolder,
        value=1,
        text_color= "#0097b2",
        fg_color="#0097b2",           # main circle color (when selected)
        hover_color="#00788f",        # circle color on hover
        border_color="#0097b2"        # circle outline when not selected
        )
    suEmployeeTypeButton0.pack(side="top", padx=10)
    suEmployeeTypeButton1.pack(side="top", padx=10, pady=(5,10))

    #sign up button
    suButton = ctk.CTkButton(
    suContainerFrame,
    text="Sign Up",
    command=lambda: auth_callback(container, 0, container)
            if signUpFunct(
                suUsernameEntry,
                suPasswordEntry,
                suEmployeeEmailEntry,
                suEmployeeTypeVarHolder
            )
            else None
    )
    suButton.pack(side="bottom", anchor="e", padx=25, pady=25)

    return container