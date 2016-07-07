#coding:utf8
'''
contextlib 测试代码
'''
import time
import contextlib



#上下文管理器
@contextlib.contextmanager
def access_time():
    start = time.time()
    yield
    delta = time.time() - start
    print delta
    return

#测试
#with access_time():
#    time.sleep(5)




if __name__ == "__main__":
    pass
