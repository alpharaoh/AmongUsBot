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

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def processDiscussion(image: complex):
    delay = 7 #Delay between voting ends and round starting
    discussion = {"?","who",'whos',"imposter?","iniposior?","inijposior?","impostor?","inoster?","tnrpester?","tnsester?","inraostor?","inaoster?","tnsoster?","tnpester?",'hnnsester?'}
    voting = {"voting", "results","result","vetting","vartine"}

    raw_output = pytesseract.image_to_string(image)

    if debug_mode:
        print(raw_output.strip().lower())
    
    out = set(raw_output.strip().lower().split(" "))

    if len(out.intersection(discussion)) != 0: #if one of the keywords for discussion time is present
        print("DISCUSSION [UNMUTED]")
        web.unmute()

    elif len(out.intersection(voting)) != 0: #if one of the keywords for ended voting is present
        print("VOTING ENDED [MUTING SOON]")

        time.sleep(delay + time_delay)
        web.mute() #mute

def processEnding(image: complex):
    delay = 4 #Delay between getting role and game starting
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
        web.unmute()

    elif len(out.intersection(victory)) != 0: #if one of the keywords for victory is present
        print("VICTORY [UNMUTED]")
        web.unmute()

    elif len(out.intersection(crewmate)) != 0: #if one of the keywords for crewmate is present
        print("YOU GOT CREWMATE [MUTING SOON]")

        time.sleep(delay + time_delay)
        web.mute() #mute

    elif len(out.intersection(imposter)) != 0: #if one of the keywords for imposter is present
        print("YOU GOT IMPOSTER [MUTING SOON]")

        time.sleep(delay + time_delay)
        web.mute() #mute
    else:
        pass
