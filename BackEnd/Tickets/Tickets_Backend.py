#tickets backend.py

import os
import customtkinter as ctk
from PIL import Image, ImageTk

from FrontEnd.Tickets.TicketCreation import load_TicketCreation

from BackEnd.Tickets.UpdateTicketHistory_Backend import updateTicketHistory
from BackEnd.SQLiteQueries.TicketQueries import * # usage of * since too many was called/used
from BackEnd.ReadfromFile import get_userEmpType
from BackEnd.ReadfromFile import get_loggedIn_UsersId

# global variable
current_displayed_ticket_id = None
all_ticket_buttons = {}

# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
# logic for ticket reloading | --.py
# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
def reloadTicket(value, scrollableFrame, divider, rFrame, filter_order): 

    # Clear previous widgets
    for widget in scrollableFrame.winfo_children():
        widget.destroy()
    
    sortOrder = ""
    if filter_order == "Ascending" :
        sortOrder = "ASC"
    elif filter_order == "Descending" :
        sortOrder = "DESC"

    ###
    loggedUser_Id = get_loggedIn_UsersId()

    if value == "All Tickets":
        ticket_ContentsHolder = get_AllTickets(sortOrder)
    elif value == "My tickets":
        ticket_ContentsHolder = get_MyTickets(loggedUser_Id, sortOrder)
    elif value == "Inquiries":
        ticket_ContentsHolder = get_TicketByLevel("Inquiry", sortOrder)
    elif value == "Non-Urgent":
        ticket_ContentsHolder = get_TicketByLevel(value, sortOrder)
    elif value == "Urgent":
        ticket_ContentsHolder = get_TicketByLevel(value, sortOrder)

    #start of loop
    for row in ticket_ContentsHolder:
        #saves each of the contents in these variables
        id, title, status, level, created_at, submitted_by = row

        #creation of widget for every tickets
        tContentFrame = ctk.CTkFrame(
            scrollableFrame,
            fg_color="#d2fdff"
        )
        tContentFrame.pack(side="top", fill="x", expand=True, padx=(0,15), pady=15)

        #left frame | right frame
        ticket_LeftFrame = ctk.CTkFrame(
            tContentFrame,
            fg_color="#d2fdff"
            )
        ticket_LeftFrame.pack(side="left", anchor="w", padx=25, pady=25)

        ticket_frame = ctk.CTkFrame(
            tContentFrame,
            fg_color="#d2fdff"
            )
        ticket_frame.pack(side="right", anchor="e", padx=25, pady=25)

        #contents of left header frame
        ticket_headerFrame = ctk.CTkFrame(
            ticket_LeftFrame,
            fg_color="#d2fdff"
            )
        ticket_headerFrame.pack(side="top", anchor="w")

        #query to get ticket submitters username | submitted by is an ID
        submitterName = get_TicketSubmitterName(submitted_by)

        ticketSubmitter = ctk.CTkLabel(
            ticket_headerFrame,
            text=f"{submitterName} | ",
            font=("Arial", 16, "bold"),
            text_color="#000000"
        )
        ticketSubmitter.pack(side="left", anchor="nw")

        ticketTitle = ctk.CTkLabel(
            ticket_headerFrame,
            text=f"{title} | ",
            font=("Arial", 16, "bold"),
            text_color="#000000"
        )
        ticketTitle.pack(side="left", anchor="nw")

        ticketLevel = ctk.CTkLabel(
            ticket_headerFrame,
            text=f"{level}",
            font=("Arial", 16, "bold"),
            text_color="#000000"
        )
        ticketLevel.pack(side="left", anchor="nw")

        ##sub frame
        ticket_subFrame = ctk.CTkFrame(
            ticket_LeftFrame,
            fg_color="#d2fdff"
            )
        ticket_subFrame.pack(side="top", anchor="w")

        ticketDate = ctk.CTkLabel(
            ticket_subFrame,
            text=f"Created at {created_at} | ",
            text_color="#000000"
        )
        ticketDate.pack(side="left")

        # query
        latestHandler = get_LatestHandler(id)

        ticketHandler = ctk.CTkLabel(
            ticket_subFrame,
            text=f"{latestHandler}",
            text_color="#000000"
        )
        ticketHandler.pack(side="left")

        #contents of right frame
        ticketStatus = ctk.CTkLabel(
            ticket_frame,
            text=f"{status}",
            text_color="#000000",
            fg_color="#d2fdff"
            )
        ticketStatus.pack(side="top", pady=5)

        ticketRemarks = ctk.CTkButton(
            ticket_frame,
            text = "View Ticket",
            text_color="#000000",
            fg_color="#00c2cb",
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

# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
# logic for showing full ticket | --.py
# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
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
            all_ticket_buttons[current_displayed_ticket_id].configure(text="View Ticket")

    current_displayed_ticket_id = ticketId
    clicked_btn.configure(text="Close Ticket")

    # query for ticket
    ticketDetailsHolder = get_TicketDetails(ticketId)
    # get from ^ saves it here v
    id, title, desc, status, level, submitted_by = ticketDetailsHolder

    # remove previous content
    for widget in frame.winfo_children():
        widget.destroy()

    divider.pack(side="left", fill="y")
    frame.pack(side="left", fill="both", expand=True)

    # 
    fullticketFrame = ctk.CTkFrame(
        frame, 
        fg_color="#d2fdff"
        )
    fullticketFrame.pack(fill="both", expand=True)

    #query to get ticket submitters username | submitted by is an ID
    submitterName = get_TicketSubmitterName(submitted_by)

    submitterHeaderFrame = ctk.CTkFrame(
        fullticketFrame,
        fg_color="#d2fdff"
    )
    submitterHeaderFrame.pack(side="top", anchor="nw", fill="x", padx=25, pady=(25, 5))

    ticketSubmitterText = ctk.CTkLabel(
            submitterHeaderFrame,
            text="Ticket By : ",
            text_color="#000000"
        )
    ticketSubmitterText.pack(side="left")

    ticketSubmitter = ctk.CTkLabel(
            submitterHeaderFrame,
            text=f"{submitterName}",
            font=("Arial", 16, "bold"),
            text_color="#000000"
        )
    ticketSubmitter.pack(side="left")

    headerFrame = ctk.CTkFrame(
        fullticketFrame,
        fg_color="#d2fdff"
        )
    headerFrame.pack(side="top", anchor="w", fill="x", padx=25, pady=(5, 25))

    #headerframe lul
    tHandlerText = ctk.CTkLabel(
        headerFrame,
        text="Ticket Handler : ",
        text_color="#000000"
        )
    tHandlerText.pack(side="left")

    # query
    latestHandler = get_LatestHandler(id)
    handlerName = get_TicketHandlers_Name(latestHandler)

    tHandlerName = ctk.CTkLabel(
        headerFrame,
        text=f"{handlerName}",
        text_color="#000000",
        font=("Arial", 15)
        )
    tHandlerName.pack(side="left")

    tStatus_Msg = ctk.CTkLabel(
        headerFrame,
        text=status,
        text_color="#000000",
        font=("Arial", 15, "bold")
        )
    tStatus_Msg.pack(side="right")

    tStatus_Level = ctk.CTkLabel(
        headerFrame,
        text=f"{level} | ",
        text_color="#000000",
        font=("Arial", 15, "bold")
        )
    tStatus_Level.pack(side="right")

    tStatusText = ctk.CTkLabel(
        headerFrame,
        text="Status: ",
        text_color="#000000"
        )
    tStatusText.pack(side="right")

    # title
    titleText = ctk.CTkLabel(
        fullticketFrame,
        text=title,
        text_color="#000000",
        font=("Arial", 15, "bold")
        )
    titleText.pack(side="top", anchor="w", padx=25, pady=(0, 10))

    # 
    bodyFrame = ctk.CTkScrollableFrame(
        fullticketFrame,
        fg_color="#e9feff",
        width=350,
        height=550,  # ← chosen height between your min and max
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
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
    # -------------------------------------------------------------------------------- #

    # query for this ticket's history
    ticketHistoryDetailsHolder = get_ThisTicketsHistory(id)

    # if it has contents
    if ticketHistoryDetailsHolder:
        xDivider = ctk.CTkFrame(bodyFrame, height=2, fg_color="gray")
        xDivider.pack(side="top", fill="x", padx=10)

        # loop to continously generate the ticket history
        for row in ticketHistoryDetailsHolder:    
            handler, updateDesc = row

            th_Frame = ctk.CTkFrame(
                bodyFrame,
                fg_color="#e9feff",
                )
            th_Frame.pack(side="top", anchor="w", padx=15, pady=10)
            th_Frame.pack_propagate(True)  # allows the frame to size to its content

            #query to get ticket submitters username
            handlerName = get_TicketHandlers_Name(handler)

            # Inner frame for aligning contents neatly
            th_innerFrame = ctk.CTkFrame(th_Frame, fg_color="transparent")
            th_innerFrame.pack(anchor="w")  # anchor to the left only

            # Handler label
            th_ticketHandler = ctk.CTkLabel(
                th_innerFrame,
                text=f"{handlerName} :",
                anchor="w",
                justify="left",
                text_color="#000000"
            )
            th_ticketHandler.pack(anchor="w", pady=2)

            # Description label
            th_updateDesc = ctk.CTkLabel(
                th_innerFrame,
                text=f"{updateDesc}",
                anchor="w",
                justify="left",
                text_color="#000000"
            )
            th_updateDesc.pack(anchor="w", pady=2)

    # -------------------------------------------------------------------------------- #

    # Remarks Section
    remarksText = ctk.CTkLabel(
        fullticketFrame,
        text="<Remarks>",
        text_color="#5e4b45"
        )
    
    remarksFrame = ctk.CTkFrame(
        fullticketFrame,
        fg_color="#e9feff",
        )

    remarkEntry = ctk.CTkEntry(
        remarksFrame,
        placeholder_text="Ticket Update Description",
        fg_color="#e9feff",
        placeholder_text_color="#000000",
        text_color="#000000"
        )
    remarkEntry.pack(side="left", fill="x", expand=True, padx=(25, 10), pady=15)

    uploadRemarkBtn = ctk.CTkButton(
        remarksFrame,
        text="Update Ticket",
        fg_color="#00c2cb",
        text_color="#000000"
        )
    uploadRemarkBtn.pack(side="right", padx=(10, 25), pady=15)

    # buttons
    buttonsFrame = ctk.CTkFrame(
        fullticketFrame,
        fg_color="#e9feff"
        )

    closeStatus_Btn = ctk.CTkButton(
        buttonsFrame,
        text="Close",
        fg_color="#00c2cb",
        text_color="#000000"
        )
    openStatus_Btn = ctk.CTkButton(
        buttonsFrame,
        text="Open",
        fg_color="#00c2cb",
        text_color="#000000"
        )
    #packs these two after checking status
    
    uploadRemarkBtn.configure(
        command = lambda: updateTicketHistory( # first three of what i need for db
            id, remarkEntry, 2,
            #id, remarkEntry.get().strip(), getUserID(),
            "Update",   # the rest of what i need for widget updates
            tHandlerName, tStatus_Msg,
            bodyFrame, buttonsFrame,
            closeStatus_Btn, openStatus_Btn
            )
    )

    closeStatus_Btn.configure(
        command = lambda: updateTicketHistory( # first three of what i need for db
            id, remarkEntry.get().strip(), get_loggedIn_UsersId(),
            "Close",   # the rest of what i need for widget updates
            tHandlerName, tStatus_Msg,
            bodyFrame, buttonsFrame,
            closeStatus_Btn, openStatus_Btn
            )
    )

    openStatus_Btn.configure(
        command = lambda: updateTicketHistory( # first three of what i need for db
            id, remarkEntry.get().strip(), get_loggedIn_UsersId(),
            "Open",   # the rest of what i need for widget updates
            tHandlerName, tStatus_Msg,
            bodyFrame, buttonsFrame,
            closeStatus_Btn, openStatus_Btn
            )
    )

    # query from logged in acc _ queries .py
    loggedUserId = get_userEmpType()

    if loggedUserId == 0:
        remarksText.pack_forget()
        remarksFrame.pack_forget()
        buttonsFrame.pack_forget()
    else:
        remarksText.pack(side="top", anchor="w", padx=25, pady=(0, 10))
        remarksFrame.pack(side="top", anchor="w", fill="x", padx=25)

        buttonsFrame.pack(side="top", anchor="se", padx=50, pady=25)
        if status == "Open":
            closeStatus_Btn.pack(side="right")
        elif status == "Close":
            openStatus_Btn.pack(side="right")

# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
# show ticket creation frame | --.py
# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
def show_tcf():
    submitTicketWindow = ctk.CTkToplevel()
    submitTicketWindow.title("Submit a Ticket")
    submitTicketWindow.grab_set()

    main_container_frame = ctk.CTkFrame(
        submitTicketWindow,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    main_container_frame.pack(fill="both", expand=True)

    contentsHolder_Frame = ctk.CTkFrame(
        main_container_frame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
    )
    contentsHolder_Frame.pack(fill="both", expand=True, anchor="center", padx=25, pady=25)

    buttonFrame = ctk.CTkFrame(
        contentsHolder_Frame,
        fg_color="#e0fdff"
        )
    buttonFrame.pack(side="top", padx=25, pady=25)

    labelFrame = ctk.CTkFrame(
        contentsHolder_Frame,
        fg_color="#e0fdff"
        )
    labelFrame.pack(side="top", padx=25, pady=25)
    labelFrame.pack_forget()

    successTicketSubmission = ctk.CTkLabel(
        labelFrame,
        text="Ticket Submitted. You can close this window now",
        text_color="#2b4c59"
    )
    successTicketSubmission.pack(side="top", padx=25, pady=25)

    #contents of button frame
    tcfInquireBtn = ctk.CTkButton(
        buttonFrame,
        text="Inquiry",
        fg_color="#00c2cb",
        text_color="#ffffff",
        command = lambda: load_TicketCreation(
            submitTicketWindow, contentsHolder_Frame, 0, buttonFrame, labelFrame
            )
    )
    tcfInquireBtn.pack(side="left", padx=25, pady=25)

    tcfNonUrgentBtn = ctk.CTkButton(
        buttonFrame,
        text="Non Urgent",
        fg_color="#00c2cb",
        text_color="#ffffff",
        command = lambda: load_TicketCreation(
            submitTicketWindow, contentsHolder_Frame, 1, buttonFrame, labelFrame
            )
    )
    tcfNonUrgentBtn.pack(side="left", padx=25, pady=25)

    tcfUrgentBtn = ctk.CTkButton(
        buttonFrame,
        text="Urgent",
        fg_color="#00c2cb",
        text_color="#ffffff",
        command = lambda: load_TicketCreation(
            submitTicketWindow, contentsHolder_Frame, 2, buttonFrame, labelFrame
            )
    )
    tcfUrgentBtn.pack(side="left", padx=25, pady=25)