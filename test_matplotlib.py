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
x = [1,2,3]
y = [1,2,3]
plt.pie(x, labels=y)
plt.show()
if __name__ == '__main__':
    #main()
    
    pass
