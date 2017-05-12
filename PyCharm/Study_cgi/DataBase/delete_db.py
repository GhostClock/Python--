#!/usr/bin/python
# coding=utf-8
import pymysql

def delete(db):
    cursor = db.cursor()

    sql = "delete from emplpyee where age > '%d'" % (30)

    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as error:
        print error.message