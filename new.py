#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import random
import threading
from threading import Thread
class baseman(object):
    def __init__(self):
        self.healthy=random.uniform(0,100)
        self.attack=100-self.healthy
        self.basehealthy=self.healthy
        self.live=True
    def kill(self,other):
        if self.live==False:
            return ;
        if(other.healthy<self.attack):
            other.die()
        else:
            other.healthy=other.healthy-self.attack
    def die(self):
        self.live=False
class arena(object):
    def __init__(self):
        self.man=[]
        self.n=0
    def newMan(self,n):
        if isinstance(n,int):
            self.n=n
            for i in range(n):
                self.man.append(baseman())
    def runGame(self):
        GameMap={}
        if self.n!=0:
            for i in range(self.n/2):
                first=random.randint(0,self.n-1)
                while(first in GameMap):
                    first=random.randint(0,self.n-1)
                second=random.randint(0,self.n-1)
                while(second in GameMap or first==second):
                    second=random.randint(0,self.n-1)
                GameMap[first]=second
                GameMap[second]=first
                self.man[first].kill(self.man[second])
                self.man[second].kill(self.man[first])
            self.man=filter(self.isLive,self.man)
            self.n=len(self.man)
    def WCG(self,n,m):
        if isinstance(n,int):
            self.newMan(m)
            for i in range(n):
                self.runGame()
                if(len(self.man)==1):
                    print "攻击力:%d 基础生命值:%d 剩余生命值:%d"%(self.man[0].attack,self.man[0].basehealthy,self.man[0].healthy)
                    return self.man[0]
    def isLive(self,thisman):
        return thisman.live

threads=[]
are=arena()
sumtemp=0
coe=0
def runthread(n):
    m=are.WCG(100,n)
    global sumtemp
    sumtemp+=(m.attack*m.healthy)
    global coe
    coe+=m.healthy
for i in range(100):
    t=Thread(target=runthread,args=(10000))
    threads.append(t)
for i in threads:
    if __name__=='__main__':
        i.start()
for i in threads:
    i.join()
if coe!=0:
    sumtemp=sumtemp/coe
print coe
print sumtemp


