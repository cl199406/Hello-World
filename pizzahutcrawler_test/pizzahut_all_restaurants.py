# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:57:31 2018

@author: cl
"""
from pymongo import MongoClient
import requests,time
from urllib.parse import quote
from bs4 import BeautifulSoup as BS
import bs4,json
cities=[]
filename='city.txt'
with open(filename,'r',encoding='UTF-8-sig') as f:
    for line in f:
        city=line.replace('\n','')
        if city != '':
            cities.append(city)
cities=list(set(cities))
url='http://www.pizzahut.com.cn/'
result={}
conn=MongoClient(host='127.0.0.1',port=27017)
db=conn.mydb.test_set
for i in range(len(cities)):
    s=requests.Session()
    cookies=requests.cookies.RequestsCookieJar()
    city_urlcode=quote(cities[i])
    restaurants=[]
    headers={
        'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Host': 'www.pizzahut.com.cn',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',}
    firsthtml=s.get(url,headers=headers)
    cookies.set('AlteonP',firsthtml.cookies['AlteonP'],domain='www.pizzahut.com.cn')
    cookies.set('iplocation',city_urlcode,domain='www.pizzahut.com.cn')
    page=1
    while True:
        data={
        'pageIndex':page,
        'pageSize':50,
        }
        resp=s.post('http://www.pizzahut.com.cn/StoreList/Index',headers=headers,data=data,cookies=cookies)
        html=BS(resp.text,'html.parser')
        divs=html.find_all('div',class_='re_RNew')
        temp_item=[]
        for div in divs:
            items={}
            if isinstance(div,bs4.element.Tag):
                items['name']=div.contents[1].string
                items['address']=div.contents[3].string
                items['phone']=div.contents[5].string
                temp_item.append(items)
        if not temp_item:
            break
        restaurants+=temp_item
        page+=1
        time.sleep(2)
    result[cities[i]]=restaurants
    db.insert_one({cities[i]:restaurants})
    print('\r下载进度:{0:.2f}%'.format((i+1)*100/385),end='')
with open('D:/test/city.json','w',encoding='utf-8') as f:
    f.write(json.dumps(result,indent=4,ensure_ascii=False))
for i in db.find():
    print(i)