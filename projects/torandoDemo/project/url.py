#!/usr/bin/env python
# coding=utf-8

# 在这个文件中记录项目中所有和映射的类，即完成前面中handlers = [...]的功能

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from handler.index import IndexHandler
from handler.optform import OptionForm

url = [
    (r'/', IndexHandler),
    (r'/option', OptionForm),
]



