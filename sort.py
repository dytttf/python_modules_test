#coding:utf8

wait_list = [1, 4, 5, 7, 9, 2, 9,45, 67, 23, 45, 67, 89, 0, 9, 12, 45]

def sort_quick(lis):
    '''快速排序法
    从序列中选定一个值
        将所有元素与此值比较
        大的放一个队列
        小的放一个队列
        然后对每个队列进行递归调用自身 最后合并
    '''
    if len(lis) == 2:
        if lis[1] < lis[0]:
            return lis[::-1]
        return lis
    if len(lis) < 2:
        return lis
    #
    middle = lis[len(lis) / 2]
    _left_lis = []
    _middle_lis = []
    _right_lis = []
    for i in lis:
        if i < middle:
            _left_lis.append(i)
        elif i == middle:
            # 若无此步骤 可能遇到无限递归 当所有元素刚好都比选中的元素大或者小的时候
            _middle_lis.append(i)
        else:
            _right_lis.append(i)
    return sort_quick(_left_lis) + _middle_lis + sort_quick(_right_lis)


def sort_quick_pretty(lis, start=0, end=-1):
    """不着用额外内存空间的快排实现"""
    if end == -1:
        end = len(lis) - 1
    # 递归基准情形
    if end - start < 10:
        return sort_insert(lis, 0, -1)
    # 三数中值分割
    center = (start + end) / 2
    if lis[center] < lis[start]:
        lis[center], lis[start] = lis[start], lis[center]
    if lis[end] < lis[start]:
        lis[end], lis[start] = lis[start], lis[end]
    if lis[center] < lis[end]:
        lis[center], lis[end] = lis[end], lis[center]
    pivot = lis[center]
    lis[center], lis[end-1] = lis[end-1], lis[center]

    #
    i, j = 1, end-2
    while 1:
        if i > j:
            break
        if lis[i] < pivot:
            i += 1
            continue
        if lis[j] > pivot:
            j -= 1
            continue
        lis[i], lis[j] = lis[j], lis[i]
        i += 1
        j -= 1

    lis[i], lis[end-1] = lis[end-1], lis[i]
    sort_quick_pretty(lis, start, i-1)
    sort_quick_pretty(lis, i+1, end)
    return lis

def sort_insert(lis, start=0, end=-1):
    """插入排序 将新数据添加到已排好的序列中"""
    if end == -1:
        end = len(lis) - 1
    for i in range(start+1, end+1):
        temp = lis[i]
        for j in range(i, -1 + start, -1):
            if lis[j-1] > temp:
                lis[j] = lis[j-1]
            else:
                break
        # 不能放在循环中的else里(当else无法成立的时候即所有元素都大于目标)
        lis[j] = temp
    return lis

#print sort_insert(wait_list)
#print sort_quick_pretty(wait_list)

def sort_bubble(lis):
    '''冒泡排序
    从第一个元素开始遍历，如果大于其后元素，则调换位置，然后继续比较
    记录调换次数 当调换次数为0时 排序结束
    不为0 则递归或者从新开始遍历
    '''
    _exchange_count = 0
    for i in range(len(lis)):
        # 判断是否位最后一位
        if not lis[i+1:]:
            break
        # 交换位置
        if lis[i] > lis[i+1]:
            lis[i], lis[i+1] = lis[i+1], lis[i]
            _exchange_count += 1
    if _exchange_count == 0:
        return lis
    else:
        return sort_bubble(lis)

def merge(left_lis, right_lis):
    l, r = 0, 0
    result = []
    while l < len(left_lis) and r < len(right_lis):
        if left_lis[l] <= right_lis[r]:
            result.append(left_lis[l])
            l += 1
        else:
            result.append(right_lis[r])
            r += 1
    result += left_lis[l:]
    result += right_lis[r:]
    return result


def sort_merge(lis):
    """归并排序 重点在归并"""
    if len(lis) <= 1:
        return lis
    num = int(len(lis) / 2)
    _left_lis = sort_merge(lis[:num])
    _right_lis = sort_merge(lis[num:])
    return merge(_left_lis, _right_lis)


def sort_shell(lis):
    """谢尔排序"""
    le = len(lis)
    increment_sequence = [x for x in xrange(len(lis) / 2) if x % 2 == 1]
    increment_sequence.reverse()
    for incr in increment_sequence:
        while 1:
            _sort_count = 0
            for i in range(le - incr):
                if lis[i] > lis[i + incr]:
                    lis[i], lis[i + incr] = lis[i + incr], lis[i]
                    _sort_count += 1
            if not _sort_count:
                break
    return lis

#print sort_merge(wait_list)
#print sort_shell(wait_list)
