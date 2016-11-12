#coding:utf8
import os

#
#这些代码在工作路径执行 结果不同
# ./代表工作目录 及脚本命令执行目录 而不是脚本所在目录
print os.path.realpath('./')
print os.path.realpath(__file__)
print os.path.abspath('./')
print os.path.abspath(__file__)

def modify_file(path):
    u'''修改指定目录下指定文件'''
    def modify(file_content):
        #file_content = file_content.replace("", "")
        return file_content
    
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            abs_file = os.path.join(root, filename)
            if not abs_file.endswith('.py'):
                continue
            with open(abs_file, 'r') as f:
                old_str = f.read()
            new_str = modify(old_str)
            with open(abs_file, 'w') as f:
                f.write(new_str)
    return


if __name__ == "__main__":
    path = r'E:\FPAN\新闻回复\新闻回复online'.decode('utf8')
    modify_file(path)
