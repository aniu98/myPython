from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import threading

exitFlag = False

def click(x, y, delay, num=2):
    mouse = Controller()
    mouse.position = (x, y)
    for i in range(1, num):
        i=i
        time.sleep(delay)
        mouse.position = (x, y)
        mouse.click(Button.left, 1)

def seeAd(x,y,delay):
    click(x, y, delay)
    # 静音
    click(1839, 77, 1.5)
    print("close ad after 30s %s" % time.ctime(time.time()))
    click(1882, 77, 32)

def breakDo():
    pass
    # mouse = Controller()
    # mouse.position=(262, 27)
    # mouse.click(Button.left, 1)
def main():
    while True:
        if exitFlag:
            breakDo()
            break
        time.sleep(1)
        print("sss")
    
class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        main()


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    global exitFlag
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        exitFlag = True
        return False
keyboard.Listener(on_press=on_press, on_release=on_release).start()

if __name__ == '__main__':
    thread1 = myThread()
    thread1.start()
    thread1.join()
    print("---------end--------------")
