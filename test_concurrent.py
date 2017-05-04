#coding:utf8
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait
from concurrent.futures import as_completed

def work(seconds):
    time.sleep(seconds)
    return seconds

def call_back(future):
    print("I am callback")
    return future

times = range(1, 10)

# 建立线程池
pool = ThreadPoolExecutor(max_workers=5)
#建立进程池
#pool = ProcessPoolExecutor(max_workers=10)

#使用 submit函数生成一个线程 返回值是一个 Future 对象
future_tasks = [pool.submit(work, i) for i in times]
for task in future_tasks:
    task.add_done_callback(call_back)
    print(task.cancel())
    print(task)
print(task.set_running_or_notify_cancel())

# Future对象方法集合
# add_done_callback(fn)  线程完成后立刻执行的函数
# cancel() 尝试取消  # 尚未执行的任务可以取消 当任务数大于线程数时
# canceled() 返回取消状态
# done() 返回完成状态
# exception(timeout=None) 返回执行中遇到的异常
# result(timeout=None) 返回函数返回值
# running() 返回运行状态
# set_exception(exception) 测试使用 将任务返回结果设置为指定异常 
# set_result(result) 测试使用 将任务返回结果设置为指定值
# set_running_or_notify_cancel() 如果任务被取消了 返回False 如果任务是 running 返回True

if 0:
    # wait(fs, timeout=None, return_when='ALL_COMPLETED')
    # 返回 (完成任务列表, 未完成任务列表)
    # 阻塞等待任务完成 三种阻塞模式
    # FIRST_COMPLETED  完成一个则返回
    # FIRST_EXCEPTION
    # ALL_COMPLETED
    result = wait(future_tasks, return_when='FIRST_COMPLETED')
    #result = wait(future_tasks)
    while future_tasks:
        done_task = list(result.done)
        print(done_task)
        future_tasks = [x for x in future_tasks if x not in done_task]
        result = wait(future_tasks, return_when='FIRST_COMPLETED')


if 0:
    # as_completed(fs, timeout=None)
    # 返回迭代器
    # 每次迭代返回一个完成的任务
    for task in as_completed(future_tasks):
        print(task)

if 0:
    results = pool.map(work, times)
    for result in results:
        print(result)
