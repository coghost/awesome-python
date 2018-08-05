# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/11 10:05 AM'
__description__ = '''
快速排序
1. 选基准常用第1个元素, 大于基准向右, 小于向左
2. 以此往复, 直到完成
3. 重复1,2 直到左右, 均OK
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import pythm
from pygorithm.sorting import quick_sort

def qsort(arr):
    if len(arr) < 2:
        return arr
    return qsort([x for x in arr[1:] if x < arr[0]]) + arr[0:1] + \
           qsort([x for x in arr[1:] if x >= arr[0]])


def run():
    arr = pythm.get_list(10, 20)
    print(arr)
    arr = qsort(arr)
    print(arr)


if __name__ == '__main__':
    run()
    d = quick_sort.get_code()
    print(d)

