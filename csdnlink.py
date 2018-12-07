# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:51:22 2018

@author: cl
"""

import re
from urllib import request


def getlink(url):
    headers=('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36')
    opener=request.build_opener()
    opener.addheaders=[headers]
    request.install_opener(opener)
    file=request.urlopen(url)
    data=str(file.read().decode('utf-8'))
    pat='(https?://[^\s]+\.(\w|/)*)'
    link=re.compile(pat,re.S).findall(data)
    link=list(set(link))
    return link
url='http://blog.csdn.net/'
linklist=getlink(url)
for link in linklist:
    print(link[0])
    