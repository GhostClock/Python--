#!/usr/bin/python
# coding=utf-8

import pymysql

def insertData(db,id,first_name,last_name,age,sex,income):
    cursor = db.cursor()

    sql = "insert into emplpyee (id,first_name,last_name,age,sex,income) values ('%d','%s','%s','%d','%s','%d')" % \
          (id,first_name,last_name,age,sex,income)

    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Warning:
        print "Code "
        db.rollback()

