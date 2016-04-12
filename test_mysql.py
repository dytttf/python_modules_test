#coding:utf8
import time
import MySQLdb
from urlparse import urlparse

#很NB的一个东西, 可以将数据以字典形式返回
#cursor = mysql_conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

#cursor = mysql_conn.cursor()
def get_mysql_conn(db_string):
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
            charset = args.get('charset', 'utf8'),
            autocommit = True
            )
    mysql_conn.query("set names 'utf8'")
    return mysql_conn

class Cursor(object):
    '''重新封装cursor使得可以自动捕获mysql连接超时错误并重新连接'''
    def __init__(self, mysql_conn, db_string, **kwargs):
        self.cursor = mysql_conn.cursor(**kwargs)
        self.db_string = db_string
        self.kwargs = kwargs
        self.conn = mysql_conn

    def __getattr__(self, name):
        '''不存在的属性调用原cursor'''
        return getattr(self.cursor, name)

    def execute(self, sql, args=None):
        try:
            result = self.cursor.execute(sql, args=args)
        except MySQLdb.OperationalError as e:
            #捕获超时异常
            err_args = e.args
            code = err_args[0]
            if code in (2006, 2013):
                print u"超时重连 %s"%code
                #重连
                mysql_conn = self.get_mysql_conn()
                self.cursor = mysql_conn.cursor(**self.kwargs)
                self.conn = mysql_conn
                return self.execute(sql, args)
            else:
                raise MySQLdb.OperationalError(*err_args)
        return result

    def get_mysql_conn(self):
        par = urlparse(self.db_string)
        try:
            args = dict([tuple(x.split('=')) for x in par.query.split('&')])
        except:
            args = {}
        mysql_conn = MySQLdb.connect(
                host = par.hostname,
                user = par.username,
                passwd = par.password,
                db = par.path.strip('/'),
                charset = args.get('charset', 'utf8'),
                autocommit = True
                )
        mysql_conn.query("set names 'utf8'")
        return mysql_conn

def test_timeout():
    db_string = 'mysql://root:123456@localhost:3306/test?charset=utf8'
    mysql_conn = get_mysql_conn(db_string)
    cursor = Cursor(mysql_conn, db_string)
    #cursor = mysql_conn.cursor()
    cursor.execute("show databases;")
    time.sleep(70)
    try:
        cursor.execute("show databases;")
    except Exception as e:
        print e
    try:
        cursor.close()
        mysql_conn.close()
    except Exception as e:
        print e
    
    

if __name__ == "__main__":
    #db_string = 'mysql://root:123456@192.168.85.21:3306/test1?charset=utf8'
    #mysql_conn = get_mysql_conn(db_string)
    #cursor = Cursor(mysql_conn, db_string)
    #sql = 'show databases'
    #e = cursor.execute(sql)
    #print e
    #cursor.close()
    #mysql_conn.close()
    test_timeout()
    pass

