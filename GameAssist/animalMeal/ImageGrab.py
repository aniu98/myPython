#  pip install pillow
from PIL import ImageGrab
import numpy as np
import cv2


print("start")
screenshot = ImageGrab.grab()
x=5
y=50
width=467
height=854
screenshot = ImageGrab.grab(bbox=(x,y,width,height))


screenshot_array = np.array(ImageGrab.grab(bbox=(x,y,width,height)))
# 用下面的方法是转换色差
screenshot_array = cv2.cvtColor(screenshot_array, cv2.COLOR_BGR2RGB)


# cv2.imshow('screenshot',screenshot_array)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

while True:
    image_array = np.array(ImageGrab.grab(bbox=(x,y,width,height)))
    image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    cv2.imshow('screen monitoring',image_array)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
