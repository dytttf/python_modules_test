#coding:utf-8

def fib(n):
    a = 1
    b = 1
    while a < n:
        a = yield a
        print '##',a
        a = 1
        #a, b = b, a+b

a = fib(4)
print a.next()
#send()控制yield返回值
#send(...)
#   send(arg) -> send 'arg' into generator,
#   return next yielded value or raise StopIteration.
print 'a.send(2)',a.send(2)
print 'a.send(3)',a.send(3)
print 'a.send(2.5)',a.send(2.5)


from contextlib import contextmanager

# yield实现上下文管理协议
@contextmanager
def tag(name):
    print '<%s>' % name
    yield
    print '</%s>' % name

with tag('h1'):
    print 'foo'
