# coding:utf-8
'''
python FTP 服务搭建测试
模块  pyftpdlib
'''
import os
import pyftpdlib
import socket

# 最简单的方法, 命令行下执行
# python -m pyftpdlib -p 21

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

if not os.path.exists('./temp_ftp'):
    os.mkdir('./temp_ftp')
if not os.path.exists('./temp_ftp/readme.txt'):
    with open('./temp_ftp/readme.txt', 'w') as f:
        f.write('this is a ftpdlib test dir and file\n')

authorizer = DummyAuthorizer()
# 密码用户
authorizer.add_user("username", '12345', './', perm="elradfmw")
# 匿名用户
authorizer.add_anonymous("./temp_ftp")

handler = FTPHandler
handler.authorizer = authorizer
# the string sent when client connects
handler.banner = u'Welcome!!!'

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 可重用地址端口
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#0.0.0.0虚机才可以访问
soc.bind(('0.0.0.0', 21))

# 
server = FTPServer(soc, handler)
server.serve_forever()

