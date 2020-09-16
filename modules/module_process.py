### Summary

# This module takes an input as an image, converts the image to a string and determines 
# the game state

# -------------------------------------------------

import requests
from modules.config import *
from PIL import Image
import pytesseract #pip3 install pytesseract
import os
import time

# If you are getting pytesseract error, change r"C:\Program Files\Tesseract-OCR\tesseract.exe" to r"C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe" and 
# change USER to you computer name
#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def processDiscussion(image: complex) -> int:
    #1 = Not found, 2 = Discussion found, 3 = Voting ended found

    discussion = {"?","impestoe","who",'whos',"wino","innoosttor?","imsoster?","inostor?","imposter?","inyoostor?","iniposior?","inijposior?","impostor?","inoster?","tnrpester?","tnsester?","inraostor?","inaoster?","tnsoster?","tnpester?",'hnnsester?'}
    discussion.update(keyword_whos_imposter)
    voting = {"voting", "results","result","vetting","vartine","votingiresults","vetting)","\\n\\nvatiing","results\\n\\n","resulis\\n\\n","resuilis\\n\\n","resulis","resuilis"}
    discussion.update(keyword_voting_ended)
    raw_output = pytesseract.image_to_string(image)
    
    out = set(raw_output.strip().strip('\n').strip("\\").strip("/").lower().split(" "))

    if debug_mode:
        print(out)

    if len(out.intersection(discussion)) != 0: #if one of the keywords for discussion time is present
        print("DISCUSSION [UNMUTED]")
        requests.get(f"http://{address}:{port}/unmute")

        return 2

    elif len(out.intersection(voting)) != 0: #if one of the keywords for ended voting is present
        print("VOTING ENDED [MUTING SOON]")

        return 3
    else:
        return 1

def processEnding(image: complex) -> bool:
    delay = 3.5 #Delay between getting role and game starting

    defeat = {"defeat","deteat","netrtorat","neffeat","netfeat","defeat\\n\\n"}
    defeat.update(keyword_defeat)
    victory = {"victory","vicory","viton"}
    victory.update(keyword_victory)
    imposter = {"imposter","impostor","tmonetor"}
    imposter.update(keyword_imposter)
    crewmate = {"crewmate"}
    crewmate.update(keyword_crewmate)
    
    raw_output = pytesseract.image_to_string(image)
    
    out = set(raw_output.strip().strip('\n').strip("\\").strip("/").lower().split(" "))
    
    if debug_mode:
        print(out)

    if len(out.intersection(defeat)) != 0: #if one of the keywords for defeat is present
        print("DEFEAT [UNMUTED]")
        requests.get(f"http://{address}:{port}/clear") #unmute everyone including the dead
        return True

    elif len(out.intersection(victory)) != 0: #if one of the keywords for victory is present
        print("VICTORY [UNMUTED]")
        requests.get(f"http://{address}:{port}/clear") #unmute everyone including the dead
        return True

    elif len(out.intersection(crewmate)) != 0: #if one of the keywords for crewmate is present
        print("YOU GOT CREWMATE [MUTING SOON]")

        time.sleep(delay + delay_start)
        requests.get(f"http://{address}:{port}/mute") #mute
        return False

    elif len(out.intersection(imposter)) != 0: #if one of the keywords for imposter is present
        print("YOU GOT IMPOSTER [MUTING SOON]")

        time.sleep(delay + delay_start)
        requests.get(f"http://{address}:{port}/mute") #mute
        return False
    else:
        print(".")
        return False

if __name__ == "__main__":
    print("[*] Please run start.py: ")
    exit()