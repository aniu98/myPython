import re
import requests
from requests import RequestException
# import urllib.request

url = "http://cloudum.hq.cmcc/address-list/findUserInfo"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "107",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "JSESSIONID=D1BCB968D167C1E8EC5173393691B2A5; AIPortal_OA_Account=ZIXSvHS7Up7B2/UxmVMKh7cetr6yjuf99aubEDY6ziLirOGgljn3LicKhVI3nRJ2az/oX1tcZyA3YW9Gy50ZIPPz67NsG8/dhPhPAqoUe+7RPahColF5xeGcZW+0dpQD0cw7ttfNyoDKytnqPkrJSBrMNmN+1+lP8GkF5s70OIk=; Portal_Flag=Rphw+WuLxwt2wC+W5EqbmOieNGgouKwio3GoS1JsGAhAMSw1xckHAWBuUJqHrmZMZIo+zloT4TK3XMByTBZwmQ==; RT='z=1&dm=hq.cmcc&si=p9ragjb5l3h&ss=lycl1x9s&sl=r&tt=d2y&bcn=http%3A%2F%2Ftodo.hq.cmcc%2Fcpa%2Fbeacon&ld=3bzy&ul=3hc9&hd=3hcs'",
    "Host": "cloudum.hq.cmcc",
    "Origin": "http://cloudum.hq.cmcc",
    "Referer": "http://cloudum.hq.cmcc/address-list/login?flag=zhuanV2&ticket=Egi7nejEDhE2uBrJiA8-9AtYOx_f3xKoExS-6f9VS71is_YSD9iOwWHfoHwpsgq8bNkCKNsSwEWbmiPpt-hNS6fpUbhZLc6Hl2B82nGClbI",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


def get_Data(url):
    try:
        # 请求头部，如果不加头部，则会被反爬虫网站识别出是爬虫，会导致获取不到数据

        # 获取网页源代码数据
        # response = requests.get(url, headers=headers)
        data_dict = "biz_type=3&orgCode=5500000018&email=&preferredMobile=&staffCode=&pageSize=10&currentPage=1&_t=1720081969336"
        response = requests.post(url, headers=headers, data=data_dict)
        if response.status_code == 200:
            return response.json()
        return None
    except RequestException:
        print('请求出错')
        return None


def main():
    try:
        data = get_Data(url)
        print(type(data))
        print(type(data["data"]["userInfos"]))
        # for

    except Exception:
        print('出错啦！')


if __name__ == '__main__':
    main()
