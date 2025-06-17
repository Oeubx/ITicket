#TEST WELCOME PAGE UI

#imports
import tkinter as tk
from tkinter import font
import sys
import os
import sqlite3 as sql

#starts
backEndTest = tk.Tk()

#sql testTest database initialization
dbConn = sql.connect('testTestImIpt.db')
pointer = dbConn.cursor()
dbConn.commit()

#db creation
#test2 creation of tables
#try:
#    pointer.execute(
#        """
#        CREATE TABLE IF NOT EXISTS employeeTest (
#            emp_Id INTEGER PRIMARY KEY AUTOINCREMENT,
#            emp_username TEXT,
#            emp_password TEXT,
#            emp_email TEXT,
#            emp_type INTEGER #0 if normal emp, #1 if IT emp
#        )
#        """
#    )
#    dbConn.commit()
#    print("Table created successfully\n")
#except sql.Error as nt:
#    print("Unsuccessfull creation of Table: ", nt)
#db insertion

#dbConn.commit()
#try:
#    pointer.execute(
#    "INSERT INTO employeeTest (emp_username, emp_password) VALUES (?, ?)", ("test", "test1")
#    )
#    dbConn.commit()
#    print("Table content created successfully\n")
#except sql.Error as nt:
#    print("Unsuccessfull creation of Table: ", nt)

#test6 updating
#updater = "UPDATE employeeTest SET emp_username = ?, emp_password = ?, emp_email = ? WHERE emp_Id = 6"
#usernameToUpdate = "esquivelTestAcc"
#passwordToUpdate = "esquiveltestacc"
#emailToUpdate = "esquiveltestacc@gmail.com"
#
#pointer.execute(updater, (usernameToUpdate, passwordToUpdate, emailToUpdate))
#dbConn.commit()

#test4 printing the contents in the database
#pointer.execute("SELECT * FROM employeeTest")
#tableContentHolder = pointer.fetchall()

#for row in tableContentHolder:
#    print(f"{row}")

#functions

#basic login -user -pass functions
def showPass():
    if loginPassEntry.cget('show') == "":
        loginPassEntry.config(show="*")
        loginPassButton.config(text="(O)")
    else:
        loginPassEntry.config(show="")
        loginPassButton.config(text="(X)")

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

def clearSignUpFrames():
    signUpUsernameHolder.set("")
    signUpPassHolder.set("")
    signUpEmpEmailEntryHolder.set("")
    signUpEmpTypeVar.set(value=-1)

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

        clearSignUpFrames()

    else :
        print("Error Cant sign you up")

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
        forgotLoginPassEntry.config(state="normal")
        forgotLoginUserFound.pack(side="bottom", padx=10)
    else :
        forgotLoginUserFound.pack_forget()
        forgotLoginPassEntry.config(state="disabled")
        forgotLoginUserNotFound.pack(side="bottom", padx=10)

def forgotShowPass():
    if forgotLoginPassEntry.cget('show') == "":
        forgotLoginPassEntry.config(show="*")
        forgotLoginPassButton.config(text="(O)")
    else:
        forgotLoginPassEntry.config(show="")
        forgotLoginPassButton.config(text="(X)")

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
        signUpPassEntry.config(state="disabled")
        signUpUserFound.pack(side="bottom", padx=10)
    else :
        signUpUserFound.pack_forget()
        signUpPassEntry.config(state="normal")
        signUpUserNotFound.pack(side="bottom", padx=10)

def signUpShowPass():
    if signUpPassEntry.cget('show') == "":
        signUpPassEntry.config(show="*")
        signUpPassButton.config(text="(O)")
    else:
        signUpPassEntry.config(show="")
        signUpPassButton.config(text="(X)")

#contents
welcomeText = tk.Label(backEndTest, text="hALLO")
welcomeText.pack()

#
loginStuffsFrame = tk.LabelFrame(backEndTest, text="test")
loginStuffsFrame.pack()

##login -username entry -password entry contents
loginContentsFrame = tk.LabelFrame(loginStuffsFrame, text="Login Container")
loginContentsFrame.pack(side="top", padx=10, pady=10)

##user frame
usernameFrame = tk.Frame(loginContentsFrame)
usernameFrame.pack(side="top", padx=10, pady=10, anchor="w")

loginText = tk.Label(usernameFrame, text="Username :")
loginText.pack(side="left")

loginUserHolder = tk.StringVar()
loginEntry = tk.Entry(usernameFrame, width=20, textvariable=loginUserHolder)
loginEntry.pack(side="right")

##pass frame
passwordFrame = tk.Frame(loginContentsFrame)
passwordFrame.pack(side="bottom", padx=10, pady=10)

loginPassText = tk.Label(passwordFrame, text="Password : ")
loginPassText.pack(side="left")

loginPassHolder = tk.StringVar()
loginPassEntry = tk.Entry(passwordFrame, show="*", textvariable=loginPassHolder)
loginPassEntry.pack(side="left")

loginPassButton = tk.Button(passwordFrame, text="(O)", command=showPass)
loginPassButton.pack(side="left")
##end of login - -

#3 buttons misc login
loginMiscFrame = tk.Frame(loginStuffsFrame)
loginMiscFrame.pack(side="top", padx=15, pady=15)

forgotPassBtn = tk.Button(loginMiscFrame, text="Forgot Password?")
forgotPassBtn.pack(padx=5, pady=5)

loginBtn = tk.Button(loginMiscFrame, text="Login", command=loginFunct)
loginBtn.pack(padx=5, pady=5)

signUpBtn = tk.Button(loginMiscFrame, text="or Sign Up")
signUpBtn.pack(padx=5, pady=5)

#forgot pass contents
forgotPassContentsFrame = tk.LabelFrame(backEndTest, text="Forgot Password")
forgotPassContentsFrame.pack(padx=10, pady=10)

##forgot user frame
forgotUsernameFrame = tk.Frame(forgotPassContentsFrame)
forgotUsernameFrame.pack(side="top", padx=10, pady=10, anchor="w")

forgotUsernameSubFrame1 = tk.Frame(forgotUsernameFrame)
forgotUsernameSubFrame1.pack(side="top", padx=10, pady=10, anchor="w")

forgotUsernameSubFrame2 = tk.Frame(forgotUsernameFrame)
forgotUsernameSubFrame2.pack(side="top", padx=10, pady=10, anchor="w")

forgotLoginText = tk.Label(forgotUsernameSubFrame1, text="Username :")
forgotLoginText.pack(side="left")

forgotLoginUserHolder = tk.StringVar()
forgotLoginEntry = tk.Entry(forgotUsernameSubFrame1, width=20,
                             textvariable=forgotLoginUserHolder)
forgotLoginEntry.pack(side="left")

forgotLoginButtonToCheckUser = tk.Button(forgotUsernameSubFrame1, text="(^v)",
                                          command=forgotPassFindUser)
forgotLoginButtonToCheckUser.pack(side="left")

forgotLoginUserFound = tk.Label(forgotUsernameSubFrame2,
                                 text="Username found. Please input desired password.")
forgotLoginUserNotFound = tk.Label(forgotUsernameSubFrame2,
                                    text="Username not found. Please input the correct username.")

##forgot pass frame
forgotPasswordFrame = tk.Frame(forgotPassContentsFrame)
forgotPasswordFrame.pack(side="top", padx=10, pady=10)

forgotLoginPassText = tk.Label(forgotPasswordFrame, text="Password : ")
forgotLoginPassText.pack(side="left")

forgotLoginPassHolder = tk.StringVar()
forgotLoginPassEntry = tk.Entry(forgotPasswordFrame, show="*",
                                state="disabled", textvariable=forgotLoginPassHolder)
forgotLoginPassEntry.pack(side="left")

forgotLoginPassButton = tk.Button(forgotPasswordFrame, text="(O)", command=forgotShowPass)
forgotLoginPassButton.pack(side="left")

##btn frame contents for updating forgot pass
forgotPassBtnFrame = tk.Frame(forgotPassContentsFrame)
forgotPassBtnFrame.pack(side="right", padx=10, pady=10)

forgotPassBtnInsideForgotPassBtnFrame = tk.Button(forgotPassBtnFrame, text="Update Password", 
                                       command=forgotPassFunct)
forgotPassBtnInsideForgotPassBtnFrame.pack()
##end of forgot pass contents - -

#sign up contents
signUpFrame = tk.LabelFrame(backEndTest, text="Sign Up")
signUpFrame.pack(padx=10, pady=10)

##contents of signup username fraem
signUpUsernameFrame = tk.Frame(signUpFrame)
signUpUsernameFrame.pack(side="top", padx=10, pady=10)

signUpUsernameSubFrame1 = tk.Frame(signUpUsernameFrame)
signUpUsernameSubFrame1.pack(side="top", padx=10, pady=10, anchor="w")

signUpUsernameSubFrame2 = tk.Frame(signUpUsernameFrame)
signUpUsernameSubFrame2.pack(side="top", padx=10, pady=10, anchor="w")

signUpUsernameText = tk.Label(signUpUsernameSubFrame1, text="Username: ")
signUpUsernameText.pack(side="left")

signUpUsernameHolder = tk.StringVar()
signUpUsernameEntry = tk.Entry(signUpUsernameSubFrame1, width =20, 
                                textvariable=signUpUsernameHolder)
signUpUsernameEntry.pack(side="left")

signUpUsernameButtonToCheckUser = tk.Button(signUpUsernameSubFrame1,  text="(^v)",
                                          command=signUpFindUser)
signUpUsernameButtonToCheckUser.pack(side="left")

signUpUserFound = tk.Label(signUpUsernameSubFrame2,
                                 text="Username already taken. Please input a different username.")
signUpUserNotFound = tk.Label(signUpUsernameSubFrame2,
                                    text="Username not yet taken. Please proceed to input desired password.")

##contents of signup password frame
signUpPasswordFrame = tk.Frame(signUpFrame)
signUpPasswordFrame.pack(side="top", padx=10, pady=10)

signUpPassText = tk.Label(signUpPasswordFrame, text="Password : ")
signUpPassText.pack(side="left")

signUpPassHolder = tk.StringVar()
signUpPassEntry = tk.Entry(signUpPasswordFrame, show="*",
                                state="disabled", textvariable=signUpPassHolder)
signUpPassEntry.pack(side="left")

signUpPassButton = tk.Button(signUpPasswordFrame, text="(O)", command=signUpShowPass)
signUpPassButton.pack(side="left")

##contents of contact num
signUpEmployeeEmailFrame = tk.Frame(signUpFrame)
signUpEmployeeEmailFrame.pack(side="top", padx=10, pady=10)

signUpEmpContactLabel = tk.Label(signUpEmployeeEmailFrame, text="Email : ")
signUpEmpContactLabel.pack(side="left")

signUpEmpEmailEntryHolder = tk.StringVar()
signUpEmpEmailEntry = tk.Entry(signUpEmployeeEmailFrame,
                                  textvariable=signUpEmpEmailEntryHolder)
signUpEmpEmailEntry.pack(side="left")

##contents of checking if dude is an IT or not
signUpEmployeeTypeFrame = tk.Frame(signUpFrame)
signUpEmployeeTypeFrame.pack(side="top", padx=10, pady=10)

signUpEmpTypeFrameLeft = tk.Frame(signUpEmployeeTypeFrame)
signUpEmpTypeFrameLeft.pack(side="left", anchor="n")
signUpEmpTypeFrameRight = tk.Frame(signUpEmployeeTypeFrame)
signUpEmpTypeFrameRight.pack(side="right")

signUpEmpTypeVar = tk.IntVar(value=-1)
signUpEmpTypeQuestion = tk.Label(signUpEmpTypeFrameLeft, text="Employee Type : ")
signUpEmpTypeQuestion.pack(side="top")

signUpEmpTypeRadioBtn1 = tk.Radiobutton(signUpEmpTypeFrameRight, text="Normal Employee",
                                        variable=signUpEmpTypeVar, value=0)
signUpEmpTypeRadioBtn2 = tk.Radiobutton(signUpEmpTypeFrameRight, text="IT Employee",
                                        variable=signUpEmpTypeVar, value=1)

signUpEmpTypeRadioBtn1.pack(side="top", anchor="w")
signUpEmpTypeRadioBtn2.pack(side="top", anchor="w")

##btn frame contents for sign up
signUpBtnFrame = tk.Frame(signUpFrame)
signUpBtnFrame.pack(side="right", padx=10, pady=10)

signUpBtnInsideSignUpFrame = tk.Button(signUpBtnFrame, text="Sign Up", 
                                       command=signUpFunct)
signUpBtnInsideSignUpFrame.pack()
##end of sign up contents - -

#end
backEndTest.mainloop()