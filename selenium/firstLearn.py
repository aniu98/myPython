#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1 pip install  selenium

# （2）下载浏览器的 WebDriver。
#   各浏览器的 WebDriver 可以在 这里 查找或者自己搜索。
# 浏览器名称	WebDriver 下载地址
# Chrome	https: // sites.google.com/a/chromium.org/chromedriver/
# http: // chromedriver.storage.googleapis.com/index.html
# Firefox	https: // github.com/mozilla/geckodriver/releases/
# IE	http: // selenium-release.storage.googleapis.com/index.html

# （3）安装浏览器的 WebDriver。
#   将下载的 WebDriver 复制到对应的目录。不同操作系统的位置不一样，具体参照如下：
# 操作系统	WebDriver 放置路径
# Windows	Python 的 Scripts 目录下
# MAC / usr/local/bin/


# 导入库
from selenium import webdriver
import time
# 声明浏览器
browser = webdriver.Chrome()
# WebDriver 复制到对应的目录
# browser = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
url = 'https:www.baidu.com'
# 打开浏览器预设网址
browser.get(url)
print("start sleep......")
# 打印网页源代码
time.sleep(100)
print("start get page_source")
data= browser.page_source
print("start print")
print(data.encode("GBK","ignore") )

# browser.get(url)#打开浏览器预设网址
# input_first = browser.find_element_by_id('q')
# input_two = browser.find_element_by_css_selector('#q')
# print(input_first)
# print(input_two)
print("end")
# 关闭浏览器
# browser.close() 



