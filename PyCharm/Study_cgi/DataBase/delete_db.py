#!/usr/bin/python
# coding=utf-8
import pymysql

def delete(db,tablename):
    cursor = db.cursor()

    sql = "delete from %r where id > '%d'" % (tablename,30)

    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as error:
        print error.message