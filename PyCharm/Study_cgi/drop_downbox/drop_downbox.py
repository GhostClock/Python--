#!/usr/bin/python
# coding:utf-8

import cgi,cgitb

form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    dropdownbox_value = form.getvalue('dropdown')
else:
    dropdownbox_value = "没有内容"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset:\"utf-8\">"
print "</head>"
print "<body>"
print "<h2>选中的是: %s </h2>" % dropdownbox_value
print "</body>"
print "</html>"