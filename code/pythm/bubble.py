# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '05/07/2018 18:11'
__description__ = '''
冒泡排序
a = [12, 4, 3, 5, 13, 1, 17, 19, 15]

1. 比较 a[i], a[i+1]
- if a[i] > a[i+1]: a[i], a[i+1] = a[i+1], a[i]
2. 直到每一组相邻元素都完成, 至此得到最大的数
3. 重复1和2, 这时2的最后一个元素, 由于已确定最后一个数为最大, 故每次比较的结束为该数的前一个数
4. 重复直到无

'''

import os
import sys
# import random
import copy

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from izen import dec
from logzero import logger as log
from pygorithm.sorting import bubble_sort

import pythm
from pythm import trace, chaos_list

ar1 = copy.copy(chaos_list)
ar2 = copy.copy(chaos_list)


# print(ar1, ar2)


def pyg():
    ar = [12, 4, 3, 5, 12, 14, 14, 13, 1, 17, 19, 15]
    print(bubble_sort.sort(ar))
    # print(bubble_sort.time_complexities())
    print(bubble_sort.get_code())


@trace(1, 0)
def pgbub():
    ar = [12, 4, 3, 5, 13, 1, 17, 19, 15]
    ar.extend([x * 2 for x in ar])
    for i in range(len(ar)):
        for j in range(len(ar) - 1, i, -1):
            if ar[j] < ar[j - 1]:
                ar[j], ar[j - 1] = ar[j - 1], ar[j]
    print(ar)


@dec.prt(1)
# @trace(1, 0)
def bub_and_quit(ar):
    """冒泡, 如果不再有变化, 则直接退出

    经测试: len=72 -> 0.001030 sec
    """
    print(len(ar))
    end = len(ar) - 1
    for j in range(end):
        c = False
        for i in range(end - j):
            if ar[i] > ar[i + 1]:
                ar[i], ar[i + 1] = ar[i + 1], ar[i]
                c = True
        if not c:
            break
    print(ar)


# @dec.prt(1)
# @trace(1, 0)
def bub(ar):
    """完整运行, 不检测
    经测试: len=72 -> 0.001218 sec
    """
    print(len(ar))
    end = len(ar)
    for i in range(end):
        for j in range(end - 1 - i):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
    print(ar)


def bub_it(ar):
    """
    ar = [12, 4, 3, 5, 12, 14, 14, 13, 1, 17, 19, 15]
    :param ar:
    :type ar:
    :return:
    :rtype:
    """
    for i in range(len(ar) - 1, 0, -1):
        done = True
        for j in range(i):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
                done = False
        if done:
            break
    return ar


if __name__ == '__main__':
    pass
    # pgbub()
    # bub_and_quit(ar1)
    # bub(ar2)
    # ar_l = [12, 4, 3, 5, 12, 14, 14, 13, 1, 17, 19, 15]
    a = pythm.set_chaos_len(16)
    print(a)
    a = bub_it(a)
    print(a)
