#coding:utf-8
import sqlite3

#链接数据库，不存在则创建
#conn = sqlite3.connect('./test.db')
#内存中创建数据库
conn = sqlite3.connect(':memory:')

#建立游标
cursor = conn.cursor()
#执行语句
cursor.execute('create table test1(id integer primary key, pid varchar(100)\
                , name text NULL)')
#提交
conn.commit()

#执行插入语句
sql = 'insert into test1 values("1","01","duanyifei")'
cursor.execute(sql)
conn.commit()

#查询
cursor.execute('select * from test1')
l = cursor.fetchall()
print l



