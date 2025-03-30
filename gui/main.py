import json
import os
from tkinter import END
import customtkinter as ctk
from PIL import Image, ImageTk

class GuiAgent:
    def __init__(self, app):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        img = Image.open('gui/utils/img/logo.png')
        resized_img = img.resize((200, 150), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(resized_img)
        self.app = app
        self.height = 700
        self.app.geometry(f"900x{self.height}")
        self.app.title("CustomTkinter")
        self.details = [
            {'name': 'Health', 'info': '0'},
            {'name': 'Combat Indicator', 'info': 'No combat'}
        ]
        self.main_frame = ctk.CTkFrame(master=self.app, width=600, height=self.height)
        self.left_frame = ctk.CTkFrame(master=self.app, width=300, height=self.height , bg_color='#33373c',
                                       fg_color='#33373c')
        self.textbox = ctk.CTkTextbox(master=self.main_frame , width=600, height=self.height, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.load_gui()
        self.live_bot_updates()

    def text_input(self, frame, text, info):
        label = ctk.CTkLabel(frame, text=info, fg_color="transparent")
        entry = ctk.CTkEntry(frame, placeholder_text=text)
        label.pack()
        entry.pack()
    
    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)

    def map_selection(self):
        path_to_json = 'gameplay\maps'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        
        label = ctk.CTkLabel(self.left_frame, text="Choose your map", fg_color="transparent", width=300)
        optionmenu = ctk.CTkOptionMenu(self.left_frame, width=220, 
                                       values=json_files,
                                         command=self.optionmenu_callback)
        optionmenu.set("None")

        label.pack()
        optionmenu.pack()

    def sidebar(self):
        logo_label = ctk.CTkLabel(self.left_frame, image=self.logo, text='', width=300).pack()
        self.map_selection()

    def live_bot_updates(self):
        try:
            with open("gui/utils/log/log.txt", "r", encoding="utf-8") as file:
                content = file.read()
        except Exception as e:
            content = f"Error: {e}"
        self.textbox.delete("0.0", END)
        self.textbox.insert("0.0", content)
        self.app.after(100, self.live_bot_updates)

    def clear_bot_update_textfield(self):
        with open("gui/utils/log/log.txt", "w", encoding="utf-8") as file:
            file.write("")
        self.textbox("1.0", END)

    def load_gui(self):
        # Configure grid for the main window
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)

        # Place frames using grid
        self.left_frame.grid(row=0, column=0, sticky="ns")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        clear_btn = ctk.CTkButton(self.main_frame, bg_color='#2b2b2b', fg_color='darkred', text='Clear', command=self.clear_bot_update_textfield)
        clear_btn.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

        self.sidebar()
        
        #for detail in self.details:
        #    self.text_input(self.main_frame, detail['name'], detail['info'])



        #progressbar = ctk.CTkProgressBar(self.app, orientation="horizontal").pack()
        