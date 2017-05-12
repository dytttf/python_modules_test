#coding:utf8
import time
from threading import Thread, Condition

def work(i, cond):
    while 1:
        cond.acquire()
        print("i am %s" % i)
        cond.notify()
        cond.wait()
        time.sleep(1)
        cond.release()


def producer(cond):
    while 1:
        cond.acquire()
        print("one job")
        cond.wait()
        time.sleep(1)
        cond.release()

def test_cond():
    cond = Condition()
    thread_list = []
    t = Thread(target=producer, args=(cond,))
    t.start()
    thread_list.append(t)
    for i in range(3):
        t = Thread(target=work, args=(i, cond))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()
    return

if __name__ == "__main__":
    test_cond()
