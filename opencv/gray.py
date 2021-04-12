#coding:utf-8
import cv2
import numpy as np

import Image


img = cv2.imread("./img/girl1.jpg")

len1,len2,len3=len(img),len(img[0]),len(img[0][0])
print("img len is {},{},{}".format(len1,len2,len3))


img2=np.zeros((len1, len2, len3), dtype=np.int)
for row in range(0,500):
	for col in range(0,500):
		pixel=img[row,col]
		b=img[row,col,0]
		g=img[row,col,1]
		r=img[row,col,2]
		gray=(b+g+r)/3
		img2[row,col]=[gray,gray,gray]
cv2.imshow("avage",Image.fromarray(img2))

# img3=np.zeros((2, 2, 3), dtype=np.int)
# for row in range(0,500):
# 	for col in range(0,500):
# 		pixel=img[row,col]
# 		b=img[row,col,0]
# 		g=img[row,col,1]
# 		r=img[row,col,2]
# 		gray=(b*0.3+g*0.59+r*0.11)
# 		img3[row,col]=[gray,gray,gray]
# cv2.imshow("sum",img3)






key = cv2.waitKey(0)
if key==27: #按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()
