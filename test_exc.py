#coding:utf8
'''
异常类测试
'''
import sys
import time
import traceback

class myexc(Exception):
    
    def __init__(self, l, n):
        super(Exception, self).__init__()
        self.l = l
        self.n = n

    def __str__(self):
        return 'my error %s, %s'%(self.l,self.n)

# 自定义异常类
try:
    1/2
    raise myexc(1,2)
except myexc as e:
    print e
    print traceback.format_exc()
    

# 异常捕获的一些用法
try:
    # 1/0
    int("")
# except (ZeroDivisionError,ValueError) as e:
except Exception as e:
# except ZeroDivisionError as e:
    print e
else:
    print u"no error"
finally:
    print u"finished"


try:
    1/0
    # int('')
except ZeroDivisionError as e:
    print '{0!r}'.format(e)
    # int("")
except Exception as e:
    print '{0!r}'.format(e)


# 测试 KeyboardInterrupt
def test_keybord():
    while 1:
        time.sleep(1)
    return

try:
    print "Ctrl+c"
    test_keybord()
except KeyboardInterrupt as e:
# 不能使用 Exception,
# KeyboardInterrupt 继承 BaseException
#except Exception as e:
    print e


try:
    sys.exit(0)
except BaseException as e:
    print e
# 自己抛出异常
# raise Exception, 'hello'


# ----- exceptions ------
import exceptions


# 一般基类继承顺序
# Method resolution order:
#  |      StandardError
#  |      Exception
#  |      BaseException
#  |      __builtin__.object

# 捕获异常时可以捕获到其所有的子类

# 一般异常都存在 args, message 属性
# args 为实例化类时提供的参数 貌似只有前两个

# ArithmeticError
# 各种算术错误引发的异常
# 以下类的基类 OverflowError, ZeroDivisionError, FloatingPointError

# AssertionError
# 使用 assert 语句引发的异常

# AttributeError
# 属性引用时 不存在或不可访问 引发的异常 或者 赋值失败 引发的异常

# BaseException
# 所有异常类的基类

# BufferError
# 缓存异常

# BytesWarning
# 不懂

# DeprecationWarning
# 关于被弃用的特征的警告 (已经被弃用)

# EOFError
# 当没有读取到任何字符却直接读取到 EOF(文件结束标识符) 的时候抛出异常

# EnvironmentError
# IOError 和 OSError 的基类 可支持 errno, filename, strerror 等属性
# exceptions.EnvironmentError(1, 'strerror', 'filename.txt')
# args: (1, 'strerror')

# Exception
# 常规错误的基类
# 所有内建 非系统退出的异常 都从此类派生

# FloatingPointError
# 浮点计算错误

# FutureWarning
# 关于构造将来语义会有改变的警告

# GeneratorExit
# 迭代器退出时触发的异常
# 后来被定义为非错误 因此在2.6版本时其基类由 StandardError 改为 BaseException 

# IOError
# 输入/输出操作失败 引发异常
# 例如 “file not found” or “disk full”

# ImportError
# 导入模块/对象失败
# 当 import 导入时寻找模块失败 或者 from ... import name 是寻找 name 失败

# ImportWarning
# 导入模块时对可能发生的错误显示的警告信息

# IndentationError
# 缩进错误
# 不要混用 tab 和 space ...

# IndexError
# 继承自 LookupError
# 索引超出范围时触发,当分片时不会引发异常, 如果使用非整型索引将会抛出 TypeError

# KeyError
# 继承自 LookupError
# 当在字典中找不到指定 key 时触发

# KeyboardInterrupt
# 程序被主动停止 一般是 Ctrl+C, 继承于 BaseException

# LookupError
# 无效数据查询的基类 派生出 IndexError, KeyError

# MemoryError
# 内存溢出错误(对于Python 解释器不是致命的)

# NameError
# 找不到变量

# NotImplementedError
# 继承自 RuntimeError
# 尚未实现的方法 当使用的类中的某个方法需要被重新实现时可定义此异常

# OSError
# 继承自 EnvironmentError
# 操作系统错误 当函数遇到系统错相关错误时引发
# 此异常会存在errno 属性 具体值以及原因可在 errno 模块中查看

# OverflowError
# 继承自 ArithmeticError
# 数值运算超出最大限制

# PendingDeprecationWarning
# 关于特性将会被废弃的警告 (将被弃用)

# ReferenceError
# 没理解
# 弱引用(Weak reference)试图访问已经垃圾回收了的对象

# RuntimeError
# 其基类有 NotImplementedError, 
# 当不知道这个异常属于哪个异常的时候，就叫这个了

# RuntimeWarning
# 可疑的运行时行为(runtime behavior)的警告

# StandardError
# 所有的内建标准异常的基类
# 除 StopIteration, GeneratorExit, KeyboardInterrupt, SystemExit 之外的异常都继承 
# StandardError, 其本身继承 Exception

# StopIteration
# 继承自 Exception
# 当迭代器的 next() 方法发现迭代完成时引发此异常, 由于此异常正常情况下不算错误, 所以其基
# 类由 StandardError 改为 Exception

# SyntaxError
# 标准错误之一
# 语法错误抛出异常
# 特殊属性 filename, lineno, msg, offset, print_file_and_line, text
# text 出错行的文本内容

# SyntaxWarning
# 可疑的语法的警告

# SystemError
# 一般的解释器系统错误

# SystemExit
# 继承自 BaseException
# sys.exit(0) 退出时会引发此异常 特殊属性为 code 退出码

# TabError
# 继承自 IndentationError
# Tab 和空格混用

# TypeError
# 当操作或函数应用与不合适类型的对象时引发 

# UnboundLocalError
# 继承自 NameError
# 访问未初始化的本地变量

# UnicodeDecodeError
# 继承自 UnicodeError-->ValueError
# Unicode 解码时的错误
# 特殊属性
# encoding (使用何种编码解码时出错)
# end (解码发生错误的结束位置)
# start (解码发生错误的开始位置)
# object (解码对象)
# reason (错误原因)

# UnicodeEncodeError
# 同 UnicodeDecodeError 不同之处在于编码时报错

# UnicodeError
# Unicode 相关的错误

# UnicodeTranslateError
# Unicode 转换时错误

# UnicodeWarning
# 继承自 Warning--Exception
# Unicode 相关的警告基类

# UserWarning
# 用户代码生成的警告

# ValueError
# 当内建操作或函数，接收到类型正确，但值不正确的参数，
# 而且这种情况不能用诸如 IndexError 这样的更精确的异常进行描述时引发。

# Warning
# 警告的基类

# WindowsError
# 当 Windows 特定的错误发生时，或者当错误号码与 errno 值不对应时引发。
# Winerror 和 strerror 的值创建自 Windows 平台 API 中的 GetLastError() 函数
# 和 FormatMessage() 函数的返回值。Errno 值将 winerror 值映射到相应的 errno.h 值。
# 这是 OSError 的一个子类。

# ZeroDivisionError
# 除数为 0 错误
