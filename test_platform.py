# coding:utf8
import sys
import platform

# windows 版本信息
# example ('7', '6.1.7601', 'SP1', u'Multiprocessor Free')
print platform.win32_ver()
# linux OS (操作系统类别, 版本, 名称)  
print platform.linux_distribution()
# mac_ver(release='', versioninfo=('', '', ''), machine='')
print platform.mac_ver()



# architecture(executable=r'C:\Python27\pythonw.exe', bits='', linkage='')
# return (bits,linkage)
# 系统位数 文件格式
print platform.architecture()
# return (操作系统类别, 版本, 名称)
# example ('Ubuntu', '14.10', 'utopic')
# windows 下怎么啥都没呢
print platform.dist()


# 操作系统发布版本号
# windows-7  -->  7
# Linux-3.16.0-23-generic  --> 3.16.0-23-generic
print platform.release()
# 操作系统版本
print platform.version()
# 操作系统名字
print platform.system()
# Returns a tuple of strings (system,node,release,version,machine,processor)
# ('Windows', 'zhangsan', '7', '6.1.7601', 'AMD64', 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel')
print platform.uname()
#
#print platform.system_alias(1,1,1)
# c运行库类别  版本
# example ('glibc', '2.4')
print platform.libc_ver()

# Returns the machine type, e.g. 'i386'
print platform.machine()

# 计算机名 computer's network name 
print platform.node()

# platform(aliased=0, terse=0)  系统版本 等信息
print platform.platform()
print platform.platform(1)
print platform.platform(1, 1)

# popen  类是os.popen
# print platform.popen("dir").read()

# processor()
# example Intel64 Family 6 Model 42 Stepping 7, GenuineIntel
print platform.processor()




# java 版本的python Jpython 的版本接口
print platform.java_ver()
#
print platform.python_branch()
# (python版本, 构建日期)
print platform.python_build()
# 编译器版本
print platform.python_compiler()
# python 类别 CPython, Jython, IronPython, PyPy
print platform.python_implementation()
#
print platform.python_revision()
# python 版本号
print platform.python_version()
print platform.python_version_tuple()
print sys.version
