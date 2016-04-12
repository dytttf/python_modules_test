# coding:utf-8
import math
def great_circle():
    lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
    radius = 3956 # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a)*math.cos(b)) + (math.sin(a)*math.sin(b)*math.cos(theta)))
    return radius * c

def great_circle_c():
    lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
    cdef float radius = 3956.0 # miles
    cdef float pi = 3.1415926
    cdef float x = pi / 180.0
    cdef float a,b,theta,c
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a)*math.cos(b)) + (math.sin(a)*math.sin(b)*math.cos(theta)))
    return radius * c

if __name__ == "__main__":
    pass
    
