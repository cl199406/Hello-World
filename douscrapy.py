# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:35:52 2018

@author: cl
"""
#爬取豆瓣TOP250电影相关信息
#并将其整理写入txt文件中
#善用spilt(),strip()函数进行文本的整理

import requests,time
from bs4 import BeautifulSoup

name=[]
infos=[]
rate=[]
quote=[]
base_url='https://movie.douban.com/top250'
for i in range(0,250,25):
    url=base_url+'?start='+str(i)
    res=requests.get(url)
    html=res.text

    bf=BeautifulSoup(html,'html.parser')
    ht=bf.find('ol',class_='grid_view')
    info=ht.find_all('div',class_='info')

    for d in info:
        name.append(d.find('span',class_='title').getText())
        infos.append(''.join(d.find('p').getText().strip().split()))
        rate.append(' '.join(d.find('div',class_='star').getText().strip().split('\n')))
        quote.append(d.find('p',class_='quote').getText().strip())
    time.sleep(3)
for i in range(len(name)):
    with open('doubantop250movie.txt','a+',encoding='utf-8') as f:
        f.write((name[i])+'\n'+(infos[i])+'\n'+(rate[i])+'\n'+(quote[i])+'\n')
    
 