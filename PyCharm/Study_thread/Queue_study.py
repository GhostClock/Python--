#!/usr/bin/python
# coding:utf-8

import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread): #继承父类threading.Thread
    def __init__(self,threadID,counter,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.counter = counter
        self.qu = q
    def run(self):
        print "Starting" + self.name
        print process_data(self.name, self.qu)
        print "Exiting" + self.name

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not  workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName,data)
        else:
            queueLock.release()

        time.sleep(1)


theadList = ["线程-1","线程-2","线程-3"]
nameList = ["one","two","three","four","five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in theadList:
    th = myThread(threadID,tName,workQueue)
    th.start()
    threads.append(th)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1
for t in threads:
    t.join()
print "Main Thread Exiting"