# coding:utf8
import codecs

# help(codecs)

def test_BOM():
    with open('bom_txt.txt', 'r') as f:
        s = f.read()
    print s.decode('utf8')
    if s[:3] == codecs.BOM_UTF8:
        print u"没错"
    return


#编码器测试
gbk_lookup = codecs.lookup('gbk')
gbk_str = '我是GBK编码'.decode('utf8').encode('gbk')
unicode_tuple = gbk_lookup.decode(gbk_str)
print unicode_tuple
print gbk_lookup.encode(unicode_tuple[0])
#

#测试简化调用lookup   
gbk_encoder = codecs.getencoder('gbk')
print gbk_encoder(u"我")
#print gbk_encoder("我")
#

#测试register
#注册一个编码查找函数 如果找不到指定编码 则调用此函数
codecs.register(lambda name: codecs.lookup('utf-8'))
unknown_encoder = codecs.getencoder('aaa')
print unknown_encoder
#

utf8_file = codecs.open("utf8_file.txt", mode="w", encoding="utf8")
#utf8_file = open("utf8_file.txt", "w")
utf8_file.write(u"你好")
utf8_file.close()






if __name__ == "__main__":
    #test_BOM()
    pass
