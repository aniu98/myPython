# pip install pynput
# import pyttsx3
from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import threading

exitFlag = 0
# engine = pyttsx3.init()
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程: " + self.name)
        runJob(self.name, self.counter, 5)
        print ("退出线程: " + self.name)
def breakDo():
    mouse = Controller()
    # mouse.position=(262, 27)
    mouse.click(Button.left, 1)
def click(threadName,delay,x,y,num):
    mouse = Controller()
    mouse.position=(x, y)
    # print('The current pointezr position is {0} and time is {1}'.format( mouse.position, time.ctime(time.time())))
    for i in range(1,num):
        if exitFlag:
            breakDo()
            break
        time.sleep(delay)
        # print ("%s: %s" % (threadName, time.ctime(time.time())))
        mouse.click(Button.left, 1)
def runJob(threadName, delay, counter):
    count=1
    while counter:
        if exitFlag:
            breakDo()
            break
        # click(threadName,delay,138,387,2)
        # click(threadName,delay,1694,387,2)
        # click(threadName,delay,1809,387,2)
        # click(threadName,delay,138,519,2)
        # click(threadName,delay,1694,519,2)
        # click(threadName,delay,1809,519,2)

        # click(threadName,delay,1653,402,2)
        # click(threadName,delay,1746,386,2)
        # click(threadName,delay,1846,391,2)
        # click(threadName,delay,1659,530,2)
        # click(threadName,delay,1747,531,2)
        # click(threadName,delay,1851,537,2)

        # click(threadName,delay,1662,630,2)
        # click(threadName,delay,1664,721,2)
        # click(threadName,delay,1532,366,2)

        # click(threadName,delay,1873,760,21)
        # 3333333333333333333
        # 点餐
        click(threadName,delay,1609,387,2)
        click(threadName,delay,1694,387,2)
        click(threadName,delay,1809,387,2)
        click(threadName,delay,1609,519,2)
        click(threadName,delay,1694,519,2)
        click(threadName,delay,1809,519,2)

        # 收钱
        # click(threadName,delay,1653,402,2)
        # click(threadName,delay,1746,386,2)
        # click(threadName,delay,1846,391,2)
        # click(threadName,delay,1659,530,2)
        # click(threadName,delay,1747,531,2)
        # click(threadName,delay,1851,537,2)

        # click(threadName,delay,1549,384,2)
        # click(threadName,delay,1662,658,2)
        # click(threadName,delay,1664,721,2)
        

        # 手机宣传
        click(threadName,0.08,1873,760,31*15)
        # click(threadName,0.03,289,572,32*5)
        count=count+1
        print(count)
        # 在线1h
        click(threadName,0.08,1692,558,2)
        # 领取
        click(threadName,0.08,1800,565,2)
        # 教育孩子
        click(threadName,0.08,1600,728,2)
        if count%60==0:
            # engine.say('我要开始休息5分钟了')
            print("{0} : start sleep 5min".format(time.ctime(time.time())))
            # time.sleep(8)
            print("{0} : sleep 5min end ".format(time.ctime(time.time())))
            # engine.say('休息结束了')
            # engine.runAndWait()
        # time.sleep(20)
thread1 = myThread(1, "Thread-1", 0.08)
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
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()
exitFlag=1
print(exitFlag)
print("exitFlag runAndWait")

thread1.join()
print("主线程结束")
