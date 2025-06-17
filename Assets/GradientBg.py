import customtkinter as ctk
import tkinter as tk

def draw_gradient(event=None, canvas=None, start_color=None, end_color=None):
    if event is not None:
        canvas = event.widget

    canvas.delete("all")
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    if width < 2 or height < 2:
        return

    for x in range(width):
        ratio = x / (width - 1)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(x, 0, x, height, fill=hex_color)

def create_gradient_frame(parent):
    gradient_frame = ctk.CTkFrame(parent)
    gradient_frame.pack(fill="both", expand=True)

    gradient_canvas = tk.Canvas(gradient_frame, highlightthickness=0)
    gradient_canvas.pack(fill="both", expand=True)

    start_rgb = (205, 255, 216)
    end_rgb = (148, 185, 255)

    def on_configure(event):
        draw_gradient(event, gradient_canvas, start_rgb, end_rgb)

    gradient_canvas.bind("<Configure>", on_configure)

    return gradient_canvas
