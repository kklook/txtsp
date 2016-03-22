#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import re
import urllib2
from urllib2 import urlopen
import time
import os
import threading
from threading import Thread
class Spider(object):
    def __init__(self):
        self.rule_1='<h5>(.*?)下一页</a>'
        self.rule_2='class="page-en">(.*?)</a>'
        self.rule_3='(.*?)</h5>'
    def compile(self,rule):
        RE=re.compile(rule,re.S)
        return RE
    def getPage(self,url):
        request=urllib2.Request(url)
        opener=urlopen(request)
        return opener.read()
    def mkdir(self,path):
        if(not os.path.exists(path)):
            os.makedirs(path)
            return True
        else:
            return False
    def saveImgLoop(self,url,dirname,i):
        value=None
        date=None
        try:
            value=urlopen(url)
            date=value.read()
        except urllib2.HTTPError,e:
            for i in range(3):
                time.sleep(0.5)
                try:
                    value=urlopen(url)
                    date=value.read()
                except urllib2.HTTPError,e:
                    print url+'第'+str(i+1)+'次重试出错'
                    if(i==2):
                        print url+' is not exitis'
                        return None
                    continue
                else:
                    break
        with open('static/'+dirname+'/'+str(i)+'.jpg','wb') as f:
            f.write(date)
    def saveImg(self,i,end,dirname):
        k=1
        thread=[]
        while k<=end:
            url='http://img1.mm131.com/pic/'+str(i)+'/'+str(k)+'.jpg'
            t=Thread(target=self.saveImgLoop,args=(url,dirname,k))
            thread.append(t)
            k=k+1
        for t in thread:
            t.start()
        for t in thread:
            t.join()
    def run(self):
        i=1100
        while i<1120:
            url="http://www.mm131.com/xinggan/"+str(i)+'.html'
            try:
                date=self.getPage(url)
            except urllib2.HTTPError,e:
                i=i+1
                continue
            date=date.decode('gbk').encode('utf-8')
            value=re.search(self.compile(self.rule_1),date)
            p=re.findall(self.compile(self.rule_2),value.group(1))
            dirname=re.findall(self.compile(self.rule_3),value.group(1))
            p=p[-1]
            dirname=dirname[0]
            self.mkdir('static')
            self.mkdir('static/'+str(i))
            with open('static/'+str(i)+'/'+'name.txt','w') as f:
                f.write(dirname)
            self.saveImg(i,int(p),str(i))
            i=i+1

s=Spider()
s.run()
print '完成任务'