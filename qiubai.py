# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:24:02 2018

@author: cl
"""

import re
from urllib import request

def getcontent(url,page):
     headers=('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
     opener=request.build_opener()
     opener.addheaders=[headers]
     request.install_opener(opener)
     data=request.urlopen(url).read().decode('utf-8')
     userpat='<img src=".+?" alt="(.*?)">'
#     userpat='target="_blank" title="(.*?)">'
     contentpat='<div class="content">(.*?)</div>'
     userlist=re.compile(userpat,re.S).findall(data)
     contentlist=re.compile(contentpat,re.S).findall(data)
#     print(userlist)
#     print(contentlist)
     x=1
     for content in contentlist:
         content=content.replace('\n','')
         name=content+str(x)
         #exec(name+'=content')
         x+=1
     y=1
     for user in userlist:
#         name='content'+str(y)
         print('用户'+str(page)+str(y)+'是'+user)
         print('内容是')
         exec('print(name)')
         print('\n')
         y+=1
for i in range(1,3):
    url='http://www.qiushibaike.com/8hr/page'+str(i)
    getcontent(url,i)