#coding:utf8
'''
enum 模块简单测试
'''
import enum

Month = enum.Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


for name, member in Month.__members__.items():
    print(name, "=>", member, ':', member.value)

# 装饰器保证不会出现重复值
@enum.unique
class Weekday(enum.Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    
for name, member in Weekday.__members__.items():
    print(name, "=>", member, ':', member.value)
