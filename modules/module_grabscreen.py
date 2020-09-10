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

def grabDiscussionTitle(xResolution: int, yResolution: int):
    
    settings = {'top': int(0.08 * yResolution) + adjust_y, 'left':int(xResolution * 0.18) + adjust_x, 'width':int(xResolution * 0.7), 'height':int(0.25 * yResolution)}

    sct = mss()

    first_time = True

    while True:
        #Take image of screen
        sct_img = sct.grab(settings)
        img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        if first_time:
            print("Ready.\nYou can play now.\n")
            first_time = False

        #Process image
        module_process.processDiscussion(frame)

def grabEndingScreen(xResolution: int, yResolution: int):
    settings = {'top': int(0.065 * yResolution) + adjust_y, 'left':int(xResolution * 0.22) + adjust_x, 'width':int(xResolution * 0.5), 'height':int(0.13 * yResolution)} 

    sct = mss()

    while True:
        #Take image of screen
        sct_img = sct.grab(settings)
        img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # time.sleep(1)
        # cv2.imshow('Test', np.array(frame)) #output screen, for testing only

        module_process.processEnding(frame)

        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break

if __name__ == "__main__":
    print("Please run start.py: ")
    exit()
