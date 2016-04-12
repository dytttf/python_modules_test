#coding:utf8
'''
发布订阅模式
'''
import message

#Example
def hello(name):
    print "hello, %s."%name
def hi(name):
    print "hi, %s."%name

def stop(name):
    print 'hello, %s. greet5'%name
    print 'discontinued.'
    ctx = message.Context()
    ctx.discontinued = True
    return ctx

#订阅一个话题,并发布
message.sub('greet', hello)
message.sub('greet', hi)
message.pub('greet', 'lai')
message.pub('greet1', 'lai1')


#订阅另一个话题，并发布
message.sub('greet1', hello)
message.pub('greet1', 'lai1')


#取消订阅
message.unsub('greet', hello)
message.pub('greet', 'unsub')

#声明一个话题
message.declare('greet2', 'lai2')
#第一次订阅不用发布就可以收到预定义的消息
message.sub('greet2', hello)

#测试调整队列顺序
message.sub('greet', hello)
#stop执行后别的函数不再执行
message.sub('greet', stop, front=True)

message.pub('greet', 'stop')




