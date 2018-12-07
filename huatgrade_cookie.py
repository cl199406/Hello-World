# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:17:47 2018

@author: cl
"""

import urllib
from urllib import parse
import http.cookiejar
url='http://yjsjw.hust.edu.cn/hublogin.action'
data={'username':'M201671018',
              'password':'304677',
              'usertype':'xs',
              }
postdata=parse.urlencode(data).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWe\
             bKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file=opener.open(req)
data1=file.read()
print(data1)
url2='http://yjsjw.hust.edu.cn/hub.jsp'
data2=urllib.request.urlopen(url2).read()
#print(data2.decode('utf-8'))
#data3=urllib.request.urlopen(url,data).read()
data4=urllib.request.urlopen('http://yjsjw.hust.edu.cn/aam/wsxk/yjs/xs!gotogrcj.action?cdbh=1445').read()
print(data4.decode('utf-8'))