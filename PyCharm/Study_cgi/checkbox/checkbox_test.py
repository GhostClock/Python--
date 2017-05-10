#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi,cgitb


# 创建FieldStorage的实例化
form = cgi.FieldStorage()

if form.getvalue('google'):
    google_flag = "是"
else:
    google_flag = "否"

if form.getvalue("baidu"):
    baidu_flag = "是"
else:
    baidu_flag = "否"


print "Content-type:text/html"
print
print "<html>"
print "<head>"
print '<meta charset:"utf-8">'
print "</head>"
print "<body>"
print "<h2>是否选择了谷歌: %s</h2>" % google_flag
print "<h2>是否选择了百度: %s</h2>" % baidu_flag
print "</body>"
print "</html>"
