### Summary

# This module takes an input as an image, converts the image to a string and determines 
# the game state and if the channel should be muted or unmuted and passes this to the 
# send command module

# -------------------------------------------------

from modules import module_sendcommand
web = module_sendcommand.web() # Python will initalise this object when this when program starts

from modules.config import *
from PIL import Image
import pytesseract #pip3 install pytesseract
import os
import time

# If you are getting pytesseract error, change r"C:\Program Files\Tesseract-OCR\tesseract.exe" to r"C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe" and 
# change USER to you computer name
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def processDiscussion(image: complex):
    found = False
    delay = 6

    delay_voting = 7 #Delay between voting ends and round starting
    discussion = {"?","impestoe","who",'whos',"wino","innoosttor?","imsoster?","inostor?","imposter?","inyoostor?","iniposior?","inijposior?","impostor?","inoster?","tnrpester?","tnsester?","inraostor?","inaoster?","tnsoster?","tnpester?",'hnnsester?'}
    voting = {"voting", "results","result","vetting","vartine","votingiresults","vetting)"}

    raw_output = pytesseract.image_to_string(image)

    if debug_mode:
        print(raw_output.strip().lower())
    
    out = set(raw_output.strip().lower().split(" "))

    if len(out.intersection(discussion)) != 0: #if one of the keywords for discussion time is present
        found = True
        print("DISCUSSION [UNMUTED]")
        web.unmute()

        return found

    elif len(out.intersection(voting)) != 0: #if one of the keywords for ended voting is present
        found = True
        print("VOTING ENDED [MUTING SOON]")

        time.sleep(delay + delay_voting)
        web.mute() #mute

        return found
    else:
        return found

def processEnding(image: complex):
    delay = 3.5 #Delay between getting role and game starting

    defeat = {"defeat","deteat"}
    victory = {"victory","vicory","viton"}
    imposter = {"imposter","impostor","tmonetor"}
    crewmate = {"crewmate"}
    
    raw_output = pytesseract.image_to_string(image)

    if debug_mode:
        print(raw_output.strip().lower())
    
    out = set(raw_output.strip().lower().split(" "))

    if len(out.intersection(defeat)) != 0: #if one of the keywords for defeat is present
        print("DEFEAT [UNMUTED]")
        web.unmute_and_clear() #unmute everyone including the dead

    elif len(out.intersection(victory)) != 0: #if one of the keywords for victory is present
        print("VICTORY [UNMUTED]")
        web.unmute_and_clear() #unmute everyone including the dead

    elif len(out.intersection(crewmate)) != 0: #if one of the keywords for crewmate is present
        print("YOU GOT CREWMATE [MUTING SOON]")

        time.sleep(delay + delay_start)
        web.mute() #mute

    elif len(out.intersection(imposter)) != 0: #if one of the keywords for imposter is present
        print("YOU GOT IMPOSTER [MUTING SOON]")

        time.sleep(delay + delay_start)
        web.mute() #mute
    else:
        pass
