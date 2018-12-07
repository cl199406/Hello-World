# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:33:58 2018

@author: cl
"""

import re
from urllib import request
import http.cookiejar

vid='1472528692'
comid='6173403130078248384'
#url='http://coral.qq.com/article/'+vid+'/comment?commentid='+comid+'&reqnum=20'
url='https://video.coral.qq.com/varticle/1472528692/comment/v2?callback=_varticle\
1472528692commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6222164778406202058&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1542366057232'
headers={'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'Accept-Encoding':' gb2312,utf-8',
         'Accept-Language':' zh-CN,zh;q=0.9',
         'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)',
         'Connection':'keep-alive',
         'referer':'qq.com'}
cjar=http.cookiejar.CookieJar()
opener=request.build_opener(request.HTTPCookieProcessor(cjar))
header=[]
for key,value in headers.items():
    item=(key,value)
    header.append(item)
opener.addheaders=header
request.install_opener(opener)
data=request.urlopen(url).read().decode('utf-8')
print(data)
idpat='"id":"(.*?)"'
userpat='"nick":"(.*?)"'
conpat='"content":"(.*?)"'

idlist=re.compile(idpat,re.S).findall(data)
userlist=re.compile(userpat,re.S).findall(data)
conlist=re.compile(conpat,re.S).findall(data)

for i in range(0,10):
    print('user is:'+eval('u"'+userlist[i]+'"'))
    print('content is:'+eval('u"'+conlist[i]+'"'))
    print('\n')
