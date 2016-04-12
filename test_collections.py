#coding:utf8
import collections
'''
dir()
['Callable', 'Container', 'Counter', 'Hashable', 'ItemsView', 'Iterable',
'Iterator', 'KeysView', 'Mapping', 'MappingView', 'MutableMapping',
'MutableSequence', 'MutableSet', 'OrderedDict', 'Sequence', 'Set',
'Sized', 'ValuesView', '__all__', '__builtins__', '__doc__',
'__file__', '__name__', '__package__', '_abcoll', '_chain',
'_class_template', '_eq', '_field_template', '_get_ident',
'_heapq', '_imap', '_iskeyword', '_itemgetter', '_repeat',
'_repr_template', '_starmap', '_sys', 'defaultdict', 'deque', 'namedtuple']
'''


# #Counter
# #计数器,支持迭代,字典方法
# #Example
# l = [1,2,3,4,5,2,4,1,6,8,3,6]
# counter = collections.Counter(l)

# print dir(counter)
# #出现次数最多的n个元素
# print counter.most_common(2)
# #减法
# counter.subtract([1])
# counter.subtract(collections.Counter([1]))
# counter.subtract({1:2})
l_1 = [1,2,3,4,5,2,4,1,6,8,3,6]
counter_1 = collections.Counter(l_1)
l_2 = [1,2,3,4,5,2,4,1,6,8,3,6,6]
counter_2 = collections.Counter(l_2)
print counter_1 - counter_2
print bool(counter_1 - counter_2)

print counter_2 - counter_1






# #defaultdict
# #用法和dict几乎一样，唯一不同之处在于初始化字典时可以自定义默认值
# #下面两种方式效果一样，不过defaultdict比较快
# dic = collections.defaultdict(list)
# for i in range(5):
#     dic[i].append(i)
# print dic
# dic = dict()
# for i in range(5):
#     dic.setdefault(i, []).append(i)
# print dic


# #namedtuple(typename, field_names, verbose=False, rename=False)
# my_tuple = collections.namedtuple('my',['name','age','sex'])#
# mt = my_tuple('duanyifei', 23, 'm')
# print mt.index('duanyifei')
# print mt.count(23)
# print mt.name
# #转化为OrderDict
# md = mt._asdict()


