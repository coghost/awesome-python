# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/5/25 7:17 PM'
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


def turn_list_each_two_elements_to_tuple(orig=None):
    if not orig:
        orig = [x for x in range(20)]
    ttt = iter(orig)
    ttt = list(zip(ttt, ttt))
    return ttt


def test_zip():
    a = [x for x in range(20)]
    print(a)
    a = iter(a)
    a = list(zip(a, a))
    print(a)


if __name__ == '__main__':
    t = turn_list_each_two_elements_to_tuple()
    print(t)
