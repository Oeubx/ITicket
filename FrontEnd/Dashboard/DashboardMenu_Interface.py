import customtkinter as ctk
import os
from PIL import Image

#will update to get_assets
def get_profileIcon():
    # Get the absolute path to the icon
    current_dir = os.path.dirname(__file__)  # = /path/to/frontend/dashboard
    icon_path = os.path.join(current_dir, "..", "..", "Assets", "Icons", "profile.png")
    # Load image and wrap it in CTkImage

    profile_icon = ctk.CTkImage(Image.open(icon_path), size=(20, 20))  # adjust size as needed
    return profile_icon

def load_dashboardMenu(
        menuFrame, menuIconBtn,
        toggle_callback
    ):
    
    if hasattr(menuFrame, "loaded") and menuFrame.loaded:
        return  # Already built

    icon = get_profileIcon()

    mHome = ctk.CTkButton(
        menuFrame,
        text="Home",
        image=icon,
        compound="left",
        command=toggle_callback
    )
    mHome.pack(side="top", pady=(25, 0))

    employeesFrame = ctk.CTkFrame(menuFrame)
    employeesFrame.pack(padx=15, pady=15)

    employeeDropdown = ctk.CTkOptionMenu(
        employeesFrame,
        values=["All Employees", "IT employees", "Employees"]
    )
    employeeDropdown.pack(side="left", anchor="n", pady=20)

    employee_RefreshIcon = ctk.CTkLabel(
        employeesFrame,
        text="",
        image=icon
    )
    employee_RefreshIcon.pack(side="left", anchor="n")

    employees_SubFrame = ctk.CTkFrame(employeesFrame, fg_color="green")
    employees_SubFrame.pack(side="bottom", padx=15, pady=15)

    mTickets = ctk.CTkButton(
        menuFrame,
        text="Tickets",
        image=icon,
        compound="left"
    )
    mTickets.pack(side="top")

    menuFrame.loaded = True  # Mark as initialized