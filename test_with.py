#coding:utf8
from contextlib import contextmanager
import time

#使用__enter__, __exit__ 定义类实现with
class test_with_class(object):
    def __enter__(self):
        print "enter"

    def __exit__(self, *args):
        print "exit"

#with test_with_class() as a:
#    print 1


#使用contextmanager将一个生成器函数转换为上下文管理器
@contextmanager
def test_context():
    print "enter"
    try:
        yield 1
    finally:
        print 'exit'
    return

with test_context() as f:
    print 1

if __name__ == "__main__":
    pass
