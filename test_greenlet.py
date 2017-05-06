# coding:utf-8
'''
greenlet
线程下的微线程
相当于一个代码块，可由用户指定何时执行某个微线程

switch(...):
    切换到此微线程并执行
    如果此微线程已结束，则返回给定的参数

throw(...):
    抛出异常 默认抛出 greenlet.GreenletExit()
    可指定异常 throw(IOError)

getcurrent()
    获取当前所在微线程

dead:
    微线程是否已结束

'''
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)


def test2():
    print(56)
    gr1.switch()
    print(78)
print(greenlet)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
print("gr1.dead: %s"%gr1.dead)
print("gr2.dead: %s"%gr2.dead)
print("切换回 gr2")
gr2.switch()
print("gr2.dead: %s"%gr2.dead)
