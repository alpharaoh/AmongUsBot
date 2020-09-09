### Summary

#PLEASE RUN THIS PROGRAM AND CHECK FOR ERRORS

# This is where you will set up configurations for your server
# This step is crucial for the program to work
# Please watch my tutorial at 

# -------------------------------------------------


chrome_driver_path = "./chromedriver"
# To get this key go to https://discord.com/developers/applications/
# Click on bot
# Copy token
discord_bot_token = "*"
discord_channel = *""


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
