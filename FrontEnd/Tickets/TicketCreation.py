
import customtkinter as ctk

from BackEnd.Auth.LoggedIn_Acc import getUserDetails
from BackEnd.Tickets.TicketCreation_Backend import update_problems, submitTicket

def load_TicketCreation(toplevelWindow, frame, level: int, buttonFrame, successLabel):
    buttonFrame.pack_forget()

    mainFrame = ctk.CTkFrame(frame)
    mainFrame.pack(side="top", fill="both", expand=True, padx=25, pady=25)

    headerFrame = ctk.CTkFrame(mainFrame)
    headerFrame.pack(side="top", anchor="n", fill="x", padx=25, pady=25)

    submitterDetails = getUserDetails()
    submitterName = ctk.CTkLabel(
        headerFrame,
        text=f"{submitterDetails[1]}"   #index 1 to get their username
    )
    submitterName.pack(side="left", padx=15, pady=15)

    level_names = ["Inquiry", "Non-Urgent", "Urgent"]
    ticketLevel = ctk.CTkOptionMenu(
        headerFrame,
        values=level_names
    )
    ticketLevel.pack(side="right", padx=15, pady=15)
    ticketLevel.set(level_names[level])

    ticketContentsFrame = ctk.CTkFrame(
        mainFrame
    )
    ticketContentsFrame.pack(side="top", fill="x", padx=25)

    # Categories
    categories = [
        "Hardware Problems",
        "Network & Internet Problems",
        "Software & Application Problems",
        "Account & Access Problems",
        "Peripheral & External Device Problems",
        "Other Issues"
    ]

    # Problem lists per category
    hardware_problems = [
        "PC/Laptop won’t start or crashes",
        "Slow computer performance",
        "Keyboard or mouse not working",
        "Monitor/display issues",
        "Printer not printing or paper jams",
        "Scanner malfunction",
        "External devices not recognized",
        "Network cables or ports faulty",
        "Battery or power adapter issues",
        "Other: Please describe the issue."
    ]

    network_problems = [
        "No internet connection",
        "Slow or intermittent internet",
        "Wi-Fi connectivity problems",
        "VPN not connecting or dropping",
        "Unable to access websites or services",
        "Network printer or shared drive inaccessible",
        "IP address conflicts",
        "Firewall or security blocking access",
        "Other: Please describe the issue."
    ]

    software_problems = [
        "Browser issues (e.g., Chrome crashing)",
        "Email client problems",
        "Software installation/update failures",
        "Application crashes or freezes",
        "Access denied or permission errors",
        "License or activation issues",
        "Compatibility problems after updates",
        "Other: Please describe the issue."
    ]

    account_problems = [
        "Forgot password or account locked",
        "Unable to log in",
        "Permission denied (access rights)",
        "Multi-factor authentication issues",
        "User profile corruption or missing data",
        "Account provisioning delays",
        "Other: Please describe the issue."
    ]

    peripheral_problems = [
        "Printer or scanner offline",
        "Fax machine or multifunction device issues",
        "External monitors/projectors not detected",
        "Headsets, webcams, or microphones not working",
        "Mobile device syncing/connectivity problems",
        "Other: Please describe the issue."
    ]

    other_problems = [
        "Data backup or recovery issues",
        "Software/hardware compatibility questions",
        "Performance tuning or optimization",
        "Security incidents or malware infections",
        "Configuration and setup assistance",
        "IT policy or compliance questions",
        "Other: Please describe the issue."
    ]

    selected_problem = ctk.StringVar()
    category_to_problems = {
        categories[0]: hardware_problems,
        categories[1]: network_problems,
        categories[2]: software_problems,
        categories[3]: account_problems,
        categories[4]: peripheral_problems,
        categories[5]: other_problems,
    }

    #receive the category as the ticket title
    category_dropdown = ctk.CTkOptionMenu(
        ticketContentsFrame,
        values=categories,
        command=lambda cat: update_problems(
            cat, problems_frame, selected_problem, category_to_problems
            )
    )
    category_dropdown.pack(side="top", anchor="w", padx=25, pady=25)
    if level == 0:
        category_dropdown.set(categories[5])
    else :
        category_dropdown.set(categories[0])

    problems_frame = ctk.CTkFrame(ticketContentsFrame)
    problems_frame.pack(side="top", fill="both", expand=True, padx=25)

    update_problems(
        categories[0], problems_frame, selected_problem, category_to_problems
        )

    ticketSubDescription = ctk.CTkEntry(
        ticketContentsFrame,
        #can be empty because of the options
        placeholder_text="Describe the issue here"
        )
    ticketSubDescription.pack(side="top", anchor="w", fill="x", padx=25, pady=25)

    errorLabel1 = ctk.CTkLabel(
        ticketContentsFrame,
        text="Please choose from any of the options above if applicable or describe the issue.",
        text_color="#FF0000"
        )
    errorLabel1.pack_forget()

    buttonsFrame = ctk.CTkFrame(
        mainFrame
    )
    buttonsFrame.pack(side="top", anchor="e", padx=25, pady=25)

    cancelTicketSubmissionBtn = ctk.CTkButton(
        buttonsFrame,
        text="Cancel",
        command= toplevelWindow.destroy
    )
    cancelTicketSubmissionBtn.pack(side="left", anchor="e", padx=25, pady=25)

    submitTicketBtn = ctk.CTkButton(
        buttonsFrame,
        text="Submit Ticket",
        command=lambda: submitTicket(
            ticketLevel, category_dropdown, 
            selected_problem, ticketSubDescription, errorLabel1,
            mainFrame, successLabel 
            )
    )
    submitTicketBtn.pack(side="left", anchor="e", padx=25, pady=25)