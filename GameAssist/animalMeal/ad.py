# -*- coding:utf-8 -*-
from pynput.mouse import Button,Controller
import time

def click(x,y,delay,num=2):
	mouse= Controller()
	mouse.position=(x,y)
	for i in range(1,num):
		time.sleep(delay)
		mouse.position=(x,y)
		mouse.click(Button.left,1)
def main():
	for x in range(0,110):
		print("start click ad %s "%x)
		# # 升级动物
		# click(1666,696,2)
		
		# 调鱼
		# click(1770,453,2)

		# 宣传
		click(1791,790,50)
		click(1695,550,2)

		# 许愿池
		# time.sleep(1.5)
		# click(1873,760,0.08,100*4)
		# click(1700,624,1)
		# click(1693,561,1.5)
		
		# mute
		click(1839,77,2)
		print("close ad after 30s %s"% time.ctime(time.time()))
		click(1882,77,32)
if __name__ == '__main__':
	main()
	print("---------end--------------")