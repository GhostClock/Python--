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
ok = connent_db.content('192.168.1.100',3306,'root','admin123','test')
db = ok[1]

table_name = "emplpyee"

# 创建数据表
# create_table.create(db,table_name) # 这里要判断数据表是否存在

# 插入数据
# row = 0
# for row in range(0,50):
#     row += 1
#     insert_db.insertData(db,table_name,row,'Mac','Mohan',20,'F',1000 + row * 2)

# 查询数据
# query_db.query(db,table_name)

# 更新数据库
update_db.update(db,table_name)

# 删除数据库
delete_db.delete(db,table_name)
query_db.query(db,table_name)

# 关闭数据库
close_db.close_db(db)


