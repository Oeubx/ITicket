
import customtkinter as ctk

from BackEnd.Tickets.Tickets_Backend import reloadTicket, show_tcf

def load_ticketsInterface(frame):
    #t = tickets

    #main frames
    leftFrame = ctk.CTkFrame(
        frame,
        fg_color="#ffffff"
        )
    leftFrame.pack(side="left", fill="both", expand=True)

    yDivider = ctk.CTkFrame(
        frame,
        width=2,
        height=30,
        fg_color="gray"
        )
    #yDivider.pack(side="left", fill="y", padx=10, pady=10)
    yDivider.pack_forget()

    rightFrame = ctk.CTkFrame(
        frame,
        fg_color="#ffffff"
        )
    #rightFrame.pack(side="left", fill="both", expand=True)
    rightFrame.pack_forget()

    #main frames
    # Add a variable to store filter value (default is Ascending)
    #initialize the frame and loads the tickets first
    scrollable_frame = ctk.CTkScrollableFrame(leftFrame)
    reloadTicket("All Tickets", scrollable_frame, yDivider, rightFrame, "Ascending")

    #header widgets
    tDropdown = ctk.CTkOptionMenu(
        leftFrame,
        values=["All Tickets", "My tickets", "Inquiries", "Non-urgent", "Urgent"]
        #command = is in the bottom most part
    )
    tDropdown.pack(side="top", anchor="w", padx=25, pady=(25,5))

    #no backend on this yet
    tFilter = ctk.CTkOptionMenu(
        leftFrame,
        values=["Ascending", "Descending"]
    )
    tFilter.pack(side="top", anchor="w", padx=25, pady=(5, 15))

    #content widgets
    scrollable_frame.configure(
        width=400,
        height=400,
        fg_color="white",       # optional background color
        scrollbar_fg_color="gray",  # optional styling
    )
    scrollable_frame.pack(side="top", padx=20, fill="both", expand=True)

    createTicketBtn = ctk.CTkButton(
        leftFrame,
        text = "Submit a Ticket",
        command = lambda: show_tcf()
    )
    createTicketBtn.pack(side="bottom", anchor="e", padx=50, pady=25)

    #adds the command here
    tDropdown.configure(
        command=lambda values: reloadTicket(
            values, scrollable_frame, yDivider, rightFrame,
            tFilter.get()
        )
    )

    # Add command for tFilter so changing it reloads tickets with current dropdown value and new filter
    tFilter.configure(
        command=lambda _: reloadTicket(
            tDropdown.get(), scrollable_frame, yDivider, rightFrame,
            tFilter.get()
        )
    )

    ##############################################################################
    