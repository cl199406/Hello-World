# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:21:09 2018

@author: cl
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

# ***selenium 自动操作网页***                                                   #进行点击下一页操作
options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver=webdriver.Chrome(chrome_options=options)
driver.get('https://wk.baidu.com/view/aa31a84bcf84b9d528ea7a2c?pcf=2')
'''
time.sleep(10)

page = driver.find_element_by_xpath("//div[@class_='pagerwg-loadSucc']")
driver.execute_script('arguments[0].scrollIntoView();', page)               #拖动网页到可见的元素去
nextpage = driver.find_element_by_xpath("//div[@class_='pagerwg-button']")
nextpage.click()
'''
# ***对打开的html进行分析***
html = driver.page_source
bf1 = BeautifulSoup(html, 'lxml')

# 获得文章标题
title = bf1.find('div', class_='doc-title')
print(title.text)
filename = title.text.strip() + '.txt'

# 获得文章内容
texts_list = []
result = bf1.find_all('p', class_='txt')
#result1=BeautifulSoup(result,'lxml')
#result2=result1.find_all('p',class_='txt')
for each in result:
    bf3=BeautifulSoup(str(each), 'lxml')
    text=bf3.find_all('p')
    for each_ in text:
        texts_list.append(each_.text)
contents = ''.join(texts_list).replace(' '*20, '\n')
contents.strip()
# ***保存为.txt文件
with open(filename, 'w', encoding='utf-8') as f:
    f.writelines(contents)
    f.write('\n')
