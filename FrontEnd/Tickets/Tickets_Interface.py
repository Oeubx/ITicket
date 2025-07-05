
import customtkinter as ctk

from BackEnd.Tickets.Tickets_Backend import reloadTicket, show_tcf

def load_ticketsInterface(frame):
    #t = tickets

    #main frames
    leftFrame = ctk.CTkFrame(
        frame,
        fg_color="#d2fdff",
        bg_color="#d2fdff"
        )
    leftFrame.pack(side="left", fill="both", expand=True)

    yDivider = ctk.CTkFrame(
        frame,
        width=2,
        height=30,
        fg_color="gray",
        border_color="#d2fdff",
        bg_color="#d2fdff"
        )
    #yDivider.pack(side="left", fill="y", padx=10, pady=10)
    yDivider.pack_forget()

    rightFrame = ctk.CTkFrame(
        frame,
        fg_color="#d2fdff",
        bg_color="#d2fdff"
        )
    #rightFrame.pack(side="left", fill="both", expand=True)
    rightFrame.pack_forget()

    #main frames
    # Add a variable to store filter value (default is Ascending)
    # initialize the frame and loads the tickets first
    scrollable_frame = ctk.CTkScrollableFrame(leftFrame)
    reloadTicket("All Tickets", scrollable_frame, yDivider, rightFrame, "Ascending")

    #header widgets
    tDropdown = ctk.CTkOptionMenu(
        leftFrame,
        values=["All Tickets", "My tickets", "Inquiries", "Non-Urgent", "Urgent"],
        #command = is in the bottom most part
        fg_color="#00c2cb",
        bg_color="#e9feff",
        text_color="#ffffff",
        dropdown_fg_color="#ffffff",
        dropdown_text_color="#1f3b4d",
        dropdown_hover_color="#d2fdff",
    )
    tDropdown.pack(side="top", anchor="w", padx=25, pady=(25,5))

    #no backend on this yet
    tFilter = ctk.CTkOptionMenu(
        leftFrame,
        values=["Ascending", "Descending"],
        fg_color="#00c2cb",
        bg_color="#e9feff",
        text_color="#ffffff",
        dropdown_fg_color="#ffffff",
        dropdown_text_color="#1f3b4d",
        dropdown_hover_color="#d2fdff",
    )
    tFilter.pack(side="top", anchor="w", padx=25, pady=(5, 15))

    #content widgets
    scrollable_frame.configure(
        width=400,
        height=400,
        fg_color="#e9feff",
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
    )
    scrollable_frame.pack(side="top", padx=20, fill="both", expand=True)

    createTicketBtn = ctk.CTkButton(
        leftFrame,
        text = "Submit a Ticket",
        fg_color="#00c2cb",
        text_color="#FFFFFF",
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
    