# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:39:12 2018

@author: cl
"""

import requests
import os,time
from bs4 import BeautifulSoup

def get_html(url):
   headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;WOW64) AppleWebKit/537.36 \
             (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
   proxies={'http:':'121.23.10.27:8080'}
   try:
       resp=requests.get(url,headers=headers)
   except:
       resp=requests.get(url,headers=headers,proxies=proxies)
   return resp.
def mkdir(path):
    isExists=os.path.exists(os.path.join('D:/test',path))
    
    if not isExists:
        os.makedirs(os.path.join('D:/test',path))
        os.chdir(os.path.join('D:/test',path))
        return True
    else:
        print(path,'already exists')
        return False
    
def get_imgs():
    for url in all_page():
        path=url.split('-')[-1]
        mkdir(path)
        html=get_html(url).text
        soup=BeautifulSoup(html,'lxml')
        allimgs=soup.select('div.text > p > img')
        download(allimgs)
        print('ok')
def all_page():
    base_url='http://jandan.net/ooxx/'
    soup=BeautifulSoup(get_html(base_url).text,'lxml')
    allpage=soup.find('span',class_='current-comment-page').string[1:-1]
    urllist=[]
    for page in range(1,int(allpage)+1):
        allurl=base_url+'page-'+str(page)
        urllist.append(allurl)
    return urllist
def download(list):
    for img in list:
        urls=img['src']
        if urls[0:5]=='http:':
            img_url=urls
        else:
            img_url='http:'+urls
        filename=img_url.split('/')[-1]
        with open(filename,'wb') as f:
            try:
                f.write(get_html(img_url).content)
            except:
                print('failed:',filename)
if __name__=='__main__':
    t1=time.time()
    get_imgs()
    print(time.time()-t1)
