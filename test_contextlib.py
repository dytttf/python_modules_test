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

class Test(object):
    def __init__(self, *args):
        self.args = args

    def enter(self):
        print "enter"

    def exit(self):
        print "exit"

    def run(self):
        print self.args
        #print aaa
# 不需要定义 __enter__ 和 __exit__
# 在函数中自己调用 进入和退出的方法 使用 contextmanager 将函数包装成 上下文管理器

@contextlib.contextmanager
def make_Test(*args):
    t = Test(*args)
    t.enter()
    # 不会自动捕获异常 需要主动 try
    try:
        yield t
    #except Exception, err:
    except RuntimeError, err:
        print 'error', err
    finally:
        t.exit()


with make_Test(1,2,3) as f:
    f.run()

# 无返回值
@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield 
    print('</{}>'.format(name))

with tag('h1'):
    print name
    
if __name__ == "__main__":
    pass
