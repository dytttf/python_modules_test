#coding:utf8
import re

s = "the sum of 7 and 9 is [7+9]."


# 基本用法 将目标替换为固定字符串
print re.sub('\[7\+9\]', '16', s)
# output> the sum of 7 and 9 is 16.


# 高级用法 1 使用前面匹配的到的内容 \1 代表 pattern 中捕获到的第一个分组的内容
print re.sub('\[(7)\+(9)\]', r'\2\1', s)
# output> the sum of 7 and 9 is 97.


# 高级用法 2 使用函数型 repl 参数, 处理匹配到的 SRE_Match 对象
def replacement(m):
    p_str = m.group()
    if p_str == '7':
        return '77'
    if p_str == '9':
        return '99'
    return ''
print re.sub('\d', replacement, s)
# output> the sum of 77 and 99 is [77+99].


# 高级用法 3 使用函数型 repl 参数, 处理匹配到的 SRE_Match 对象 增加作用域 自动计算
scope = {}
example_string_1 = "the sum of 7 and 9 is [7+9]."
example_string_2 = "[name = 'Mr.Gumby']Hello,[name]"

def replacement(m):
    code = m.group(1)
    st = ''
    try:
        st = str(eval(code, scope))
    except SyntaxError:
        exec code in scope
    return st

# 解析: code='7+9'
#       str(eval(code, scope))='16'
print re.sub('\[(.+?)\]', replacement, example_string_1)
# output> the sum of 7 and 9 is 16.


# 两次替换
# 解析1: code="name = 'Mr.Gumby'"
#       eval(code)
#	raise SyntaxError
#       exec code in scope
#       在命名空间 scope 中将 "Mr.Gumby" 赋给了变量 name

# 解析2: code="name"
#        eval(name) 返回变量 name 的值 Mr.Gumby
print re.sub('\[(.+?)\]', replacement, example_string_2)
# output> Hello,Mr.Gumby
