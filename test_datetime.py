#coding:utf8
import datetime

#时间<-->字符转换

now = datetime.datetime.now()

now_str = now.strftime("%Y-%m-%d %H:%M:%S")

now = datetime.datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")


today = datetime.date.today()

today_str = today.strftime("%Y-%m-%d %H:%M:%S")

# 不存在
#today = datetime.date.strptime(now_str, "%Y-%m-%d %H:%M:%S")


#时间差

t = datetime.timedelta(days=1)





if __name__ == "__main__":
    pass
