
import customtkinter as ctk

from datetime import datetime   #for date n time
curr_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from BackEnd.SQLiteQueries.TicketQueries import *

def showTicketReopenWindow(status, defaultStatus):
    ticketReopen_window = ctk.CTkToplevel()
    ticketReopen_window.title("Ticket Status")
    ticketReopen_window.grab_set()

    frameHolder = ctk.CTkFrame(
        ticketReopen_window,
        fg_color="#a5fbff",
        bg_color="#a5fbff"
        )
    frameHolder.pack(fill="both", expand=True)

    container = ctk.CTkFrame(frameHolder, fg_color="transparent")
    container.pack(expand=True)

    labelFrame = ctk.CTkFrame(container, fg_color="transparent")
    labelFrame.pack(padx=25, pady=15)

    if status == "Open":
        changeStatusLabel = "closing"
    elif status == "Close":
        changeStatusLabel = "opening"

    reopenLabel = ctk.CTkLabel(
        labelFrame,
        text=f"Ticket is currently '{status}'. Would you like to continue {changeStatusLabel} this ticket?",
        text_color="green",
        wraplength=400  # helps prevent long lines from overflowing
    )
    reopenLabel.pack(padx=15, pady=10)

    statusTextVar = ctk.StringVar(value=defaultStatus)
    statusEntryDesc = ctk.CTkEntry(
        container,
        textvariable=statusTextVar,
        fg_color="#e9feff",
        placeholder_text_color="#000000",
        text_color="#000000",
        width=250
    )
    statusEntryDesc.pack(padx=15, pady=10)

    result = ctk.BooleanVar(value=False)

    btnFrame = ctk.CTkFrame(container, fg_color="transparent")
    btnFrame.pack(padx=25, pady=15)

    def confirm():
        result.set(True)
        ticketReopen_window.destroy()

    def cancel():
        result.set(False)
        ticketReopen_window.destroy()

    closeBtn = ctk.CTkButton(btnFrame, text="Cancel", command=cancel)
    closeBtn.pack(side="left", padx=10)

    confirmBtn = ctk.CTkButton(btnFrame, text="Confirm", command=confirm)
    confirmBtn.pack(side="left", padx=10)

    ticketReopen_window.wait_window()

    return result.get(), statusTextVar.get().strip()

# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
# for ticket history reloading when updating | --.py
# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
def renderFullTicket(bodyFrame, ticketId):
    # clear history
    for widget in bodyFrame.winfo_children():
        widget.destroy()

    # query for ticket
    ticketDetails = get_TicketDescription(ticketId)

    tDesc = ctk.CTkLabel(
        bodyFrame,
        text=ticketDetails,
        anchor="nw",
        justify="left",   
        text_color="#000000"
        )
    tDesc.pack(side="top", anchor="nw", padx=15, pady=15)

    # -------------------------------------------------------------------------------- #
    # Ticket History
    # -------------------------------------------------------------------------------- #

    # query for this ticket's history
    ticketHistoryDetailsHolder = get_ThisTicketsHistory(ticketId)

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

# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
# logic for updating ticket History | --.py
# --------------------------------------------------------- #
# 
# --------------------------------------------------------- #
def updateTicketHistory(
        ticketId, remarkEntryWidget, handlerId,
        stringStatus,
        handlerWidget, statusWidget,
        historyFrame, btnsFrame,
        closeBtn, openBtn
        ):
    # to be used for opening and closing of ticket
    updateDescription = ""
    ticketUpdated = False
    
    if stringStatus == "Update":
        updateDescription = remarkEntryWidget.get().strip()

        update_thisTicket(ticketId, handlerId, updateDescription)

        remarkEntryWidget.delete(0, "end")
        ticketUpdated = True
    elif stringStatus == "Open":
        updateDescription = "Close this Ticket"
        confirmTicketStatus, updateDescription = showTicketReopenWindow(stringStatus, updateDescription)

        if confirmTicketStatus:
            update_thisTicket(ticketId, handlerId, updateDescription)
            update_thisTicketsStatus("Closed", ticketId)
            ticketUpdated = True
    elif stringStatus == "Close":
        updateDescription = "Re-open this ticket"
        confirmTicketStatus, updateDescription = showTicketReopenWindow(stringStatus, updateDescription)

        if confirmTicketStatus:
            update_thisTicket(ticketId, handlerId, updateDescription)
            update_thisTicketsStatus("Open", ticketId)
            ticketUpdated = True

    if ticketUpdated:      
        #query to get ticket submitters username
        handlerName = get_TicketHandlers_Name(handlerId)

        if handlerName:
            handlerWidget.configure(text=handlerName)
        else:
            handlerWidget.configure(text="No handler yet")
        
        if stringStatus == "Open" or stringStatus == "Update":
            statusWidget.configure(text="Open")
        elif stringStatus == "Close":
            statusWidget.configure(text="Closed")

        renderFullTicket(historyFrame, ticketId)

        if stringStatus == "Close":
            for widget in btnsFrame.winfo_children():
                widget.pack_forget()
            openBtn.pack(side="right")

        elif stringStatus == "Open":
            # show Close, hide Open
            for widget in btnsFrame.winfo_children():
                widget.pack_forget()
            closeBtn.pack(side="right")

    # i need to refresh the ticket interface too
    # why? | its hard bro