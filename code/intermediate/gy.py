# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/7/1 11:06 AM'
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

from izen import helper


def c_gen():
    alist = range(3)
    for i in alist:
        yield i * i


def get_child_candidates(distance, min_dist, max_dist):
    pass


def run():
    g = c_gen()
    print(g)
    for i in g:
        print(i)


def rbig(fpth):
    cnt = ''
    with open(fpth) as fp:
        cnt = fp.read()
    #     for l in fp:
    #         print(l)
    cnt = helper.read_file(fpth)
    print(cnt)


if __name__ == '__main__':
    rbig('gy.py')
