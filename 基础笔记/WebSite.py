import MySQLdb

host = "localhost"
port = 3306
user = "root"
password = "admin123"
db = "website"
charset = "utf8"

connect = MySQLdb.connect(host=host,port=port,user=user,passwd=password,db=db,charset=charset)
print connect










