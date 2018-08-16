# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 14:05
@Author  : Fate
@File    : 11代理.py
'''

import urllib
from urllib import request, parse
import re
from http import cookiejar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# 无密码

# proxy = {
#     "http": "10.3.133.146:808"
# }


proxy = {
    "http": "User1:123456@10.3.133.146:808"
}
# 创建处理器
proxy_handler = urllib.request.ProxyHandler(proxy)
# 打开器
opener = urllib.request.build_opener(proxy_handler)

response = opener.open('http://www.baidu.com/')

print(response.read().decode('utf-8'))