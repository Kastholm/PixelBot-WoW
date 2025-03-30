import json
import time
from mss import mss
import cv2 as cv
import numpy as np
import pyautogui
from pyautogui import ImageNotFoundException
import pytesseract

from screen import convert_scr_to_string, record_part_of_screen, monitor
pytesseract.pytesseract.tesseract_cmd = r'utils\Tesseract-OCR\tesseract.exe'

class RecordCoordinatesAgent:

    def __init__(self, toggle_screenshot_threads, queued_coordinates_indicator):
        self.screenshot = None
        self.resized_screenshot = None
        self.toggle_screenshot_threads = toggle_screenshot_threads
        self.queued_coordinates_indicator = queued_coordinates_indicator
        # Monitor

    def record_screen(self):
        with mss() as sct:
            while True:
                if self.toggle_screenshot_threads.is_set():
                
                    with open(r"screen\utils\bar_axises.json", "r") as file:
                        data = json.load(file)
                    self.screenshot = sct.grab(monitor) #Capture the entire computer screen
                    self.screenshot = np.array(self.screenshot) #Convert screenshot into an array so cv can read it
                    self.resized_screenshot = cv.resize(self.screenshot, (0,0), fx=0.9, fy=0.9) #Resize the screenshot

                    coordinates_scr = record_part_of_screen(
                        "Coordinates", self.resized_screenshot,
                        top=data['bar_axises']['coordinates_bar_axis']['top'],
                        left=data['bar_axises']['coordinates_bar_axis']['left'],
                        w=data['bar_axises']['coordinates_bar_axis']['width'],
                        h=data['bar_axises']['coordinates_bar_axis']['height']
                    )

                    coordinates = convert_scr_to_string(coordinates_scr)
                    self.queued_coordinates_indicator.put(coordinates)

                    cv.waitKey(1)
                else:
                    self.toggle_screenshot_threads.wait() 
                
                time.sleep(0.1)