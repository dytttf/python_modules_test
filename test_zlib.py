#coding:utf8
u'''
测试字符串压缩

'''
import zlib

s = "fionqsofnqigbqerigb;sdacjnreiugsdfjvnqerigubqerg;jrebagsdjklfnaregbsdjkfcnaigvbjqerigvbafhvbalskjdfabnsdjk;fbqogbjrgjkvabrougbqerjgbnskdfnqrigbqeirfgbqrqjhfbjqiwewewewewewewewewewewewewewewewewewewewewewewewewewewewewewerqwefbqwwwwweeeeeeeeeeeeeeaaaaaaaaaaaaaaaa333333dnqofnigb4alfgb3i4ubgfasd.mkfn4iowutfgb4i3gbljkfbqiwerhbfgirfblwefb43igfbaslfbqirfgbva,sgbrielgbqerigbqerfvnalkbfqiugbqler"

print "original size {0}".format(len(s))

compressed_s = zlib.compress(s)
print "compressed size {0}".format(len(compressed_s))

decompressed_s = zlib.decompress(s)
print "decompressed size {0}".format(len(decompressed_s))




