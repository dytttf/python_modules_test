# conding:utf-8
import sys


# reload(sys)
# sys.setdefaultencoding("gbk")
# print "放哪送饭呢哦in分".decode("utf8").encode("gbk").decode()

# GIL锁默认切换时间
print sys.getcheckinterval()
# sys.setcheckinterval(100)

a = 1
print sys.getrefcount(a)


# 查看python执行路径
print sys.executable

#sys.exit("test sys exit")

print sys.maxunicode

if __name__=="__main__":
    pass
