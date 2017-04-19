import requests

url = "https://www.zhihu.com/#signin"

try:
     z = requests.get(url) 
except EOFError :
    print "error",EOFError.message

print z.status_code

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

z1 = requests.get(url,headers=headers)
print z1.status_code

from lxml import etree

sel = etree.HTML(z1.content)

_xsrf = sel.xpath('//input[@name="_xsrf"]/@value')[0]
print _xsrf

# 模拟登录
loginurl = 'https://www.zhihu.com/login/email'
fromdata = {
    '_xsrf':_xsrf,
    'password':'yuanhappy131',
    'email':'zhangyuanlaifen@163.com'
}
z2 = requests.post(url=loginurl,data=fromdata,headers=headers)

print z2.status_code

headers['Cookie'] = z2.headers['Set-Cookie']
mylog = "https://www.zhihu.com/people/pa-chong-21/logs"
z3 = requests.get(url=mylog,headers=headers)
print z3.url
print z3.text
