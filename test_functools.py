# coding:utf8
import functools
from functools import partial

# cmp_to_key(mycmp)
# Convert a cmp= function into a key= function
# 将比较函数转换为 key 函数
# 所谓比较函数 就是接受两个参数，然后在函数内判断大小返回True或False
# 所谓 key 函　就是接收一个函数， 然后将其转换为一个可比较的东西
# 比如 原序列是 [1,2,3,4,5] 进行排序的序列就是 [key(1), key(2), key(3), ...]
# sorted(range(5), key=lambda x: -x) 实现倒序 将 1 转换为 -1
print sorted(range(5), key=functools.cmp_to_key(lambda x, y: y-x))

#reduce


# total_ordering(cls)
# 用于简化比较函数的写法。如果你已经定义了 __eq__ 方法
# 以及 __lt__、__le__、__gt__ 或者 __ge__() 其中之一 即可自动生成其它比较方法



# partial(func, *args, **keywords)
# 偏函数

def say(word='', name=''):
    print '%s: %s'%(name, word)
    return

say_me = partial(say, name='me')
say_me('hello')


# Code from https://gist.github.com/carymrobbins/8940382
class partialmethod(partial):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return partial(self.func, instance,
                       *(self.args or ()), **(self.keywords or {}))

#wraps(wrapped,
#    assigned=('__module__', '__name__', '__doc__'),
#    updated=('__dict__',))
# 使用此装饰器函数消除自定义装饰器函数的副作用 例如 被装饰函数的 __name__ 等属性会变化

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs())
    return wrapper

def add(x,y):
    return x+y
print add

@decorator
def add(x,y):
    return x+y
print add


# update_wrapper(wrapper, wrapped,
#               assigned=('__module__', '__name__', '__doc__'),
#               updated=('__dict__',))
# 更强大的 wraps,  wraps 只是 update_wrapper 的特例

#def wraps(wrapped,
#          assigned = WRAPPER_ASSIGNMENTS,
#          updated = WRAPPER_UPDATES):
#    return partial(update_wrapper, wrapped=wrapped,
#                   assigned=assigned, updated=updated)


# 装饰器
def A(C):
    def B(*args, **kwargs):
        result = C(*args, **kwargs)
        return result
    return B

@A
def C(*args, **kwargs):
    print args
    print kwargs
    return
'''
等价关系推导
        @A
C <==>  def C():    <==>  A(C) <==> B
            ...

C(*args) <==> B(*args) <==> C(*args) <==> result
'''
