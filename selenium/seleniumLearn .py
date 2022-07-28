# pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

# driver_path = ChromeDriverManager().install()
# print("--"+driver_path)
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')  # 实例化对象
url = "https:www.baidu.com"
# 打开浏览器预设网址
driver.get(url)
print("start get page_source")
data=driver.page_source
print("start print")
print(driver.title)
print(driver.current_url)  # 打印当前页面URL
user = driver.find_element_by_class_name('s-top-login-btn').text  # 获取结果数目
print(user)

above = driver.find_element_by_link_text("hao123")
print(above)
ActionChains(driver).move_to_element(above).perform()


# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
print("--")

driver.get("https://www.ip138.com/mobile.asp?mobile=13461459318&action=mobile")
# 删除多输入的一个 m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
print(driver.title)
print(driver.find_element_by_tag_name("tbody"))
span=driver.find_element_by_tag_name("tbody").find_element_by_tag_name("span")
print(span.text)
