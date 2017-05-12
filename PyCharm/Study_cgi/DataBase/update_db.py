#!/usr/bin/python
# coding=utf-8

import pymysql

def update(db):
    cursor = db.cursor()

    sql = "update emplpyee set age = age + 1 where sex = '%c'" % ('M')
    try:
        cursor.execute(sql)
        db.commit
    except pymysql.Error as error:
        db.rollback() # 出错的话，九回滚
        print error.message