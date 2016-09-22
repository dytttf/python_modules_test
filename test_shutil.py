#coding:utf-8
import os
import glob
import shutil

print shutil.abspath(__file__)
print __file__

curpath = os.path.dirname(__file__)

test_dir = os.path.join(curpath, 'test')
test_dir_1 = os.path.join(curpath, 'test_1')
test_file = os.path.join(test_dir, 'test.txt')

# 初始化测试目录和文件
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

if not os.path.exists(test_file):
    with open(test_file, 'w') as f:
        f.write('test')

#copyfile
shutil.copyfile(test_file, os.path.join(test_dir, 'test1.txt'))
#copy
shutil.copy(test_file, os.path.join(test_dir, 'test2.txt'))
#copy2  复制软连接等属性
shutil.copy2(test_file, os.path.join(test_dir, 'test3.txt'))


#copyfileobj
f = open(os.path.join(test_dir, 'test.txt'), 'r')
ff = open(os.path.join(test_dir, 'test4.txt'), 'w')
shutil.copyfileobj(f, ff)
print f
print ff
f.close()
ff.close()


#copytree  目录
if os.path.exists(test_dir_1):
    shutil.rmtree(test_dir_1)

shutil.copytree(test_dir, test_dir_1)


# 压缩功能
# root_dir  从此目录开始寻找
# base_dir  需要压缩的文件
shutil.make_archive('test', 'zip', root_dir='../',
    base_dir='python_modules_test/test')


#同步当前文件夹内所有test_开头的文件到指定目录
def sync_github():
    dest_dir = r'D:\Documents\GitHub\python_modules_test'
    filenames = glob.glob('test_*.py')
    for filename in filenames:
        abs_file = os.path.abspath(filename)
        shutil.copyfile(abs_file, os.path.join(dest_dir, filename))
    return

if __name__ == "__main__":
    # sync_github()
    pass








