# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/6 12:34 PM'
__description__ = '''
参考:
- https://www.cnblogs.com/chengxiao/p/6129630.html
- https://baike.baidu.com/item/堆排序/2840151?fr=aladdin
- https://www.cnblogs.com/idorax/p/6441043.html

堆: 分为大顶堆/小顶堆,是完全二叉树 

大顶堆: 每个结点的值都大于或者等于其左右孩子结点的值
小顶堆: 每个结点的值都小于或者等于其左右孩子结点的值

i.e. 
max_heap:
ar[i] > ar[2*i + 1] and ar[i] > ar[2*i + 2]
min_heap:
ar[i] < ar[2*i + 1] and ar[i] < ar[2*i + 2]

堆排序
1. 将待排序序列构造成一个 max_heap, 此时, 整个序列的最大值就是堆顶的根节点. 
将其与末尾元素进行交换,此时末尾就是最大值. 
然后将剩余的 n-1 个元素重新构造成一个堆, 此时堆顶为剩余元素最大, 以此重复就能获取一个有序序列了


'''

import os
import sys
import heapq

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)
import pythm


def py_heap():
    arr = pythm.get_list(10, 20)
    print(arr)
    hp = list(arr)
    heapq.heapify(hp)
    print(hp)
    d = []
    for i in range(len(arr)):
        d[i] = heapq.heappop(hp)

    print(d)


def heap_sort(lst):
    for start in range((len(lst) - 2) / 2, -1, -1):
        sift_down(lst, start, len(lst) - 1)

    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(lst, 0, end - 1)
    return lst


def _sift_down(lst, start, end):
    root = start

    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


def sift_down(arr, node_index, end):
    """
    初始化堆时, 自下而上, 自右而左
    交换堆顶与堆尾, 自上而下

    :param arr: 待排序数组
    :type arr: list
    :param node_index: 结点索引
    :type node_index: int
    :param end: 比较的结束索引, 最后一个可用元素
    :type end: int
    :return:
    :rtype:
    """
    while True:
        # 左, 右, 结点
        left_child = 2 * node_index + 1
        right_child = left_child + 1

        # 如果左节点越界, 结束
        if left_child > end:
            break
        # 如果右节点存在, 且大于左节点, 移动索引
        if right_child <= end and arr[left_child] < arr[right_child]:
            left_child += 1
        if arr[node_index] < arr[left_child]:
            # 交换值
            arr[node_index], arr[left_child] = arr[left_child], arr[node_index]
            # 更新索引
            node_index = left_child
        else:
            break


def bsort(arr):
    # 1. 自下而上, 自右而左, 生成大顶堆
    # 2. 交换首尾元素, 重复 <1.> 生成新的移除最后一个排序元素的大顶堆
    # 如果是奇数
    leaf_last = len(arr) - 1
    none_leaf_node = leaf_last // 2

    print(none_leaf_node, leaf_last)

    for i in range(none_leaf_node, -1, -1):
        sift_down(arr, i, leaf_last)

    leaf_last = len(arr) - 1
    for i in range(leaf_last, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i - 1)


def prt_tree(arr):
    """
    line 1: 2^0
    line 2: 2^1
    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    j = 0
    t = 0
    for i, v in enumerate(arr):
        print(v, end=' ' * j)
        if t % 2 ** j == 0:
            print('')
            j += 1
            t = 0
        t += 1


def run():
    arr = pythm.get_list(11, 20)
    # arr = [18, 15, 4, 2, 9, 7, 16, 6, 11, 31]
    print(arr)
    bsort(arr)
    print(arr)
    # prt_tree(arr)


if __name__ == '__main__':
    # py_heap()
    run()
