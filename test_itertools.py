#coding:utf8
import itertools
print dir(itertools)
l = [1,2,3]

#combinations
#print u"组合"
#print list(itertools.combinations(l, 2))

#combinations_with_replacement
#print u"组合中元素可重复"
#print list(itertools.combinations_with_replacement(l, 2))

#permutations
#print u"排列"
#print list(itertools.permutations(l, 2))

#太恐怖了
#计数器，无限循环,使用list()会把电脑卡死的
#count(start=0, step=1)
#print itertools.count(5,2)

#不断重复给定序列中的元素
#itertools.cycle("abc")

#不断重复给定元素,可指定次数
#repeat(object [,times]) 
#print list(itertools.repeat("abc", 2))

#groupby
#根据所传入key函数进行分组，groupby(iterable[, keyfunc]),若无key则key = lambda x: x
'''
def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"
friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
#friends = sorted(friends, key=height_class)
#m 分组名  n 此分组下所有元素的迭代器
for m, n in itertools.groupby(friends, key=height_class):
    print(m)
    print(list(n))
    #
    #print n
'''

#compress
#根据[1, 1, 1, 0]的真假值情况，选择第一个参数'ABCD'中的元素。A, B, C
#print list(itertools.compress("abcd",[0,1,0,1]))

#islice
#切片迭代器  islice(iterable, [start,] stop [, step])
#print list(itertools.islice(range(10), 2,5,2))

#izip
#将多个迭代器合并为一个，长度按照最小长度
#print list(itertools.izip(range(5), range(10,14), range(20,23)))

#izip_longest(iter1 [,iter2 [...]], [fillvalue=None])
#将多个迭代器合并为一个，长度按照最大长度，默认填充None
#print list(itertools.izip_longest(range(5), range(10,14), range(20,23)))

#chain
#print u"连接迭代器"
#print list(itertools.chain(xrange(5), xrange(2)))

#dropwhile
#从头开始，跳过返回True的元素，一旦返回False，则以后不再判断
#print list(itertools.dropwhile(lambda x:x>5, [7,6,7,1]))
#print list(itertools.dropwhile(lambda x:x>5, [7,1,7,1]))
#print list(itertools.dropwhile(lambda x:x>5, [2,1,7,1]))
#print list(itertools.dropwhile(lambda x:x<5, [2,1,7,1]))

#takewhile
#返回False则停止
#print list(itertools.takewhile(lambda x:x>5, [7,3,4,6,7,1]))
#print list(itertools.takewhile(lambda x:x>5, [1,3,4,6,7,1]))
#print list(itertools.takewhile(lambda x:x<5, [1,3,4,6,7,1]))

#ifilter
#类似filter只不过返回的是一个迭代器
#print type(filter(lambda x:x>5, range(10)))
#print type(itertools.ifilter(lambda x:x>5, range(10)))

#ifilterfalse
#返回False的元素

#imap
#
#result = itertools.imap(pow, [1,2,3], [1,2,3])
#print type(result)
#print list(result)

#starmap
#result = itertools.starmap(pow, [(1,2), (2,3)])
#print type(result)
#print list(result)


#product(*iterables)
#print list(itertools.product([1,2], [2,3]))
#print list(itertools.product([1,2], repeat=4))

#tee(iterable, n=2)
#print itertools.tee(range(2), 3)
#print list(itertools.tee(range(2), 3)[0])


