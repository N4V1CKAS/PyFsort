import os
import sys
import shutil
import customtkinter as ctk
from tkinter import filedialog

# Get icon.ico path
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "images", "icon.ico")
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "images", "icon.ico")

# Setup stuff :P
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("400x480")
app.title("PyFsort")
app.configure(fg_color="#0d1117")
app.resizable(False, False)
app.iconbitmap(icon_path)

# Global var for the folder path!
folder = ""

# Frame header
frame_A = ctk.CTkFrame(
    master = app,
    fg_color="#151b23",
    width = 400,
    height = 50
)
frame_A.pack_propagate(False) # Stop frame from resizing to fit child
frame_A.pack(pady = 5, padx = 20, fill="x")

header = ctk.CTkLabel(
    frame_A,
    text = "📁 PyFsort",
    font = ("Arial", 24),
    text_color = "#f0f6fc"
)
header.pack(pady = 15)

# Simple seperator line
ctk.CTkFrame(app, height=2, fg_color="#3d444d").pack(fill="x", padx=20, pady=5)

# Choose a folder func
def select_folder():
    global folder
    folder = filedialog.askdirectory()
    print(folder)
    folder_textlabel.configure(text=folder)

# Middle Frame
frame_B = ctk.CTkFrame(
    master = app,
    fg_color="#151b23",
    width = 350,
    height = 105
)
frame_B.pack_propagate(False)
frame_B.pack(pady = 5, padx = 20, fill="x")

browse_btn = ctk.CTkButton(
    frame_B, 
    text = "Browse Folders",
    fg_color="#2F373F",
    hover_color="#30363d",
    text_color="#f0f6fc",
    command = select_folder,
    )
browse_btn.pack(pady=(15, 10), anchor = "center")

folder_textlabel = ctk.CTkLabel(
    frame_B,
    text = "",
    anchor = "center",
    fg_color="#0d1117",
    text_color="#f0f6fc",
    height = 35,
    width = 300
    )
folder_textlabel.pack(pady = 1, anchor = "center")

# The core logic, THE BRAIN OF THE ENTIRE THINGG!!!
def button_pressed():
    console_textbox.configure(state="normal")
    console_textbox.delete("0.0", "end")
    if folder == "":
        print("Empty Folder Location")
        console_textbox.insert("end", "Empty Folder Location")
        console_textbox.configure(state="disabled")
    else:
        with os.scandir(folder) as files:
            for entry in files:
                if entry.is_file():
                    filename, extensions = os.path.splitext(entry.name)
                    extensions = extensions.lower()
            
                    folder_path = os.path.join(folder, extensions)
            
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                
                    dest = os.path.join(folder_path, entry.name)
            
                    if not os.path.exists(dest):
                        shutil.move(entry.path, folder_path)
                        print("Moved: " + entry.name)
                        console_textbox.insert("end", "Moved: " + entry.name + "\n")
                    else:
                        print("Skipped (already exists): " + entry.name)
                        console_textbox.insert("end", "Skipped (already exists): " + entry.name + "\n")

            console_textbox.configure(state="disabled")

# Bottom frame
frame_C = ctk.CTkFrame(
    master = app,
    fg_color="#151b23",
    width = 350,
    height = 275
)
frame_C.pack_propagate(False)
frame_C.pack(pady = 5, padx = 20, fill="x")

sort_btn = ctk.CTkButton(
    frame_C,
    text = "Sort Files",
    fg_color="#238636",
    hover_color="#2ea043",
    text_color="#f0f6fc",
    command = button_pressed
)
sort_btn.pack(pady=(15, 10), anchor = "center")

console_textbox = ctk.CTkTextbox(
    frame_C,
    fg_color="#0d1117",
    text_color="#f0f6fc",
    height = 200,
    width = 300
)
console_textbox.pack(pady=0, anchor = "center")
console_textbox.configure(state="disabled")

# RUN THE APP WOW!
app.mainloop()
