#!/usr/bin/python
# coding:utf-8

# 通过设置HTTP头来实现

print "Content-Disposition: attachment;filename=\"1.png\"";
print

# 打开文件
f = open("1.png","rb")

str  = f.read();
print str

# 关闭文件
f.close()