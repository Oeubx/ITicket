# Menu Logic
import customtkinter as ctk

app = ctk.CTk()

main_frame = ctk.CTkFrame(app)
main_frame.pack()

menu_container_frame = ctk.CTkFrame(main_frame, width=250, height=250, fg_color="lightgray")
menu_container_frame.pack(side="right", padx=25)

def toggle_menu():
    if menu_panel.winfo_ismapped():
        print("The menu is visible!")
        menu_panel.pack_forget()
        show_menu_button.pack(side="right", anchor="n", padx=25)
    else:
        print("The menu is hidden!")
        menu_panel.pack(side="left")
        show_menu_button.pack_forget()

menu_panel = ctk.CTkFrame(menu_container_frame, width=250, height=250, fg_color="blue")

menu_content_frame = ctk.CTkFrame(menu_panel, width=250, height=250)
menu_content_frame.pack()

home_button = ctk.CTkButton(menu_content_frame, width=25, text=" Home ")
home_button.pack(side="left")

spacer_frame = ctk.CTkFrame(menu_content_frame, width=25)
spacer_frame.pack(side="left")

close_menu_button = ctk.CTkButton(menu_content_frame, width=25, text=" X ", command=toggle_menu)
close_menu_button.pack(side="right")

placeholder_button = ctk.CTkButton(menu_container_frame, width=25, text="empty")
placeholder_button.pack(side="right", anchor="n", padx=25)

filler_panel = ctk.CTkFrame(menu_container_frame, width=250, height=250, fg_color="white")
filler_panel.pack(side="right", padx=25)

show_menu_button = ctk.CTkButton(menu_container_frame, width=25, text="sub menu", command=toggle_menu)
show_menu_button.pack(side="right", anchor="n", padx=25)

app.mainloop()
