#!/usr/bin/python
# coding:utf-8

i = int(input("输入净利润>"))
I = [1000000,60000,40000,20000,10000,0]
r = [0.01,0.015,0.03,0.05,0.075,0.1]
for j in range(len(I)):
    if i > I[j]:
        b = [0,0,0,0,0,0]
        b[j] = i -I[j]
        for k in  range(j,len(I)):
            b[k] = I[k]
        bonus = sum(map(lambda (i1,i2) : i1 * i2, zip(b,r)))
        break

print "奖金: ",bonus