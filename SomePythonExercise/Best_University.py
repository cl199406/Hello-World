# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:15:54 2018

@author: cl
"""
#爬取最好大学排名
import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return 'error'
    
def univ(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
                

def printuniv(ulist,num):
    print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format(u[0],u[1],u[2],chr(12288)))
        

def main():
    ulist=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=getHTMLText(url)
    univ(ulist,html)
    printuniv(ulist,20)
main()