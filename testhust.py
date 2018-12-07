# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:15:06 2018

@author: cl
"""
#爬取华科研究生就业信息网学生毕业去向登记
from selenium import webdriver
from bs4 import BeautifulSoup

options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
browser=webdriver.Chrome(chrome_options=options)
browser.get('http://career.hust.edu.cn/default.html')
browser.implicitly_wait(3)
a=browser.find_element_by_class_name('loginLinkRight')
a.click()
browser.switch_to_window(browser.window_handles[1])


name=browser.find_element_by_id('username_text')
name.send_keys('M201671018')
password=browser.find_element_by_id('password_text')
password.send_keys('kbf_45623')
b=browser.find_element_by_class_name('login_box_landing_btn')
b.click()
browser.switch_to_window(browser.current_window_handle)
browser.switch_to_frame('iframe_150278421730350766')
browser.find_element_by_class_name('grzx').click()

current_window = browser.current_window_handle
all_window=browser.window_handles
for window in all_window:
    if window != current_window:
        browser.switch_to.window(window)
browser.refresh()
print(browser.current_url)
browser.get(browser.current_url)
browser.switch_to_frame('iframe_150285106733187588')
b=browser.find_element_by_id('gnmkList')
b.find_element_by_link_text('毕业去向登记').click()
browser.switch_to_frame('frame_content')
html=browser.page_source


bf1=BeautifulSoup(html,'lxml')
txt=bf1.form
table=txt.find_all('table')
with open('毕业去向登记.txt','w',encoding='utf-8') as f:
    for c in table:
        f.write(c.get_text().strip().replace('\n'*4,'\n').replace('\n'*3,'\n'))
        
    

    
    



