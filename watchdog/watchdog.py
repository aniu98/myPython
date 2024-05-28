# pip install watchdog

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
  
# 自定义的事件处理类，继承于FileSystemEventHandler
class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # 文件被修改时触发的事件处理函数
        print(f"File modified: {event.src_path}")

# 创建观察者对象和事件处理对象
event_handler = MyEventHandler()
observer = Observer()

# 需要监控的文件夹路径
folder_path = "E:\\workspace\\github\\algorithm-visualizer"

# 将观察者对象与事件处理对象关联，并启动观察
observer.schedule(event_handler, folder_path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()