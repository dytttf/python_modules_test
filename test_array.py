# coding:utf-8
'''
'''
import sys
import array


a = array.array('c', 'string')
print a[0]
a[0] = 'c'
print a

print sys.getsizeof(a)
print sys.getsizeof(list('string'))

