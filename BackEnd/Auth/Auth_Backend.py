#auth_backend
import customtkinter as ctk

from FrontEnd.Auth.Auth_Header import load_authHeader

from FrontEnd.Auth.Login_Interface import load_loginpage
from FrontEnd.Auth.Forgotpw_Interface import load_forgotpwpage
from FrontEnd.Auth.Signup_Interface import load_signuppage  

from FrontEnd.Dashboard.Dashboard_Interface import load_dashboard

def load_auth(gradient_frame, authValue, previous_frame):
    # w = widget, n = count, a/b = counterpart, n = count
    #w1, w2, w3a, w3b1, w3b2 = load_authHeader(gradient_frame)
    #preserved_widgets = {w1, w2, w3a, w3b1, w3b2}

    if previous_frame and previous_frame.winfo_exists():
        for widget in previous_frame.winfo_children():
            #if widget not in preserved_widgets:
            widget.destroy()
    
    if authValue == 0 : # l = login page
        load_authHeader(gradient_frame)
        load_loginpage(gradient_frame, authValue, load_auth)
    elif authValue == 1 : #fp = forgot password
        load_authHeader(gradient_frame)
        load_forgotpwpage(gradient_frame, authValue, load_auth)
    elif authValue == 2 : #su = sign up
        load_authHeader(gradient_frame)
        load_signuppage(gradient_frame, authValue, load_auth)
    elif authValue == 3 : #d = dashboard
        load_dashboard(gradient_frame, authValue, load_auth)
    else :
        print("auth error found")
