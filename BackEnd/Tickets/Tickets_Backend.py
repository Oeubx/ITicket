#tickets backend.py

import os
import customtkinter as ctk
from PIL import Image, ImageTk

from Assets.GradientBg import create_gradient_frame

from FrontEnd.Tickets.TicketCreation import load_TicketCreation

from BackEnd.SQLite_Calls import SQLiteCall
from BackEnd.Auth.LoggedIn_Acc import getUserID, getUserEmpType

from BackEnd.Tickets.UpdateTicketHistory_Backend import updateTicketHistory

_, pointer = SQLiteCall()

current_displayed_ticket_id = None
all_ticket_buttons = {}

def get_ITicketIcon(window):
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "Assets", "Icons", "main logo.png")

    image = Image.open(icon_path)
    icon = ImageTk.PhotoImage(image)
    return icon

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #
def reloadTicket(value, scrollableFrame, divider, rFrame, filter_order): 
    empId = getUserID()

    # Clear previous widgets
    for widget in scrollableFrame.winfo_children():
        widget.destroy()
    
    sortOrder = ""
    if filter_order == "Ascending" :
        sortOrder = "ASC"
    elif filter_order == "Descending" :
        sortOrder = "DESC"

    select_AllTickets = f"SELECT * FROM Ticket ORDER BY created_at {sortOrder}"

    select_LoggedUsersTickets = f"SELECT * FROM Ticket WHERE submitted_by = ? ORDER BY created_at {sortOrder}"
    loggedUser_Id = empId

    select_TicketLevel = f"SELECT * FROM Ticket WHERE ticket_level = ? ORDER BY created_at {sortOrder}"
    
    #select_AllTickets = "SELECT * FROM Ticket"
    #select_LoggedUsersTickets = "SELECT * FROM Ticket WHERE submitted_by = ?"
    #select_TicketLevel = "SELECT * FROM Ticket WHERE ticket_level = ?"

    if value == "All Tickets":
        pointer.execute(select_AllTickets)
    elif value == "My tickets":
        pointer.execute(select_LoggedUsersTickets, (loggedUser_Id, ))
    elif value == "Inquiries":
        pointer.execute(select_TicketLevel, (0, ))
    elif value == "Non-urgent":
        pointer.execute(select_TicketLevel, (1, ))
    elif value == "Urgent":
        pointer.execute(select_TicketLevel, (2, ))

    # collects the data
    ticket_ContentHolder = pointer.fetchall()

    #start of loop
    for row in ticket_ContentHolder:
        #saves each of the contents in these variables
        id, title, desc, status, level, created_at, submitted_by = row

        statusMessage = ""
        if status == 0:
            statusMessage = "Open"
        elif status == 1 :
            statusMessage = "Close"
        else :
            statusMessage = "Error Ticket Status"

        levelMessage = ""
        if level == 0 :
            levelMessage = "Inquiry"
        elif level == 1 :
            levelMessage = "Non - Urgent"
        elif level == 2 :
            levelMessage = "Urgent"
        else :
            levelMessage = "Error Ticket Level"

        #creation of widget for every tickets
        tContentFrame = ctk.CTkFrame(
            scrollableFrame,
            fg_color="#dbe1e3"
        )
        tContentFrame.pack(side="top", fill="x", expand=True, padx=(0,15), pady=15)

        #left frame | right frame
        ticket_LeftFrame = ctk.CTkFrame(tContentFrame)
        ticket_LeftFrame.pack(side="left", anchor="w", padx=25, pady=25)

        ticket_frame = ctk.CTkFrame(tContentFrame)
        ticket_frame.pack(side="right", anchor="e", padx=25, pady=25)

        #contents of left header frame
        ticket_headerFrame = ctk.CTkFrame(ticket_LeftFrame)
        ticket_headerFrame.pack(side="top", anchor="w")

        #query to get ticket submitters username
        getSubmitterName_query = """
            SELECT emp_username FROM Employee WHERE emp_Id = ?
        """
        pointer.execute(getSubmitterName_query, (submitted_by, ))
        submitterNameResult = pointer.fetchone()

        submitterName = submitterNameResult[0] if submitterNameResult else "Unkown Ticket Submitter | "

        ticketSubmitter = ctk.CTkLabel(
            ticket_headerFrame,
            text=f"{submitterName} | ",
            font=("Arial", 16, "bold")
        )
        ticketSubmitter.pack(side="left", anchor="nw")

        ticketTitle = ctk.CTkLabel(
            ticket_headerFrame,
            text=f"{title} | ",  #assigns ticket title
            font=("Arial", 16, "bold")
        )
        ticketTitle.pack(side="left", anchor="nw")

        ticketLevel = ctk.CTkLabel(
            ticket_headerFrame,
            text=f"{levelMessage}",  #assigns ticket level
            font=("Arial", 16, "bold")
        )
        ticketLevel.pack(side="left", anchor="nw")

        ##sub frame
        ticket_subFrame = ctk.CTkFrame(ticket_LeftFrame)
        ticket_subFrame.pack(side="top", anchor="w")

        ticketDate = ctk.CTkLabel(
            ticket_subFrame,
            text=f"Created at {created_at} | "     #assigns ticket date created at
        )
        ticketDate.pack(side="left")

         # logic for handler
        # Get latest handler for the ticket
        latestHandlerQuery = """
            SELECT ticket_Handler
            FROM Ticket_History
            WHERE ticket_Id = ?
            ORDER BY "updatedAt" DESC
            LIMIT 1
        """
        #DESCENDING takes the latest history and the handler,
        # LIMIT 1 takes the first only
        pointer.execute(latestHandlerQuery, (id,))
        latestHandlerResult = pointer.fetchone()

        latestHandler = latestHandlerResult[0] if latestHandlerResult else "No Handler"
        #

        ticketHandler = ctk.CTkLabel(
            ticket_subFrame,
            text=f"{latestHandler}"    #assigns FK referencing emp_id of IT emp
        )
        ticketHandler.pack(side="left")

        #contents of right frame
        ticketStatus = ctk.CTkLabel(
            ticket_frame,
            text=f"{statusMessage}"     # if close or open
            )
        ticketStatus.pack(side="top", pady=5)

        ticketRemarks = ctk.CTkButton(
            ticket_frame,
            text = "Open Ticket",
            command=lambda tid=id: showFullTicket(divider, rFrame, tid)
        )
        ticketRemarks.pack(side="top")

        # Save the button to a dictionary with ticket ID
        all_ticket_buttons[id] = ticketRemarks

        # Assign the command **after** storing the button
        ticketRemarks.configure(
            command=lambda tid=id,
            btn=ticketRemarks: showFullTicket(divider, rFrame, tid, btn)
        )

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #
def showFullTicket(divider, frame, ticketId, clicked_btn):
    global current_displayed_ticket_id, all_ticket_buttons

    # If the same ticket is already open, close it
    if current_displayed_ticket_id == ticketId:
        for widget in frame.winfo_children():
            widget.destroy()
        divider.pack_forget()
        frame.pack_forget()
        current_displayed_ticket_id = None

        # Reset the button text back to "See Ticket"
        clicked_btn.configure(text="Open Ticket")
        return

    # Close currently open ticket if another is clicked
    if current_displayed_ticket_id is not None:
        for widget in frame.winfo_children():
            widget.destroy()
        # Reset previous button label
        if current_displayed_ticket_id in all_ticket_buttons:
            all_ticket_buttons[current_displayed_ticket_id].configure(text="See Ticket")

    current_displayed_ticket_id = ticketId
    clicked_btn.configure(text="Close Ticket")

    # query for ticket
    selectTicket = "SELECT * FROM Ticket WHERE ticket_Id = ?"
    pointer.execute(selectTicket, (ticketId,))
    ticketDetailsHolder = pointer.fetchone()
    #saves it ^ here v
    id, title, desc, status, level, created_at, submitted_by = ticketDetailsHolder
    #were not displaying created_at, submitted_by anyway

    statusMessage = ""
    if status == 0:
        statusMessage = "Open"
    elif status == 1 :
        statusMessage = "Close"
    else :
        statusMessage = "Error Ticket Status"

    levelMessage = ""
    if level == 0 :
        levelMessage = "Inquiry"
    elif level == 1 :
        levelMessage = "Non - Urgent"
    elif level == 2 :
        levelMessage = "Urgent"
    else :
        levelMessage = "Error Ticket Level"

    # ─── Reset View ──────────────────────────────────────
    for widget in frame.winfo_children():  # remove previous content
        widget.destroy()

    divider.pack(side="left", fill="y", padx=10, pady=10)
    frame.pack(side="left", fill="both", expand=True)

    # ─── Container Frame for Full Ticket ─────────────────
    fullticketFrame = ctk.CTkFrame(frame, fg_color="#ffffff")
    fullticketFrame.pack(fill="both", expand=True)

    #query to get ticket submitters username
    getSubmitterName_query = """
        SELECT emp_username FROM Employee WHERE emp_Id = ?
    """
    pointer.execute(getSubmitterName_query, (submitted_by, ))
    submitterNameResult = pointer.fetchone()

    submitterName = submitterNameResult[0] if submitterNameResult else "Unkown Ticket Submitter | "

    ticketSubmitter = ctk.CTkLabel(
            fullticketFrame,
            text=f"{submitterName}",
            font=("Arial", 16, "bold"),
            text_color="#000000"
        )
    ticketSubmitter.pack(side="top", anchor="nw", padx=25, pady=(25, 5))

    headerFrame = ctk.CTkFrame(
        fullticketFrame,
        fg_color="#ffffff"
        )
    headerFrame.pack(side="top", anchor="w", fill="x", padx=25, pady=(5, 25))

    #headerframe lul
    tHandlerText = ctk.CTkLabel(
        headerFrame,
        text="Ticket Handler: ",
        text_color="#5e4b45"
        )
    tHandlerText.pack(side="left")

    # logic for handler
    # Get latest handler for the ticket
    latestHandlerQuery = """
        SELECT ticket_Handler
        FROM Ticket_History
        WHERE ticket_Id = ?
        ORDER BY "updatedAt" DESC
        LIMIT 1
    """
    #DESCENDING takes the latest history and the handler,
    # LIMIT 1 takes the first only
    pointer.execute(latestHandlerQuery, (id,))
    latestHandlerResult = pointer.fetchone()

    latestHandler = latestHandlerResult[0] if latestHandlerResult else "No Handler"
    #

    tHandlerName = ctk.CTkLabel(
        headerFrame,
        text=f"{latestHandler}",
        text_color="#5e4b45",
        font=("Arial", 15, "bold")
        )
    tHandlerName.pack(side="left")

    tStatus_Msg = ctk.CTkLabel(
        headerFrame,
        text=statusMessage,
        text_color="#5e4b45",
        font=("Arial", 15, "bold")
        )
    tStatus_Msg.pack(side="right")

    tStatus_Level = ctk.CTkLabel(
        headerFrame,
        text=f"{levelMessage} | ",
        text_color="#5e4b45",
        font=("Arial", 15, "bold")
        )
    tStatus_Level.pack(side="right")

    tStatusText = ctk.CTkLabel(
        headerFrame,
        text="Status: ",
        text_color="#5e4b45"
        )
    tStatusText.pack(side="right")

    titleText = ctk.CTkLabel(
        fullticketFrame,
        text=title,
        text_color="#5e4b45"
        )
    titleText.pack(side="top", anchor="w", padx=25, pady=(0, 10))

    bodyFrame = ctk.CTkFrame(
        fullticketFrame,
        fg_color="#a6a6a6"
        )
    bodyFrame.pack(side="top", anchor="w", fill="x", padx=25, pady=(0, 15))

    tDesc = ctk.CTkLabel(
        bodyFrame,
        text=desc,
        anchor="nw",
        justify="left",   
        text_color="#000000"
        )
    tDesc.pack(side="top", anchor="nw", padx=15, pady=15)

    # -------------------------------------------------------------------------------- #
    # Ticket History

    # query for this ticket's history
    selectTicketHistory = """
        SELECT * FROM Ticket_History
        WHERE ticket_Id = ?
        ORDER BY "updatedAt" ASC
    """
    pointer.execute(selectTicketHistory, (id,))
    ticketHistoryDetailsHolder = pointer.fetchall()

    # if it has contents
    if ticketHistoryDetailsHolder:
        xDivider = ctk.CTkFrame(bodyFrame, height=2, fg_color="gray")
        xDivider.pack(side="top", fill="x", padx=10)

        # loop to continously generate the ticket history
        for row in ticketHistoryDetailsHolder:    
            th_id, ticketId_ptr, handler, updateDesc, updatedAt = row

            th_Frame = ctk.CTkFrame(
                bodyFrame
                )
            th_Frame.pack(side="top", anchor="w", padx=25, pady=10)
            th_Frame.pack_propagate(True)  # allows the frame to size to its content

            #query to get ticket submitters username
            getHandlerName_query = """
                SELECT emp_username FROM Employee WHERE emp_Id = ?
            """
            pointer.execute(getHandlerName_query, (handler, ))
            handlerNameResult = pointer.fetchone()

            handlerName = handlerNameResult[0] if handlerNameResult else "Unkown Ticket Handler"

            # Inner frame for aligning contents neatly
            th_innerFrame = ctk.CTkFrame(th_Frame, fg_color="transparent")
            th_innerFrame.pack(anchor="w")  # anchor to the left only

            # Handler label
            th_ticketHandler = ctk.CTkLabel(
                th_innerFrame,
                text=f"{handlerName} :",
                anchor="w",
                justify="left"
            )
            th_ticketHandler.pack(anchor="w", pady=2)

            # Description label
            th_updateDesc = ctk.CTkLabel(
                th_innerFrame,
                text=f"{updateDesc}",
                anchor="w",
                justify="left"
            )
            th_updateDesc.pack(anchor="w", pady=2)

    # -------------------------------------------------------------------------------- #

    # Remarks Section
    remarksText = ctk.CTkLabel(
        fullticketFrame,
        text="<Remarks>",
        text_color="#5e4b45"
        )
    remarksFrame = ctk.CTkFrame(fullticketFrame, fg_color="#a6a6a6")

    remarkEntry = ctk.CTkEntry(
        remarksFrame,
        placeholder_text="Ticket Update Description",
        placeholder_text_color="#000000"
        )
    remarkEntry.pack(side="left", fill="x", expand=True, padx=(25, 10), pady=15)

    uploadRemarkBtn = ctk.CTkButton(
        remarksFrame,
        text="Update Ticket"
        )
    uploadRemarkBtn.pack(side="right", padx=(10, 25), pady=15)

    # buttons
    buttonsFrame = ctk.CTkFrame(fullticketFrame, fg_color="#a6a6a6")

    closeStatus_Btn = ctk.CTkButton(
        buttonsFrame,
        text="Close"
        )
    openStatus_Btn = ctk.CTkButton(
        buttonsFrame,
        text="Open"
        )
    #packs these two after checking status
    
    uploadRemarkBtn.configure(
        command = lambda: updateTicketHistory( # first three of what i need for db
            id, remarkEntry, getUserID(),
            "Update",   # the rest of what i need for widget updates
            tHandlerName, tStatus_Msg,
            bodyFrame, buttonsFrame,
            closeStatus_Btn, openStatus_Btn
            )
    )

    closeStatus_Btn.configure(
        command = lambda: updateTicketHistory( # first three of what i need for db
            id, remarkEntry.get().strip(), getUserID(),
            "Close",   # the rest of what i need for widget updates
            tHandlerName, tStatus_Msg,
            bodyFrame, buttonsFrame,
            closeStatus_Btn, openStatus_Btn
            )
    )

    openStatus_Btn.configure(
        command = lambda: updateTicketHistory( # first three of what i need for db
            id, remarkEntry.get().strip(), getUserID(),
            "Open",   # the rest of what i need for widget updates
            tHandlerName, tStatus_Msg,
            bodyFrame, buttonsFrame,
            closeStatus_Btn, openStatus_Btn
            )
    )

    loggedUserId = getUserEmpType()

    if loggedUserId == 0:
        remarksText.pack_forget()
        remarksFrame.pack_forget()
        buttonsFrame.pack_forget()
    else:
        remarksText.pack(side="top", anchor="w", padx=25, pady=(0, 10))
        remarksFrame.pack(side="top", anchor="w", fill="x", padx=25)

        buttonsFrame.pack(side="top", anchor="se", fill="x", padx=25, pady=25)
        if status == 0:     #if ticket is open //0
            closeStatus_Btn.pack(side="right", padx=25)
        elif status == 1:   #if ticket is closed //1
            openStatus_Btn.pack(side="right", padx=25)

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #
def show_tcf():
    submitTicketWindow = ctk.CTkToplevel()
    #submitTicketWindow.geometry("500x150")
    submitTicketWindow.title("Submit a Ticket")
    submitTicketWindow.grab_set()

    #icon not working i DO NOT KNOW WHY
    #icon = get_ITicketIcon(submitTicketWindow)
    #submitTicketWindow.iconphoto(False, icon)  # Set the icon
    #submitTicketWindow._icon_photo = icon 

    #reused the gradient bg
    gradientFrame = create_gradient_frame(submitTicketWindow)
    gradientFrame.pack(fill="both", expand=True)

    buttonFrame = ctk.CTkFrame(gradientFrame)
    buttonFrame.pack(side="top", padx=25, pady=25)

    labelFrame = ctk.CTkFrame(gradientFrame)
    labelFrame.pack(side="top", padx=25, pady=25)
    labelFrame.pack_forget()

    successTicketSubmission = ctk.CTkLabel(
        labelFrame,
        text="Ticket Submitted. You can close this window now",
        text_color="green"
    )
    successTicketSubmission.pack(side="top", padx=25, pady=25)

    #contents of button frame
    tcfInquireBtn = ctk.CTkButton(
        buttonFrame,
        text="Inquiry",
        command = lambda: load_TicketCreation(
            submitTicketWindow, gradientFrame, 0, buttonFrame, labelFrame
            )
    )
    tcfInquireBtn.pack(side="left", padx=25, pady=25)

    tcfNonUrgentBtn = ctk.CTkButton(
        buttonFrame,
        text="Non Urgent",
        command = lambda: load_TicketCreation(
            submitTicketWindow, gradientFrame, 1, buttonFrame, labelFrame
            )
    )
    tcfNonUrgentBtn.pack(side="left", padx=25, pady=25)

    tcfUrgentBtn = ctk.CTkButton(
        buttonFrame,
        text="Urgent",
        command = lambda: load_TicketCreation(
            submitTicketWindow, gradientFrame, 2, buttonFrame, labelFrame
            )
    )
    tcfUrgentBtn.pack(side="left", padx=25, pady=25)