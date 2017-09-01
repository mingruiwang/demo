# -*- coding:utf-8 -*-
import MySQLdb
db = MySQLdb.connect("localhost", "root", "123", "python")
cursor = db.cursor()
cursor.execute("select * from employee")
result = cursor.fetchall()
print result

# sql = """insert into employee (ID,FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
# VALUES (4,"JACK","MICL",32,1,21000.0)"""
# cursor.execute(sql)
# db.commit()
# 一次性插入多条数据
sql = "insert into employee  VALUES (%s,%s,%s,%s,%s,%s)"
data = [(7, "jim", "jim", 32, "1", 1232), (8, "tom", "tom", 34, "0", 1111)]
cursor.executemany(sql, data)

db.commit()
db.close()








