#coding:utf8

#当for循环执行完成后执行else 被break时不执行
for i in range(10):
    #if i > 6:
    if i > 11:
        break
else:
    print 1

#print i


#当while循环执行完成后执行else 被break时不执行
i = 0
while i < 10:
    i += 1
    if i > 11:
    #if i > 5:
        break
else:
    print i
