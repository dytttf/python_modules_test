#coding:utf8
import code

a = 1
b = "hello"

# 新建一个终端 加载定义好的变量
# 参数
# banner 进入终端时打印出的提示信息
# readfunc 终端接收命令的函数 默认为 raw_input
# local 终端作用域

code.interact(banner="code.interact session", readfunc=None, local=locals())

# class InteractiveInterpreter
# 控制代码交互执行

# class InteractiveConsole
# 控制台输出样式定义
