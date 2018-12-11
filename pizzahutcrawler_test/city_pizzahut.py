# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:42:22 2018

@author: cl
"""

import requests
import re
from bs4 import BeautifulSoup
import bs4

url='http://www.pizzahut.com.cn/StoreList#'
resp=requests.get(url)
resp.encoding=resp.apparent_encoding
html=BeautifulSoup(resp.text,'html.parser')
tag1=html.find('div',attrs={'class':'city_window'})#定位到按省查询的标签
file=open('D:/test/city.txt','a')#打开一个文本文件存储数据
for tag in tag1.children:
    if isinstance(tag,bs4.element.Tag):
        for con in tag('a')[1:]:#去掉第一个标记省份的a标签
            if isinstance(con,bs4.element.Tag):
                file.write('\r'+con.string+'\n')
file.close()