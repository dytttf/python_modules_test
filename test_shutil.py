#coding:utf-8
import os
import glob
import shutil

print shutil.abspath(__file__)
print __file__

curpath = os.path.dirname(__file__)

test_dir = os.path.join(curpath, 'test')

#copyfile
shutil.copyfile(os.path.join(test_dir, 'test.txt'), os.path.join(test_dir, 'test1.txt'))
#copy
shutil.copy(os.path.join(test_dir, 'test.txt'), os.path.join(test_dir, 'test2.txt'))
#copy2  复制软连接等属性
shutil.copy2(os.path.join(test_dir, 'test.txt'), os.path.join(test_dir, 'test3.txt'))


#copyfileobj
f = open(os.path.join(test_dir, 'test.txt'), 'r')
ff = open(os.path.join(test_dir, 'test4.txt'), 'w')
shutil.copyfileobj(f, ff)
print f
print ff
f.close()
ff.close()


#copytree  目录
if os.path.exists(os.path.join(curpath, 'tes1t')):
    shutil.rmtree(os.path.join(curpath, 'tes1t'))
shutil.copytree(test_dir, os.path.join(curpath, 'tes1t'))


#同步当前文件夹内所有test_开头的文件到指定目录
def sync_github():
    dest_dir = r'D:\Documents\GitHub\python_modules_test'
    filenames = glob.glob('test_*.py')
    for filename in filenames:
        abs_file = os.path.abspath(filename)
        shutil.copyfile(abs_file, os.path.join(dest_dir, filename))
    return

if __name__ == "__main__":
    sync_github()
    pass








