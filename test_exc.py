#coding:utf8
'''
异常类测试
'''
import traceback

class myexc(Exception):
    def __init__(self, l, n):
        super(Exception, self).__init__()
        self.l = l
        self.n = n

    def __str__(self):
        return 'my error %s, %s'%(self.l,self.n)

#自定义异常类
try:
    1/2
    raise myexc(1,2)
except myexc as e:
    print e
    print traceback.format_exc()

#异常捕获的一些用法
try:
    #1/0
    int("")
#except (ZeroDivisionError,ValueError) as e:
except Exception as e:
#except ZeroDivisionError as e:
    print e
else:
    print u"no error"
finally:
    print u"finished"


try:
    1/0
    #int('')
except ZeroDivisionError as e:
    print '{0!r}'.format(e)
    int("")
except Exception as e:
    print '{0!r}'.format(e)

def test_keybord():
    while 1:
        time.sleep(1)
    return
try:
    print "Ctrl+c"
    test_keybord()
except KeyboardInterrupt as e:
    print 1
    print e







