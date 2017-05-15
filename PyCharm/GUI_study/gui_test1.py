#!/usr/bin/python
# coding:utf-8

from Tkinter import *

root = Tk()


li = ["C","Python","php","Java","Swift","OC","C++","C#"]
moive = ["CSS","GUI","MySQL"]

listb = Listbox(root) # 创建两个列表组件
listb2 = Listbox(root)

for item in li: # 第一个小部件插入数据
    listb.insert(0,item)

for item in moive:# 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack() # 将小部件放置主窗口
listb2.pack()

root.mainloop()


