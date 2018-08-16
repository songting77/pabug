# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 9:13
@Author  : Fate
@File    : 01Handler.py
'''


import urllib

from urllib import request

# 处理器 处理HTTPS
handler = urllib.request.HTTPSHandler()
# handler = urllib.request.HTTPHandler()

# 打开器
opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/'
resp = urllib.request.urlopen(url)
print(resp)
'''
fullurl, data=None, timeout
'''

# 通过打开器，打开网页
response = opener.open(url)

print(response)

# 安装opener , 全局的opener
urllib.request.install_opener(opener)

res = urllib.request.urlopen(url)
print(res)
