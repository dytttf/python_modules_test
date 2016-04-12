#coding:utf8
u'''
测试atexit

1、很遗憾，在被kill的时候也不会运行
2、必须在程序被终止之前执行的注册才可以，比如把while 放在register上面就不行

'''
import time
import atexit


def func():
    print 1
    return

atexit.register(func)

while 1:
    time.sleep(1)
    print 2


if __name__ == "__main__":
    pass
