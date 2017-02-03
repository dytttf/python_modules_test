#coding:utf8
'''
测试 getattr  和 getattribute 的区别
仅在新式类中生效 旧式类无 getattribute
'''
class Ts(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def method(self):
        pass

    def __getattr__(self, item):
        '''只有当 __getattribute__ 抛出 AttributeError 时被调用'''
        self.__dict__[item] = "a"
        return self.__getattribute__(item)

    def __getattribute__(self, item):
        '''
        对任何属性的调用都会从这里过 不论属性是否存在
        '''
        # 抛出 AttributeError 后调用 __getattr__
        #raise AttributeError
        # 抛出其他异常代码终止
        return object.__getattribute__(self, item)


if __name__ == '__main__':
    t = Ts(100, 20)
    m = t.y + t.x
    print m
    print t.y
    print t.name

    t.name = 'JJJ'
    print t.name
