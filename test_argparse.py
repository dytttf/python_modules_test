#coding:utf8
'''
http://python.usyiyi.cn/python_278/library/argparse.html
'''
import argparse
import sys
parser = argparse.ArgumentParser()
def main():
    parser.add_argument('--frist', action="store",default="")
    parser.add_argument('--restart', default=None, help="restart qq process")
    #不加-为必选参数
    #parser.add_argument('num', default=None, help="restart qq process")
    #action="store_true" >> cmd_args.port = True
    #parser.add_argument("--port", action="store_true", type=int)
    parser.add_argument("--port", type=int)
    parser.add_argument("-p", type=int)
    #metavar帮助信息描述
    parser.add_argument("--meta", metavar="test_metavar")
    #dest 将dest参数传递给aaa,然后dest被销毁  相当于别名之类的
    parser.add_argument("--dest", dest="aaa")
    
    print sys.argv
    cmd_args = parser.parse_args(sys.argv[1:])
    #cmd_args = parser.parse_args()
    parser.print_usage()
    print cmd_args.port
    print cmd_args.p
    print cmd_args.meta
    print cmd_args.aaa
    print cmd_args
    return

if __name__ == "__main__":
    main()
