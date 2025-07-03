
import customtkinter as ctk

from BackEnd.ReadfromFile import get_loggedIn_UsersId, get_userEmpType
from BackEnd.Tickets.UpdateTicketHistory_Backend import updateTicketHistory
from BackEnd.SQLiteQueries.MenuBarContentsQueries import get_MyTickets
from BackEnd.SQLiteQueries.TicketQueries import (
    get_FullTicketDetails,
    get_LatestHandler,
    get_ThisTicketsHistory,
    get_TicketHandlers_Name
)

def load_MyTickets(frame):
    userId = get_loggedIn_UsersId()

    myTicketsFrame = ctk.CTkFrame(
        frame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    myTicketsFrame.pack(side="top", fill="both", expand=True)

    # Header bar
    headerFrame = ctk.CTkFrame(
        myTicketsFrame,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    headerFrame.pack(side="top", anchor="nw")

    headerText = ctk.CTkLabel(
        headerFrame,
        text="ITicket : My Tickets",
        text_color="#000000",
        font=("Arial", 32, "bold"),
        height=50,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
    )
    headerText.pack(side="left", anchor="nw", padx=50, pady=25)

    #main holder of everything
    epContentsFrame = ctk.CTkScrollableFrame(
        myTicketsFrame,
        width=1500,
        height=1000,
        fg_color="#e9feff",
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
        )
    epContentsFrame.pack(side="top", anchor="nw", padx=50, pady=(0,50))

    #create filtering here
    
    myTickets = get_MyTickets(userId, "DESC")
    for (ticketId,) in myTickets:

        # query for ticket
        ticketDetailsHolder = get_FullTicketDetails(ticketId)
        # get from ^ saves it here v
        id, title, desc, status, level, submitterName = ticketDetailsHolder

        # 
        fullticketFrame = ctk.CTkFrame(
            epContentsFrame, 
            fg_color="#d2fdff"
            )
        fullticketFrame.pack(fill="both", expand=True, pady=(0,15))

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
        latestHandler = get_LatestHandler(ticketId)
        #handlerName = get_TicketHandlers_Name(latestHandler)

        tHandlerName = ctk.CTkLabel(
            headerFrame,
            text=f"{latestHandler}",
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
                id, remarkEntry, get_loggedIn_UsersId(),
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
                status,   # the rest of what i need for widget updates
                tHandlerName, tStatus_Msg,
                bodyFrame, buttonsFrame,
                closeStatus_Btn, openStatus_Btn
                )
        )

        openStatus_Btn.configure(
            command = lambda: updateTicketHistory( # first three of what i need for db
                id, remarkEntry.get().strip(), get_loggedIn_UsersId(),
                status,   # the rest of what i need for widget updates
                tHandlerName, tStatus_Msg,
                bodyFrame, buttonsFrame,
                closeStatus_Btn, openStatus_Btn
                )
        )

        # query from logged in acc _ queries .py
        loggedUserType = get_userEmpType()

        if loggedUserType == 0:
            remarksText.pack_forget()
            remarksFrame.pack_forget()
            buttonsFrame.pack_forget()
        else:
            remarksText.pack(side="top", anchor="w", padx=25, pady=(0, 10))
            remarksFrame.pack(side="top", anchor="w", fill="x", padx=25)

            buttonsFrame.pack(side="top", anchor="se", padx=50, pady=25)
            if status == "Open":
                closeStatus_Btn.pack(side="right")
            elif status == "Closed":
                openStatus_Btn.pack(side="right")