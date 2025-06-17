
import customtkinter as ctk

from datetime import datetime   #for date n time
curr_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from Assets.GradientBg import create_gradient_frame

from BackEnd.SQLite_Calls import SQLiteCall
dbConn, pointer = SQLiteCall()

def showTicketReopenWindow(status, defaultStatus):
    ticketReopen_window = ctk.CTkToplevel()
    ticketReopen_window.title("Ticket Status")
    ticketReopen_window.grab_set()

    gradientFrame = create_gradient_frame(ticketReopen_window)
    gradientFrame.pack(fill="both", expand=True)

    # Fix: container for all widgets
    container = ctk.CTkFrame(gradientFrame, fg_color="transparent")
    container.pack(expand=True)  # Use expand to center it vertically

    labelFrame = ctk.CTkFrame(container, fg_color="transparent")
    labelFrame.pack(padx=25, pady=15)

    if status == "Open":
        changeStatusLabel = "opening"
    elif status == "Close":
        changeStatusLabel = "closing"

    reopenLabel = ctk.CTkLabel(
        labelFrame,
        text=f"Ticket is {status}. Would you like to continue {changeStatusLabel} this ticket?",
        text_color="green",
        wraplength=400  # helps prevent long lines from overflowing
    )
    reopenLabel.pack(padx=15, pady=10)

    statusTextVar = ctk.StringVar(value=defaultStatus)
    statusEntryDesc = ctk.CTkEntry(
        container,
        textvariable=statusTextVar
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

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #
def renderTicketHistory(bodyFrame, ticketId):
    # clear history
    for widget in bodyFrame.winfo_children():
        widget.destroy()

    selectTicketHistory = """
        SELECT * FROM Ticket_History
        WHERE ticket_Id = ?
        ORDER BY "updatedAt" ASC
    """
    pointer.execute(selectTicketHistory, (ticketId,))
    ticketHistoryDetailsHolder = pointer.fetchall()

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

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #
def updateTicketHistory(
        ticketId, remarkEntryWidget, handlerId,
        stringStatus,
        handlerWidget, statusWidget,
        historyFrame, btnsFrame,
        closeBtn, openBtn
        ):
    # to be used for opening and closing of ticket
    updateDescription = ""
    
    if stringStatus == "Update":
        updateDescription = remarkEntryWidget.get().strip()

        insert_TH_query = """
            INSERT INTO Ticket_History (
                ticket_id,
                ticket_Handler,
                update_Description,
                update_Date           
                )
            VALUES (?, ?, ?, ?)    
        """
        pointer.execute(insert_TH_query,
                        (ticketId, handlerId, updateDescription, curr_dateTime)
                        )
        dbConn.commit()

        # i dont think we need to update ticket status if plain update
        #updates the ticket status
        # 0 for open
        # 1 for close
        #update_Ticket_query = """
        #    UPDATE Ticket
        #    SET
        #        ticket_status = ?
        #    WHERE ticket_Id = ?
        #"""
        #pointer.execute(update_Ticket_query, (1, ticketId))
        #dbConn.commit()
        #

        #clears the widget
        remarkEntryWidget.delete(0, "end")
    elif stringStatus == "Open":
        updateDescription = "Re-open this Ticket"
        confirmTicketStatus, updateDescription = showTicketReopenWindow(stringStatus, updateDescription)

        if confirmTicketStatus:
            insert_TH_query = """
                INSERT INTO Ticket_History (
                    ticket_id,
                    ticket_Handler,
                    update_Description,
                    update_Date           
                    )
                VALUES (?, ?, ?, ?)    
            """
            pointer.execute(insert_TH_query,
                            (ticketId, handlerId, updateDescription, curr_dateTime)
                            )
            dbConn.commit()

            #updates the ticket status
            update_Ticket_query = """
                UPDATE Ticket
                SET
                    ticket_status = ?
                WHERE ticket_Id = ?
            """
            # 0 default value to re open the ticket
            pointer.execute(update_Ticket_query, (0, ticketId))
            dbConn.commit()
    elif stringStatus == "Close":
        updateDescription = "Close this ticket"
        confirmTicketStatus, updateDescription = showTicketReopenWindow(stringStatus, updateDescription)

        if confirmTicketStatus:
            insert_TH_query = """
                INSERT INTO Ticket_History (
                    ticket_id,
                    ticket_Handler,
                    update_Description,
                    update_Date           
                    )
                VALUES (?, ?, ?, ?)    
            """
            pointer.execute(insert_TH_query,
                            (ticketId, handlerId, updateDescription, curr_dateTime)
                            )
            dbConn.commit()

            #updates the ticket status
            update_Ticket_query = """
                UPDATE Ticket
                SET
                    ticket_status = ?
                WHERE ticket_Id = ?
            """
            # 1 default value to re open the ticket
            pointer.execute(update_Ticket_query, (1, ticketId))
            dbConn.commit()
    # end of if, elif, elif ahh

    getHandlerName_query = """
        SELECT emp_username FROM Employee WHERE emp_Id = ?
        """
    pointer.execute(getHandlerName_query, (handlerId, ))
    result = pointer.fetchone()

    if result:
        handlerWidget.configure(text=result[0])
    else:
        handlerWidget.configure(text="No handler yet")
    
    if stringStatus == "Open" or stringStatus == "Update":
        statusWidget.configure(text="Open")
    elif stringStatus == "Close":
        statusWidget.configure(text="Closed")

    renderTicketHistory(historyFrame, ticketId)

    if stringStatus == "Close":
        for widget in btnsFrame.winfo_children():
            widget.pack_forget()
        openBtn.pack(side="right", padx=25)

    elif stringStatus == "Open":
        # show Close, hide Open
        for widget in btnsFrame.winfo_children():
            widget.pack_forget()
        closeBtn.pack(side="right", padx=25)

    # i need to refresh the ticket interface too