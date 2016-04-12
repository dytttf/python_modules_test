# -*- coding: cp936 -*-
import time
t = time.time()#t为时间戳
t = t-3600
lt = time.localtime(t)  #lt为时间元组
mt = time.mktime(lt)  #mt为时间戳，逆转换
gt1 = time.strftime('%Y-%m-%d',lt)
gt2 = time.strftime('%H:%M:%S',lt)
#print time.strftime("%H:%M:%S")
#print gt2
#输出当前时间
def nowtime(num,j=1,c=10):
    i = 0
    #输出一次时间
    if num==1:
        global gt1,gt2
        print gt1
        print gt2
    #输出多次时间，间隔和次数自定，默认1s，10次
    if num==2:
        print gt1
        while 1:
            i+=1
            t = time.time()
            lt = time.localtime(t)
            gt1 = time.strftime('%Y-%m-%d',lt)
            gt2 = time.strftime('%H:%M:%S',lt)
            print gt2
            if i==c:
                break
            time.sleep(j)
def deftime():
    at = time.asctime(lt)  #时间元组转换为默认时间显示方式 'Sat Jun 28 19:07:56 2014'
    st = time.strptime(at) #逆转换

def test_clock():
    print time.clock()
    time.sleep(1)
    print time.clock()  #从第一次调用到当前的时间差
    time.sleep(2)
    print time.clock()  #从第一次调用到当前的时间差
    time.sleep(3)
    print time.clock()  #从第一次调用到当前的时间差
    return

def call_time(func):
    '''装饰器，计算执行时间'''
    def _deco(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        print '%s() : %s' % (func.__name__, time.clock())
        return result
    return _deco

def get_timestamp():
    s = "2016-04-07 00:00:00"
    t = time.strptime(s, "%Y-%m-%d %H:%M:%S")
    print time.mktime(t)
    return 


if __name__ == "__main__":
    #test_clock()
    get_timestamp()
    pass
    
    
