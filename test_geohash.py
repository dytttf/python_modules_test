#coding:utf8
import Geohash
#longitude : 经度
#latitude  : 纬度

lng = 116.37439
lat = 39.94758

h = Geohash.encode(lat,lng)
print h
print Geohash.decode(h)
