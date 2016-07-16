#coding:utf8
'''
定义一些小函数
'''

# ip转换为数字
def ip_to_number(ip_address):
    '''
    a.b.c.d
    (2^24)*a + (2^16)*b + (2^8)*c + (2^0)*d
    
    11111111 00000000 00000000 00000000
    (2^24)*a
             11111111 00000000 00000000
             (2^16)*b
                      11111111 00000000
                      (2^8)*c
                               11111111
                               (2^0)*d
    1.1.1.1
    2^24 + 2^16 + 2^8 + 2^0
    00000001 00000001 00000001 00000001

    2.2.2.2
    2^25 + 2^17 + 2^9 + 2^1
    00000010 00000010 00000010 00000010
    
    
    '''
    number = 0
    for v in ip_address.split('.'):
        number = number * 256 + int(v, 10)
    return number


def get_random_ip():
    import random
    ip_list = []
    for i in range(4):
        ip_list.append(str(random.sample(range(1, 253), 1)[0]))
    return ".".join(ip_list)


def string_to_number(string, ignore_case=False):
    '''
    redis实战 P165
    只转换前6位
    '''
    if ignore_case:
        string = string.lower()
    pieces = map(ord, string[:6])
    while len(pieces) < 6:
        pieces.append(-1)
    score = 0
    for piece in pieces:
        score = score * 257 + piece + 1
    return score * 2 + (len(string) > 6)
        
    


if __name__ == "__main__":
    print get_random_ip()
    
