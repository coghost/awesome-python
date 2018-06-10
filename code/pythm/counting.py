# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/6 10:58 AM'
__description__ = '''
计数排序
时间复杂度 O(n+k)
对于给定的输入序列的每个元素 x, 确定小于 x 的个数
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)
import pythm


def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m  # init with zeros
    for a in array:
        count[a] += 1  # count occurences
    i = 0
    for a in range(m):  # emit
        for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array, count)


def bsort(arr):
    """
    arr元素已定,
    :param arr: 数组
    :type arr:
    :param max_el: 最大元素
    :type max_el:
    :return:
    :rtype:
    """
    # 1. 初始化一个 (最大元素 +1) 新0数组
    el_len = max(arr) + 1
    el_arr = [0] * el_len

    # 2. 统计相同元素
    for _ in arr:
        el_arr[_] += 1

    d = []
    # 遍历数组, 在索引位置的相同元素
    for i, a in enumerate(el_arr):
        if not a:
            continue
        d += [i] * a
    return d


def run():
    # arr = [1, 4, 0, 0, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]
    # arr = [1, 4, 7, 3, 2, 1]
    arr = pythm.get_list(10, 30)
    # print(counting_sort(arr, max(arr)))
    print(arr)
    # arr = bsort(arr)
    # print(arr)
    import heapq
    print(arr)
    hp = list(arr)
    heapq.heapify(hp)
    print(hp)


if __name__ == '__main__':
    run()
