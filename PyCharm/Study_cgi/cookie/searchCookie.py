#!/usr/bin/python
# coding:utf-8

# 检索 Cookie

# 导入模块
import os
import Cookie

print "Content-type:text/html"
print

print """
    <html>
        <head>
            <meta charset="utf-8">
            <title>读取Cookie</title>
        </head>
        <body>
            <h1>读取Cookie的消息</h1>
 """

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print "cookie date: %s <br/>" % data
    except KeyError:
        print "Cookie未设置或者已经过时"
        
print """
    </body>
    </html>
"""

