# coding:utf-8
'''
python对象引用关系图
'''
import objgraph
x = ['a', 1, [2, 3]]
objgraph.show_refs([x], filename='test.png')
objgraph.show_most_common_types(limit=3)
