import requests
import re

from queue import Queue

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

'''
广度爬取：来一层抓一层
利用队列实现 (判断队列是否为空/超出层级-生成新的url )

'''

def getHtml(url):
    res = requests.get(url, headers=headers)
    return res.content.decode('utf-8','ignore')


def getUrl(url):
    html = getHtml(url)
    urlre = '<a.*href=\"(https?://.*?)\".*>'
    #预编译
    urlc = re.compile(urlre)
    urlList = urlc.findall(html)
    return urlList


def vastSpider(depth):
    while urlList:
        url = urlList.pop(0)
        if depthDict[url] < depth:
            print('\t\t\t' * depthDict[url], "已经抓取了第%d层：%s" % (depthDict[url], url))

            sonUrllist = getUrl(url)
            for newUrl in sonUrllist:
                if newUrl  in sonUrllist:
                    depthDict[newUrl] = depthDict[url] + 1
                    urlList.append(newUrl)



if __name__ == '__main__':
    startUrl = "https://www.baidu.com/s?wd=崔晶"
    urlList = []
    urlList.append(startUrl)

    #层级控制
    depthDict = {}
    depthDict[startUrl]=1

    #广度爬虫
    vastSpider(3)