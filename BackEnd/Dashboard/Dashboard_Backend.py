
import customtkinter as ctk

from FrontEnd.Dashboard.DashboardMenu_Interface import load_dashboardMenu
from FrontEnd.Dashboard.DashboardProfile_Interface import load_dashboardProfile

#has packing and unpacking issues
def show_menu(
        leftFrame, leftBtn,
        centerFrame,
        rightFrame, rightBtn
    ):

    # If menu is visible, hide it and show the button
    if leftFrame.winfo_ismapped():
        leftFrame.pack_forget()
        leftBtn.pack(side="left", anchor="nw", pady=25, padx=25)
    else:
        # If profile is currently visible, hide it first
        if rightFrame.winfo_ismapped():
            rightFrame.pack_forget()
            rightBtn.pack(side="right", anchor="ne", pady=25, padx=25)

        leftBtn.pack_forget()

        # Load menu contents only once
        if not hasattr(leftFrame, "loaded") or not leftFrame.loaded:
            load_dashboardMenu(
                leftFrame,
                leftBtn,
                lambda: show_menu(
                    leftFrame, leftBtn,
                    centerFrame,
                    rightFrame, rightBtn
                )
            )
            leftFrame.loaded = True

        # Re-pack in correct order: left → center → right (if applicable)
        leftFrame.pack(side="left", anchor="nw", fill="y")
        centerFrame.pack_forget()
        centerFrame.pack(side="right", fill="both", expand=True)
        rightFrame.pack_forget()

# --------------------------------------------------------- #
# queries for profile menu | .py
# --------------------------------------------------------- #
def show_ProfileMenu(
        leftFrame, leftBtn,
        centerFrame,
        rightFrame, rightBtn,
        auth_callback, container,
        mainFrameHolder
    ):

    if rightFrame.winfo_ismapped():
        rightFrame.pack_forget()
        rightBtn.pack(side="right", anchor="ne", pady=25, padx=25)
    else:
        # Hide menu if open
        if leftFrame.winfo_ismapped():
            leftFrame.pack_forget()
            leftBtn.pack(side="left", anchor="nw", pady=25, padx=25)

        rightBtn.pack_forget()

        if not hasattr(rightFrame, "loaded") or not rightFrame.loaded:
            load_dashboardProfile(
                rightFrame, rightBtn,
                lambda: show_ProfileMenu(
                    leftFrame, leftBtn,
                    centerFrame,
                    rightFrame, rightBtn,
                    auth_callback, container,
                    mainFrameHolder
                ),
                auth_callback, container,
                leftFrame, centerFrame,
                mainFrameHolder
            )
            rightFrame.loaded = True

        centerFrame.pack(side="left", fill="both", expand=True)
        rightFrame.pack(side="left", anchor="ne", fill="y")