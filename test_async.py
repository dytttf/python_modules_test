#coding:utf8
import asyncio
'''
async with ...
async for ...
'''

# 定义协程函数
async def hello():
    print("hello world")
    await asyncio.sleep(1.0)
    print("hello world end")

# 建立一个协程任务队列
tasks = [hello() for i in range(10)]

async def test_as_completed(tasks):
    for task in asyncio.as_completed(tasks):
        print("先执行一次")
        result = await task
        print("完成")

# 获取一个协程事件循环
event_loop = asyncio.get_event_loop()
# 开始执行协程事件
# 执行一个
#event_loop.run_until_complete(hello())
# 执行一堆
#event_loop.run_until_complete(asyncio.gather(*tasks))
#event_loop.run_until_complete(asyncio.wait(tasks))

# 测试 as_completed
event_loop.run_until_complete(test_as_completed(tasks))
