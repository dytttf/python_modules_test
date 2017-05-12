#coding:utf-8
import time

def fib(n):
    a = 1
    b = 1
    while a < n:
        a = yield a
        print('##',a)
        a = 1
        #a, b = b, a+b

a = fib(4)
print(next(a))

#send()控制yield返回值
#send(...)
#   send(arg) -> send 'arg' into generator,
#   return next yielded value or raise StopIteration.
print('a.send(2)',a.send(2))
print('a.send(3)',a.send(3))
print('a.send(2.5)',a.send(2.5))


from contextlib import contextmanager

# yield实现上下文管理协议
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('foo')



def test():
    print("before sleep")
    # yield要等sleep完成后才会返回 仍然是同步操作 sleep不支持异步
    yield time.sleep(3)
    print("end sleep")

def test1():
    t = test()
    print(1)
    next(t)
    print(2)
    next(t)
    return

test1()
