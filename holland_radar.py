# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:27:43 2018

@author: cl
"""
#霍兰德人格分析雷达图

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
radar_labels=np.array(['研究型','艺术型','社会型',\
                       '企业型','常规型','现实型'])
data=np.array([[0.40,0.32,0.35,0.3,0.3,0.88],
              [0.85,0.35,0.3,0.4,0.4,0.3],
              [0.43,0.89,0.30,0.28,0.22,0.30],
              [0.3,0.25,0.48,0.85,0.45,0.40],
              [0.2,0.3,0.4,0.53,0.65,0.25],
              [0.34,0.31,0.38,0.40,0.92,0.28]])
data_labels=('艺术家','实验员','工程师','推销员','社会工作者'\
             ,'记事员')
angles=np.linspace(0,2*np.pi,6,endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure(facecolor='white')
plt.subplot(111,polar=True)
plt.plot(angles,data,'o-',linewidth=1,alpha=0.2)
plt.fill(angles,data,alpha=0.25)
plt.thetagrids(angles*180/np.pi,radar_labels,frac=1.2)
plt.figtext(0.52,0.95,'霍兰德人格分析',ha='center',size=20)
legend=plt.legend(data_labels,loc=(0.94,0.80),labelspacing=0.1)
plt.setp(legend.get_texts(),fontsize='large')
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show()