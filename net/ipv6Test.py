import requests

# 获取IPv4地址：https://ipv4.ipw.cn/api/ip/myip
# 获取IPv6地址：https://ipv6.ipw.cn/api/ip/myip
# 确认用户网络是IPv4还是IPv6访问优先：https://test.ipw.cn/api/ip/myip?json
print("ssss")
r = requests.get('https://test.ipw.cn/api/ip/myip?json')
print("ssss")
clientIP = r.text
print(clientIP)

r = requests.get('https://ipv6.ipw.cn/api/ip/myip')
print("ssss")
clientIP = r.text
print(clientIP)