import customtkinter as ctk

def load_AboutUs(Iticket):
    aboutUs_Frame = ctk.CTkFrame()
    aboutUs_Frame.pack()

    #Contents of aboutUs frame
    #remo frame
    remoFrame = ctk.CTkFrame(aboutUs_Frame)
    remoFrame.pack()

    remo_HeaderFrame = ctk.CTkFrame(remoFrame)
    remo_HeaderFrame.pack()
    
    #esquivel frame
    esquivelFrame = ctk.CTkFrame(aboutUs_Frame)
    esquivelFrame.pack()
    
    esquivel_HeaderFrame = ctk.CTkFrame(esquivelFrame)
    esquivel_HeaderFrame.pack()

    #piolen frame
    piolenFrame = ctk.CTkFrame(aboutUs_Frame)
    piolenFrame.pack()
    
    piolen_HeaderFrame = ctk.CTkFrame(piolenFrame)
    piolen_HeaderFrame.pack()

    #ulgasan frame
    ulgasanFrame = ctk.CTkFrame(aboutUs_Frame)
    ulgasanFrame.pack()

    ulgasan_HeaderFrame = ctk.CTkFrame(ulgasanFrame)
    ulgasan_HeaderFrame.pack()