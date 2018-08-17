import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
#获取网页源码，返回html源码
def getHtml(url):
    res = requests.get(url, headers=headers)
    return res.content.decode('utf-8','ignore')

#筛选出HTML中的 URL(正则来写)
def getUrl(url):
    html = getHtml(url)
    urlre = '<a.*href=\"(https?://.*?)\".*>'
    #预编译
    urlc = re.compile(urlre)
    urlList = urlc.findall(html)

    return urlList

def getEmail():
    pass


def getMovie(url):
    re.search('tv',url)
    pass
#开始深度爬
def deepSpider(url,deepth):
    print('\t\t\t' * depthDict[url], "已经抓取了第%d层：%s" % (depthDict[url], url))
    if depthDict[url] >= deepth:
        return

    #新URL
    sonUrlList =getUrl(url)
    for newUrl  in sonUrlList:
        if newUrl not in depthDict:
            depthDict[newUrl] = depthDict[url]+1
            deepSpider(newUrl,deepth)

if __name__ == '__main__':
    #起始url
    starturl = "http://www.baidu.com/?swd='二狗'"
    #层级控制（是字典。可利用url做键）
    depthDict = {}

    depthDict[starturl] = 1

    deepSpider(starturl,3)