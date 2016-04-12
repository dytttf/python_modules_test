#coding:utf8
import re

s = "the sum of 7 and 9 is [7+9]."

ss = "[name = 'Mr.Gumby']Hello,[name]"

file_pat = re.compile(r"\[(.+?)\]")
#定义一个作用域
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        st = str(eval(code,scope))
        print 1
        return st  #使用自定义的作用域
    except SyntaxError:
        print 2
        exec code in scope   #使用自定义的作用域
        return ""

print file_pat.sub(replacement,s)

#print file_pat.sub(repalcement,ss)

#replacement(match) 遍历match中所有的组，match为自动传入的参数（file_pat在s中的应用）

#eval()的一个特性：
#name = "hello"
#eval(name)  返回hello


