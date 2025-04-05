import queue
import random
import time
import threading

import pyautogui
from utils.log.write_to_log import write_to_log

star_img = r'gameplay\utils\img\star.png'

def random_number():
    number = random.uniform(1, 3)
    return int(number)

def random_sleep():
    sleep_duration = random.uniform(0.25, 0.91)
    time.sleep(sleep_duration)

def get_latest(q):
    latest = None
    while True:
        try:
            latest = q.get_nowait()
        except queue.Empty:
            return latest

def locate_star_from_screenshot():
            try:
                locate_star = pyautogui.locateCenterOnScreen(r"gameplay\utils\img\star.png", confidence=0.8)
                star_is_visible = locate_star is not None 
                star_position = locate_star
                print('start found')
            except pyautogui.ImageNotFoundException:
                star_is_visible = False  
                star_position = None
                print('no star')
            
            return star_is_visible, star_position