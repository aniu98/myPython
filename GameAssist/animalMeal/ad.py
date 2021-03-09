# -*- coding:utf-8 -*-
from pynput.mouse import Button, Controller
from pynput import keyboard
import time

exitFlag = False

def click(x, y, delay, num=2):
    mouse = Controller()
    mouse.position = (x, y)
    for i in range(1, num):
        i=i
        if exitFlag: 
            break
        time.sleep(delay)
        mouse.position = (x, y)
        mouse.click(Button.left, 1)
def main():
    for x in range(0, 110):
        if exitFlag:
            break
        print("start click ad %s " % x)
        # # 升级动物
        # click(1666,696,2)

        # 调鱼
        # click(1770,453,2)

        # 宣传
        # if x == 0:
        #     click(1791, 790, 2)
        # else:
        #     click(1791, 790, 50)

        # click(1695, 550, 2)

        # 许愿池
        time.sleep(1.5)
        click(1873,760,0.08,100*4)
        click(1700,624,1)
        click(1693,561,1.5)

        # mute
        click(1839, 77, 2)
        print("close ad after 30s %s" % time.ctime(time.time()))
        click(1882, 77, 32)


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(key))
    global exitFlag
    if key == keyboard.Key.esc:
        # Stop listener
        exitFlag = True
        print(exitFlag)
        return False
if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    main()
    print("---------end--------------")
