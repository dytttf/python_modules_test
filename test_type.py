# coding:utf8
'''
type 测试
'''

# 普通定义类
class Hello(object):
    def hello(self, name='world'):
        print("Hello, %s"%name)

print("###use calss method define")
h = Hello()
h.hello()
print("type of class Hello: %s"%type(Hello),)
print("type of hello's instance h: %s"%type(h),)

print("\n")
# 使用type定义类
def fn(self, name='world'):
    print("Hello, %s"%name)
Hello = type('Hello', (object, ), dict(hello=fn))

print("###use type define")
h = Hello()
h.hello()
print("type of class Hello: %s"%type(Hello),)
print("type of hello's instance h: %s"%type(h),)

# 以上完全相同




