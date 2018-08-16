# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 15:15
@Author  : Fate
@File    : 14requests代理.py
'''

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# {'协议（小写）':'协议://用户名:密码@ip:port'}
proxy = {
    'https': 'https://User1:123456@10.3.133.146:808',
    "http": '10.3.133.142:808'
}

response = requests.get('https://blog.csdn.net/Gi1gamesh', headers=headers, proxies=proxy)

print(response)
print(response.cookies)


