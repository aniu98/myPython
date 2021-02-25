# pip install pynput
from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import threading

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        runJob(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def click(threadName,delay,x,y,num):
    mouse = Controller()
    mouse.position=(x, y)
    print('The current pointer position is {0} and time is {1}'.format(
            mouse.position, time.ctime(time.time())))
    for i in range(1,num):
        if exitFlag:
            break
        time.sleep(delay)
        # print ("%s: %s" % (threadName, time.ctime(time.time())))
        mouse.position=(x, y)
        mouse.click(Button.left, 1)
def runJob(threadName, delay, counter):
    while counter:
        if exitFlag:
            break
        # 广告
        print("50s see ads ")
        click(threadName,50,1791,790,2)
        # 确认
        print("3s   confirm  ")
        click(threadName,2,1695,550,2)
        # 确认
        print("3s   mute  ")
        click(threadName,2,1839,77,2)
        # 关闭
        print("32s close")
        click(threadName,30,1882,77,2)

        # time.sleep(50)
        # for x in range(1,5):
        #     click(threadName,1,1609,387,2)
        #     click(threadName,1,1694,387,2)
        #     click(threadName,1,1809,387,2)
        #     click(threadName,1,1609,519,2)
        #     click(threadName,1,1694,519,2)
        #     click(threadName,1,1809,519,2)


        # # 广告
        # print("50s see ads ")
        # click(threadName,50,233,582,2)
        # # 确认
        # print("3s   confirm  ")
        # click(threadName,2,160,409,2)
        # # 确认
        # print("3s   mute  ")
        # click(threadName,2,246,77,2)
        # # 关闭
        # print("32s close")
        # click(threadName,30,290,77,2)

        # time.sleep(40)


thread1 = myThread(1, "Thread-1", 0.2)
thread1.start()
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        exitFlag=1
        print(exitFlag)
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
exitFlag=1
print(exitFlag)
print("exitFlag")

