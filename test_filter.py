#coding:utf8
'''
filter(function or None, sequence)
'''

if 1:
    #过滤爬虫id
    filename = 'b_spider.txt'
    with open(filename, "r") as f:
        l = f.readlines()
    l = filter(lambda x:x.startswith("192.168"), l)
    l.sort()
    with open("new_"+filename, 'w') as f:
        for s in l:
            f.write(s)
    

if __name__ == "__main__":
    pass
