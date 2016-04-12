#coding:utf8
import os

#
#这些代码在工作路径执行 结果不同
# ./代表工作目录 及脚本命令执行目录 而不是脚本所在目录
print os.path.realpath('./')
print os.path.realpath(__file__)
print os.path.abspath('./')
print os.path.abspath(__file__)
