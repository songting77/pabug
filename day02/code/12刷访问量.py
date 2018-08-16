# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 14:18
@Author  : Fate
@File    : 12刷访问量.py
'''

import urllib
from urllib import request
import random

# 代理池
proxies = [{'http': "118.190.95.43:9001"},
           {'http': '115.46.68.38:8123'},
           {'https': "203.130.46.108:9090"}
           ]

for i in range(5):

    proxy = random.choice(proxies)
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)

    url = 'https://blog.csdn.net/Gi1gamesh/article/details/80690415'
    try:
        response = opener.open(url, timeout=5)
        if response.code != 200:
            proxies.remove(proxy)
    except Exception as e:
        pass
    print(proxy)
