import math
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}


#计算总共页数
def getPageNum(url):
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,'lxml')
    pagetotalNum = soup.select("#ClientPageControl1_hdnTotalCount")[0]['value']
    pageofSize = soup.select("#ClientPageControl1_hdnPageSize")[0]['value']
    # print(pagetotalNum,pageofSize)
    #计算总的显示页数,math.ceil:浮点向上取整。
    page = math.ceil(int(pagetotalNum)/int(pageofSize))
    print(page)
    return page


#每一页的数据
def getStock(url):
    url = 'http://quote.stockstar.com/fund/stock_3_1_1.html'
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,'lxml')

    stockList = soup.select('#datalist > tr')
    for stock in stockList:
        #清洗数据
        stockNum = stock.select("td:nth-of-type(1)>a")[0].text
        stockName = stock.select("td:nth-of-type(2)")[0].text
        dayGrowth = stock.select("td:nth-of-type(6)>span")[0].text
        subscribe = stock.select("td:nth-of-type(7)")[0].text
        print(stockNum,stockName,dayGrowth,subscribe)



if __name__ == '__main__':
    # getStock(url = 'http://quote.stockstar.com/fund/stock_3_1_1.html')
    # getPageNum(url = 'http://quote.stockstar.com/fund/stock_3_1_1.html')
    page = getPageNum(url = 'http://quote.stockstar.com/fund/stock_3_1_1.html')
    for i in range(1,page+1):
        url = "http://quote.stockstar.com/fund/stock_3_1_%d.html" % i
        getStock(url)