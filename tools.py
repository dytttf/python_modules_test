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
        

def shard_key(base, key, total_elements, shard_size):
    '''计算redis分片用key
    redis实战 P216
    '''
    import binascii
    if isinstance(key, (int, long)) or key.isdigit():
        shard_id = int(str(key), 10) // shard_size
    else:
        shards = 2 * total_elements // shard_size
        shard_id = binascii.crc32(key) % shards
    return "%s:%s"%(base, shard_id)

def everySystem(number, system):
    '''
    实现数字向任意进制的转换
    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '''
    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = base[:system]
    chars = []
    while 1:
        number, mod = divmod(number, system)
        if number < system:
            chars.append(base[mod])
            chars.append(base[number])
            break
        else:
            chars.append(base[mod])
    chars.reverse()
    chars = [str(x) for x in chars]
    return "".join(chars)

def unicode_to_html(char_list):
    '''
    unicode 字符转换为 html 实体字符
    '''
    html_char_list = []
    for char in char_list:
        code = re.search(r"\\u([^\\\'\"]+)", repr(char))
        if not code:
            html_char_list.append(char)
        else:
            html_char_list.append("&#%s;"%int(code.group(1), 16))
    return "".join(html_char_list)


def keepalive(handle_func=None, interval=1):
   '''装饰器
   功能：
      捕获被装饰函数的异常并重新调用函数
      函数正常结束则结束
   装饰器参数：
      @handle_func:function
         异常处理函数 默认接收参数 e
      @interval:number
         函数重启间隔
   '''
   def wrapper(func):
      @functools.wraps(func)
      def keep(*args, **kwargs):
         while 1:
            try:
               result = func(*args, **kwargs)
            except Exception as e:
               if handle_func:
                  handle_func(e)
               time.sleep(interval)
               continue
            break
         return result
      return keep
   return wrapper


def RPN_value(expression):
    """后缀表达式求值"""
    if not isinstance(expression, list):
        expression = expression.split(",")
    expression = [int(x) if x.isdigit() else x for x in expression]
    expression.reverse()
    temp_list = []
    while expression:
        top = expression.pop()
        # 遇到符号则开始求值
        if not isinstance(top, int):
            num1 = temp_list.pop()
            num2 = temp_list.pop()
            top = eval("%s%s%s" % (num2, top, num1))
        # 入栈
        temp_list.append(top)
    return temp_list[0]


def recursive_encode_utf8(data):
    """对json格式数据进行操作  将其中任何层级的字符串转为utf8编码"""
    if isinstance(data, basestring):
        if isinstance(data, unicode):
            data = data.encode("utf8")
        else:
            try:
                data = data.decode("gbk")
                data = data.encode("utf8")
            except:
                pass
    elif isinstance(data, (list, tuple)):
        data = [recursive_encode_utf8(x) for x in data]
    elif isinstance(data,  (int, float, long)):
        pass
    elif isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            key = recursive_encode_utf8(key)
            value = recursive_encode_utf8(value)
            new_data.update({key: value})
        data = new_data
    return data
        

if __name__ == "__main__":
    #print get_random_ip()
    #print everySystem(1000, 36)
    #print RPN_value("1,2,3,+,4,*,+,5,-")
    data = [u"你好", 1, 2]
    print(recursive_encode_utf8(data))
