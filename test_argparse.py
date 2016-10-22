# coding:utf8
'''
http://python.usyiyi.cn/python_278/library/argparse.html
'''
import argparse
import sys

# 父解析器
parent_parser = argparse.ArgumentParser(
    description=u"I'm Father Parser",
    add_help=False, # 不设为False 则会冲突默认的 -h选项
    )
parent_parser.add_argument("--parent")


parser = argparse.ArgumentParser(
    prog=u"Program Name (default: sys.argv[0])",
    # usage=u"%(prog)s usage [option]",
    description=u"""
            Test
            argparse
            module
            """, # -h 帮助命令下显示
    epilog=u"额外的描述 追加在帮助文档最下方",
    parents=[parent_parser], # 可继承父类 公用参数
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prefix_chars='-+', # 默认为 - , -+代表支持 +host这样的参数形式
    fromfile_prefix_chars="@", # 默认 None  被当作文件的参数
    argument_default=None, # 设置参数的默认值
    conflict_handler='resolve', # 出现重复选项时的处理方式 默认 error 抛出异常
                                # resolve 覆盖
    add_help=True, # 增加帮助选项 默认True  可使用 -h/--help
                   # 改为False后不能使用 -h/--help
    )

# formatter_class参数
# 默认情况下 ArgumentParser对象会对命令行帮助信息中的 \
#    description 和 epilog 文本进行去除换行
# 格式化类
#    HelpFormatter  默认
#    RawDescriptionHelpFormatter  保持 desctiption 和 epilog 原本格式
#    RawTextHelpFormatter    保留所有帮助文本的空白 包括参数描述
#    ArgumentDefaultsHelpFormatter
#         添加每个参数的默认值信息(PS: 为什么没有 help 的参数就不显示默认值呢)


# add_argument(name or flags...[, action][, nargs][, const]
#               [, default][, type][, choices][, required][, help]
#               [, metavar][, dest])

# 测试 name or flags 参数名  例如 foo, -f, --foo
# 不加前缀为位置参数 foo  必须指定
# 加前缀为可选参数 -f --foo
# parser.add_argument("foo")
parser.add_argument("-f")
# 一次可指定多个参数 不过 使用 -f2 传递的参数会被赋值给 -f1
parser.add_argument("-f1", "-f2")

# action  将参数按照指定动作处理
# 支持
# store 保存参数的值  默认动作
parser.add_argument("-store", action='store')

# store_const 转换为由 const 参数指定的值
parser.add_argument("--store_const", action="store_const", const='const')

# store_true 和 store_false 是 store_const 的特殊情形 分别用于转换为 True 和 False
parser.add_argument("--debug", action="store_true")
#等价于
parser.add_argument("--debug", action="store_const", const=True)

# append 将参数值保存到列表中
# 使用此方式时 注意 构造 parser 时的 argument_default参数默认值如果不是 None 或者 list
# 就会报错
parser.add_argument("--append", action="append")
# 用法 python filename.py  --append 1 --append 2
# 默认如果不使用 action="append"的时候 出现重复选项会用后面的覆盖前面的

# append_const 将 const 指定的值直接添加到列表中 使用此选项是不能指定选项值
parser.add_argument("--append_const", action="append_const", const='append_const')
# 用法 python filename.py  --append_const

# count 计数
parser.add_argument("-c", action="count")
# 用法 python filename.py  -c # c的值为 1
# 用法 python filename.py  -cccc # c的值为 4
parser.add_argument("-count", action="count")
# 用法 python filename.py  -countcount # 错误
# 用法 python filename.py  -count -count # count值为 2

# help 自定义帮助选项 
parser.add_argument("--hh", action="help")
# 用法 python filename.py  --hh # 相当与  -h 选项

# version 打印版本信息
parser.add_argument("--version", action="version", version="%(prog)s 2.0")
# action 动作支持自定义 只需要继承 argparse.Action并定义 __call__ 方法
# __call__ 接收 4 个参数 parser, namespace, values, option_string

class DateTimeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        import datetime
        print parser, namespace, values, option_string
        values = datetime.datetime.strptime(values, "%Y-%m-%d %H:%M:%S")
        setattr(namespace, self.dest, values)

parser.add_argument("--datetime", action=DateTimeAction)
# 用法 python filename.py --datetime "2016-10-22 17:50:00"


# nargs 参数 不指定此参数则 默认为 N=1
# N 一个整数  收集选项后 N 个参数到列表中
parser.add_argument("--nargsN", nargs=2)
# ? 参数存在则从命令行读取 不存在则默认读取 default 的值 当指定 const 参数并且在命令行
#   中使用了该选项但没有给值时将读取 const 的值
parser.add_argument("--nargs?", nargs='?', const='const', default='default')
# 用法 python filename.py --nargs? # 值为 const
# 用法 python filename.py # 值为 default
# * 跟随选项后面的所有参数都会被收集到选项的列表中
parser.add_argument("--nargs*", nargs='*')
# 用法 python filename.py --nargs* 1 2 3 4 # 值为 ['1', '2', '3', '4']
# + 同 * 不过限制参数至少有 1 个
parser.add_argument("--nargs+", nargs='+')
# 用法 python filename.py --nargs+ # 错误
# argparse.REMAINDER 将此选项后面的所有值 ( 包括选项 )都收集起来
parser.add_argument("--nargsREM", nargs=argparse.REMAINDER)
# 用法 python filename.py --nargsREM 1 -f 1 # 值为 ['1', '-f', '1']


# default 参数
# argparse.SUPPRESS 当参数值为这个的时候并且命令行中未出现此选项 则不创建此属性
parser.add_argument("--suppress", default=argparse.SUPPRESS)
# 用法 python filename.py # 不出现此属性

# type 指定命令行参数的值被转换后的类型
# argparse.FileType argparse提供的工厂类型 FileType
#                   支持 file 对象的mode=和bufsize=参数
parser.add_argument('--file', type=argparse.FileType('w'))
# 用法 python filename.py --file temp.txt # 生成了一个 temp.txt 文件

# choices 限制命令行参数的值 选取范围
parser.add_argument('--choices', choices=['choices_1', 'choices_2'])
# 用法 python filename.py --choices choices_3 # 错误

# require 将一个选项变为必须的
# parser.add_argument('--require', require=True)  # --require默认是可选参数

# help 此命令行参数的描述信息
parser.add_argument('--help', action="help", help="%(prog)s help info")
# 隐藏特定选项的帮助
parser.add_argument('--suppress_help', help=argparse.SUPPRESS)

# metavar ArgumentParser 生成帮助信息时会用到
parser.add_argument('--metavar', metavar="metavar_var")

# dest 指定改变调用的属性名称
parser.add_argument("--dest", dest="dest_dest")

# 子命令解析器 parser.add_subparsers([title][, description][, prog][, parser_class]
#                   [, action][, option_string][, dest][, help][, metavar])
# subparsers = parser.add_subparsers(title=u'子解析器')
# parser_sub_a = subparsers.add_parser('a', help=u"子解析器 a 帮助信息")
# parser_sub_a.add_argument("--test")
# 用法 python filename.py a -h
# 用法 python filename.py a --test test


# add_argument_group(title=None, description=None)
# 分组只在分开显示帮助信息的时候有用
groups = parser.add_argument_group('group')
groups.add_argument("--group")

# add_mutually_exclusive_group(required=False)
# 互斥分组 此分组内的参数只能出现一个 required 参数要求必须指定至少一个参数
mut_groups = parser.add_mutually_exclusive_group()
mut_groups.add_argument("--big")
mut_groups.add_argument("--small")


# set_defaults(**kwargs) 指定默认命令值 覆盖同名参数从命令行中得到值
parser.set_defaults(default_1='1')


# parse_args(args=None, namespace=None)
cmd_args = parser.parse_args() # 默认解析 sys.argv[1:]
# cmd_args = parser.parse_args("-f1 1".split())
# cmd_args = parser.parse_args("-f1=1".split())
# 短选项
# cmd_args = parser.parse_args("-xX".split()) # NameSpace(x="X")
# parser.add_argument('-x', action="store_true")
# parser.add_argument('-y', action="store_true")
# parser.add_argument('-z')
# cmd_args = parser.parse_args("-xyzZ".split()) # NameSpace(x=True, y=True, z="Z")
# 伪参数 -- 用来对付出现的负数值
# parser.add_argument('negative')
# cmd_args = parser.parse_args("-- -1".split()) # NameSpace(negative='-1')

# 允许简写 不出现歧义的情况下
# python filename.py -m 1 # NameSpace(metavar='1')
# 部分解析 忽略未知的选项 但如果存在一个选项是已知选项的前缀(-f:-foo) 则此选项会被解析
# cmd_args = parser.parse_known_args()

# 返回用法字符串
usage_str = parser.format_usage()
# 打印用法
parser.print_usage()
# 返回帮助信息字符串
help_str = parser.format_help()
# 打印帮助信息
parser.print_help()

print cmd_args
print "\n"
print cmd_args.dest_dest
# print cmd_args.dest  # 不再存在
print cmd_args.default_1

# 正常退出 并打印 message
parser.exit(status=0, message="bye")
# 已状态码 2 退出 并打印用法信息到标准错误输出
# parser.error("bye")

if __name__ == "__main__":
    pass
