# coding:utf-8
'''
检测内存信息
'''
import gc
import pprint


# 会导致内存泄漏的例子
'''
class Leak(object):
    def __init__(self):
        pass

while 1:
    A = Leak()
    B = Leak()
    A.b = B
    B.a = A
    A = None
    B = None
'''
#

print gc.isenabled()
#查看垃圾回收器的阈值
'''
(700, 10, 10)
这两个次数即上面get_threshold()返回的(700, 10, 10)返回的两个10。
也就是说，每10次0代垃圾回收，会配合1次1代的垃圾回收；而每10次1代的垃圾回收，
才会有1次的2代垃圾回收。
'''
print gc.get_threshold()

#手动启动垃圾回收
gc.collect()

class Leak(object):
    def __init__(self):
        pass

def main():
    collected = gc.collect()
    print 'Garbage collector before running: collected %d objects.' % (collected)
    print 'Creating reference cycles...'
    A = Leak()
    B = Leak()
    A.b = B
    B.a = A
    A = None
    B = None
    collected = gc.collect()
    pprint.pprint(gc.garbage)
    print 'Garbage collector after runninf: collected %d objects.' % (collected)

if __name__ == '__main__':
    main()
