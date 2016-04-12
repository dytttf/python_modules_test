#coding:utf8
import time
import os
import urllib2
import threading
import multiprocessing
'''
import ghost
count = 0
gh = ghost.Ghost(wait_timeout=5, display=True)
def req(num):
    url = 'http://www.baidu.com'
    gh.open(url)
thread_list = []
for i in range(2):
    print "----------: ",i 
    t = threading.Thread(target=req, args=(i,))
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
print "---over---", count
'''


def test():
    print os.getpid()
    return


if __name__ == '__main__':
    p = multiprocessing.Process(target=test)
    p.start()
    p.join()
    #help(multiprocessing)
    print '111',os.getpid()
