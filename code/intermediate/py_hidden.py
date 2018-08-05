# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/7/2 3:17 PM'
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


def draw_point(x, y):
    print('drawing@ x={}, y={}'.format(x, y))


def test_draw_point():
    p_tuple = (3, 4)
    p_dict = {'x': 3, 'y': 5}
    draw_point(*p_tuple)
    draw_point(**p_dict)


def run():
    test_draw_point()


if __name__ == '__main__':
    # run()
    a = 4.9
    b = 6.125
    c = b / a
    print(c)
