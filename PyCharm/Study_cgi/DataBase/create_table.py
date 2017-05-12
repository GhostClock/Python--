#!/usr/bin/python
# coding=utf-8

import connent_db
import pymysql

def create(db):
    cursor = db.cursor()

    # 创建数据表
    # 如果数据表已经查找使用execute()方法将其删除表
    cursor.execute("drop table if exists employee")
    # 创建数据表的SQL语句
    create_table_sql = """
        create table emplpyee (
            id int,
            first_name char(20) not null,
            last_name char(20),
            age int,
            sex char(1),
            income float
        )
        """
    try:
        result = cursor.execute(create_table_sql)
        print "result = %r" % result
        return result
    except pymysql.Warning as w:
        print w.message
