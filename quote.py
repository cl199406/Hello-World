# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:30:26 2018

@author: cl
"""

import requests,re
from bs4 import BeautifulSoup
'''
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
stockURL='http://quote.eastmoney.com/stocklist.html'
lst=[]
getStockList(lst,stockURL)

'''
url1='http://quote.eastmoney.com/stocklist.html'
html=requests.get(url1)
html.encoding=html.apparent_encoding
bf=BeautifulSoup(html.text,'html5lib')#最好用html.parse
br=bf.find_all('a')
lst=[]
for q in br:
    try:
        href=q.attrs['href']
        lst.append(re.findall('[s][hz]\d{6}',href)[0])
    except:
        continue
base_url='https://gupiao.baidu.com/stock/'
        
a=lst[132]
print(a)
url=base_url+a+'.html'
hl=requests.get(url)
hl.raise_for_status()
hl.encoding=hl.apparent_encoding
html=hl.text
soup=BeautifulSoup(html,'html.parser')
infodict={}
stockinfo=soup.find('div',attrs={'class':'stock-bets'})
print(stockinfo.text)
name=stockinfo.find_all('a',class_='bets-name')[0]
print(name.text)
infodict.update({'股票名称：':name.text.split()[0]})
keylist=stockinfo.find_all('dt')
valuelist=stockinfo.find_all('dd')
print(keylist,valuelist)
for i in range(len(keylist)):
    key=keylist[i].text
    val=valuelist[i].text
    infodict[key]=val
    fpath='D:/test/baidustockinfo.txt'
    with open(fpath,'w',encoding='utf-8') as f:
        f.write(str(infodict)+'\n')
  
    
           

   

        
