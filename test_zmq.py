#coding:utf8
"""
ZMQ python api 饿时
"""
import zmq


# 建立上下文
context = zmq.Context()

# 1.Request-Reply模式：
if 0:
    server_socket_type = zmq.REP
    client_socket_type = zmq.REQ

# 2.Publish-Subscribe模式:
if 0:
    server_socket_type = zmq.PUB
    client_socket_type = zmq.SUB

# 3.Parallel Pipeline模式：
if 0:
    server_socket_type = zmq.PULL
    work_socket_type_recv = zmq.PULL
    work_socket_type_send = zmq.PUSH
    client_socket_type = zmq.PUSH

# socket_type: REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH
# 
socket = context.socket(zmq.REP)
# 服务端绑定一个监听地址
socket.bind("tcp://127.0.0.1:5555")
# 客户端绑定一个监听地址
# socket.connect("tcp://127.0.0.1:5555")
# 设置客户端过滤条件
# socket.setsockopt(zmq.SUBSCRIBE,'')

#接收数据
# recv(flags=0, copy=True, track=False)
# recv_json(flags=0, **kwargs)
# recv_multipart(flags=0, copy=True, track=False) #receive a multipart message as a list of bytes or Frame objects
# recv_pyobj(flags=0)
# recv_string(flags=0, encoding='utf-8')  #receive a unicode string, as sent by send_string


# 发送数据
# send(data, flags=0, copy=True, track=False)
# send_json(obj, flags=0, **kwargs)
# send_multipart(msg_parts, flags=0, copy=True, track=False)
# send_pyobj(obj, flags=0, protocol=3)
# send_string(u, flags=0, copy=True, encoding='utf-8')

if not socket.closed:
    socket.close()
if not context.closed:
    context.destroy()
