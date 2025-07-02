
import customtkinter as ctk

from FrontEnd.Dashboard.DashboardMenu_Interface import load_dashboardMenu

# --------------------------------------------------------- #
# backend for menubar | Dashboard_Interface.py
# --------------------------------------------------------- #
def show_menu(
        auth_callback,
        container, barFrame, mainFrame, 
        menuBtn
    ):

    # If menu is visible, hide it and show the button
    if barFrame.winfo_ismapped():
        barFrame.pack_forget()
        menuBtn.pack(side="left", anchor="nw", pady=25, padx=25)
    else:
        menuBtn.pack_forget()

        # Load menu bar contents only once
        if not hasattr(barFrame, "loaded") or not barFrame.loaded:
            load_dashboardMenu(
                auth_callback,
                container, barFrame, mainFrame,
                lambda: show_menu(
                    auth_callback,
                    container, barFrame, mainFrame, 
                    menuBtn
                )
            )
            barFrame.loaded = True

        # Repacking
        barFrame.pack_forget()
        mainFrame.pack_forget()

        barFrame.pack(side="left", anchor="nw", fill="y")
        mainFrame.pack(side="left", fill="both", expand=True)
