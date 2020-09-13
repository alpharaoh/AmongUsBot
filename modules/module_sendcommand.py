### Summary

# This module will send messages to run the commands on behalf of user since
# discord does not allow bots to run commands we have to use selenium library

# -------------------------------------------------

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from modules.config import *
import time

class web:
    def __init__(self):
        self.muted = False
        self.site = discord_channel
        path = chrome_driver_path
        self.driver = webdriver.Chrome(path)
        self.driver.get(self.site)

        self.xPath = "//div[@class='markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP']" #Find chatbox for discord

        try:
        #Wait 120s for user to login to discord or else quit program
            WebDriverWait(self.driver, 120).until(
                        EC.presence_of_element_located((By.XPATH, self.xPath)), message='Sorry, you took too long.')
            print("\n[*] Starting engine... \n[*] This may take a moment...\n")

        except Exception as e:
            print(e)
            exit()
    
    def unmute_and_clear(self):
        #When the game ends
        if self.muted == False:
            pass
        else:
            text_box = self.driver.find_element_by_xpath(self.xPath)
            text_box.send_keys(".unmute_and_clear" + Keys.ENTER) #This unmutes and clears the list of people that died
            self.muted = False

    def mute(self):
        if self.muted == True:
            pass
        else:
            text_box = self.driver.find_element_by_xpath(self.xPath)
            text_box.send_keys(".mute" + Keys.ENTER)
            self.muted = True

    def unmute(self):
        if self.muted == False:
            pass
        else:
            text_box = self.driver.find_element_by_xpath(self.xPath)
            text_box.send_keys(".unmute" + Keys.ENTER)
            self.muted = False
