# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


'''
pipeline:在文件/数据库写入数据
'''

import json

class QiubaiPipeline(object):
    def open_spider(self, spider):
        #使用时打开文件，名字遵循文档
        self.fp = open('./糗事百科.txt',mode='a',encoding='utf-8')

    def process_item(self, item, spider):
        #开始保存数据在文件中
        data = {}
        data['nickname']=item['nickname']
        data['content']=item['content']
        data['vote']=item['vote']
        data['comments']=item['comments']
        self.fp.write(json.dumps(data,ensure_ascii=False)+'\n')
        return data

    def close_spider(self,spider):
        #爬虫结束
        self.fp.close()


class QiubaiPipeline2(object):
    def open_spider(self, spider):
        #使用时打开文件，名字遵循文档
        self.fp = open('./糗事百科pipline2.txt',mode='a',encoding='utf-8')

    def process_item(self, item, spider):
        #再此处pipline已经给过data了，所以此处返回item就好
        # data = {}
        # data['nickname']=item['nickname']
        # data['content']=item['content']
        # data['vote']=item['vote']
        # data['comments']=item['comments']
        self.fp.write(json.dumps(item,ensure_ascii=False)+'\n')
        return item

    def close_spider(self,spider):
        #爬虫结束
        self.fp.close()
