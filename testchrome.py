# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:09:28 2018

@author: cl
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
driver=webdriver.Chrome()
driver.get('http://www.python.org')
assert 'Python' in driver.title
elem=driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
print(driver.page_source)
'''
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options=options)#手机模拟访问
driver.get('https://www.baidu.com/')
