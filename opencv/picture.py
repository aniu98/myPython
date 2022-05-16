import cv2
import numpy as np
 
# 手势识别  
def binaryMask(frame, x0, y0, width, height):
	cv2.rectangle(frame,(x0,y0),(x0+width, y0+height),(0,255,0)) #画出截取的手势框图
	roi = frame[y0:y0+height, x0:x0+width] #获取手势框图
	cv2.imshow("roi", roi) #显示手势框图
	res = skinMask(roi) #进行肤色检测
	cv2.imshow("res", res) #显示肤色检测后的图像
	return res
 
##########方法一###################
##########BGR空间的手势识别#########
def skinMask(roi):
	rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB) #转换到RGB空间
	(R,G,B) = cv2.split(rgb) #获取图像每个像素点的RGB的值，即将一个二维矩阵拆成三个二维矩阵
	skin = np.zeros(R.shape, dtype = np.uint8) #掩膜
	(x,y) = R.shape #获取图像的像素点的坐标范围
	for i in range(0, x):
		for j in range(0, y):
			#判断条件，不在肤色范围内则将掩膜设为黑色，即255
			if (abs(R[i][j] - G[i][j]) > 15) and (R[i][j] > G[i][j]) and (R[i][j] > B[i][j]):
				if (R[i][j] > 95) and (G[i][j] > 40) and (B[i][j] > 20) \
						and (max(R[i][j],G[i][j],B[i][j]) - min(R[i][j],G[i][j],B[i][j]) > 15):
					skin[i][j] = 255
				elif (R[i][j] > 220) and (G[i][j] > 210) and (B[i][j] > 170):
					skin[i][j] = 255
	res = cv2.bitwise_and(roi,roi, mask = skin) #图像与运算
	return res