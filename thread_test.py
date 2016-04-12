#coding:utf8
import threading
import Queue
'''
import time
import thread

def timer(no,interval):
    i = 0
    while i<10:
        print "Thread:%d Time:%s\n"%(no,time.ctime())
        time.sleep(interval)
        i+=1
    thread.exit_thread()
def test():
    thread.start_new_thread(timer,(1,1))
    thread.start_new_thread(timer,(2,2))

if __name__=="__main__":
    test()


import threading
import time

class timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print 'Thread Object(%d), Time:%s\n'%(self.thread_num,time.ctime())
            time.sleep(self.interval)
    def stop(self):
        self.thread_stop = True

def test():
    thread1 = timer(1,1)
    thread2 = timer(2,2)
    thread1.start()
    thread2.start()
    time.sleep(10)
    thread1.stop()
    thread2.stop()

if __name__=="__main__":
    test()


import thread
import time

mylock = thread.allocate_lock()
num = 0

def add_num(name):
    global num
    while True:
        mylock.acquire()
        print "Thread %s locked! num=%s"%(name,str(num))
        if num >=5:
            print "Thread %s released! num=%s"%(name,str(num))
            mylock.release()
            thread.exit_thread()
        num+=1
        print 'Thread %s released! num=%s'%(name,str(num))
        mylock.release()
def test():
    thread.start_new_thread(add_num,('A',))
    thread.start_new_thread(add_num,('B',))
if __name__=="__main__":
    test()



import threading

mylock = threading.RLock()
num = 0

class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.t_name = name
        self.stop_thread = False

    def run(self):
        global num
        while not self.stop_thread:
            mylock.acquire()
            print "\nThread(%s) loacked,Number:%d"%(self.t_name,num)
            if num>=4:
                mylock.release()
                print "\nThread(%s) released,Number:%d"%(self.t_name,num)
                break
            num+=1
            print "\nThread(%s) released,Number: %d"%(self.t_name,num)
            mylock.release()
    def stop(self):
        self.stop_thread = True

def test():
    thread1 = myThread('B')
    thread2 = myThread('A')
    thread1.start()
    thread2.start()
    thread1.stop()
    thread2.stop()
if __name__=="__main__":
    test()
'''
