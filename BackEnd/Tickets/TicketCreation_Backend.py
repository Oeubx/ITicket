
import customtkinter as ctk

from BackEnd.Auth.LoggedIn_Acc import getUserID

from BackEnd.SQLite_Calls import SQLiteCall
dbConn, pointer = SQLiteCall()

from datetime import datetime   #for date n time of ticket
curr_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def update_problems(category, problems_frame, selected_problem, category_to_problems):
    for widget in problems_frame.winfo_children():
        widget.destroy()

    for problem in category_to_problems[category]:
        rb = ctk.CTkRadioButton(
            problems_frame,
            text=problem,
            variable=selected_problem,
            value=problem
        )
        rb.pack(side="top", anchor="w", padx=10, pady=5)

def submitTicket( #passes the widgets and .gets their values
        ticketLevel, category_dropdown,
        #passes the values to check if empty
        selected_problem_var, descriptionEntry, errorMsg,
        mainFrame, successLabel
        ):

    selected = selected_problem_var.get()
    description = descriptionEntry.get().strip()

    # if true proceed
    # discrete math or variable
    # T | T = T
    # T | F = T
    # F | T = T
    # F | F = F
    if selected or description :
        #title of ticket
        finalTitle = f"{category_dropdown.get()}"

        #levl of ticket
        levelSTR = ticketLevel.get()
        levelINT = 0

        if levelSTR == "Inquiry":
            levelINT = 0
        elif levelSTR == "Non-Urgent":
            levelINT = 1
        elif levelSTR == "Urgent":
            levelINT = 2
        
        #combined description of ticket
        finalDescription = f"{selected_problem_var.get()}\n\n{descriptionEntry.get().strip()}"

        #access index1 to get logged user's username
        submitterId = getUserID()

        #sqlite query
        ticketInserter = """
            INSERT INTO Ticket (
                ticket_title,
                ticket_desc,
                ticket_status,
                ticket_level,
                created_at,
                submitted_by
                )
            VALUES (?, ?, ?, ?, ?, ?)    
        """

        #values to insert
        value0 = finalTitle
        value1 = finalDescription
        value2 = 0 #default 0 for open, 1 if close
        value3 = levelINT #0 for inquiry, 1 for nonurgent, 2 for urgent
        value4 = curr_dateTime
        value5 = f"{submitterId}"

        pointer.execute(ticketInserter,
            (value0, value1, value2, value3, value4, value5)
            )
        #puts it in the database
        dbConn.commit()

        mainFrame.pack_forget()
        successLabel.pack(side="top", padx=25, pady=25)
    #else show error message
    else :
        descriptionEntry.pack_configure(pady=(25,0)) # adjusts the padding 
        errorMsg.pack(side="top", anchor="w", padx=25, pady=(5,15))

# if textbox instead
#in frontend file
#    ticketSubDescription = ctk.CTkTextbox(
#        ticketContentsFrame,
#        height=30
#        )
#    ticketSubDescription.pack(side="top", anchor="w", fill="x", expand=True, padx=25, pady=25)
#    setup_auto_resize_textbox(ticketSubDescription)
#
#in backend file
# gpt generated auto resize
#def setup_auto_resize_textbox(textbox_widget):
#    def auto_resize_textbox(event=None):
#        content = textbox_widget.get("0.0", "end")
#        num_lines = content.count("\n") + 1
#        textbox_widget.configure(height=max(30, num_lines * 20))  # Adjust as needed
#
#    # Bind the auto-resize on key release
#    textbox_widget.bind("<KeyRelease>", auto_resize_textbox)
