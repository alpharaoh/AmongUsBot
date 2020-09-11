from mss import mss
import cv2
from PIL import Image
import numpy as np
import time

from modules import module_process
from modules.config import *

x, y = int(screen_resolution.split("x")[0]), int(screen_resolution.split("x")[1])

if test_window_type == "discuss":
    top, left = float(discuss_offset_scalars.split("x")[0]), float(discuss_offset_scalars.split("x")[1])
    width, height = float(discuss_dimension_scalars.split("x")[0]), float(discuss_dimension_scalars.split("x")[1])
elif test_window_type == "ending":
    top, left = float(ending_offset_scalars.split("x")[0]), float(ending_offset_scalars.split("x")[1])
    width, height = float(ending_dimension_scalars.split("x")[0]), float(ending_dimension_scalars.split("x")[1])
else:
    print("Invalid test_window_type specified")
    exit
    

mon = {'top': int(top*y) + adjust_y, 'left':int(x*left) + adjust_x, 'width':int(x*width), 'height':int(height*y)}

sct = mss()

while 1:
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    time.sleep(1)

    if test_window_type == "discuss":
        module_process.processDiscussion(img_bgr)
    elif test_window_type == "ending":
        module_process.processEnding(img_bgr)

    cv2.imshow('Among Us Test', np.array(img_bgr))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
