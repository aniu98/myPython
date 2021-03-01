import time
#pip install eventlet
import eventlet

eventlet.monkey_patch()
with eventlet.Timeout(2, False):  # 设置超时时间为2秒
    time.sleep(3)
    print('超过时长的将不再运行')
print('其他操作')
