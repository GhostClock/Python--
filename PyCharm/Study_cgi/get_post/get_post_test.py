#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi,cgitb


# 创建FieldStorage的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_age = form.getvalue('age')

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print '<meta charset="utf-8">'
print "</head>"
print "<body>"
print "<h2>name: %s</h2><br/><h2>age: %s</h2>" % (site_name,site_age)
print "</body>"
print "</html>"
