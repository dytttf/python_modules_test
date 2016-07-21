# coding:utf8
'''
redis测试
    timeout: 测试超时重连
    test_watch: 测试watch
'''
import time
import redis
import threading

redis_uri = "redis://localhost:6379/0"

def timeout():
    conn = redis.StrictRedis.from_url(redis_uri,
                                      #retry_on_timeout=True,
                                      #socket_timeout=20,
                                      )
    print conn.keys("*")
    conn_list = conn.connection_pool._available_connections
    print [id(x) for x in conn_list]
    time.sleep(15)
    print conn.keys("*")
    conn_list = conn.connection_pool._available_connections
    print [id(x) for x in conn_list]
    return


def test_watch():
    def work_1(conn):
        conn.set("test_watch_str", "1")
        pipe = conn.pipeline()
        pipe.watch("test_watch_str")
        print u"开始监视---尚未执行 : multi"
        time.sleep(4)
        try:
            pipe.multi()
            pipe.get('test_watch_str')
            print u"执行成功结果 ： %s"%pipe.execute()
        except redis.exceptions.WatchError as e:
            print u"捕获WatchError成功"
            print e
        except Exception as e:
            print e
        return

    def work_2(conn):
        time.sleep(1)
        conn.set("test_watch_str", "1")
        print u"修改成功"
        return 
    conn = redis.StrictRedis.from_url(redis_uri)
    thread_list = []
    thread_1 = threading.Thread(target=work_1, args=(conn, ))
    thread_list.append(thread_1)
    thread_2 = threading.Thread(target=work_2, args=(conn, ))
    thread_list.append(thread_2)
    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
    return


def script_load(script):
    '''载入lua脚本'''
    sha = [None]
    def call(conn, keys=[], args=[], force_eval=False):
        if not force_eval:
            if not sha[0]:
                sha[0] = conn.execute_command(
                    "SCRIPT", "LOAD", script, parse="LOAD"                
                )
            try:
                return conn.execute_command(
                    "EVALSHA", sha[0], len(keys), *(keys+args)                
                )
            except redis.exceptions.ResponseError as msg:
                if not msg.args[0].startswith('NOSCRIPT'):
                    raise
        return conn.execute_command(
                "EVAL", script, len(keys), *(keys+args))
    return call

def test_incr():
    conn = redis.StrictRedis.from_url(redis_uri)
    key = "test_incr"
    from multiprocessing.dummy import Pool
    conn.delete(key)

    pool = Pool(100)
    pool.map(lambda x: conn.incrby(key,2), range(100000))
    print conn.get(key)
    

if __name__ == "__main__":
    timeout()
    #test_watch()
    #test_incr()
