#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
class Cookie(object):
    def __init__(self):
        self.cookie=cookielib.MozillaCookieJar()
        self.handle=urllib2.HTTPCookieProcessor(self.cookie)
        self.opener=urllib2.build_opener(self.handle)
        self.value={'username':'null122','userpass':'liang123'}
        self.data=urllib.urlencode(self.value)
    def open(self):
        self.opener.open('http://www.sodu.cc/handler/login.html',self.data)
        req=urllib2.Request('http://www.sodu.cc/home.html')
        page=self.opener.open(req)
        print page.read()
cookie=Cookie()
cookie.open()