import json
from mss import mss
import cv2 as cv
import numpy as np
from pyautogui import ImageNotFoundException
import pyautogui    
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


screen_width, screen_height = pyautogui.size()
monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}

colors = {
    "RED": {"lower": (0, 100, 100), "upper": (10, 255, 255)},
    "GREEN": {"lower": (40, 100, 100), "upper": (80, 255, 255)},
    "BLUE": {"lower": (100, 100, 100), "upper": (140, 255, 255)},
    "MAGENTA": {"lower": (140, 100, 100), "upper": (160, 255, 255)},
    "YELLOW": {"lower": (25, 100, 100), "upper": (35, 255, 255)}
}
        
def cv_text_input(screenshot, text, pos, clr): # Display text on cv screen
    text = cv.putText(screenshot, text, (pos), cv.FONT_HERSHEY_DUPLEX,  1, (clr), 2, cv.LINE_AA)
    return text

def record_part_of_screen(name, scr, top, left, w, h):
    scr = scr[top:top+h, left:left+w] #Define scr from Numpy array
    cv.imshow(name, scr)
    return scr

def calculate_scr_clrBlack_procentage(scr):
    convert_scr_BGR_to_HSV = cv.cvtColor(scr, cv.COLOR_BGR2HSV)
    count_notBlack_pixels = cv.countNonZero(cv.cvtColor(scr, cv.COLOR_BGR2GRAY)) #Convert to graytone and count pixels not 0 which is = not black
    count_all_pixels = convert_scr_BGR_to_HSV.shape[0] * convert_scr_BGR_to_HSV.shape[1] #Count all pixels available in screenshot
    if count_all_pixels == 0:
        return 0
    calculate_to_percentage = int(np.round(count_notBlack_pixels / count_all_pixels, 2) * 100)  #Calculate percentage number
    return calculate_to_percentage

""" def convert_scr_to_string(scr):
    scr = cv.resize(scr, (0,0), fx=0.5, fy=0.5) #resize
    string = pytesseract.image_to_string(scr).strip()
    return string 
    Dette er den gamle version, måske den stadig er nødvendig
    """

def convert_scr_to_string(scr):
    scr = cv.cvtColor(scr, cv.COLOR_BGR2GRAY)
    scr = cv.threshold(scr, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(scr, config='--psm 7')
    return text

def define_which_color_status_shows(scr):
    convert_scr_BGR_to_HSV = cv.cvtColor(scr, cv.COLOR_BGR2HSV)
    for color, ranges in colors.items():
        mask = cv.inRange(convert_scr_BGR_to_HSV, np.array(ranges['lower']), np.array(ranges['upper'])) #Make a mask
        detected_pixels = cv.countNonZero(mask) #Count how many pixels fits the provided HSV color
        if detected_pixels > 80:
            return color
    return "No Color"