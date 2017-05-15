#!/usr/bin/python
# coding:utf-8

import json

# 将数组编码成json数据
data = [{'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}]
j = json.dumps(data)
print j

# 使用参数让json数据格式化输出
print json.dumps({'a':"Google",'b':7},sort_keys=True,indent=4,separators=(',',': '))

# json.loads 用于解码json数据,该函数返回Python字段的数据类型
data2 = '{"a":1,"b":2,"c":3,""d:4,"e":5,"f":6,"g":7}'
text = json.loads(data2)
print text


