# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:21:59 2018

@author: cl
"""

import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;WOW64) AppleWebKit/537.36 \
             (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    resp=requests.get(url,headers=headers).text
    return resp
def html_parse():
    for url in all_page():
        soup=BeautifulSoup(get_html(url),'lxml')
        alldiv=soup.find_all('div',class_='pl2')
        names=[a.find('a')['title'] for a in alldiv]

        alla=soup.find_all('p',class_='pl')
        authors=[a.string for a in alla]

        allb=soup.find_all('span',class_='rating_nums')
        rating=[a.string for a in allb]

        quote=soup.select('tr.item > td:nth-of-type(2)')
        quotes=[]
        for div in quote:
            sumspan=div.find('span',class_='inq')
            sums=sumspan.string if sumspan else 'none'
            quotes.append(sums)
        
        for name,author,rating,quote in zip(names,authors,rating,quotes):
            name='书名：'+name+'\n'
            author='作者信息：'+author+'\n'
            ratescore='评分：'+rating+'\n'
            sum='一句话简介：'+quote+'\n'
            data=name+author+ratescore+sum   
            f.writelines(str(data)+'----------'+'\n') 
def all_page():
    base_url='https://book.douban.com/top250?start='
    urllist=[]
    for page in range(0,250,25):
        allurl=base_url+str(page)
        urllist.append(allurl)
    return urllist
filename='豆瓣图书Top250.txt'
f=open(filename,'w',encoding='utf-8')
html_parse()
f.close()
print('success!')