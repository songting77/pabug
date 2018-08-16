# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/14 16:57
@Author  : Fate
@File    : changeCookie.py
'''


def changeCookie(cookie):
    cookieDict = {}
    cookieList = cookie.split(';')
    for cookie in cookieList:
        name = cookie.strip().split('=', 1)[0]
        value = cookie.strip().split('=', 1)[1]
        cookieDict[name] = value

    print(cookieDict)
if __name__ == '__main__':
    cookie = "anonymid=jfcb0wwz-aaoe7i; _r01_=1; ln_uact=18588403840; __utma=151146938.389542758.1524625502.1524625502.1524625502.1; __utmz=151146938.1524625502.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/965557295/profile; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20180425/1110/h_main_sUHq_0c140000306f195a.jpg; _ga=GA1.2.389542758.1524625502; depovince=GUZ; JSESSIONID=abc6JJ-hAirX3ecwII3uw; ick_login=136c74d0-d373-4361-9331-28609e837615; jebecookies=3728f908-550f-4a6c-bfd3-f54b834b5a4b|||||; _de=8799AF8CDA498E75CA882FBE19A95DF9; p=beab1a57465dede929b68712b43f57725; first_login_flag=1; t=28559929ee22adeecc177dd5bac635d15; societyguester=28559929ee22adeecc177dd5bac635d15; id=965557295; xnsid=c85dbd84; loginfrom=syshome; wp_fold=0"
    changeCookie(cookie)
