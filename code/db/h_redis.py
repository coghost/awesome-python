# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = 'lihe <imanux@sina.com>'
__date__ = '13/12/2017 12:07 PM'
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

import click
import hot_redis
import redis

from cde import REDIS_CONF

rdb_out = hot_redis.HotClient(**REDIS_CONF)
rd = redis.StrictRedis(**REDIS_CONF)


def hot_redis_test(clear=False):
    """
        测试 hot redis 常用功能

    :return:
    """
    # clear = True
    dat = {
        'base': 10,
        'crx': 2,
        'jobbole': 1,
    }

    # 初始化一个字典
    _dict = hot_redis.Dict(client=rdb_out, key='ig.dict')
    # 更新, 自动写入 redis
    _dict['fns'] = dat

    # 删除字典
    if clear:
        _dict.clear()

    # 测试 list
    _list = hot_redis.List(client=rdb_out, key='ig.list')
    _list += list(dat.keys())

    # pop list
    if clear:
        for i in range(len(_list)):
            _list.pop()

    # 字符串
    _string = hot_redis.String(client=rdb_out,
                               key='ig.string',
                               initial=','.join([str(_) for _ in dat.keys()])
                               )
    # 没有找到 hot_redis 如何删除, 只好使用 redis 默认的
    if clear:
        rd.delete('ig.string')


@click.command()
@click.option('--clear', '-c',
              is_flag=True,
              help='clear redis temp keys\nUSAGE: <cmd> -c')
def run(clear):
    hot_redis_test(clear)


if __name__ == '__main__':
    run()
