#!/usr/bin/python
# coding=utf-8

import pymysql

# 连接数据库
def content(host,port,user,password,database):
    try:
        db = pymysql.connect(host = host,port = port,user = user,password = password,db = database)
        return (db.open,db)
    except Exception as error:
        print error.message


# ok = content('127.0.0.1',3306,'root','','sys')
# print  ok[1].db