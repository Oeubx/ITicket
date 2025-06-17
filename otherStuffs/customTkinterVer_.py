#TEST WELCOME PAGE UI

#imports
import customtkinter as ctk
from tkinter import font
import sys
import os
import sqlite3 as sql

#starts
backEndTest = ctk.CTk()

#sql testTest database initialization
dbConn = sql.connect('testTestImIpt.db')
pointer = dbConn.cursor()
dbConn.commit()

#basic login -user -pass functions
def showPass():
    if loginPassEntry.cget('show') == "":
        loginPassEntry.configure(show="*")
        loginPassButton.configure(text="(O)")
    else:
        loginPassEntry.configure(show="")
        loginPassButton.configure(text="(X)")
#
def forgotPassFunct():
    pointer.execute("SELECT emp_username FROM employeeTest WHERE emp_username = ?",
                    (forgotLoginUserHolder.get().strip(), ) )
    result = pointer.fetchone()

    updatePassCommand = "UPDATE employeeTest SET emp_password = ? WHERE emp_username = ?"

    if result :
        pointer.execute(updatePassCommand, 
                        (
                        forgotLoginPassHolder.get().strip() ,
                        forgotLoginUserHolder.get().strip()
                        )
                    )
        dbConn.commit()
        print("pw updated")
    else :
        print("pw not updated")

def loginFunct():
    pointer.execute("SELECT emp_username, emp_password FROM employeeTest")
    userContentsHolder = pointer.fetchall()
    userFound = False

    for username, password in userContentsHolder:
        if username == loginUserHolder.get() :
            userFound = True
            if password == loginPassHolder.get() :
                print("success")
                return
            else :
                print("error wrong pass")
                return
            
    if not userFound :
        print("no username found")

def signUpFunct():
    signUpCommand = """
                    INSERT INTO employeeTest 
                    (emp_username, emp_password, 
                    emp_email, emp_type)
                    VALUES (?, ?, ?, ?)
                    """
    uniqueUser = False
    uniquePass = False
    boolEmail = False

    if signUpUsernameHolder.get().strip() == "":
        print("Error Sign Up username input")
    else :
        uniqueUser = True
        if signUpPassHolder.get().strip() == "":
            print("Error Sign Up password input")
        else :
            uniquePass = True
            if signUpEmpEmailEntryHolder.get().strip() == "":
                print("Error Sign Up email input")
            else :
                boolEmail = True

    if uniqueUser and uniquePass and boolEmail :
        pointer.execute(signUpCommand,
                        ( 
                          signUpUsernameHolder.get().strip() ,
                          signUpPassHolder.get().strip() ,
                          signUpEmpEmailEntryHolder.get().strip() ,
                          signUpEmpTypeVar.get()
                        )
                       )
        dbConn.commit()
        print("Success signing you up")
    else :
        print("Error Cant sign you up")
#
def forgotPassFindUser():
    pointer.execute("SELECT emp_username FROM employeeTest")
    userContentsHolder = pointer.fetchall()
    userFound = False

    for (username,) in userContentsHolder:
        if username == forgotLoginUserHolder.get() :
            userFound = True
            break
            
    if userFound:
        forgotLoginUserNotFound.pack_forget()
        forgotLoginPassEntry.configure(state="normal")
        forgotLoginUserFound.pack(side="bottom", padx=10)
    else :
        forgotLoginUserFound.pack_forget()
        forgotLoginPassEntry.configure(state="disabled")
        forgotLoginUserNotFound.pack(side="bottom", padx=10)
#
def forgotShowPass():
    if forgotLoginPassEntry.cget('show') == "":
        forgotLoginPassEntry.configure(show="*")
        forgotLoginPassButton.configure(text="(O)")
    else:
        forgotLoginPassEntry.configure(show="")
        forgotLoginPassButton.configure(text="(X)")

def signUpFindUser():
    pointer.execute("SELECT emp_username FROM employeeTest")
    userContentsHolder = pointer.fetchall()
    userFound = False

    for (username,) in userContentsHolder:
        if username == signUpUsernameHolder.get() :
            userFound = True
            break
            
    if userFound:
        signUpUserNotFound.pack_forget()
        signUpPassEntry.configure(state="disabled")
        signUpUserFound.pack(side="bottom", padx=10)
    else :
        signUpUserFound.pack_forget()
        signUpPassEntry.configure(state="normal")
        signUpUserNotFound.pack(side="bottom", padx=10)

def signUpShowPass():
    if signUpPassEntry.cget('show') == "":
        signUpPassEntry.configure(show="*")
        signUpPassButton.configure(text="(O)")
    else:
        signUpPassEntry.configure(show="")
        signUpPassButton.configure(text="(X)")


#contents
welcomeText = ctk.CTkLabel(backEndTest, text="hALLO")
welcomeText.pack()

#scrollable frame
canvas = ctk.CTkCanvas(backEndTest, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ctk.CTkScrollbar(backEndTest, orientation="vertical",
                             command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ctk.CTkFrame(canvas)
canvas_window = canvas.create_window((0, 0),
                                     window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Function to resize the frame width when the canvas is resized
def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", on_canvas_configure)

loginStuffsFrame = ctk.CTkFrame(scrollable_frame)
loginStuffsFrame.pack()

loginContentsFrame = ctk.CTkFrame(loginStuffsFrame)
loginContentsFrame.pack(side="top", padx=10, pady=10)

usernameFrame = ctk.CTkFrame(loginContentsFrame)
usernameFrame.pack(side="top", padx=10, pady=10, anchor="w")

loginText = ctk.CTkLabel(usernameFrame, text="Username :")
loginText.pack(side="left")

loginUserHolder = ctk.StringVar()
loginEntry = ctk.CTkEntry(usernameFrame, width=200, textvariable=loginUserHolder)
loginEntry.pack(side="right")

passwordFrame = ctk.CTkFrame(loginContentsFrame)
passwordFrame.pack(side="bottom", padx=10, pady=10)

loginPassText = ctk.CTkLabel(passwordFrame, text="Password : ")
loginPassText.pack(side="left")

loginPassHolder = ctk.StringVar()
loginPassEntry = ctk.CTkEntry(passwordFrame, show="*", textvariable=loginPassHolder)
loginPassEntry.pack(side="left")

loginPassButton = ctk.CTkButton(passwordFrame, text="(O)", command=showPass)
loginPassButton.pack(side="left")

loginMiscFrame = ctk.CTkFrame(loginStuffsFrame)
loginMiscFrame.pack(side="top", padx=15, pady=15)

forgotPassBtn = ctk.CTkButton(loginMiscFrame, text="Forgot Password?")
forgotPassBtn.pack(padx=5, pady=5)

loginBtn = ctk.CTkButton(loginMiscFrame, text="Login", command=loginFunct)
loginBtn.pack(padx=5, pady=5)

signUpBtn = ctk.CTkButton(loginMiscFrame, text="or Sign Up")
signUpBtn.pack(padx=5, pady=5)

###
forgotPassContentsFrame = ctk.CTkFrame(scrollable_frame)
forgotPassContentsFrame.pack(padx=10, pady=10)

forgotUsernameFrame = ctk.CTkFrame(forgotPassContentsFrame)
forgotUsernameFrame.pack(side="top", padx=10, pady=10, anchor="w")

forgotUsernameSubFrame1 = ctk.CTkFrame(forgotUsernameFrame)
forgotUsernameSubFrame1.pack(side="top", padx=10, pady=10, anchor="w")

forgotUsernameSubFrame2 = ctk.CTkFrame(forgotUsernameFrame)
forgotUsernameSubFrame2.pack(side="top", padx=10, pady=10, anchor="w")

forgotLoginText = ctk.CTkLabel(forgotUsernameSubFrame1, text="Username :")
forgotLoginText.pack(side="left")

forgotLoginUserHolder = ctk.StringVar()
forgotLoginEntry = ctk.CTkEntry(forgotUsernameSubFrame1, width=200,
                             textvariable=forgotLoginUserHolder)
forgotLoginEntry.pack(side="left")

forgotLoginButtonToCheckUser = ctk.CTkButton(forgotUsernameSubFrame1, text="(^v)",
                                          command=forgotPassFindUser)
forgotLoginButtonToCheckUser.pack(side="left")

# These CTkLabels are hidden by default, only shown later via logic
forgotLoginUserFound = ctk.CTkLabel(forgotUsernameSubFrame2,
                                 text="Username found. Please input desired password.")
forgotLoginUserNotFound = ctk.CTkLabel(forgotUsernameSubFrame2,
                                    text="Username not found. Please input the correct username.")

forgotPasswordFrame = ctk.CTkFrame(forgotPassContentsFrame)
forgotPasswordFrame.pack(side="top", padx=10, pady=10)

forgotLoginPassText = ctk.CTkLabel(forgotPasswordFrame, text="Password : ")
forgotLoginPassText.pack(side="left")

forgotLoginPassHolder = ctk.StringVar()
forgotLoginPassEntry = ctk.CTkEntry(forgotPasswordFrame, show="*",
                                state="disabled", textvariable=forgotLoginPassHolder)
forgotLoginPassEntry.pack(side="left")

forgotLoginPassButton = ctk.CTkButton(forgotPasswordFrame, text="(O)", command=forgotShowPass)
forgotLoginPassButton.pack(side="left")

forgotPassBtnFrame = ctk.CTkFrame(forgotPassContentsFrame)
forgotPassBtnFrame.pack(side="right", padx=10, pady=10)

forgotPassBtnInsideForgotPassBtnFrame = ctk.CTkButton(forgotPassBtnFrame, text="Update Password", 
                                       command=forgotPassFunct)
forgotPassBtnInsideForgotPassBtnFrame.pack()

###
signUpFrame = ctk.CTkFrame(scrollable_frame)
signUpFrame.pack(padx=10, pady=10)

signUpUsernameFrame = ctk.CTkFrame(signUpFrame)
signUpUsernameFrame.pack(side="top", padx=10, pady=10)

signUpUsernameSubFrame1 = ctk.CTkFrame(signUpUsernameFrame)
signUpUsernameSubFrame1.pack(side="top", padx=10, pady=10, anchor="w")

signUpUsernameSubFrame2 = ctk.CTkFrame(signUpUsernameFrame)
signUpUsernameSubFrame2.pack(side="top", padx=10, pady=10, anchor="w")

signUpUsernameText = ctk.CTkLabel(signUpUsernameSubFrame1, text="Username: ")
signUpUsernameText.pack(side="left")

signUpUsernameHolder = ctk.StringVar()
signUpUsernameEntry = ctk.CTkEntry(signUpUsernameSubFrame1, width=200, 
                                textvariable=signUpUsernameHolder)
signUpUsernameEntry.pack(side="left")

signUpUsernameButtonToCheckUser = ctk.CTkButton(signUpUsernameSubFrame1,  text="(^v)",
                                          command=signUpFindUser)
signUpUsernameButtonToCheckUser.pack(side="left")

signUpUserFound = ctk.CTkLabel(signUpUsernameSubFrame2,
                                 text="Username already taken. Please input a different username.")
signUpUserNotFound = ctk.CTkLabel(signUpUsernameSubFrame2,
                                    text="Username not yet taken. Please proceed to input desired password.")

signUpPasswordFrame = ctk.CTkFrame(signUpFrame)
signUpPasswordFrame.pack(side="top", padx=10, pady=10)

signUpPassText = ctk.CTkLabel(signUpPasswordFrame, text="Password : ")
signUpPassText.pack(side="left")

signUpPassHolder = ctk.StringVar()
signUpPassEntry = ctk.CTkEntry(signUpPasswordFrame, show="*",
                                state="disabled", textvariable=signUpPassHolder)
signUpPassEntry.pack(side="left")

signUpPassButton = ctk.CTkButton(signUpPasswordFrame, text="(O)", command=signUpShowPass)
signUpPassButton.pack(side="left")

signUpEmployeeEmailFrame = ctk.CTkFrame(signUpFrame)
signUpEmployeeEmailFrame.pack(side="top", padx=10, pady=10)

signUpEmpContactLabel = ctk.CTkLabel(signUpEmployeeEmailFrame, text="Email : ")
signUpEmpContactLabel.pack(side="left")

signUpEmpEmailEntryHolder = ctk.StringVar()
signUpEmpEmailEntry = ctk.CTkEntry(signUpEmployeeEmailFrame,
                                  textvariable=signUpEmpEmailEntryHolder)
signUpEmpEmailEntry.pack(side="left")

signUpEmployeeTypeFrame = ctk.CTkFrame(signUpFrame)
signUpEmployeeTypeFrame.pack(side="top", padx=10, pady=10)

signUpEmpTypeFrameLeft = ctk.CTkFrame(signUpEmployeeTypeFrame)
signUpEmpTypeFrameLeft.pack(side="left", anchor="n")
signUpEmpTypeFrameRight = ctk.CTkFrame(signUpEmployeeTypeFrame)
signUpEmpTypeFrameRight.pack(side="right")

signUpEmpTypeVar = ctk.IntVar()
signUpEmpTypeQuestion = ctk.CTkLabel(signUpEmpTypeFrameLeft, text="Employee Type : ")
signUpEmpTypeQuestion.pack(side="top")

# WARNING: customtkinter does not support CTkRadioButton by default as of latest version.
# You may need to implement your own radio button system using CTkSegmentedButton or
# other alternatives. Below code may not work as-is with CTkRadioButton.
# Suggest researching alternative ways to replicate radio button behavior in customtkinter.
# If CTkRadioButton is supported later, adjust imports and replace accordingly.
#signUpEmpTypeRadioBtn1 = tk.Radiobutton(signUpEmpTypeFrameRight, text="Normal Employee",
#                                        variable=signUpEmpTypeVar, value=0)
#signUpEmpTypeRadioBtn2 = tk.Radiobutton(signUpEmpTypeFrameRight, text="IT Employee",
#                                        variable=signUpEmpTypeVar, value=1)

#signUpEmpTypeRadioBtn1.pack(side="top", anchor="w")
#signUpEmpTypeRadioBtn2.pack(side="top", anchor="w")

signUpBtnFrame = ctk.CTkFrame(signUpFrame)
signUpBtnFrame.pack(side="right", padx=10, pady=10)

signUpBtnInsideSignUpFrame = ctk.CTkButton(signUpBtnFrame, text="Sign Up", 
                                       command=signUpFunct)
signUpBtnInsideSignUpFrame.pack()

#end
backEndTest.mainloop()
