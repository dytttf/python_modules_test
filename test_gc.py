# coding:utf-8
'''
检测内存信息
'''
import gc
import pprint

# 调试标志
gc.DEBUG_STATS  # 输出内存回收时的信息
gc.DEBUG_COLLECTABLE  # 输出可以被回收的对象的个数信息
gc.DEBUG_UNCOLLECTABLE  # 输出无法使用但也无法回收的对象信息
gc.DEBUG_INSTANCES  # 输出实例对象
gc.DEBUG_OBJECTS  # 输出非示例对象
gc.DEBUG_SAVEALL  # 保存被回收的对象到 gc.garbage 而不是释放他们
gc.DEBUG_LEAK  # 调试程序标志位 相当于设置了所有的标志(除了 gc.DEBUG_STATS)

# gc.disable()  # 关闭自动内存回收
# gc.enable()  # 开启自动内存回收

### 获取被回收的对象个数
##print(gc.get_count())

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
# 查看内存回收机制是否开启
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
