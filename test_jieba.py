#coding:utf8
'''
jieba分词测试

精确模式，试图将句子最精确地切开，适合文本分析；
全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。 
'''

import jieba
import jieba.analyse

# #手动初始化,否则会在第一次分词时初始化,从0.28版本开始
# jieba.initialize()
# #改变主字典路径
# jieba.set_dictionary('data/dict.txt.big')

# #全模式
# seg_list = jieba.cut("我来到清华大学", cut_all=True)
# print 'Full Mode:', '/'.join(seg_list)

# #精确模式
# seg_list = jieba.cut("我来到清华大学", cut_all=False)
# print 'Default Mode:', '/'.join(seg_list)

# #默认是精确模式
# seg_list = jieba.cut("他来到网易杭研大厦")
# print '/'.join(seg_list)

# #搜索引擎模式
# seg_list = jieba.cut_for_search('小明硕士毕业于中国科学院计算所,后在日本京都大学深造')
# print ",".join(seg_list)

#添加自定义词典
#jieba.load_userdict(file_name)


# #关键词提取
# text = '''精确模式，试图将句子最精确地切开，适合文本分析；
# 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
# 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。 
# '''
# tags = jieba.analyse.extract_tags(text, topK=1)
# print '/'.join(tags)

# #词性标注
# import jieba.posseg as pseg
# words = pseg.cut("我爱北京天安门")
# for w in words:
#   print w.word, w.flag

#并行分词,暂不支持windows
#jieba.enable_parallel(4) #开启并行分词模式，参数为并行进程数
#jieba.disable_parallel() #关闭并行分词模式


# #tokenize 返回词语在原文中的起始位置 must be unicode
# #默认模式
# result = jieba.tokenize(u'永和服装饰品有限公司')
# for tk in result:
#   print "word %s\t\tstart: %d \d\d end:%d"%(tk[0], tk[1], tk[2])

# #搜索模式
# result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')
# for tk in result:
#   print "word %s\t\tstart: %d \d\d end:%d"%(tk[0], tk[1], tk[2])

