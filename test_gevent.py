#coding:utf-8
"""
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet
等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，
就保证总有greenlet在运行，而不是等待IO。

# gevent.monkey.patch_all()
使用之后一些模块的属性将会被替换成gevent定义的属性，无论这个模块是在patch之前导入还是之后导入

"""
import time

import gevent
from gevent import socket, Timeout
from gevent.event import Event


if 0:
    urls = ['www.baidu.com', 'www.sina.com.cn', 'www.python.org']
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=2)
    print [job.value for job in jobs]

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

if 0:
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
        ])


def test_timeout():
    # time.sleep(100)
    gevent.sleep(100)
    return 1

if 0:
    # timeout = Timeout(3)
    # timeout.start()
    try:
        with Timeout(3):
            gevent.spawn(test_timeout).join()
    except Timeout:
        print('timeout !!!')

event = Event()

def setter():
    print("A: Hey wait for me, i have to do something")
    gevent.sleep(3)
    print("Ok, I'm done")
    event.set()
    return 1

def waiter():
    print("I'll wait for you")
    event.wait()
    print("It's about time")
    return 1

if 0:
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
    ])

def talk(msg):
    print(msg+msg)
    gevent.sleep(0)
    print msg
    event.set()
    return
g1 = gevent.spawn(talk, 'bar')
print("g1 %s"%g1)
print(gevent.getcurrent())
#gevent.get_hub().switch()
#gevent.sleep(0)
#g1.switch()
event.wait()
print("ok")
