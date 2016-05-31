# coding:utf8
'''
函数性质测试
'''

def show_args(a, b=None, *args, **kwargs):
    print a
    print b
    print args
    print kwargs
    return

if __name__ == "__main__":
    #show_args(1, 2)
    show_args(1, data=1, b=1)
    pass
