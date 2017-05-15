#!/usr/bin/python
# coding:utf-8

import threading
import time

runFlag = False

exitFlag = 0


class myThread (threading.Thread): #继承父类threading.Thread
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting" + self.name
        print print_time(self.name,self.counter,5)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()

        time.sleep(delay)
        print "%s:%s" % (threadName,time.ctime(time.time()))
        counter -= 1

class myThread1 (threading.Thread): #继承父类threading.Thread
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting" + self.name
        threadLock.acquire()
        # 获得锁,成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后返回false
        print_time(self.name,self.counter,3)
        # 释放锁
        threadLock.release()
def print_time1(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print "%s:%s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

if runFlag:
    th1 = myThread(1,"线程1",1)
    th2 = myThread(2,"线程2",2)

    th1.start()
    th2.start()

    print "主线程退出"

else:
    th11 = myThread1(1,"Thread - 1",1)
    th22 = myThread1(2,"Thread - 2",2)

    th11.start()
    th22.start()

    threads.append(th11)
    threads.append(th22)

    for th in threads:
        th.join()
    print "Main Thread exit"


