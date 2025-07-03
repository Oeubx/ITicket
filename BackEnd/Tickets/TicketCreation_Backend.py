
import customtkinter as ctk

from BackEnd.SQLiteQueries.TicketQueries import createTicket
from BackEnd.ReadfromFile import get_loggedIn_UsersId

def update_problems(category, problems_frame, selected_problem, category_to_problems):
    for widget in problems_frame.winfo_children():
        widget.destroy()

    for problem in category_to_problems[category]:
        rb = ctk.CTkRadioButton(
            problems_frame,
            text=problem,
            variable=selected_problem,
            value=problem,
            fg_color="#00c2cb",         # matches dropdown
            text_color="#000000",       # readable on cyan
            hover_color="#00a0a8"       # optional hover effect
        )
        rb.pack(side="top", anchor="w", padx=10, pady=5)

def submitTicket( #passes the widgets and .gets their values
        ticketLevel, ticketTitleEntry, category_dropdown,
        #passes the values to check if empty
        selected_problem_var, descriptionEntry,
        errorMsg1, errorMsg2,
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

        #uses the title entry for ticket name if its empty, then the category title will be used
        if ticketTitleEntry.get().strip():
            finalTitle = ticketTitleEntry.get().strip()
        else:
            finalTitle = category_dropdown.get().strip()

        #levl of ticket
        
        
        #combined description of ticket based on chosen radiobutton category or the text entry for desc
        if selected:
            finalDescription = f"{selected}\n\n{description}"
        else:
            finalDescription = description

        ###
        submitterId = get_loggedIn_UsersId()

        #query
        ticketCreation_Success = createTicket(
                                    finalTitle
                                    ,finalDescription
                                    ,ticketLevel.get().strip()
                                    ,submitterId
                                )

        #if true
        if ticketCreation_Success:
            mainFrame.pack_forget()
            successLabel.pack(side="top", padx=25, pady=25)
        else:
            errorMsg2.pack(side="bottom", anchor="w", padx=25, pady=(0,15))
    #else show error message
    else :
        descriptionEntry.pack_configure(pady=(25,0)) # adjusts the padding 
        errorMsg1.pack(side="top", anchor="w", padx=25, pady=(5,15))

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
