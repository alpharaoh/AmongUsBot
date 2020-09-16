import os
os.system("cls")
print("\n[*] Warming up engine...\n")

from threading import Thread
from modules import module_grabscreen
from modules.config import *    

def startBot():
    os.system("python3 ./start_discordBot.py")

def startGrab():
    try:
        x, y = int(screen_resolution.split("x")[0]), int(screen_resolution.split("x")[1])
        module_grabscreen.grabScreen(x,y)
    
    except KeyboardInterrupt:
        print("\n[*] Stopping bot...")

    except Exception as e:
        print(e)

try:
    thread0 = Thread(target=startBot)
    thread1 = Thread(target=startGrab)

    thread0.start()
    thread1.start()

except Exception as e:
        print(e)
        exit()