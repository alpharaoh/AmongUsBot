from mss import mss
import cv2
from PIL import Image
import numpy as np
import time

from modules.config import *

x, y = int(screen_resolution.split("x")[0]), int(screen_resolution.split("x")[1])

mon = {'top': int(0.1*y) + adjust_y, 'left':int(x*0.18) + adjust_x, 'width':int(x*0.7), 'height':int(0.25*y)}

sct = mss()

while 1:
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    time.sleep(1)

    cv2.imshow('Among Us Test', np.array(img_bgr))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
