# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 9:52
@Author  : Fate
@File    : 05登陆renren.py
'''

import urllib
from urllib import request, parse
from http import cookiejar

# 创建cookie对象
import time

filename = 'renren.txt'
cookie = cookiejar.LWPCookieJar(filename)

# 处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

loginurl = 'http://www.renren.com/PLogin.do'

data = {
    'email': '18588403840',
    'password': 'Changeme_123'
}

# url编码
data = urllib.parse.urlencode(data).encode('utf-8')

# opener.add_handler()
req = urllib.request.Request(loginurl, data=data, headers=headers)
'''
response = opener.open(req)

print(response.read().decode('utf-8'))

# 保存cookie
# 忽略错误
cookie.save(ignore_discard=True, ignore_expires=True)

# http://www.renren.com/965557295/profile
url = 'http://www.renren.com/965557295/profile'
# 直接打开
profileRes = opener.open(url)
print(profileRes.read().decode('utf-8'))
print(profileRes.url)
'''

# 安装
urllib.request.install_opener(opener)
response = urllib.request.urlopen(req)
time.sleep(1)
profileRes = urllib.request.urlopen('http://www.renren.com/965557295/profile')
print(profileRes.read().decode('utf-8'))

print(urllib.request.urlopen('http://www.renren.com/967374112/profile').read().decode('utf-8'))
# 保存cookie
# 忽略错误
cookie.save(ignore_discard=True, ignore_expires=True)