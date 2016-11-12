#coding:utf8
'''
参考 http://www.pythoner.com/56.html

测试
eval
exec
'''

# eval
# 执行 python 表达式
# eval(obj, globals=globals(), locals=locals())
# examples:

# 默认作用域
a = 2
print eval("a == 2")

# 自定义作用域
scope = {}
try:
    print eval("a == 2", scope)
except NameError as e:
    print e
# 查看执行完之后的作用域
# print scope

# 自定义全局和本地作用域
global_scope = {'a':2}
# 查找顺序 local --> global
local_scope = {'a':1}
try:
    print eval("a == 2", global_scope, local_scope)
except Exception as e:
    print e


# exec
# 执行语句
# exec obj in globals(), locals()
# examples:
exec 'print a' in {'a':1}, {'a':2}
exec('print 1', {'a':1})

exec(compile('print 1', '', 'exec'))


# compile
# 编译字符代码
# compile(str, file, type)
c = compile('1 + 1 == 2', '', 'eval')
print c
