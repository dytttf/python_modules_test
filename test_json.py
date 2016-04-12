#coding:utf8
'''
测试json模块自定义序列化规则
'''
import sys
try:
    import simplejson as json
except ImportError as e:
    sys.stdout.write(str(e)+'\n')
    import json
import datetime



#dumps
class DateTimeEncoder(json.JSONEncoder): #对JSONEncoder进行扩展
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return obj,strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, obj)

d = datetime.datetime.now()
#print json.dumps(d)
print json.dumps(d, cls=DateTimeEncoder)

#sort_keys
print json.dumps({"c":0, "a":0, "b":0}, sort_keys=True)
#skipkeys
#print json.dumps({"c":0, "a":0, "b":0, d:1}, skipkeys=False)
print json.dumps({"c":0, "a":0, "b":0, d:1}, skipkeys=True)
#ensure_ascii  ?
print type(json.dumps({"我":0, "a":0, "b":0,}, ensure_ascii=False))

#default
def encode_complex(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError(repr(obj) + " is not JSON serializable")
print "encode_complex----", json.dumps(1+2j, default=encode_complex)
#print "encode_complex----", json.dumps(d, default=encode_complex)


#loads
def as_complex(dct):
    print 1
    if "__complex__" in dct:
        return complex(dct['real'], dct['imag'])
    return dct
print "as_complex-----",json.loads('{"__complex__": true, "real": 1, "imag": 2}',
                 object_hook=as_complex)


from decimal import Decimal
print repr(json.loads('1.1', parse_float=Decimal))


