print("[*] Position the windows so the text fits niceley inside the window!")

from mss import mss
import cv2
from PIL import Image
import numpy as np
import time

from modules.config import *

x, y = int(screen_resolution.split("x")[0]), int(screen_resolution.split("x")[1])

settings = {"top": int(0.08 * y) + adjust_y, "left":int(x * 0.18) + adjust_x, "width":int(x * 0.7), "height":int(0.25 * y), "mon": monitor_number}

sct = mss()

x_crop = int(x * 0.18)
y_crop = int(y * 0.08)

x_extend_crop = 150#pixels
y_extend_crop = 50#pixels

while True:
    sct_img = sct.grab(settings)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    try:
        crop_img = img_bgr[10:int(0.08 * y) + y_extend_crop, int(x_crop/2 - x_extend_crop + 80):-int(x_crop/2 + x_extend_crop)].copy()
        cv2.imshow('"Whos the imposter?" "Voting Ended" [TEST]"', np.array(crop_img))
        cv2.imshow('"Imposter" "Crewmate" "Defeat" "Victory" [TEST]"', np.array(img_bgr))

    except Exception as e:
        print(f"{e}\nLooks like your x_extend_crop or y_extend_crop values are way too high")
        exit()

    time.sleep(1) #Helps debugging

    #cv2.imshow('Among Us Test', np.array(img_bgr))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break