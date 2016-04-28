#coding:utf8
import heapq

l = range(10)
l.reverse()
print l
#将一个列表转换为 堆 
heapq.heapify(l)

print l
#取最大的n个值
print heapq.nlargest(3, l, key=None)

#依次弹出最小的元素
while l:
    print heapq.heappop(l)
    




