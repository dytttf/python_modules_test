# coding:utf-8
import timeit

# 测试异常
# t = timeit.Timer("t=t\nprint t")

# t = timeit.Timer("t=1\nprint t", )
t = timeit.Timer("print t", setup='t=1')
try:
    t.timeit(number=10)
except:
    t.print_exc()

print 'repeat'
t.repeat(repeat=3, number=1)



# 命令行模式
# python -m timeit -n 10 -r 3 "[].append(1)"
