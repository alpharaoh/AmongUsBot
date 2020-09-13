### Summary

# Run this to start the program

# -------------------------------------------------

import os
os.system("cls")
print("\n[*] Warming up engine...\n\n")
print("[*] A chrome window will open now...\n[*] Enter your discord credentials in the window before we start")
from modules import module_grabscreen
from modules.config import *

def grabScreen(self):
    module_grabscreen.grabScreen(self.x, self.y)

if __name__ == "__main__":
    try:
        x, y = int(screen_resolution.split("x")[0]), int(screen_resolution.split("x")[1])
    except Exception as e:
        print(f'{e}\n\nSet a valid resolution: e.g. "1366x768" (keeping the quotation marks)')

    module_grabscreen.grabScreen(x,y)
