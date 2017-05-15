#!/usr/bin/python
# coding:utf-8

import thread
import time

# 为线程定义一个函数
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s:%s" % (threadName,time.ctime(time.time()))


# 创建两个线程
try:
    thread.start_new_thread(print_time,("线程1",2,))
    thread.start_new_thread(print_time,("线程2",4,))

except thread.error as err:
    print "线程启动失败"
while 1:
    pass