# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:05:10 2018

@author: cl
"""

import random
def printInfo():
    print('这个模拟程序模拟两个选手的某种竞技比赛')
    print('程序需要2个运动员的能力值（以0到1之间的小数）')
def getInput():
    a=eval(input('请输入A的能力值（0-1）：'))
    b=eval(input('请输入B的能力值(0-1):'))
    n=eval(input('模拟比赛的场次：'))
    return a,b,n
def printSummary(winsA,winsB):
    n=winsA+winsB
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(winsA,winsA/n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(winsB,winsB/n))
def gameover(a,b):
    return a==15 or b==15
 
def simoneGame(proA,proB):
    scoreA,scoreB=0,0
    serving='A'
    while not gameover(scoreA,scoreB):
        if serving=='A':
            if random.random()<proA:
                scoreA+=1
            else:
                serving='B'
        else:
            if random.random()<proB:
                scoreB+=1
            else:
                serving='A'
    return scoreA,scoreB
            
def simNGames(proA,proB,n):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simoneGame(proA,proB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB

def main():
    printInfo()
    proA,proB,n=getInput()
    winsA,winsB=simNGames(proA,proB,n)
    printSummary(winsA,winsB)
main()