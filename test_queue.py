#coding:utf8
from Queue import Queue
#from multiprocessing import Queue
'''
#所有属性
['Empty', 'Full', 'LifoQueue', 'PriorityQueue', 'Queue', '__all__',
'__builtins__', '__doc__', '__file__', '__name__', '__package__',
'_threading', '_time', 'deque', 'heapq']
'''

#LifoQueue  堆，先进后出
#PriorityQueue  优先级队列，级别越低越先出来


#
#只接收队列长度一个参数
queue = Queue(maxsize=5)
'''
dir(queue)
['__doc__', '__init__', '__module__', '_get', '_init', '_put', '_qsize',
'all_tasks_done', 'empty', 'full', 'get', 'get_nowait', 'join', 'maxsize',
'mutex', 'not_empty', 'not_full', 'put', 'put_nowait', 'qsize',
'queue', 'task_done', 'unfinished_tasks']
'''

#查看最大队列长度
print queue.maxsize

#判断队列是否为空
print queue.empty()
#判断队列是否已满
print queue.full()

#向队列中添加任务,参数同get
queue.put(1, block=True, timeout=None)
#查看队列中任务数
print queue.qsize()

#测试Full异常
for i in range(10):
    print u"当前队列size",queue.qsize()
    try:
        queue.put(1, timeout=1)
    except Queue.Full as e:
        print u"队列已满"
        break
#
print u"测试put_nowait"
for i in range(2):
    try:
        queue.put_nowait(1)
    except Queue.Full as e:
        print u"队列已满"
        break

#获取任务,设置block为True,当队列为空时,若指定timeout,则等待至多·timeout· seconds,然后抛出Empty exception
#不指定timeout,则按照默认设置超时时间
#设置block为False,则不会等待，若队列为空,立刻抛出Empty exception
task = queue.get(block=True, timeout=None)
print task

#不等待,若队列为空直接抛出Empty exception
#和get的区别在于get函数默认是等待的
task = queue.get_nowait()
#task = queue.get()
print task


#查看未完成任务数,和当前队列中任务数无必要联系,
#此数目当队列中任务增加时加1，最大值为maxsize
#当调用task_done时减1
print queue.unfinished_tasks

for i in range(queue.qsize()):
    print u"队列中任务数",queue.qsize()
    #queue.get_nowait()
    #声明任务完成
    queue.task_done()
    print u"未完成任务数",queue.unfinished_tasks

#以下属性应该是内部调用的
#锁???
lock = queue.mutex

#条件
#是否为空
queue.all_tasks_done
#是否为空
queue.not_empty
#是否满
queue.not_full


#------------------------------test_Queue------------
#测试各种队列顺序
print '\n test_Queue \n'
#queue = Queue.Queue(5)
#queue = Queue.LifoQueue(5)
queue = Queue.PriorityQueue(5)
for i in 'fmasj':
    queue.put_nowait(i)

for i in range(queue.qsize()):
    print queue.get_nowait()


if __name__ == "__main__":
    pass




