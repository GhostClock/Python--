#!/usr/bin/python
# coding=utf-8

import pymysql

def insertData(db,tablename,id,first_name,last_name,age,sex,income):
    cursor = db.cursor()

    sql = "insert into %s (id,first_name,last_name,age,sex,income) values ('%d','%s','%s','%d','%s','%d')" % \
          (tablename,id,first_name,last_name,age,sex,income)

    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Warning:
        print "Code "
        db.rollback()

