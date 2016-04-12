#coding:utf8
'''
Levenshtein算法
字符串相似度检测
'''

import Levenshtein


# #计算汉明距离，要求str1和str2必须长度一致，是描述两个等长字符串
# #之间对应未知上不同字符个数
# str1 = 'fasdfa'
# str2 = '123454'

# print Levenshtein.hamming(str1, str2)

#计算编辑距离（也称为Levenshtein距离）是描述有一个字符串转化为另
#一个字符串最少的操作次数，其中操作包括插入、删除、替换

str1 = 'fasdfa'
str2 = '123454'

print Levenshtein.distance(str1, str2)