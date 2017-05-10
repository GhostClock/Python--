#!/usr/bin/python
# coding:utf-8

import cgi

form = cgi.FieldStorage()

if form.getvalue("textcontent"):
    text_content = form.getvalue("textcontent")
else:
    text_content = "没有内容"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "</head>"
print "<body>"
print "<h2>内容是:<br> %s</h2>" % text_content
print "</body>"
print "</html>"
