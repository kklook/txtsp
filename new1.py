#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import webbrowser
class Cookie(object):
    def __init__(self):
        self.cookie=cookielib.MozillaCookieJar()
        self.handle=urllib2.HTTPCookieProcessor(self.cookie)
        self.opener=urllib2.build_opener(self.handle)
        self.value={'Login.Token1':'20122617','Login.Token2':'xxxxxxxx'}
        self.data=urllib.urlencode(self.value)
    def getimg(self):
        webbrowser.open('http://ssfw3.hlju.edu.cn/ssfw/jwcaptcha.do')
    def open(self):
        self.opener.open('http://my.hlju.edu.cn/userPasswordValidate.portal',self.data)
        self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/j_spring_ids_security_check')
        page=self.opener.open('http://ssfw3.hlju.edu.cn/ssfw/pkgl/kcbxx/4/2015-2016-2.do')
        print page.read()
        return self.cookie
cookie=Cookie()
cookie.open()