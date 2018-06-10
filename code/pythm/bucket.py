# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/5 5:03 PM'
__description__ = '''
桶排序(BucketSort) 小结：
1 桶排序核心思想是：根据数据规模n划分，m个相同大小的区间 （每个区间为一个桶，桶可理解为容器）
2 每个桶存储区间内的元素(区间为半开区间例如[0,10)或者[200,300) )
3 将n个元素按照规定范围分布到各个桶中去
4 对每个桶中的元素进行排序，排序方法可根据需要，选择快速排序，或者归并排序，或者插入排序
5 依次从每个桶中取出元素，按顺序放入到最初的输出序列中(相当于把所有的桶中的元素合并到一起)
6 桶可以通过数据结构链表实现
7 基于一个前提，待排序的n个元素大小介于0~k之间的整数 或者是(0, 1)的浮点数也可（算法导论8.4的例子） 
8 桶排序的时间代价，假设有m个桶，则每个桶的元素为n/m;
当辅助函数为冒泡排序O(n2)时,桶排序为 O(n)+mO((n/m)2);
当辅助函数为快速排序时O(nlgn)时,桶排序为 O(n)+m*O(n/m log(n/m))
9 通常桶越多，执行效率越快，即省时间，但是桶越多，空间消耗就越大，是一种通过空间换时间的方式
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import pythm


def bsort(arr, buckets_num):
    """
        对 arr 分成buckets_num桶进行排序
    :param arr:
    :type arr:
    :param buckets_num:
    :type buckets_num:
    :return:
    :rtype:
    """
    # 初始化 buckets_num 个桶
    buckets = [[] for _ in range(buckets_num)]
    for i in range(buckets_num):
        buckets[i] = 0

    # 将元素放入对应桶
    for _ in range(len(arr)):
        buckets[arr[_]] += 1

    i = 0
    # 遍历所有桶
    for j in range(buckets_num):
        # 遍历桶内元素
        for k in range(buckets[j]):
            # 写入目的数组
            arr[i] = j
            i += 1


def run():
    a = pythm.get_list(16, 20)
    print(a)
    # d = []
    bsort(a, 21)
    print(a)
    print(pythm.chaos_list)
    # print(d)


if __name__ == '__main__':
    run()
