#coding:utf8

'''
#类中公共变量和私有变量
class test(object):
    add = 1
    def __init__(self):
        print self.add
        self.add = 2
        print self.add
        print test.add
'''

#继承
'''
class A(object):
    x=1

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print A.x, B.x, C.x, D.x

C.x = 2
print A.x, B.x, C.x, D.x

B.x = 3
print A.x, B.x, C.x, D.x
'''

#单例模式
#测试版
'''
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                cls, *args, **kwargs
                )
        return cls._instance
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)
'''
#双检查锁机制实现单例
'''
import threading
class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:#double check locking
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locaker.release()'
        return cls.objs[cls]
'''

#利用python模块的导入机制实现单例模式
#singleton.py
#使用多线程测试是否为单例
'''
def work():
    try:
        reload(singleton)
    except:
        import singleton
    singleton.run()
    print singleton.num
    return
import threading
thread_list = []
for i in range(2):
    t = threading.Thread(target=work)
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
'''

#mixin
#混入模式,有问题
'''
class People(object):
    def make_tea(self):
        tea_name = self.get_tea_name()
        print tea_name
        return

class UseSampleTeapot(object):
    def get_tea_name(self):
        return 'Sample Tea'

class UseKungfuTeapot(object):
    def get_tea_name(self):
        return 'Kungfu Tea'

def simple_tea_people():
    people = People()
    People.__bases__ += (UseSampleTeapot,)
    return people

def sample_and_kungfu_tea_people():
    people = People()
    people.__bases__ += (UseSampleTeapot, UseKungfuTeapot)
    return people

if __name__ == "__main__":
    people = simple_tea_people()
    people.make_tea()
'''

# #self并非必须的
# class test(object):
#     def __init__(s):
#         s.b = 1
#     def a(s, b):
#         print s.b

# print test().b


# #__init__并非构造函数
# class A(object):
#     def __new__(cls, *args, **kwargs):
#         print cls
#         print args
#         print kwargs
#         print "---------"
#         instance = object.__new__(cls, *args, **kwargs)
#         print instance
#         #
#         #return instance

#     def __init__(self, a, b):
#         print 'init gets called'
#         print 'self is',self
#         self.a, self.b = a,b

# a1 = A(1,2)
# print a1.a
# print a1.b

# class UserSet(frozenset):

#     def __new__(cls, *args):
#         if args and isinstance(args[0], basestring):
#             args = (args[0].split(), ) + args[1:]
#         return super(UserSet, cls).__new__(cls, *args)

#     def __init__(self, arg=None):
#         if isinstance(arg, basestring):
#             arg = arg.split()
#         frozenset.__init__(self, arg)

# print UserSet('I am testing')
# print frozenset('I am testing')


# #简单工厂模式
# class Shape(object):
#     def __init__(object):
#         pass
#     def draw(self):
#         pass

# class Traingle(Shape):
#     def __init__(self):
#         print 'I am a Traingle'
#     def draw(self):
#         print 'I am draw Traingle'

# class Rectangle(Shape):
#     def __init__(self):
#         print 'I am a Rectangle'
#     def draw(self):
#         print 'I am draw Rectangle'

# class Trapezoid(Shape):
#     def __init__(self):
#         print 'I am a Trapezoid'
#     def draw(self):
#         print 'I am draw Trapezoid'

# class Diamond(Shape):
#     def __init__(self):
#         print 'I am a Diamond'
#     def draw(self):
#         print 'I am draw Diamond'

# class ShapeFactory(object):
#     shapes = {'Traingle':Traingle, 'Rectangle':Rectangle, 'Trapezoid':Trapezoid, 'Diamond':Diamond,}
#     def __new__(cls, name):
#         if name in ShapeFactory.shapes.keys():
#             print 'Creating a new shape %s'%name
#             return ShapeFactory.shapes[name]()
#         else:
#             print 'Creating a new shape %s'%name
#             return Shape()

# ShapeFactory('Diamond').draw()

# class MyClass(object):
#     """docstring for MyClass"""
#     def my_method(self, arg):
#         super(MyClass, self).__init__()
#         self.arg = arg
# # print MyClass.my_method
# # print MyClass().my_method
# # print MyClass.my_method.im_self
# # print MyClass().my_method.im_self

# print MyClass().__getattr__('my_method')
        
# class some_class(object):
#     """docstring for some_class"""
#     _x = None
#     def __init__(self):
#         super(some_class, self).__init__()
#         self._x = None

#     @property
#     def x(self):
#         print 'calling get method to return value'
#         return self._x
#     @x.setter
#     def x(self, value):
#         print 'calling set method to set value'
#         self._x = value
#     @x.deleter
#     def x(self):
#         print 'calling delete method to delete calue'
#         del self._x

# a = some_class()
# print a.x
# a.x = 2
# print a.x
# del a.x
# print a.x

'''
class PropertyTest(object):
    """docstring for PropertyTest"""
    def __init__(self):
        self.__var1 =  20

    @property
    def x(self):
        return self.__var1

pt = PropertyTest()
print pt.x
pt._PropertyTest__var1 = 30
print pt.x
pt.x = 2
'''
'''
class TestStr(object):
    def __init__(self):
        self.lis = ["a", "b", "c"]
    
    def __str__(self):
        return self.lis.pop()

TS = TestStr()
print TS
print TS
print TS
'''

'''
#有最大长度的列表
class Maxlist():
    def __init__(self, max_length):
        self.list = list()
        self.max_length = max_length

    def __getattr__(self, name):
        return getattr(self.list, name)

    def append(self,item):
        if len(self.list) >= self.max_length:
            self.list.pop(0)
        return self.list.append(item)

ml = Maxlist(10)
for i in range(20):
    ml.append(i)
'''   

# 元类
# 使用metaclass为列表添加add方法
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

#2.7 版本不支持这样定义
#class MyList(list, metaclass=ListMetaclass):
class MyList(list):
    __metaclass__ = ListMetaclass
    pass

l = MyList()
l.append(1)
l.add(2)
print(l)



