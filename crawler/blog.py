import re
import requests
from requests import RequestException
# import urllib.request

url = "https://blog.csdn.net/wang_xiao_ning/article/details/122182456"

def get_page(url):
	try:
		#请求头部，如果不加头部，则会被反爬虫网站识别出是爬虫，会导致获取不到数据
		headers = {
			'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'  # 伪装成浏览器
		}
		#获取网页源代码数据
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求出错')
		return None

		
def parse_page(html):
	try:
		#使用正则匹配html代码中浏览量字段
		# print(html)
		read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
		# read_num=2
		#返回浏览量
		return read_num
	except Exception:
		print('解析出错')
		return None

	 
def main():
	try:
		html = get_page(url)
		if html:
			read_num = parse_page(html)
			if read_num:
				print('当前阅读量：', read_num)
	except Exception:
		print('出错啦！')

if __name__ == '__main__':
	main()
