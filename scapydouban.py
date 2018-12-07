# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:56:09 2018

@author: cl
"""

import requests
from bs4 import BeautifulSoup

resp=requests.get('https://book.douban.com/top250?start=0')
soup=BeautifulSoup(resp.text,'lxml')

alldiv=soup.find_all('div',class_='pl2')
names=[a.find('a')['title'] for a in alldiv]

alla=soup.find_all('p',class_='pl')
authors=[a.string for a in alla]

allb=soup.find_all('span',class_='rating_nums')
rating=[a.string for a in allb]

quote=soup.find_all('span',class_='inq')
quotes=[a.string for a in quote]

filename = '豆瓣图书Top250.txt'
for name,author,rating,quote in zip(names,authors,rating,quotes):
    name='书名：'+name+'\n'
    author='作者信息：'+author+'\n'
    ratescore='评分：'+rating+'\n'
    sum='一句话简介：'+quote+'\n'
    data=name+author+ratescore+sum   
    with open('豆瓣图书Top250.txt','a',encoding='utf-8') as f:
        f.writelines(str(data))
        
