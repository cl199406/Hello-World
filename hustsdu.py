# -*- coding: utf-8 -*-
import scrapy


class HustsduSpider(scrapy.Spider):
    name = 'hustsdu'
    allowed_domains = ['yjsjw.hust.edu.cn']
    start_urls = ['http://yjsjw.hust.edu.cn/']

    def parse(self, response):
        pass
