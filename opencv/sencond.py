#coding:utf-8
import cv2


img = cv2.imread("./img/girl1.jpg")

# # 切片
b,g,r = cv2.split(img)   # 得到各自颜色通道的二维数组数据

print(b)
# # 合并
img2 = cv2.merge(b,g,r)

cv2.imshow("img",img)





key = cv2.waitKey(0)
if key==27: #按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()