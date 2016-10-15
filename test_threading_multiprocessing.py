# coding:utf-8
import os
import time
import signal
import threading
import multiprocessing
from multiprocessing import Process, Pipe, Queue, Event, dummy


data = []
def test_global_in_multiprocess():
    '''
    测试结果global声明全局变量后，多进程仍然不会修改，多线程可以修改，
    '''
    p_list = []
    for i in range(2):
        #p = threading.Thread(target=change_data, args=(i,))
        p = multiprocessing.Process(target=change_data, args=(i,))
        p.start()
        p_list.append(p)
    for p in p_list:
        print "aaa"
        p.join()
        print "ok"

def change_data(n):
    '''global data
    print "p-%s"%n
    data.append(n)
    print 'data',data'''
    for i in range(5):
        print i
        time.sleep(1)
    return

# -------测试管道和队列--------
def reader_pipe(pipe):
    output_p, input_p = pipe
    input_p.close()
    while 1:
        try:
            msg = output_p.recv()
        except EOFError:
            break

def writer_pipe(count, input_p):
    for i in xrange(0, count):
        input_p.send(i)

def reader_queue(queue):
    while 1:
        msg = queue.get()
        if msg == 'DONE':
            break

def writer_queue(count, queue):
    for ii in xrange(0, count):
        queue.put(ii)
    queue.put('DONE')

def test_queue_pipe():
    print 'testing for pipe:'
    for count in [10, 10**4, 10**5]:
        output_p, input_p = Pipe()
        #break
        reader_p = Process(target=reader_pipe, args=((output_p, input_p),))
        reader_p.start()
        output_p.close()
        _start = time.time()
        writer_pipe(count, input_p)
        input_p.close()
        reader_p.join()
        print 'Sending %s numbers to Pipe() took %s seconds' % (count, (time.time() - _start))
        break

    print "testing for queue:"
    for count in [10**3, 10**4, 10**5]:
        queue = Queue()
        reader_p =  Process(target=reader_queue, args=((queue),))
        reader_p.daemon = True
        reader_p.start()
        _start = time.time()
        writer_queue(count, queue)
        reader_p.join()
        print "Sending %s numbers to Queue() took %s seconds" % (count, (time.time() - _start))

def test_dummy():
    u'''测试dummy  event'''
    def work(args):
        name, event = args
        if name == 5:
            time.sleep(1)
            event.set()
            print('event set')
        else:
            while 1:
                if event.is_set():
                    print('event is set')
                    break
                else:
                    time.sleep(5)
        return
    event = Event()
    lis = [(x, event) for x in range(10)] 
    pool = dummy.Pool(10)
    pool.map(work, lis)
    return

def test_kill():
    def work():
        pid = os.getpid()
        print '111',pid
        with open('temp/mul.pid', 'w') as f:
            f.write(str(pid))
        time.sleep(100)
        return
    print os.getpid()
    p = multiprocessing.Process(target=work)
    p.start()
    p.join(timeout=10)
    with open('temp/mul.pid') as f:
        pid = f.read()
    os.kill(int(pid), signal.SIGTERM)
    del p
    print 'kill'
    time.sleep(20)
    return



if __name__ == "__main__":
    #test_global_in_multiprocess()
    #print data
    #test_queue_pipe()
    #test_dummy()
    test_kill()
