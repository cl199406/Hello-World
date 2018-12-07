# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:39:31 2018

@author: cl
"""

import re
from urllib import request
import urllib

def craw(url,page):
    html1=request.urlopen(url).read()
    html1=str(html1)
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    pat2='<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    pat3='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1)+re.compile(pat3).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename="D:/test/tupian/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(x)
                x-=1
            if hasattr(e,'reason'):
                print('reason'+str(x))
        x+=1
for i in range(1,2):
    url='https://list.jd.com/list.html?cat=9987,653,655&page='+str(i)
    craw(url,i)
