#coding:utf8
'''
pymongo 3.0 模块测试
'''
import pymongo

#建立连接
conn = pymongo.MongoClient("localhost", 27017)

#查看所有数据库
print conn.database_names()
#选择数据库
db = conn.weibo
#验证用户
#db.authenticate("root", "123456")
#db = conn['weibo']
#查看当前数据库名字
print db.name
#查看所有表 collections
print db.collection_names()
#选择表
collection = db.users
#collection = db['users']
#查看表名
print collection.name
#查询数据
#data = collection.find_one({"id":5422536657L})
data = collection.find_one()
print type(data)




