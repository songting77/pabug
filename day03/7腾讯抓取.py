import math
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}

#获得页数
def getpageNum(url):
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,'lxml')
    pageTotalNum = soup.select('.lightblue.total')[0].text
    page = math.ceil(int(pageTotalNum)/int(10))
    print(page)
    return  page

#获得一页的数据
def getPythonInfo(url):
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,'lxml')

    jobList = soup.find_all('tr',class_=['odd','even'])
    for job in jobList:
        jobName = job.select('td:nth-of-type(1) > a')[0].text
        jobStyle = job.select('td:nth-of-type(2)')[0].text
        jobArea = job.select('td:nth-of-type(4)')[0].text
        jobData = job.select('td:nth-of-type(5)')[0].text

        print(jobName,jobStyle,jobArea,jobData)

        #划重点，将数据写入文本，之后sql会用
        with open('tencent.txt','a+',encoding='utf-8')as f:
            f.write(str((jobName,jobStyle,jobArea,jobData)) + '\n')
            f.flush()


if __name__ == '__main__':
    url = 'https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0&start=100'
    # getPythonInfo(url)
    page = getpageNum(url)
    for i in range(0,page+1):
        newUrl = "https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0&start=%d*10#a" %i
        getPythonInfo(newUrl)

