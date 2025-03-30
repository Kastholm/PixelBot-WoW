import queue
import threading
from tkinter import messagebox
import customtkinter as ctk
import cv2

from gameplay.main import BotAgent
from gui.main import GuiAgent
from screen.combat_indicator import CombatIndicatorAgent
from screen.coordinates import RecordCoordinatesAgent
from screen.enemy import EnemyAgent
from screen.player import PlayerAgent
from PIL import Image, ImageTk

class ThreadManager:

    def __init__(self):
        self.program_started_before = False
        self.screenshots_are_running = False

        self.toggle_screenshot_threads = threading.Event()
        self.toggle_bot_thread = threading.Event()

        self.queued_coordinates_indicator = queue.Queue()
        self.queued_combat_indicator = queue.Queue()
        self.queued_enemy_indicator = queue.Queue()
        self.queued_health_indicator = queue.Queue()
        
        self.coordinates_agent = RecordCoordinatesAgent(self.toggle_screenshot_threads, self.queued_coordinates_indicator)
        self.combat_indicator_agent = CombatIndicatorAgent(self.toggle_screenshot_threads, self.queued_combat_indicator)
        self.enemy_agent = EnemyAgent(self.toggle_screenshot_threads, self.queued_enemy_indicator)
        self.player_agent = PlayerAgent(self.toggle_screenshot_threads, self.queued_health_indicator)
        self.bot_agent = BotAgent(self.toggle_bot_thread)


        self.threads = {
            'coordinates': threading.Thread(target=self.coordinates_agent.record_screen),
            'combat_indicator': threading.Thread(target=self.combat_indicator_agent.record_screen),
            'enemy_indicator': threading.Thread(target=self.enemy_agent.record_screen),
            'player_indicator': threading.Thread(target=self.player_agent.record_screen),
            'bot_indicator': threading.Thread(target=self.bot_agent.start_bot)
        }


    def toggle_screenshot(self):
        if self.toggle_screenshot_threads.is_set():
            self.toggle_bot_thread.clear()
            self.toggle_screenshot_threads.clear()
            self.screenshots_are_running = False
        else:
            if self.program_started_before == False:
                for thread in self.threads.values():
                    thread.start()
                self.program_started_before = True
            self.screenshots_are_running = True
            self.toggle_screenshot_threads.set()

    def toggle_bot(self):
        if self.toggle_screenshot_threads.is_set():
            if self.toggle_bot_thread.is_set():
                self.toggle_bot_thread.clear()
            else:
                self.toggle_bot_thread.set()
        else:
            self.toggle_bot_thread.clear()
            messagebox.showerror("Fejl", "Screen Recorder kører ikke")


    def gui_button_layout(self, app):
        button_frame = ctk.CTkFrame(master=app, width=600)
        buttons = [
            {'name': 'pixel_button', 'path': 'utils/img/pixel_button.png', 'thread': self.toggle_screenshot},
            {'name': 'bot_button', 'path': 'utils/img/bot_button.png', 'thread': self.toggle_bot}
        ]
        for button in buttons:
            img = ctk.CTkImage(Image.open(button['path']), size=(160, 50))
            ctk.CTkButton(button_frame, text='', image=img, width=160, 
                        height=50, hover_color='#2b2b2b', bg_color='#33373c', fg_color='transparent', 
                        compound="left", command=button['thread']).pack()
        
        button_frame.grid(row=0, column=0, sticky="s")

def start_gui(thread_manager):
    app = ctk.CTk()
    GuiAgent(app)
    thread_manager.gui_button_layout(app)
    app.mainloop()

if __name__ == "__main__":
    tm = ThreadManager()
    gui_thread = threading.Thread(target=start_gui, args=(tm,))
    gui_thread.start()
    gui_thread.join()