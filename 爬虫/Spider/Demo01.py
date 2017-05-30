# coding:utf-8

import urllib2
import urllib

# response = urllib2.urlopen('https://www.v2ex.com/api/topics/hot.json')
# print response.read()

# request = urllib2.Request('https://www.v2ex.com/api/topics/hot.json')
# response = urllib2.urlopen(request)
# for dic in response.read():
#     print dic["title"]

# https://www.zhihu.com/signin
values = {'username':'zhangyuanlaifen@163.com','password':''}
data = urllib.urlencode(values)
url = 'https://passport.csdn.net/account/login'
request = urllib2.Request(url,data=data)
response = urllib2.urlopen(request)
print response.read()

