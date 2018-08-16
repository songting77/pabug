# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 10:27
@Author  : Fate
@File    : 06使用保存cookie.py
'''

import urllib
from urllib import request, parse
from http import cookiejar

# 创建cookie对象

filename = 'renren.txt'

cookie = cookiejar.LWPCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)

# 处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# opener.add_handler()
urllib.request.install_opener(opener)
req = urllib.request.Request('http://www.renren.com/967374112/profile', headers=headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
