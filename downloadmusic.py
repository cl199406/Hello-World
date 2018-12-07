# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:58:08 2018

@author: cl
"""
#下载网易云音乐的歌曲
import requests,os,time,sys,re
from scrapy.selector import Selector
from urllib import request

class wangyimusic(object):
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/'}
        self.main_url='http://music.163.com/'
        self.session=requests.Session()
        self.session.headers=self.headers
    def get_songurls(self,playlist):
        url=self.main_url+'playlist?id=%d' % playlist
        re=self.session.get(url)
        sel=Selector(text=re.text)
        songurls=sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        return songurls
    def get_songinfo(self,songurl):
        url=self.main_url+songurl
        re=self.session.get(url)
        sel=Selector(text=re.text)
        song_id=url.split('=')[1]
        song_name=sel.xpath("//em[@class='f-ff2']/text()").extract_first()
        singer='&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
        songname=singer+'-'+song_name
        return str(song_id),songname
    def download_song(self,songurl,dir_path):
        song_id,songname=self.get_songinfo(songurl)
        song_url='http://music.163.com/song/media/outer/url?id=%s.mp3'%song_id
        path=dir_path+os.sep+songname+'.mp3'
        request.urlretrieve(song_url,path)
    def work(self,playlist):
        songurls=self.get_songurls(playlist)
        dir_path=r'D:\test'
        for songurl in songurls:
            self.download_song(songurl,dir_path)
if __name__=='__main__':
    d=wangyimusic()
    d.work(2303649893)