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
    #mysql_conn.query("set names 'utf8'")
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
                #print("超时重连 %s"%code)
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
    """测试超时错误 """
    db_string = 'mysql://root:123456@localhost:3306/test?charset=utf8'
    mysql_conn = get_mysql_conn(db_string)
    cursor = Cursor(mysql_conn, db_string)
    #cursor = mysql_conn.cursor()
    cursor.execute("show databases;")
    time.sleep(70)
    try:
        cursor.execute("show databases;")
    except Exception as e:
        print(e)
    try:
        cursor.close()
        mysql_conn.close()
    except Exception as e:
        print(e)
    return

# MySQLdb 接口说明
"""
MySQLdb.connections

class Connection(_mysql.connection)
    __init__(self, *args, **kwargs)
     |      Create a connection to the database. It is strongly recommended
     |      that you only use keyword parameters. Consult the MySQL C API
     |      documentation for more information.
     |      
     |      host   
     |      user
     |      passwd
     |      db   
     |      port
     |      
     |      unix_socket # mysql配置文件中属性 socket = /var/run/mysqld/mysqld.sock
     |        string, location of unix_socket to use
     |      
     |      conv 
     |        conversion dictionary, see MySQLdb.converters
     |      
     |      connect_timeout # 连接超时时间
     |        number of seconds to wait before the connection attempt
     |        fails.
     |      
     |      compress # 是否压缩
     |        if set, compression is enabled
     |      
     |      named_pipe
     |        if set, a named pipe is used to connect (Windows only)
     |      
     |      init_command # 一旦连接建立，就为数据库服务器指定一条语句来运行
     |        command which is run once the connection is created
     |      
     |      read_default_file # 一旦连接建立，就为数据库服务器指定一条语句来运行
     |        file from which default client values are read
     |      
     |      read_default_group
     |        configuration group to use from the default file
     |      
     |      cursorclass # cursor()使用的种类，默认值为MySQLdb.cursors.Cursor
     |        class object, used to create cursors (keyword only)
     |      
     |      use_unicode # 是否使用unicode
     |        If True, text-like columns are returned as unicode objects
     |        using the connection's character set.  Otherwise, text-like
     |        columns are returned as strings.  columns are returned as
     |        normal strings. Unicode objects will always be encoded to
     |        the connection's character set regardless of this setting.
     |        Default to False on Python 2 and True on Python 3.
     |      
     |      charset
     |        If supplied, the connection character set will be changed
     |        to this character set (MySQL-4.1 and newer). This implies
     |        use_unicode=True.
     |      
     |      sql_mode # 设置mysql sql_mode 模式
     |        If supplied, the session SQL mode will be changed to this
     |        setting (MySQL-4.1 and newer). For more details and legal
     |        values, see the MySQL documentation.
     |      
     |      client_flag
     |        integer, flags to use or 0
     |        (see MySQL docs or constants/CLIENTS.py)
     |      
     |      ssl # ssl连接设置
     |        dictionary or mapping, contains SSL connection parameters;
     |        see the MySQL documentation for more details
     |        (mysql_ssl_set()).  If this is set, and the client does not
     |        support SSL, NotSupportedError will be raised.
     |      
     |      local_infile # 设置 mysql --local-infile 选项
     |        integer, non-zero enables LOAD LOCAL INFILE; zero disables
     |      
     |      autocommit # 自动commit SQL命令
     |        If False (default), autocommit is disabled.
     |        If True, autocommit is enabled.
     |        If None, autocommit isn't set and server default is used.
     |      
     |      waiter # 
     |        Callable accepts fd as an argument. It is called after sending
     |        query and before reading response.
     |        This is useful when using with greenlet and async io.
     |      
     |      There are a number of undocumented, non-standard methods. See the
     |      documentation for the MySQL C API for some hints on what they do.
"""

"""
cursor 类别
MySQLdb.cursors
        BaseCursor
        CursorDictRowsMixIn
            CursorOldDictRowsMixIn
        CursorStoreResultMixIn
            Cursor(CursorStoreResultMixIn, CursorTupleRowsMixIn, BaseCursor)
            DictCursor(CursorStoreResultMixIn, CursorDictRowsMixIn, BaseCursor)
        CursorTupleRowsMixIn
        CursorUseResultMixIn
            SSCursor(CursorUseResultMixIn, CursorTupleRowsMixIn, BaseCursor)
            SSDictCursor(CursorUseResultMixIn, CursorDictRowsMixIn, BaseCursor)
"""

    
    

if __name__ == "__main__":
    #db_string = 'mysql://root:123456@192.168.85.21:3306/test1?charset=utf8'
    #mysql_conn = get_mysql_conn(db_string)
    #cursor = Cursor(mysql_conn, db_string)
    #sql = 'show databases'
    #e = cursor.execute(sql)
    #print(e)
    #cursor.close()
    #mysql_conn.close()
    #test_timeout()
    pass

