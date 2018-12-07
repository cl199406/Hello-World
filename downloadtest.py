# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:46:32 2018

@author: cl
"""

import requests,json,time,re
from contextlib import closing

class get_photos(object):
    def __init__(self):
        self.photos_id=[]
        self.download_server='https://unsplash.com/photos/xxx/download?force=trues'
        self.target='http://unsplash.com/napi/feeds/home'
        self.headers={'authorization':'Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09',
                      'x-unsplash-client': 'web'}
    def get_ids(self,nums):
        req=requests.get(url=self.target,headers=self.headers,verify=False)
        html=json.loads(req.text)
        next_page=html['next_page']
        for each in html['photos']:
            self.photos_id.append(each['id'])
        time.sleep(1)
        for i in range(nums):
            api=re.search(r'after=(.*)',next_page).group(1)
            next_page='https://unsplash.com/napi/feeds/home?after='+api
            req=requests.get(url=next_page,headers=self.headers,verify=False)
            html=json.loads(req.text)
            next_page=html['next_page']
            for each in html['photos']:
                self.photos_id.append(each['id'])
            time.sleep(1)
        return self.photos_id
            
    def download(self,photo_id,filename):
        target=self.download_server.replace('xxx',photo_id)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
        with closing(requests.get(url=target,stream=True,headers=headers,verify=False)) as r:
            with open('%d.jpg' % filename,'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()

if __name__=='__main__':
    gp=get_photos()
    print('working')
    id=gp.get_ids(0)
    print('working again')
    for i in range(len(gp.photos_id)):
        print('正在下载第%d张图片' % (i+1))
        gp.download(gp.photos_id[i],(i+1))
        
    