#ITicket main.py

#imports
import customtkinter as ctk
import os

#base functions
def get_ITicketIcon(window):
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "Assets", "Icons", "main logo.ico")
    window.iconbitmap(icon_path)  # Use iconbitmap for .ico files

#window initialization
ITicket = ctk.CTk()
ITicket.title("ITicket")
get_ITicketIcon(ITicket)

#module imports
from Assets.GradientBg import create_gradient_frame

from BackEnd.Auth.LoggedIn_Acc import read_AuthValue_fromFile
from BackEnd.Auth.Auth_Backend import load_auth

#start
shared_frame = create_gradient_frame(ITicket)
shared_frame.pack(fill="both", expand=True)

defaultValue = read_AuthValue_fromFile()  # 0=l, 1=fp, 2=su, 3=dashboard
authValue = defaultValue

load_auth(shared_frame, authValue, previous_frame=None)

#tests

#end lul
ITicket.mainloop()
#