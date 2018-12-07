# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:43:24 2018

@author: cl
"""

from scrapy.spiders import Spider

class FirstSpider(Spider):
    name='first'
    allowed_domains=['baidu.com']
    start_urls=['http://www.baidu.com',]
    def parse(self,response):
        pass