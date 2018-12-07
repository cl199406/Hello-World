# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:58:02 2018

@author: cl
"""

import requests,time
from bs4 import BeautifulSoup

base_url='https://movie.douban.com/review/best/'

bs=requests.get(base_url)
res=bs.text

html=BeautifulSoup(res,'html.parser')

con=html.find('div',id='content')

reviewlists=con.find_all('div',class_='main review-item')
info=[]
content=[]
for view in reviewlists:
    info.append(''.join(view.find('header',class_='main-hd').getText().strip().split()))
    content.append(''.join(view.find('div',class_='main-bd').getText().strip().split()))

for i in range(len(info)):
    with open('douban_bestreview.txt','a+',encoding='utf-8') as f:
        f.write(info[i]+'\n'+content[i]+'\n')

    

