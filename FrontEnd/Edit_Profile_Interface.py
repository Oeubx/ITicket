import customtkinter as ctk
#import backend here

#pass root page
def load_editProfile(ITicket):
    #ep = edit profile

    #Main frame
    epFrame = ctk.CTkFrame(ITicket)
    epFrame.pack()

    #main holder of everything
    epContentsFrame = ctk.CTkFrame(epFrame)
    epContentsFrame.pack()

    #username frame
    epUsernameFrame = ctk.CTkFrame(epContentsFrame)
    epUsernameFrame.pack()

    epLastname_Holder = ctk.StringVar()
    epFirstname_Holder = ctk.StringVar()
    epMiddleinitial_Holder = ctk.StringVar()

    epLastname_Entry = ctk.CTkEntry(epUsernameFrame, textvariable=epLastname_Holder)
    epLastname_Entry.pack()
    
    epFirstname_Entry = ctk.CTkEntry(epUsernameFrame, textvariable=epFirstname_Holder)
    epFirstname_Entry.pack()
    
    epMiddleinitialn_Entry = ctk.CTkEntry(epUsernameFrame, textvariable=epMiddleinitial_Holder)
    epMiddleinitialn_Entry.pack()

    #password frame #lacks button to show/unshow the pass
    epPasswordFrame = ctk.CTkFrame(epContentsFrame)
    epPasswordFrame.pack()

    epPassword_Holder = ctk.StringVar()
    epPasswordEntry = ctk.CTkEntry(epPasswordFrame, show="*",
                                  textvariable=epPassword_Holder)
    epPasswordEntry.pack()

    epConfirmPass_Holder = ctk.StringVar()
    epConfirmPasswordEntry = ctk.CTkEntry(epPasswordFrame, show="*",
                                  textvariable=epPassword_Holder)
    epConfirmPasswordEntry.pack()

    #email frame
    epEmailFrame = ctk.CTkFrame(epContentsFrame)
    epEmailFrame.pack()

    epEmail_Holder = ctk.StringVar()
    epEmailEntry = ctk.CTkEntry(epEmailFrame, textvariable=epEmail_Holder)
    epEmailEntry.pack()

    #employee type frame #no logic of saving
    epEmpTypeFrame = ctk.CTkframe(epContentsFrame)
    epEmpTypeFrame.pack()

    epEmpTypeVar_Holder = ctk.IntVar()
    epEmployeeTypeButton0 = ctk.CTkRadioButton(epEmpTypeFrame, text="Normal Employee",
                                               variable=epEmpTypeVar_Holder, value=0)
    epEmployeeTypeButton1 = ctk.CTkRadioButton(epEmpTypeFrame, text="IT Employee",
                                               variable=epEmpTypeVar_Holder, value=1)

    epEmployeeTypeButton0.pack(side="top", anchor="w")
    epEmployeeTypeButton1.pack(side="top", anchor="w")

    #button frame
    epButtonFrame = ctk.CTkFrame(epContentsFrame)
    epButtonFrame.pack()

    epUpdateProfileBtn = ctk.CTkButton(epButtonFrame)
    epUpdateProfileBtn.pack(side="right", anchor="e")