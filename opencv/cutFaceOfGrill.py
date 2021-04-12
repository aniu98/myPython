#coding:utf-8
import cv2
import numpy as np

img = cv2.imread("./img/girl1.jpg")

len1,len2,len3=len(img),len(img[0]),len(img[0][0])
print("img len is {},{},{}".format(len1,len2,len3))
# 图像的形状可通过img.shape访问。它返回行，列和通道数的元组（如果图像是彩色的）
print( img.shape )
# 素总数
print( img.size )
# 图像数据类型
print( img.dtype )
cv2.imshow("src",img)



face=img[200:300,200:300]
cv2.imshow("face", face)

img[400:500,400:500]=face
cv2.imshow("move" ,img)
key = cv2.waitKey(0)
if key==27: #按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()
