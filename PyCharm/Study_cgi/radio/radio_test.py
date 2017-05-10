#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi,cgitb

form = cgi.FieldStorage()

# 接受字段数据
if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = "提交数据为空"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset:\"utf-8\">"
print "</head>"
print "<body>"
print "<h2>选中的是: %s </h2>" % site
print "</body>"
print "</html>"


