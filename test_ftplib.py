#coding:utf-8
'''
ftp 客户端测试
模块  ftplib
'''
from ftplib import FTP



'''
# 简单测试代码
ftp = FTP(host='172.16.5.38', user='user', passwd='12345')
ftp.login(user='username', passwd='12345')
ftp.retrlines('LIST')
ftp.quit()
'''

# 初始化FTP对象
ftp = FTP()

# 设置调试级别 0, 1, 2
# 2 最详细
ftp.set_debuglevel(2)

#建立链接
ftp.connect(host='172.16.5.38', port=21)

ftp.login(user='username', passwd='12345')
#匿名用户
#ftp.login()

# 对应pyftpdlib的banner
print ftp.getwelcome()

#切换目录
#ftp.cwd('bats/')

#查看当前目录下文件
ftp.dir()

#ftp.putcmd('LIST')

#下载
'''
bufsize = 1024
filename = r'C:\Users\Administrator\Desktop\aaa.bat'
file_handler = open(filename, 'wb')
ftp.retrbinary('RETR rou.bat', file_handler.write, bufsize)
'''
#上传
'''
bufsize = 1024
filename = ur'E:\FPAN\test.doc'
file_handler = open(filename, 'rb')
ftp.storbinary('STOR %s'%filename.encode('utf8').split('\\')[-1], file_handler, bufsize)
'''
#删除
'''
ftp.delete("test.doc")
'''

ftp.set_debuglevel(0)
#file_handler.close()
ftp.quit()
print 'ftp down ok'
