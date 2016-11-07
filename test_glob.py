#coding:utf8
import os
import glob

current_path = os.path.abspath('.')

py_file_list = glob.glob(os.path.join(current_path, "*.py"))
print py_file_list
# 迭代器模式
py_file_list = glob.iglob(os.path.join(current_path, "*.py"))
print py_file_list


# 通配符测试
# * 匹配 0 或多个字符
# ？ 匹配单个字符
# [] 匹配指定范围内的字符
print glob.glob(os.path.join(current_path, "[0-9]*.py"))

with open(os.path.join(current_path, '.a.txt'), 'w') as f:
    pass
# ?和* 都不能匹配 .
print glob.glob(os.path.join(current_path, "?*.txt"))
print glob.glob(os.path.join(current_path, ".?*.txt"))

os.remove(os.path.join(current_path, '.a.txt'))
