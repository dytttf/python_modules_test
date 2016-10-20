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
        print aaa
        

@contextlib.contextmanager
def make_Test(*args):
    t = Test(*args)
    t.enter()
    try:
        yield t
    #except Exception, err:
    except RuntimeError, err:
        print 'error', err
    finally:
        t.exit()


with make_Test(1,2,3) as f:
    f.run()

print 111

if __name__ == "__main__":
    pass
