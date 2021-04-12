#coding:utf-8
import cv2

# 读取照片
img = cv2.imread(r"./img/girl1.jpg")
# 照片的大小
print(img.shape)
# 灰色
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
   
# 以灰度图像方式读取图片数据（二维数组）
img_gray_read = cv2.imread("./img/girl1.jpg",cv2.IMREAD_GRAYSCALE)

rt,img_threshold = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)


pixel = img[100,100]  #[57 63 68],获取(100,100)处的像素值
print(pixel)
img[100,100]=[57,63,99] #设置像素值
b = img[100,100,0]    #57, 获取(100,100)处，blue通道像素值
g = img[100,100,1]    #63
r = img[100,100,2]      #68
r = img[100,100,2]=99    #设置red通道值
print(pixel)

cv2.imshow("img",img)
cv2.imshow("thre",img_threshold)
cv2.imshow("img_gray",img_gray)
cv2.imshow("img_gray_read",img_gray_read)
cv2.imshow("IMage",img[:100,:200])  # 取前100行，前200列的像素作为图像展示

key = cv2.waitKey(0)
if key==27: #按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()


cv2.imwrite(r"./out/girl1.jpg",img_threshold)
