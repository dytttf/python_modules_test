# coding:utf8
'''
python模块 tempfile 简单用法测试
'''
import os
import tempfile

#
# Sample method to create a file
with open('tempfile_test_1.txt', 'wb') as f:
    print 'temp', f
    print 'temp.name', f.name
if os.path.exists('./tempfile_test_1.txt'):
    os.remove('./tempfile_test_1.txt')
#
# tempfile create a temp file
temp = tempfile.TemporaryFile()
# In python 2.7.11 this method is same as NamedTemporaryFile
# and same as tempfile.mkstemp()

# Create a file in system tmp dir
# The file is created as mkstemp() would do it.
try:
    print 'temp', temp
    print 'temp.name', temp.name
finally:
    # when file closed, it will be deleted
    temp.close()

#
# Create a temp dir
directory_name = tempfile.mkdtemp()
print 'directory_name',directory_name
print 'isdir',os.path.isdir(directory_name)
os.removedirs(directory_name)

#
# Create a Named temp file
temp = tempfile.NamedTemporaryFile(suffix='_suffix_',
                                  prefix='_orefix_',
                                  dir='./')
try:
    print 'temp', temp
    print 'temp.name', temp.name
finally:
    temp.close()
    
# Return system's temp dir path
print tempfile.gettempdir()
# Idem, but you can special a path
print tempfile.tempdir
# Return a temp dir path, but not created
print tempfile.mktemp()



if __name__ == "__main__":
    pass
