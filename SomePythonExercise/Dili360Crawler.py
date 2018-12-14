# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:16:49 2018

@author: cl
"""

import requests
from bs4 import BeautifulSoup
import re,json

url='http://www.dili360.com/'
sion=requests.Session()
headers={
        'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Host': 'www.dili360.com',
        'Connection': 'keep-alive',}
cookies=requests.cookies.RequestsCookieJar()
fr=sion.get(url,headers=headers,cookies=cookies)
fr.encoding=fr.apparent_encoding
html=BeautifulSoup(fr.text,'lxml')
links=html.find_all('a',attrs={'href':re.compile('/travel/sight/20')})
items=[]
for link in links:
    item={}
    item['href']='http://www.dili360.com'+link['href']
    item['name']=link.string
    items.append(item)
img_info={}
for icon in range(len(items)):
    http=[]
    for i in range(25):
        curl=items[icon]['href'][:-4]+'/'+str(i+1)+'.htm'
        htm=sion.get(curl,headers=headers)
        resp=BeautifulSoup(htm.text,'lxml')
        con=resp.select('body > div.wpr.blue > div.body-left.br1.none-shadow > div.right > ul')
        imgs=con[0].find_all('img')
        if not imgs:
            break
        authors=con[0].find_all('a',attrs={'class':'link'})
        for img in imgs:
            http.append(img['src'][:-1]+'9')
    img_info[items[icon]['name']]=http
    print('\r当前爬取进度：{0:.2f}%'.format((icon+1)*100/len(items)),end='')
with open('D:/test/dili360.json','w',encoding='utf-8') as f:
    f.write(json.dumps(img_info,indent=4,ensure_ascii=False))
    
    