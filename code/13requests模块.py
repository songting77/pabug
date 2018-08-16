# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 14:33
@Author  : Fate
@File    : 13requests模块.py
'''

import requests
import json

'''
url,
params=None,  字典，get参数
**kwargs， urllib可用的参数
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

response = requests.get('http://www.baidu.com/', headers=headers)
# print(response.text)  # Unicode格式
# print(response.content.decode('utf-8'))  # 字节流


xcresponse = requests.get('https://www.baidu.com/s', {'wd': '西刺代理', 'ie': 'utf-8'}, headers=headers)
print(xcresponse.url)

# 去掉_o
ydurl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {
    "i": "蛇皮怪",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1534229275048",
    "sign": "6d0088e3dbed0802bf0cace9b1d067b7",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false",
}


ydresponse = requests.post(ydurl, data=data, headers=headers)
print(ydresponse.text)
data = json.loads(ydresponse.text)['translateResult'][0]
print(data)

# .json() 转为字典
print(ydresponse.json()['translateResult'][0])


