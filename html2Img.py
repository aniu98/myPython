import base64
import os
import time
# 
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
 
options = webdriver.ChromeOptions()
#options.add_argument('--headless') # Chrome最新驱动无效，可以使用firefox或phantomjs
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('window-size=1920x1080')

path = os.getcwd().replace("\\", "/")
full_path = path+'/templates/test_flask_render.html'
full_path='E:/workspace/%E4%B8%AD%E7%A7%BB%E9%87%91%E7%A7%91/%E5%92%8C%E5%8C%85%E9%A3%9F%E5%A0%82/%E6%96%B0%E7%B3%BB%E7%BB%9F%E4%BB%8B%E7%BB%8D%E4%BC%9A%E8%AE%AE%E8%B5%84%E6%96%99_2021118/3%20%E5%92%8C%E5%8C%85%E9%A3%9F%E5%A0%82_%E6%89%8B%E6%9C%BA%E8%B4%AD%E4%B9%B0%E5%95%86%E5%93%81%E5%8E%9F%E5%9E%8B/%E5%9C%A8%E7%BA%BF%E7%82%B9%E9%A4%90.html'

try:
    print("-----")
    driver = webdriver.Chrome(options=options)
    print("-----")
    driver.maximize_window()
    print("-----")
    driver.get(f'file:///{full_path}')
    time.sleep(3)
    driver.get_screenshot_as_file('./images/test-canvas.png')
    driver.save_screenshot("test-canvas.png")
    driver.quit()
    print("截图成功")
except WebDriverException:
    print("截图失败")
