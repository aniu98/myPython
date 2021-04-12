#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver # 导入库
import time
# 声明浏览器
browser = webdriver.Chrome()
url = 'https:www.baidu.com'
# 打开浏览器预设网址
browser.get(url)
print "start sleep......"
# 打印网页源代码
time.sleep(10);
print "start get page_source"
data= browser.page_source
print "start print"
print data.encode("GBK","ignore") 

# browser.get(url)#打开浏览器预设网址
# input_first = browser.find_element_by_id('q')
# input_two = browser.find_element_by_css_selector('#q')
# print(input_first)
# print(input_two)
print "end"
# 关闭浏览器
browser.close() 


