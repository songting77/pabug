import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}


def getJobInfo(url):

    response = requests.get(url, headers=headers).content.decode('gbk')
    soup = BeautifulSoup(response, 'lxml')
    jobResponsibilityList = soup.select('div.bmsg.job_msg.inbox > p')
    jobResponsibility = ''
    for jobRes in jobResponsibilityList:
        jobResponsibility += jobRes.text

    # print(jobResponsibility)

    return jobResponsibility

def getJob(url):
    # url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,3.html'
    response = requests.get(url,headers=headers).content.decode('gbk')
    print(response)
    soup =BeautifulSoup(response,'lxml')
    jobList = soup.select("#resultList > div.el")
    print(jobList)

    for job in jobList[1:]:
        jobName = job.select('span:nth-of-type(1)> a ')[0]['title']
        jobUrl = job.select('span:nth-of-type(1)> a ')[0].attrs['href']
        jobInfo =getJobInfo(jobUrl)
        company = job.select('span.t2 > a')[0]['title']
        jobAddress = job.select('span.t3')[0].text

        print(jobName,jobUrl,jobInfo,company,jobAddress)


def getPageNum(url):
    response = requests.get(url,headers=headers).content.decode('gbk')
    soup = BeautifulSoup(response,'lxml')
    # pageNum = soup.select('div.p_in > td')[0].text[1:3]
    pageNum = soup.select('div.p_in > .td')[0].text[1:3]
    print(pageNum)
    return int(pageNum)



if __name__ == '__main__':
    # getJobInfo('https://jobs.51job.com/guangzhou-thq/104771741.html?s=01&t=0')
    # getJob('https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,3.html')
    startUrl = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,3.html'
    pagenum = getPageNum(startUrl)
    for num in range(1,pagenum+1):
        newurl = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,%d.html' % num
        getJob(newurl)