import time
import pyautogui
from pynput.keyboard import Key, Controller
from cv2 import cv2
import mss
import numpy

base ='e:/workspace/github/myPython/GameAssist/animalMeal/opencv/'

tree1 = cv2.imread(base+'tanhao.png', 0)
tw, th = tree1.shape[::-1]
tw1,th1 =tree1.shape
print(tw1)
print(tree1.shape[1])
print(tw)

print(th)
img_BGR = cv2.imread(base+'aniu.png')
for x in range(1,1000):
    print(x)
    # 读取背景
    
    # 展示
    cv2.imshow('OpenCV/Numpy normal', img_BGR)
    img_gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
    cv2.imshow("open gray", img_gray)

    res2 = cv2.matchTemplate(img_gray, tree1, cv2.TM_CCOEFF_NORMED)
    print(res2)

    threshold = 0.65

    loc = numpy.where(res2 >= threshold)
    print(loc)

    for pt in zip(*loc[::-1]):
        print(pt)
        cv2.rectangle(img_BGR, pt, (pt[0] + tw, pt[1] + th), (0, 0, 255), 10)
        if pt[0] + tw < 280:
            print("ssss")
            break
    cv2.imshow("zheng fanxing", img_gray)
    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
