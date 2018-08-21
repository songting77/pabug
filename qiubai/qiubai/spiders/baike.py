# -*- coding: utf-8 -*-
import scrapy
from ..items import QiubaiItem

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    #两者都可多个
    allowed_domains = ['www.qiushibaike.com']
    #爬虫的url
    start_urls = ['https://www.qiushibaike.com/8hr/page/%d/' %(i) for i in range(1,3)]
    #spiders 把（url）-引擎-调度器-入栈（队列）-下载器--返回引擎-返回spilder.
    #数据在（默认会被回调的方法（-解析数据）：pass方法处

    def parse(self, response):
        divs = response.xpath('//div[contains(@id,"qiushi_tag_")]')
        items=[]
        for div in divs:
            #extract抽取
            nickname =div.xpath('.//h2/text()')[0].extract()
            content = div.xpath('.//div[@class="content"]/span/text()')[0].extract()
            vote = div.xpath('.//span[@class="stats-vote"]/i/text()').extract_first()
            comments = div.xpath('.//span[@class="stats-comments"]/a/i/text()')[0].extract()
            #print('=========================================================',nickname,content,vote,comments)
            # 将数据保存到字典中(先声明)
            # item = {}
            # item['nickname'] = nickname
            # item['content'] = content
            # item['vote'] = vote
            # item['comments'] = comments
            item = QiubaiItem()
            item['nickname'] = nickname
            item['content'] = content
            item['vote'] = vote
            item['comments'] = comments


            # items.append(item)
        #返回的数据必须是可迭代对象（列表，字典，map）
        # return items
            yield item

    #选择存文件：-o:重写+文件名+.xml/.txt/.csv/.json(settings中加配置解决乱码问题)
