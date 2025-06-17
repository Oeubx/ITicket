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

def load_dashboardMenu(menuFrame, menuIconBtn, toggle_callback):
    #collection of icons
    profile_icon = get_profileIcon()

    # Prevent double creation
    if getattr(menuFrame, "loaded", False):
        return

    #m = menu
    mHome = ctk.CTkButton(
        menuFrame,
        text="Home",
        image=profile_icon,
        compound="left",
        command=toggle_callback
    )
    mHome.pack(side="top")

    #employee frame
    employeesFrame = ctk.CTkFrame(menuFrame)
    employeesFrame.pack(padx=15, pady=15)

    #contents of employees Frame
    #missing command func
    employeeDropdown = ctk.CTkOptionMenu(
        employeesFrame,
        values=["All Employees", "IT employees", "Employees"]
    )
    employeeDropdown.pack(side="left", anchor="n", pady=20)

    #missing refresh function
    #get value from dropdown and show employees within that value
    employee_RefreshIcon = ctk.CTkLabel(
        employeesFrame,
        text="",
        image=profile_icon  #temp icon
    )
    employee_RefreshIcon.pack(side="left", anchor="n")

    #contents of subframe ##where the contents of the dropdown goes
    employees_SubFrame = ctk.CTkFrame(employeesFrame, fg_color="green")
    employees_SubFrame.pack(side="bottom", padx=15, pady=15)

    #missing command function to be redirected to tickets
    mTickets = ctk.CTkButton(
        menuFrame,
        text="Tickets",
        image=profile_icon, #temp icon
        compound="left"  # image on the left, text on the right
    )
    mTickets.pack(side="top")

    menuFrame.loaded = True