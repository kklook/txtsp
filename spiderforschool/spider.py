import urllib2
import urllib
import cookielib
class Spider(object):
    def __init__(self):
        self.url='http://my.hlju.edu.cn/'
        self.header={
            'Host':'my.hlju.edu.cn',
            'Cache-Control':'max-age=0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Origin':'http://my.hlju.edu.cn',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded',
            'Referer':'http://my.hlju.edu.cn/',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
        }
    def link(self,url):
        file='cookie.txt'
        cookie=cookielib.MozillaCookieJar(file)
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata=urllib.urlencode(
            {
                'user':'20122617',
                'pwd':'liang123',

            }
        )

        response=urllib2.Request(self.url,postdata,self.header)
        value=opener.open(response)
        print value.read()
        cookie.save(ignore_expires=True,ignore_discard=True)
        return opener.open(url)
    def run(self,url):
        print self.link(url).read()
s=Spider()
s.run('http://ssfw1.hlju.edu.cn/ssfw/index.do?from=')