#coding:utf8
import inspect

######---1----#######
#type checking


# #getmembers(object, predicate=None)
if 0:
    print inspect.getmembers(inspect)[0]
    # print inspect.getmembers(inspect)

def isstr(obj):
    if isinstance(obj, str):
        return True
    return False
if 0:
    print inspect.getmembers(inspect, isstr)[0]



# #getmoduleinfo(path)
if 0:
    m = inspect.getmoduleinfo('./test_inspect.py')
    print m
    print m.__class__

# #ismodule
if 0:
    print 'inspect.ismodule(inspect) --> ',inspect.ismodule(inspect)

# #isclass
if 0:
    print 'inspect.isclass(inspect) --> ',inspect.isclass(inspect)
    print 'inspect.isclass(inspect.ModuleInfo) --> ',inspect.isclass(inspect.ModuleInfo)

# #ismethod
def func():
    '''i am a function'''
    return

# #定义在类中的函数叫做方法
class test(object):
    def my_method(self):
        return

if 0:
    print 'inspect.ismethod(test.my_method) --> ',inspect.ismethod(test.my_method)
    print 'inspect.ismethod(func) --> ',inspect.ismethod(func)
    print 'inspect.isfunction(func) --> ',inspect.isfunction(func)

# #isgeneratorfunction
def generatorfunc():
    for i in range(5):
        yield i
if 0:
    print 'inspect.isgeneratorfunction(generatorfunc) --> ',inspect.isgeneratorfunction(generatorfunc)
    print 'inspect.isgenerator(generatorfunc()) --> ',inspect.isgenerator(generatorfunc())

#istraceback
if 0:
    import sys
    try:
        1/0
    except:
        exc_info = sys.exc_info()
        print exc_info
        print 'inspect.istraceback(sys.exc_info[2]) -->', inspect.istraceback(exc_info[2])

# isframe
if 0:
    pass

# getsource
if 0:
    print inspect.getsource(func)

# getsourcefile
if 0:
    print inspect.getsourcefile(func)

# getdoc
if 0:
    print inspect.getdoc(func)

# getcomments
if 0:
    print inspect.getcomments(func)

# getmodule
if 0:
    print inspect.getmodule(func)

# getmoduleinfo
if 0:
    print inspect.getmoduleinfo("./test_inspect.py")

# getclasstree
if 0:
    print inspect.getclasstree([test])
