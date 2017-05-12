#!/usr/bin/python
# -*- coding:utf-8 -*-

import cgi, os
import cgitb; cgitb.enable()


# 获取文件名
f = cgi.FieldStorage().getvalue('filename')

# 检测文件是否上传
if f is not  None:
    # 设置文件路径
    fn = os.path.basename(f.filename.replace("","/"))
    open('/tmp/' + fn,'wb').write(f.file.read())

    message = '文件 "' + fn + '" 上传成功'

else:
    message = "文件没有上传"

print """
    Content-Type:text/html
    <html>
        <head>
            <meta charset="utf-8">
            <title>文件上传</title>
        </head>
        <body>
            <p> %s </p>
        </body>
    </html>
""" % (message,)