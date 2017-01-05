#coding:utf8
'''
csv模块测试文件
'''
import re
import csv
import json
import redis
import copy
import MySQLdb
from urlparse import urlparse
import pymongo

def csv_write(info_list, file_name='', is_dict=True):
    '''
    writer
    根据字典列表写入csv
    可处理csv_write_dic()能处理的格式  [{a:1, b:2}, {a:2, b:3}]
    还可处理非字典形式  [(1,2),(2,3)]
    '''
    if not file_name:
        file_name = 'test.csv'
    writer = csv.writer(open(file_name,"wb"))
    if isinstance(info_list, dict):
        info_list = [info_list]
    if is_dict:
        keys = info_list[0].keys()
        #写入第一行
        writer.writerow(keys)
        code = compile("line = [info.get(key,'') for key in keys]", "", "exec")
    else:
        code = compile("line = list(info)", "", "exec")
    for info in info_list:
        exec code
        writer.writerow(line)
    return

def csv_write_dic(dic_list, file_name=''):
    '''
    DictWriter
    根据字典列表写入csv
    只能处理 [{a:1, b:2}, {a:2, b:3}]
    '''
    if not file_name:
        file_name = 'test.csv'
    if isinstance(dic_list, (dict)):
        dic_list = [dic_list]
    keys = dic_list[0].keys()
    #初始化
    writer = csv.DictWriter(open(file_name,"wb"), fieldnames=keys, dialect='excel')
    #写入第一行
    writer.writerow({key:key for key in keys})
    #写入字典列表
    writer.writerows(dic_list)
    return

def csv_write_from_txt(input_filename, out_filename, split_str='\t'):
    '''
    将给定文件中变为csv
    '''
    with open(input_filename,"r") as f:
        infos = f.readlines()
    infos = [x.replace("\n","").replace("\r","").split(split_str) for x in infos]
    keys = range(len(infos[0]))
    dics = [dict(zip(keys, x)) for x in infos]
    csv_write_dic(dics, out_filename)
    return 

def csv_read(file_name):
    '''
    reader
    '''
    if not file_name:
        file_name = 'test.csv'
    lis = []
    reader = csv.reader(open(file_name,"rb"))
    for line in reader:
        print line
        break
    return

def csv_read_dic(file_name=''):
    '''
    DictReader
    ###
    @fieldnames ： 指定读取的 fields, 
    @restval : 指定不存在的 field 时添加默认值  默认为None
    @restkey : 指定多余 value 存放字段 默认为None
    '''
    if not file_name:
        file_name = 'test.csv'
    #keys = ["aaa","bbb","ccc","ddd"]
    keys = []
    #reader = csv.DictReader(open(file_name,"rb"), fieldnames=keys, restkey='excess_field', restval='-1')
    reader = csv.DictReader(open(file_name,"rb"))
    for line in reader:
        print line
        break
    return

def csv_to_csv(file_name):
    '''
    reader
    '''
    if not file_name:
        file_name = 'test.csv'
    lis = []
    reader = csv.reader(open(file_name,"rb"))
    #处理
    lis = map(handle_list, list(reader))
    
    csv_write(lis, "new_"+file_name, False)
    return

def csv_to_csv_dic(file_name=''):
    '''
    DictReader
    '''
    if not file_name:
        file_name = 'test.csv'
    reader = csv.DictReader(open(file_name,"rb"))
    infos = list(reader)
    #处理
    infos = map(handle_dict, infos)
    
    csv_write_dic(infos, file_name="new_"+file_name)
    return

def handle_dict(dic):
    new_dic = {}
    for k,v in dic.iteritems():
        #此处添加处理代码
        #if k in ["TITLT", "CONTENT"]:
        #v = re.sub("[\n\r]", "", v)
        #v = re.sub("\?", "", v)
        v = v.decode('gbk')
        new_dic.update({k:v})
    return new_dic


def handle_list(line):
    new_list = []
    for i in line:
        new_list.append(i)
    return new_list


def get_mysql_conn(db_string):
    #db_string = 'mysql://user:passwd@host:port/db?charset=utf8'
    par = urlparse(db_string)
    try:
        args = dict([tuple(x.split('=')) for x in par.query.split('&')])
    except:
        args = {}
    mysql_conn = MySQLdb.connect(
            host = par.hostname,
            user = par.username,
            passwd = par.password,
            db = par.path.strip('/'),
            charset = args.get('charset', 'utf8')
            )
    return mysql_conn, mysql_conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

def mysql_to_csv():
    '''mysql直接转为csv'''
    #db_string = 'mysql://user:passwd@host:port/db?charset=utf8'
    db_string = 'mysql://root:123456&&&&@192.168.1.1:3306/test1?charset=utf8'
    conn, cursor = get_mysql_conn(db_string)
    sql = 'select * from test'
    cursor.execute(sql)
    infos = cursor.fetchall()

    #对mysql数据做处理后写入csv
    #infos = [handle_dict(info) for info in infos]
    infos = map(handle_dict, infos)
    
    csv_write_dic(infos, file_name='aaa.csv')
    
    conn.close()
    cursor.close()
    return

def redis_to_csv():
    import redis
    import json
    conn = redis.StrictRedis.from_url('redis://192.168.1.1/0')
    keys = ['data_test']
    for key in keys:
        filename = key + '.csv'
        infos = conn.lrange(key, 0, -1)
        infos = [json.loads(x) for x in infos]
        infos = [encode(x) for x in infos]
        csv_write_dic(infos, filename)
        print filename, 'ok'
    return

def csv_to_mongo(file_name):
    mongo_conn = pymongo.MongoClient("172.16.1.1", 27017)
    #选择数据库
    db = mongo_conn['cuort']
    #选择表
    collection = db['info']
    
    reader = csv.DictReader(open(file_name,"rb"))
    for dic in reader:
        collection.insert(handle_dict(dic))
        
    return

def csv_to_redis(file_name):
    conn = redis.StrictRedis.from_url('redis://192.168.1.1/0')
    reader = csv.reader(open(file_name,"rb"))
    infos = []
    for i in reader:
        url, title = i[0], i[1]
        info = {
            "news_url":url,
            "title":title.decode('gbk'),
            }
        infos.append(json.dumps(info))
    conn.lpush("sohu_reply_urls", *infos)
    return

if __name__ == "__main__":
    dic = {
        "aaa":111,
        "bbb":111,
        }
    lis = [(1,2),(2,3)]
    #csv_write_dic(dic)
    #file_name = 'test.csv'
    #csv_read('111.csv')
    #csv_read_dic(file_name)
    #csv_write(lis, '', False)
    #redis_to_csv()
    #csv_read_dic("111.csv")
    #csv_to_csv_dic("111.csv")
    #csv_to_csv_dic("aaa.csv")

    #mysql_to_csv()
    #csv_to_mongo(u"aaa.csv")
    #csv_to_redis(u"aaaa.csv")
    
    
    
    

