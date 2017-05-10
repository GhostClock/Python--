# -*- coding:utf-8 -*-

ls = [123,456,789,"dsds"]

for s in ls:
    print s

numbers = [12,13,14,65,95,100]
even = []
odd = []

while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print even
print odd


num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if i % j == 0 :
            break
    else:
        num.append(i)

print num

n = 0
while n < 10:
    n += 1
    if n % 2 == 0 :
        continue
    print  n

import  math

print math.sqrt(3)

import random
print random.choice([1,3,2,6,5,1,3,5])


print "{} - {}".format("123","321")
print "{1} - {1} - {1} - {0}".format("1","2")

print "AsdgDGYdsrsSDDD".swapcase()
print len("ssss")


aList = [123,"123",523,"vxvd"]
aList.insert(3,[1,2,3,4])
print aList

print tuple([1,23,6,12,2,4])

import time
print time.time()

print time.localtime(time.time())
print time.asctime(time.localtime())

print time.strftime("%Y-%m-%d %H:%M:%S %w",time.localtime())

import calendar
print calendar.month(2017,6)

def test(num1,num2):
    return num1 * num2

sum = lambda num1,num2 : test(num1,num2)

print sum(10,20)

# import support

from support import print_func #

print_func("World")

# print dir(math)
#
# import  sys
# for s in sys.argv:
#     print  s

# help(sys)

Money = 200
def AddMoney():
    global Money
    Money += 1

print Money
AddMoney()
print Money

# str = raw_input(">")

# put = input("> ") #可以接受一个表达式
# print put

import io
# help(io)

f = open("text.txt","a+")
print "{}-{}-{}-{}".format(f.name,f.closed,f.mode,f.softspace)
for s in range(0,50):
    f.write("{}{}".format(s,"\n"))

f.close()

f = open("text.txt","r")
ss = f.read(20)
print ss

post = f.tell()
print post

post = f.seek(20,)
print post

import os
os.remove("text.txt")

try:
    f = open("t.txt","w")
    f.write("测试文件")
except IOError :
    print "该文件无读写权限"
else:
    print "OK"
    f.close()
