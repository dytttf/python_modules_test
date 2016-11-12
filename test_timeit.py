# coding:utf-8
import timeit
# __all__ = [Timer]
'''
Class Timer():
    __init__(self, stmt='pass', setup='pass', timer=<built-in function time>)
        @stmt: execute code
        @setup: scope
        @time: function to start the time

    print_exc(self, file=None)
        cache the code and traceback.print_exc(file=file)

    repeat(self, repeat=3, num=1000000)
        for i in range(repeat):
            timeit()

    timeit(self, number=1000000)
        def inner(_it, _timer%(init)s):
            %(setup)s
            _t0 = _timer()
            for _i in _it:
                %(stmt)s
            _t1 = _timer()
            return _t1 - _t0

'''

# 测试异常
# t = timeit.Timer("t=t\nprint t")

# t = timeit.Timer("t=1\nprint t", )
t = timeit.Timer("print t", setup='t=1')
try:
    print t.timeit(number=10)
except:
    t.print_exc()

print 'repeat'
t.repeat(repeat=3, number=1)



# 命令行模式
# -n number (default: 1000000)
# -r repeat (default: 3)
# -s setup (default:pass)
# -t time.time (default: on Unix)
# -c time.colck (default: on Windows)
# -v verbose
# -h
# -- statement

# python -m timeit -n 10 -r 3 "[].append(1)"
# add
