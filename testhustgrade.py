# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:00:03 2018

@author: cl
"""

import re,time
from selenium import webdriver
from bs4 import BeautifulSoup

options=webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) \
                     AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
browser=webdriver.Chrome(chrome_options=options)
browser.get('http://yjsjw.hust.edu.cn/hub.jsp')
#a=browser.find_element_by_link_text('学号')
#a.click()
username=browser.find_element_by_xpath('//*[@id="user_t"]')
username.click()
user=browser.find_element_by_id('username')
user.send_keys('M201671018')
password=browser.find_element_by_id('pwd_t')
password.click()
psw=browser.find_element_by_id('password')
psw.send_keys('304677')
b=browser.find_element_by_name('submit')
b.click()
browser.switch_to_frame('main_side')
d=browser.find_element_by_xpath('//*[@id="218"]')
d.click()
#browser.switch_to_default_content
#print(browser.page_source)
e=browser.find_element_by_xpath('//*[@id="218"]/ul')
e.click()
f=browser.find_element_by_id('830')
f.click()
browser.implicitly_wait(1)
html=browser.page_source
url=BeautifulSoup(html,'lxml')
url=url.find('li',id='1445')
url='http://yjsjw.hust.edu.cn'+url.a['href']
browser.get(url)
html2=browser.page_source

body=BeautifulSoup(html2,'lxml')
body=body.find('div',class_='modeldiv')
string='<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>'
pattern=re.compile(string,re.S)
#body=BeautifulSoup(body,'lxml')
body='''<div class="modeldiv">
<h2 class="title foldable">成绩列表</h2>
<div class="content">
<!--以下为程序员自由设计部分，内容为表格呈现的数据与所需的表单元素-->
<form method="post" name="form1">
<table>
<!--<caption>该处为表标题，不需要时请注释掉</caption>-->
<thead>
<tr>
</tr>
<tr>
<th>课程名称</th>
<th>学时/学分</th>
<th>上课学期</th>
<th>成绩类型</th>
<th>成绩</th>
</tr>
</thead>
<tbody>
<tr id="row_1">
<td>第一外国语（英语）（主校区）</td>
<td>32/2</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        免修
                                                        
                                                
                                          </td>
</tr>
<tr id="row_2">
<td>环境工程导论</td>
<td>16/1</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        86
                                                        
                                                
                                          </td>
</tr>
<tr id="row_3">
<td>能源经济学</td>
<td>32/2</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        88
                                                        
                                                
                                          </td>
</tr>
<tr id="row_4">
<td>汽液两相流动与传热</td>
<td>32/2</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        88
                                                        
                                                
                                          </td>
</tr>
<tr id="row_5">
<td>热工信号处理与可视化</td>
<td>32/2</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        80
                                                        
                                                
                                          </td>
</tr>
<tr id="row_6">
<td>热力系统辨识与仿真</td>
<td>32/2</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        85
                                                        
                                                
                                          </td>
</tr>
<tr id="row_7">
<td>数理统计</td>
<td>48/3</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        92
                                                        
                                                
                                          </td>
</tr>
<tr id="row_8">
<td>自然辩证法概论（理工医）（主校区）</td>
<td>18/1</td>
<td>2016年秋季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        89
                                                        
                                                
                                          </td>
</tr>
<tr id="row_9">
<td>动力工程现代测试技术</td>
<td>32/2</td>
<td>2017年春季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        78
                                                        
                                                
                                          </td>
</tr>
<tr id="row_10">
<td>高等传热传质理论</td>
<td>32/2</td>
<td>2017年春季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        69
                                                        
                                                
                                          </td>
</tr>
<tr id="row_11">
<td>情报检索</td>
<td>24/1.5</td>
<td>2017年春季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        67
                                                        
                                                
                                          </td>
</tr>
<tr id="row_12">
<td>文献阅读与选题报告</td>
<td>0/1</td>
<td>2017年春季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        通过
                                                        
                                                
                                          </td>
</tr>
<tr id="row_13">
<td>现代管理理论与方法</td>
<td>32/2</td>
<td>2017年春季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        88
                                                        
                                                
                                          </td>
</tr>
<tr id="row_14">
<td>中国特色社会主义理论与实践研究(主校区)</td>
<td>36/2</td>
<td>2017年春季</td>
<td>
                                                
                                                        正常
                                                
                                                
                                            
                                          
                                </td>
<td>
                                                
                                                        76
                                                        
                                                
                                          </td>
</tr>
</tbody>
<tbody><tr>
<td align="center" colspan="5">
<input class="btn" onclick="dybb();" type="button" value="查看培养计划表"/>
<!-- 
                                   <input  type="button" class="btn" value="个人成绩单" onclick="dygrcjd();">
                                    -->
</td>
</tr>
</tbody></table>
</form>
<!--//以上为程序员自由设计部分，内容为表格呈现的数据与所需的表单元素-->
</div>
</div>'''

res=re.findall(pattern,body)
class_name=[]
class_credit=[]
class_time=[]
class_mode=[]
class_score=[]
for item in res:
    class_name.append(item[0])
    class_credit.append(item[1])
    class_time.append(item[2])
    class_mode.append(item[3].strip())
    class_score.append(item[4].strip())
print(list(zip(class_name,class_credit,class_time,class_mode,class_score)))
    
    
       