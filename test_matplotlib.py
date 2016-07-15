#encoding=utf-8
import redis
import json
import numpy as np 
import matplotlib.pyplot as plt 

def main():
    conn = redis.StrictRedis.from_url("redis://192.168.123.2/9")
    #zlist = conn.zrange('zset_baidu_poi_lat_lng_all', 0, -1)
    zlist = conn.zrange('zset_dedup_baidu_poi', 0, -1)
    x = []
    y = []
    for item in zlist:
        item = json.loads(item)
        x.append(item.get('lng', 0))
        y.append(item.get('lat', 0))
    #x = np.random.randn(1000)
    #y = np.random.randn(len(x))
    plt.scatter(x, y, color='black', alpha=0.9, edgecolors='green')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.legend()
    plt.savefig('sca_map_1.png', facecolor=(0,0,0))
    plt.show()
    return
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, '')

# 扇形图
# x = [1,2,3]
# y = [1,2,3]
# plt.pie(x, labels=y)
# plt.show()

#设置显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
#折线图
x = [1,2,3]
y = [1,2,3]
x_ticks = ['a', 'b', 'c']
plt.plot(x,y)
#标题
plt.title(u"速率")
#刻度
plt.xticks(x, x_ticks)
#设置x轴对象格式 例如纵向
x_axis = plt.gca().xaxis
for i in x_axis.get_ticklabels():
    i.set_rotation(-90)
plt.show()

def get_figure(index, title, info_list):
    #plt.figure(1)
    #430 4代表总数  3代表每一行并排图数  0代表第一个图的索引（若为1，则从第二个位置开始画）
    #传递一个参数为简便写法，只是用于子图数量少于10的情况
    #一般写法为(4,3,index)
    a = plt.subplot(4,4,index)
    
    plt.sca(a)
    x = []
    y = []
    x_ticks = []
    for index, info in enumerate(info_list):
        num = info['num']
        x.append(index)
        y.append(int(info['speed']))
        x_ticks.append(datetime.datetime.fromtimestamp(info['time']).strftime("%H:%M") + ' %s'%num)
    plt.plot(x,y)
    plt.title(u"%s 数据采集速率"%title)
    plt.xticks(x, x_ticks)
    x_axis = plt.gca().xaxis
    for i in x_axis.get_ticklabels():
        i.set_rotation(-90)
    return







if __name__ == '__main__':
    #main()
    
    pass
