# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/27 6:27 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)


def rb_search(val, arr):
    if len(arr) == 1:
        if val == arr[0]:
            return 0

    l = (len(arr) - 1) // 2
    print(val, l, arr, arr[l], val == arr[l])
    if val == arr[l]:
        return l
    if val < arr[l]:
        arr = arr[:l]
        rb_search(val, arr)
    if val > arr[l]:
        arr = arr[l:]
        rb_search(val, arr)


def rbsch(val, arr):
    l = (len(arr) - 1) // 2
    print(l, val, arr)
    if len(arr) <= 1:
        return False

    if val < arr[l]:
        arr = arr[:l]
        return rbsch(val, arr)
    elif val > arr[l]:
        arr = arr[l:]
        return rbsch(val, arr)
    elif val == arr[l]:
        return True
    else:
        return False


def b_search(val, arr):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        print(l, h, m)
        if val == arr[m]:
            return m
        elif val < arr[m]:
            h = m - 1
        elif val > arr[m]:
            l = m + 1


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def bse(arr, low, high, key):
    if low <= high:
        m = (low + high) // 2
        if key == arr[m]:
            return m
        elif key < arr[m]:
            return bse(arr, low, m - 1, key)
        elif key > arr[m]:
            return bse(arr, m + 1, high, key)
    else:
        return -1


if __name__ == '__main__':
    pass
    arr = [x for x in range(100) if x % 2]
    print(arr)
    # a = rb_search(7, arr)
    # a = b_search(1, arr)
    # a = rbsch(8, arr)
    a = bse(arr, 0, len(arr) - 1, 11)
    # print(a)
    print(a)
