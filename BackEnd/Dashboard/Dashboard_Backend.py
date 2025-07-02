
import customtkinter as ctk

from FrontEnd.Dashboard.DashboardMenu_Interface import load_dashboardMenu
from FrontEnd.Tickets.Tickets_Interface import load_ticketsInterface

# --------------------------------------------------------- #
# backend for menubar | Dashboard_Interface.py
# --------------------------------------------------------- #
def show_menu(
        auth_callback,
        container, barFrame, mainFrame, headerFrame, dContentsFrame
    ):

    if barFrame.winfo_ismapped():
        barFrame.pack_forget()

        # 🧽 Only clear widgets **below** headerFrame
        for widget in mainFrame.winfo_children():
            if widget != headerFrame:
                widget.destroy()

        # First: Clear everything except header
        for widget in mainFrame.winfo_children():
            if widget != headerFrame:
                widget.destroy()

        # Repack header
        headerFrame.pack(side="top", fill="x")

        # Then recreate content area
        contentFrame = ctk.CTkFrame(mainFrame, fg_color="#a5fbff")
        contentFrame.pack(side="top", fill="both", expand=True)

        # Re-create fresh dContentsFrame
        newContentsFrame = ctk.CTkFrame(contentFrame, fg_color="#000000", bg_color="#ffffff")
        newContentsFrame.pack(fill="both", expand=True, padx=25, pady=25)

        # Load default content again
        load_ticketsInterface(newContentsFrame)
    else:
        # 🔵 Switch to sidebar
        headerFrame.pack_forget()  # ← HIDE the header when menu opens

        if not hasattr(barFrame, "loaded") or not barFrame.loaded:
            load_dashboardMenu(
                auth_callback,
                container, barFrame, mainFrame, headerFrame,  # ✅ INCLUDE headerFrame
                lambda: show_menu(
                    auth_callback,
                    container, barFrame, mainFrame, headerFrame, dContentsFrame)
            )
            barFrame.loaded = True

         # Reset main layout order
        barFrame.pack_forget()
        mainFrame.pack_forget()
        barFrame.pack(side="left", fill="y")  # LEFT
        mainFrame.pack(side="left", fill="both", expand=True)  # RIGHT