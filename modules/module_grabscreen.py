### Summary

# This module grabs an image from the screen and funnels
# it to the processing module

# -------------------------------------------------

from mss import mss # python3 -m pip install -U --user mss
import cv2 # pip install opencv-python
from PIL import Image # python3 -m pip install Pillow
import numpy as np
import time
from modules import module_process
from modules.config import *

def returnFrame(settings: set, sct):
    #Take image of screen
    sct_img = sct.grab(settings)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    return frame

def grabScreen(xResolution: int, yResolution: int):
    settings = {"top": int(0.08 * yResolution) + adjust_y, "left":int(xResolution * 0.18) + adjust_x, "width":int(xResolution * 0.7), "height":int(0.25 * yResolution), "mon": monitor_number}

    first_time = True

    x_crop = int(xResolution * 0.18)
    y_crop = int(yResolution * 0.08)

    with mss() as sct:
        while True:
            frame = returnFrame(settings, sct)
            
            try:
                #Crop image to fit only "voting ended" and "whos the imposter?"
                cropped_frame = frame[10:(y_crop + y_extend_crop), int(x_crop/2 - x_extend_crop + 80):-int(x_crop/2 + x_extend_crop)].copy()
            
                if debug_mode:
                    cv2.imshow('Test', np.array(frame)) #output screen, for testing only
                    cv2.imshow('Test Cropped', np.array(cropped_frame)) #output screen, for testing only

            except Exception as e:
                print(f"{e}\nLooks like your x_extend_crop or y_extend_crop values are way too high")
                exit()

            if first_time:
                print("Ready.\nYou can play now.\n")
                first_time = False

            #Process image
            found = module_process.processDiscussion(cropped_frame)

            if found == False: #If discussion or voting ends found, you dont need to process ending
                found = module_process.processEnding(frame)

            if cv2.waitKey(25) & 0xFF == ord('q'): #Press Q on debug windows to exit
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    print("Please run start.py: ")
    exit()
