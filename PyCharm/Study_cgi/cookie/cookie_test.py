#!/usr/bin/python
# coding:utf-8

# Cookie的设置 cookie会在http头部单独发送
print "Content-type:text/html"
print 'Set-Cookie: name="ghost";expires=Wed,29 Otc 2018 18:00:00 GMT'
print
print """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Cookie的设置</title>
        </head>
        <body>
            <h1>Cookie设置成功</h1>
        </body>
    </html>
"""