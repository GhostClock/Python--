#!/usr/bin/python
# coding=utf-8

import connent_db
import create_table
import insert_db
import query_db
import close_db
import update_db
import delete_db

# 连接数据库
ok = connent_db.content('127.0.0.1',3306,'root','','Test')
db = ok[1]

# 创建数据表
# print create_table.create(db) #这里要判断数据表是否存在

# 插入数据
# row = 0
# for row in range(0,50):
#     row += 1
#     insert_db.insertData(db,row,'Mac','Mohan',20,'F',2000)

# 查询数据
# query_db.query(db)

# 更新数据库
update_db.update(db)
query_db.query(db)

# 删除数据库
delete_db.delete(db)


# 关闭数据库
close_db.close_db(db)


