# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:45:22 2018

@author: cl
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import requests,os,time
def mkdir(path):
    isExists=os.path.exists(os.path.join('D:/test',path))
    
    if not isExists:
        os.makedirs(os.path.join('D:/test',path))
        os.chdir(os.path.join('D:/test',path))
        return True
    else:
        print(path,'already exists')
        os.chdir(os.path.join('D:/test',path))
        return False
def allpage():
    url = 'http://jandan.net/ooxx/'
    options=webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')
    browser=webdriver.Chrome(chrome_options=options)
    browser.get(url)
    browser.implicitly_wait(3)
    #allpage = soup.find('span', class_="current-comment-page").get_text()[1:-1]
    #allimgs = soup.select('div.text > p > img')
    html=browser.page_source
    
    soup=BeautifulSoup(html,'lxml')
    allpage =int(soup.find('span', class_="current-comment-page").get_text()[1:-1])
    browser.close()
    return allpage
    




def get_imgs():
    pages=allpage()
    baseurl='http://jandan.net/ooxx/'
    for page in range(1,int(pages/8)):
        nurl=baseurl+'page-'+str(page)
        path=nurl.split('-')[-1]
        mkdir(path)
        options=webdriver.ChromeOptions()
        options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')
        bro=webdriver.Chrome(chrome_options=options)
        bro.get(nurl)
        bro.implicitly_wait(1)
        html=bro.page_source
        so=BeautifulSoup(html,'lxml')
        allimgs = so.select('div.text > p > img')
        download(allimgs)
        bro.close()

def download(all):        
        for imgs in all:
            img=imgs['src']   
            filename=img.split('/')[-1]
            with open(filename,'wb') as f:
                resp=requests.get(img)
                f.write(resp.content)
if __name__=='__main__':
    t=time.time()
    get_imgs()
    print('下载完成：花费%d分钟' %((time.time()-t)/60))
    
