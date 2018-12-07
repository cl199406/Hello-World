# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:19:42 2018

@author: cl
"""
#简单的文本进度条的实现包括整个运行实际运行时间
import time

print('执行开始'.center(25,'*'))
start=time.perf_counter()
scale=50
for i in range(scale+1):
    a='*'*i
    b='#'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    time.sleep(0.1)
print('\n'+'执行结束'.center(25,'*'))
    
    