##loginUi
import customtkinter as ctk

from BackEnd.Auth.Login_Backend import loginShowPass, loginFunct, showErrorText

def load_loginWidget(frame, returnValue):
    #l = login

    #main frame
    #global frame
    frame= ctk.CTkFrame(frame)

    if returnValue:
        return frame

def load_loginpage(frame, authValue, returnValue, auth_callback):
    frame.pack(fill="both", expand=True, padx=20, pady=25)
    
    #header
    ITicketLogo = ctk.CTkLabel(frame, text="ITickets")
    ITicketLogo.pack(side="left", anchor="n", padx=(25, 0), pady=25)

    #awaiting design
    AboutUs = ctk.CTkButton(frame, text="About Us")
    AboutUs.pack(side="right", anchor="n", padx=(0, 25), pady=25)

    #text
    welcomeTextLabel = ctk.CTkLabel(frame, text="Welcome to ITicket",
                                    text_color="black", fg_color="transparent")
    welcomeTextLabel.pack(side="top", pady=(75, 25))

    welcome_SubTextLabel = ctk.CTkLabel(frame, text="subtext")
    welcome_SubTextLabel.pack(side="top")

    #loginContainer Frame
    lContainerFrame = ctk.CTkFrame(frame)
    lContainerFrame.pack(side="top")

    Login_Text = ctk.CTkLabel(lContainerFrame, text="Log In", text_color="#0097b2")
    Login_Text.pack(side="top", pady=25)

    #usernameframe
    lUsernameFrame = ctk.CTkFrame(lContainerFrame)
    lUsernameFrame.pack(side="top", padx=10, pady=10, anchor="w")

    lUsernameText = ctk.CTkLabel(lUsernameFrame, text=" X ")
    lUsernameText.pack(side="left")

    ##lUsernameHolder = ctk.StringVar(value="")
    lUsernameEntry = ctk.CTkEntry(lUsernameFrame, width=200,
                                  placeholder_text="Username",
                                  placeholder_text_color="#0097b2")
    lUsernameEntry.pack(side="left", pady=5)
    ###holds the inputted username
    #lUsernameHolder = lUsernameEntry.get()

    #passwordframe
    lPasswordFrame = ctk.CTkFrame(lContainerFrame)
    lPasswordFrame.pack(side="top", padx=10, pady=10)

    lPasswordText = ctk.CTkLabel(lPasswordFrame, text=" X ")
    lPasswordText.pack(side="left")

    ##lPasswordHolder = ctk.StringVar(value="")
    lPasswordEntry = ctk.CTkEntry(lPasswordFrame, show="*",
                                  placeholder_text="Password",
                                  placeholder_text_color="#0097b2")
    lPasswordEntry.pack(side="left", pady=5)
    ###holds the inputted password
    ##lPasswordHolder = lPasswordEntry.get()

    lPasswordBtnShow = ctk.CTkButton(lPasswordFrame, text="(O)", width=5,
                                    command=lambda: loginShowPass(lPasswordEntry, lPasswordBtnShow))
    lPasswordBtnShow.pack(side="left")

    #3 buttons frame
    lButtonsFrame = ctk.CTkFrame(lContainerFrame)
    lButtonsFrame.pack(side="top", padx=15, pady=15)

    #fp = forgot password
    #no logic yet
    fpButton = ctk.CTkButton(lButtonsFrame, text="Forgot Password?", text_color="#0097b2",
                             bg_color="transparent", fg_color=None,
                             command=lambda: auth_callback(frame, 1, returnValue, frame))
    fpButton.pack(padx=5, pady=5)

    #l = login  #incomplete logic yet
    lButton = ctk.CTkButton(lButtonsFrame, text="Login", text_color="white",
                            command=lambda: (
                                auth_callback(frame, 3, returnValue, frame)
                                ) if loginFunct(lUsernameEntry, lPasswordEntry)
                                  else showErrorText(lUsernameEntry, lPasswordEntry)
                            )
    lButton.pack(padx=5, pady=5)

    #su = sign up
    #no logic yet
    suButton = ctk.CTkButton(lButtonsFrame, text="or Sign Up", text_color="#0097b2",
                             command=lambda: auth_callback(frame, 2, returnValue, frame))
    suButton.pack(padx=5, pady=5)

#auth_backend
import customtkinter as ctk

from FrontEnd.Auth.Login_Interface import load_loginpage
from FrontEnd.Auth.Forgotpw_Interface import load_forgotpwpage
from FrontEnd.Auth.Signup_Interface import load_signuppage  

from FrontEnd.Dashboard.Dashboard_Interface import load_dashboard

def load_auth_widgets(frame, returnValue):
    from FrontEnd.Auth.Login_Interface import load_loginWidget
    from FrontEnd.Auth.Forgotpw_Interface import load_forgotpWidget
    from FrontEnd.Auth.Signup_Interface import load_signupWidget
    from FrontEnd.Dashboard.Dashboard_Interface import load_dashboardWidget

    lFrame = load_loginWidget(frame, returnValue)
    fpFrame = load_forgotpWidget(frame, returnValue)
    suFrame = load_signupWidget(frame, returnValue)
    dFrame = load_dashboardWidget(frame, returnValue)

    lFrame.pack_forget()
    fpFrame.pack_forget()
    suFrame.pack_forget()
    dFrame.pack_forget()

    returnValue = False
    return returnValue

def load_auth(authValue, returnValue, frame, previous_frame):
    # hide previous page frame
    if previous_frame and previous_frame.winfo_exists():
        previous_frame.pack_forget()
        for widget in previous_frame.winfo_children():
            widget.pack_forget()
    
    if authValue == 0 : # l = login page
        load_loginpage(frame, authValue, returnValue, load_auth)
    elif authValue == 1 : #fp = forgot password
        load_forgotpwpage(frame, authValue, returnValue, load_auth)
    elif authValue == 2 : #su = sign up
        load_signuppage(frame, authValue, returnValue, load_auth)
    elif authValue == 3 : #d = dashboard
        load_dashboard(frame, authValue, returnValue, load_auth)
    else :
        print("auth error found")
