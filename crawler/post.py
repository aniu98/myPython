# 1.导入库
import requests
# from fake_useragent import UserAgent

# 实例化类
# ua = UserAgent()
# ua.random随机生成一个User-Agent头部信息
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

# 2. 定义请求url
url = 'https://fanyi.baidu.com/sug'

# 3. 发送网络请求
data_dict = { 'kw':'ajax'}
r= requests.post(url, headers=header, data = data_dict)
print(r)
