# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:15:00 2018

@author: cl
"""
#实现简单的单行动态刷新进度条

import time
for i in range(101):
    print('\r{0:^3.0f}%'.format(i),end='')
    time.sleep(0.1)