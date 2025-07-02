#ITicket main.py

#imports
import customtkinter as ctk
import os

# get app icon
def get_ITicketIcon(window):
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "Assets", "Icons", "main logo.ico")
    window.iconbitmap(icon_path)  # Use iconbitmap for .ico files

#window initialization
ITicket = ctk.CTk()
ITicket.title("ITicket")
get_ITicketIcon(ITicket)

#module imports
from BackEnd.Auth.LoggedIn_Acc import read_AuthValue_fromFile
from BackEnd.Auth.Auth_Backend import load_auth

#start
main_container_frame = ctk.CTkFrame(
    ITicket,
    fg_color="#a5fbff",
    bg_color="#a5fbff"
    )
main_container_frame.pack(fill="both", expand=True)

defaultValue = read_AuthValue_fromFile()  # 0=l, 1=fp, 2=su, 3=dashboard
authValue = defaultValue

load_auth(main_container_frame, authValue, previous_frame=None)

#tests

ITicket.mainloop()
#