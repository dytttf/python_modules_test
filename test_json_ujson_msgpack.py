#coding:utf8
import timeit

setup='''
import ujson
import json
import msgpack
import datetime
data_dict = {
   "letter": "abcdefg",
   "number": 123456,
   "bool": True
   }
usjon_data = ujson.dumps(data_dict)
json_data = json.dumps(data_dict)
msg_data = msgpack.packb(data_dict)

data_dict.update({"date":datetime.datetime.now()})

def decode_datetime(obj):
    if b'__datetime__' in obj:
        obj = datetime.datetime.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S.%f")
    return obj

def encode_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
    return obj
   
json_data_dt = json.dumps(json_data, default=encode_datetime)
msg_data_dt = msgpack.packb(msg_data, default=encode_datetime)

'''

# 测试基本数据类型序列化
if 0:
   number = 10 ** 6
   ujson_t = timeit.Timer("ujson.dumps(data_dict)", setup=setup).timeit(number=number)
   json_t = timeit.Timer("json.dumps(data_dict)", setup=setup).timeit(number=number)
   msgpack_t = timeit.Timer("msgpack.packb(data_dict)", setup=setup).timeit(number=number)

   s = """
   ujson: %s\n
   json: %s\n
   msgpack: %s\n
   """ % (
      ujson_t,
      json_t,
      msgpack_t,
      )

   print s


# 测试基本数据类型反序列化
if 0:
   number = 10 ** 6
   ujson_t = timeit.Timer("ujson.loads(usjon_data)", setup=setup).timeit(number=number)
   json_t = timeit.Timer("json.loads(json_data)", setup=setup).timeit(number=number)
   msgpack_t = timeit.Timer("msgpack.unpackb(msg_data)", setup=setup).timeit(number=number)

   s = """
   ujson: %s\n
   json: %s\n
   msgpack: %s\n
   """ % (
      ujson_t,
      json_t,
      msgpack_t,
      )

   print s

# 测试时间 + 基本数据类型序列化
if 0:
   number = 10 ** 6
   json_t = timeit.Timer("json.dumps(json_data, default=encode_datetime)", setup=setup).timeit(number=number)
   msgpack_t = timeit.Timer("msgpack.packb(msg_data, default=encode_datetime)", setup=setup).timeit(number=number)

   s = """
   json: %s\n
   msgpack: %s\n
   """ % (
      json_t,
      msgpack_t,
      )

   print s

# 测试时间 + 基本数据类型反序列化
if 1:
   number = 10 ** 6
   json_t = timeit.Timer("json.loads(json_data_dt, object_hook=decode_datetime)", setup=setup).timeit(number=number)
   msgpack_t = timeit.Timer("msgpack.unpackb(msg_data_dt, object_hook=decode_datetime)", setup=setup).timeit(number=number)

   s = """
   json: %s\n
   msgpack: %s\n
   """ % (
      json_t,
      msgpack_t,
      )

   print s

