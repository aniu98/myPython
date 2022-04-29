import base64
import os
import time
from PIL import Image
# 
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
def join_images(png1, png2, size=0, output='result.png'):
    """
    图片拼接
    :param png1: 图片1
    :param png2: 图片2
    :param size: 两个图片重叠的距离
    :param output: 输出的图片文件
    :return:
    """
    # 图片拼接
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size  # 获取两张图片的大小
    joint = Image.new('RGB', (size1[0], size1[1]+size2[1]-size))    # 创建一个空白图片
    # 设置两张图片要放置的初始位置
    loc1, loc2 = (0, 0), (0, size1[1] - size)
    # 分别放置图片
    joint.paste(img1, loc1)
    joint.paste(img2, loc2)
    # 保存结果
    joint.save(output)
 
options = webdriver.ChromeOptions()
#options.add_argument('--headless') # Chrome最新驱动无效，可以使用firefox或phantomjs
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('window-size=1920x1080')

path = os.getcwd().replace("\\", "/")
full_path = path+'/templates/test_flask_render.html'
full_path='E:/workspace/%E4%B8%AD%E7%A7%BB%E9%87%91%E7%A7%91/%E5%92%8C%E5%8C%85%E9%A3%9F%E5%A0%82/%E6%96%B0%E7%B3%BB%E7%BB%9F%E4%BB%8B%E7%BB%8D%E4%BC%9A%E8%AE%AE%E8%B5%84%E6%96%99_2021118/3%20%E5%92%8C%E5%8C%85%E9%A3%9F%E5%A0%82_%E6%89%8B%E6%9C%BA%E8%B4%AD%E4%B9%B0%E5%95%86%E5%93%81%E5%8E%9F%E5%9E%8B/%E5%9C%A8%E7%BA%BF%E7%82%B9%E9%A4%90.html'
driver = webdriver.Chrome()
# 设置浏览器窗口最大化
driver.maximize_window()  # 设置打开页面最大化,目的是更好的截取错误图
# 打开税网
driver.get(full_path)
# 1. 截取当前页面
driver.save_screenshot('result.png')


JS = {
    '滚动到页尾': "window.scroll({top:document.body.clientHeight,left:0,behavior:'auto'});",
    '滚动到': "window.scroll({top:%d,left:0,behavior:'auto'});",
}
# 获取body大小
body_h = int(driver.find_element_by_xpath('//body').size.get('height'))
body_h = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

# 计算当前页面截图的高度
# （使用driver.get_window_size()也可以获取高度，但有误差，推荐使用图片高度计算）
current_h = Image.open('result.png').size[1]
image_list = ['result.png']  # 储存截取到的图片路径
print("---")
print(body_h,current_h)
print(int(body_h/current_h))
for i in range(1, int(body_h/current_h)):
    # 1. 滚动到指定锚点
    print("--111-")
    driver.execute_script(JS['滚动到'] % (current_h * i))
    # 2. 截图
    driver.save_screenshot(f'test_{i}.png')
    join_images('result.png', f'test_{i}.png')
# 处理最后一张图
print("end")
driver.execute_script(JS['滚动到页尾'])
driver.save_screenshot('test_end.png')
# 拼接图片
join_images('result.png', 'test_end.png', size=current_h-int(body_h % current_h))
driver.quit()

