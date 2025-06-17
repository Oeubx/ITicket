
#from BackEnd.SQLite_Calls import SQLiteCall, get_dbConn

from FrontEnd.Dashboard.DashboardMenu_Interface import load_dashboardMenu
from FrontEnd.Dashboard.DashboardProfile_Interface import load_dashboardProfile

def show_menu(leftFrame, leftBtn, centerFrame, rightFrame, rightBtn):
    # leftFrame = menu frame
    # rightFrame = profile frame
    # Load the menu content
    load_dashboardMenu(leftFrame, leftBtn,
                       lambda: show_menu(leftFrame, leftBtn,
                                         centerFrame,
                                         rightFrame, rightBtn))

    # Check if menu frame is currently visible BEFORE forgetting packing
    menu_is_visible = leftFrame.winfo_ismapped()

    # Forget everything
    leftFrame.pack_forget()
    leftBtn.pack_forget()
    centerFrame.pack_forget()
    rightFrame.pack_forget()
    rightBtn.pack_forget()

    if menu_is_visible:
        leftBtn.pack(side="left", anchor="nw", pady=25, padx=25)
    else:
        leftFrame.pack(side="left", anchor="nw", fill="y", padx=(0, 25))

    # Repack center and right
    centerFrame.pack(side="left", fill="both", expand=True, pady=25, padx=25)

    if rightFrame.winfo_ismapped():
        rightFrame.pack(side="left", anchor="ne", fill="y", padx=(25, 0))
    else:
        rightBtn.pack(side="right", anchor="ne", pady=25, padx=25)

def show_ProfileMenu(pFrame, pButton, auth_callback, dashboardFrame):
    # pFrame = profile frame
    # loads widgets
    load_dashboardProfile(
        pFrame, pButton,
        lambda: show_ProfileMenu(
            pFrame, pButton, auth_callback, dashboardFrame
            ),
        auth_callback, dashboardFrame)
    
    if pFrame.winfo_ismapped():
        pFrame.pack_forget()
        pButton.pack(side="right", anchor="ne", pady=25, padx=25)
    else:
        pFrame.pack(side="right", anchor="ne", fill="y", padx=(25,0))
        pButton.pack_forget()