# -*- coding:utf-8 -*-

import win32gui
import time
from pynput.mouse import Button, Controller
from pynput import keyboard

import numpy
from PIL import ImageGrab, Image
import cv2


class animalMealAssist(object):
	"""docstring for animalMealAssist"""
	def __init__(self, wdName):
		super(animalMealAssist, self).__init__()
		self.wdName = wdName
		# 获得窗口句柄
		self.hwnd=win32gui.FindWindow(0, wdname)
		if not self.hwnd:
			print("没有找到窗口,请确认窗口名称:【%s】"% wdname)
			exit()
		# 窗口显示在最前面
		win32gui.SetForegroundWindow(self.hwnd)
		self.position=win32gui.GetWindowRect(self.hwnd)
		

	def screenshot(self):
		image = ImageGrab.grab(self.position)
		
	def start(self):
		print(self.position)
	def showMonitor(self):
		while True:
			image = ImageGrab.grab(self.position)
			image_array= cv2.cvtColor(numpy.array(image), cv2.COLOR_BGR2RGB)
			cv2.imshow(u'showMonitor',image_array)
			if  cv2.waitKey(25) & 0xFF == ord('q'):
				cv2.destroyAllWindows()
				break
if __name__ == "__main__":
    # wdname 为动物餐厅窗口的名称，必须写完整
    wdname = u'动物餐厅'
    demo = animalMealAssist(wdname)
    demo.showMonitor()
