# -*- coding:utf-8 -*-
import numpy as np
# 这么写为了vscode 不抒错
from cv2 import cv2
from PIL import ImageGrab
# pip install pywin32
from win32 import win32gui
# from win32gui import FindWindow, GetWindowRect

while True:
    window_name = u'动物餐厅'
    id = win32gui.FindWindow(0, window_name)
    bbox = win32gui.GetWindowRect(id)
    image_array = np.array(ImageGrab.grab(bbox=bbox))
    image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    cv2.imshow('screenshot',image_array)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
