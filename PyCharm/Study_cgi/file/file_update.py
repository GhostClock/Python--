#!/usr/bin/python
# coding:utf-8

import cgi,os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form.getvalue('filename')


#检测文件是否上传
if fileitem.filename :
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn,'wb').write(fileitem.filename)

    message = '文件 "' + fn + '" 上传成功'

else:
    message = "文件没有上传"

print """\
    Content-type:text/html\n
    <html>
        <head>
            <meta charset="utf-8">
            <title>文件上传</title>
        </head>
        <body>
            <p> %s </p>
        </body>
    </html>
""" % message