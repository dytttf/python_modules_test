#coding:utf8
import inspect

######---1----#######
#type checking

# #getmembers(object, predicate=None)
# print inspect.getmembers(inspect)[0]
# def isstr(obj):
#     if isinstance(obj, str):
#         return True
#     return False
# print inspect.getmembers(inspect, isstr)[0]

# #getmoduleinfo(path)
# m = inspect.getmoduleinfo('./test_inspect.py')
# print m
# print m.__class__

# #ismodule
# print 'inspect.ismodule(inspect) --> ',inspect.ismodule(inspect)
# #isclass
# print 'inspect.isclass(inspect) --> ',inspect.isclass(inspect)
# print 'inspect.isclass(inspect.ModuleInfo) --> ',inspect.isclass(inspect.ModuleInfo)
# #ismethod
# def func():
#     return 
# #定义在类中的函数叫做方法
# class test(object):
#     def my_method(self):
#         return
# print 'inspect.ismethod(test.my_method) --> ',inspect.ismethod(test.my_method)
# print 'inspect.ismethod(func) --> ',inspect.ismethod(func)
# print 'inspect.isfunction(func) --> ',inspect.isfunction(func)
# #isgeneratorfunction
# def generatorfunc():
#     for i in range(5):
#         yield i
# print 'inspect.isgeneratorfunction(generatorfunc) --> ',inspect.isgeneratorfunction(generatorfunc)
# print 'inspect.isgenerator(generatorfunc()) --> ',inspect.isgenerator(generatorfunc())

#istraceback
import sys
try:
    1/0
except:
    exc_info = sys.exc_info()
    print exc_info
    print 'inspect.istraceback(sys.exc_info[2]) -->', inspect.istraceback(exc_info[2])




