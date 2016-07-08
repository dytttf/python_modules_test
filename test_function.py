# coding:utf8
'''
函数性质测试
'''

def show_args(a, b=None, *args, **kwargs):
    print a
    print b
    print args
    print kwargs
    return

#outer_arg = 0

#测试嵌套函数作用域
def outer():
    #global outer_arg
    outer_arg = 0
    def inner():
        global outer_arg
        outer_arg = 1
        print outer_arg
    inner()
    print outer_arg
    return


import time
#装饰器
def timeit():
    def wrap(func):
        def call(*args, **kwargs):
            print time.time()
            print args
            resp = func(*args, **kwargs)
            print time.time()
            return resp
        return call
    return wrap

@timeit()
def test_timeit(a):
    print 12
    return
#
#装饰器逻辑
#test_timeit(*args)
#    --> timeit()(test_timeit)(*args)
#        -->wrap(test_timeit)(*args)
#           -->call(*args)
                    

if __name__ == "__main__":
    #show_args(1, 2)
    #show_args(1, data=1, b=1)
    #outer()
    test_timeit(1)
    pass
