#coding:utf-8
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
