### Summary

#PLEASE RUN THIS PROGRAM AND CHECK FOR ERRORS

# This is where you will set up configurations for your server
# This step is crucial for the program to work
# Please watch my tutorial at 

# -------------------------------------------------


chrome_driver_path = "./chromedriver.exe"
# To get this key go to https://discord.com/developers/applications/
# Click on bot
# Copy token
discord_bot_token = "*"
discord_channel = "*"

screen_resolution = "1920x1080"
adjust_x = 0 # adjust x by pixels. e.g. 3 = 3 pixels right, -2 = 2 pixles left
adjust_y = 0 # adjust y by pixels. e.g. 2 = 2 pixels up, -20 = 20 pixles down

# These scalars should only be adjusted if text isn't being correctly identified by start.py,
# or if you are debugging test.py to find the right fit. These operate as multipliers for the current resolution,
# so if you are operating at a non 1080p resolution, you will likely need to adjust these (use test.py and sample images)
discuss_offset_scalars = "0.08x0.18" # top x left
discuss_dimension_scalars = "0.7x0.25" # width x height
ending_offset_scalars = "0.065x0.22" # top x left
ending_dimension_scalars = "0.5x0.13" # width x height

time_delay = 0 # adjust time delay. 1 = one second more delay, -0.5 = 0.5 seconds less time

# time_delay is added or taken away from the delay set between when the screen 
# shows imposter, crewmate, or vote ended to when the round starts

debug_mode = False #Shows parsed output coming from image to text algorithm

test_window_type = "ending" # use "ending" or "discuss" to identify what window type test.py will test with
# test_window_type = "discuss"

# -------------------------------------------------










if __name__ == "__main__":
    try:
        import pytesseract # pip3 install pytesseract
        import threading 
        import selenium #pip3 install selenium
        import numpy
        import time
        import PIL # python3 -m pip install Pillow
        import mss # python3 -m pip install -U --user mss
        import cv2 # pip install opencv-python
        import os

        print("[*] No errors, your good to go!")
    except Exception as e: 
        print(f"{e}\n\n[*] Looks like your missing dependancies\n[*] Watch: ")
        exit()
