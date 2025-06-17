#TEST WELCOME PAGE UI


#imports
import tkinter as tk
from tkinter import font
import sys
import os
import sqlite3 as sql


#headers
mainpage = tk.Tk()


#loginpage frame
loginPageFrame = tk.Frame(mainpage, bg="light blue")
loginPageFrame.grid(row=0, sticky="nsew", pady=15)


##login page header
ITicketIcon = tk.Label(loginPageFrame, text="temp val", bg="light blue")
aboutUs = tk.Label(loginPageFrame, text="About Us", bg="light blue")


ITicketIcon.grid(row=0, column=0, padx=(15,350), pady=20, sticky="nw")
aboutUs.grid(row=0, column=2, padx=(350,15), pady=20, sticky="ne")


##login page header text
loginPageHeaderFrame = tk.Frame(loginPageFrame, bg="light blue")
loginPageHeaderFrame.grid(row=0, column=1, padx=15, sticky="n")


titleframe = tk.Frame(loginPageHeaderFrame, bg="light blue")
titleframe.grid()


loginPageWelcomeText1 = tk.Label(titleframe, text="Welcome to ", font=("Arial", 32), bg="light blue")
loginPageWelcomeText2 = tk.Label(titleframe, text="ITicket", font=("Arial",32,"bold"), bg="light blue")


loginPageWelcomeText1.grid(row=0, column=0, padx=0, pady=(50,15), sticky="n")
loginPageWelcomeText2.grid(row=0, column=1, padx=0, pady=(50,15), sticky="n")


loginPageSubHeaderText1 = tk.Label(loginPageHeaderFrame,
                                  text="A smart, simple way to report IT issues and get faster support",
                                  bg="light blue")
loginPageSubHeaderText2 = tk.Label(loginPageHeaderFrame,
                                  text="--streamline your workflow with ITicket.",
                                  bg="light blue")


loginPageSubHeaderText1.grid(row=1,pady=(15,0), sticky="n")
loginPageSubHeaderText2.grid(row=2,pady=(0,15), sticky="n")


loginFrame = tk.LabelFrame(loginPageFrame, text="", padx=20)
loginFrame.grid(column=1, row=1, padx=15, pady=15, sticky="n")


##contents of loginFrame


#functions of loginFrame
def showPass():
   passwordEntry.config(show="")


loginText = tk.Label(loginFrame, text="Log in", font=("Arial", 20), fg="blue")


usernameFrame = tk.LabelFrame(loginFrame, text="Username", width=20)
passwordFrame = tk.LabelFrame(loginFrame, text="Password", width=20)


usernameIcon = tk.Label(usernameFrame, text="Temp icon")
passwordIcon = tk.Label(passwordFrame, text="Temp icon")


usernameEntry = tk.Entry(usernameFrame, text="")
passwordEntry = tk.Entry(passwordFrame, text="", show="*")


passwordShowIcon = tk.Button(passwordFrame, text="(0)", command=showPass())


##3buttons inside loginFrame
forgotPWbtn = tk.Button(loginFrame, text="Forgot Password ?")
logIntn = tk.Button(loginFrame, text="Log In", width=20, background="blue", fg="white")
signUpbtn = tk.Button(loginFrame, text="or Sign up")


##printing of contents of loginFrame
loginText.grid(row=0, column=2, pady=35)


usernameFrame.grid(row=1, column=2, pady=15, padx=25)
passwordFrame.grid(row=2, column=2, pady=15, padx=25)


usernameIcon.grid(row=0, column=1, pady=10, padx=(15,0))
passwordIcon.grid(row=0, column=1, pady=10)


usernameEntry.grid(row=0, column=2, pady=10, padx=(0,25))
passwordEntry.grid(row=0, column=2, pady=10, padx=(0,25))


passwordShowIcon.grid(row=0, column=3, pady=10, padx=(0,15))


##printing of buttons
forgotPWbtn.grid(row=3, column=2, pady=15, padx=25)
logIntn.grid(row=4, column=2, pady=15, padx=25)
signUpbtn.grid(row=5, column=2, pady=15, padx=25)


#end of login page


#functions


#contents


#printing of contents


#end
mainpage.mainloop()

