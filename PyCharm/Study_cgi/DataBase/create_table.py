#!/usr/bin/python
# coding=utf-8

import connent_db
import pymysql

def create(db ,tablename):
    cursor = db.cursor()

    # 创建数据表的SQL语句 if not exists 判断该表是否存在
    create_table_sql = """
        create table if not exists %s (
            id int,
            first_name char(20) not null,
            last_name char(20),
            age int,
            sex char(1),
            income float
        )
        """ % tablename
    try:
        result = cursor.execute(create_table_sql)
        print "result = %r" % result
        return result
    except pymysql.Warning as w:
        print w.message
