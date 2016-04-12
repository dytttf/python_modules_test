#coding:utf8
'''
python 3 和 python 2 的  `^` 规则不同
'''
import binascii

def dongting_crc32(s):
    '''天天动听CRC32加密'''
    a = [0] * 256
    for t in range(256):
        n = t
        for r in range(8):
            if 1 & n:
                n = n >> 1 & 2147483647 ^ 3988292384
            else:
                n = n >> 1 & 2147483647
        a[t] = n
    n = 4294967295
    for t in range(len(s)):
        n = n >> 8 & 16777215 ^ a[255 & n ^ ord(s[t])]
    print n
    n ^= 4294967295
    print n
    return hex(n >> 3)
    

if __name__ == "__main__":
    #print dongting_crc32('6777360')
    print hex(binascii.crc32('40015915') >> 3)
