#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
def getZhiHu():
    request=urllib2.Request("https://www.zhihu.com/#signin")
    response=urllib2.urlopen(request)
    inner=response.read()
    pattern=re.compile('<input type="hidden" name="_xsrf" value="(\w+?)"/>',re.S)
    result=re.search(pattern,inner)
    return result.group(1)
xsrf=getZhiHu()
print xsrf
value={'password':'ling123','remember_me':'true','email':'714779883@qq.com'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36','Referer':'http://www.zhihu.com/articles',
         'Accept': '*/*',
         'host':'www.zhihu.com',
         'method':'post',
         'path':'/login/email',
         'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
         'x-requested-with':'XMLHttpRequest'}
request=urllib2.Request('https://www.zhihu.com/#signin',urllib.urlencode(value),headers)
response=urllib2.urlopen(request)
print response.read()