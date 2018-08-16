# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 15:33
@Author  : Fate
@File    : 15requests登陆.py
'''

import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}

data = {
    'email': '18588403840',
    'password': 'Changeme_123'
}

loginurl = 'http://www.renren.com/PLogin.do'

# 创建session对象
session = requests.session()

# 保存cookie
res = session.post(url=loginurl, data=data, headers=headers)
print(session.get(url='http://www.renren.com/965557295/profile', headers=headers).text)
# 保存

cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
print(cookie_dict)


# c_dict = {'_de': '8799AF8CDA498E75CA882FBE19A95DF9', 'anonymid': 'jktejf7x-l926t8', 'first_login_flag': '1',
#           'id': '965557295',
#           'ln_hurl': 'http://hdn.xnimg.cn/photos/hdn121/20180425/1110/h_main_sUHq_0c140000306f195a.jpg',
#           'ln_uact': '18588403840', 'loginfrom': 'syshome', 'p': 'beab1a57465dede929b68712b43f57725',
#           'societyguester': '28559929ee22adeecc177dd5bac635d15', 't': 'ebf75001ca076c976947b69ffa2a7bb6',
#           'xnsid': 'c89aca19', 'JSESSIONID': 'abcP8QcKvAFvbbUAtz3uw'}
#
# cookie = requests.utils.cookiejar_from_dict(c_dict)
# # for c in cookie:
#
# session.cookies = cookie
#
# # print(session.get('http://www.renren.com/965557295/profile', allow_redirects=False).text)
# print(session.get(url='http://www.renren.com/965557295/profile', headers=headers, allow_redirects=False).text)

'''
response = requests.post(url=loginurl, data=data, headers=headers)
print(response.text)
print(response.cookies)
print(requests.get(url='http://www.renren.com/965557295/profile',headers=headers).text)
'''
