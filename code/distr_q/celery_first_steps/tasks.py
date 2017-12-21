# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '19/12/2017 5:41 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys
import time

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-3])
sys.path.append(app_root)

from celery import Celery

# app = Celery('tasks',
#              backend='redis://:123456@localhost:6380/0',
#              broker='amqp://admin:admin@localhost:5672/cc')

app = Celery('tasks',
             backend='rpc://admin:admin@localhost/cc',
             broker='amqp://admin:admin@localhost:5672/cc')


@app.task
def add(x, y):
    return x + y


@app.task
def d0(x, y):
    time.sleep(10)
    return x / y


if __name__ == '__main__':
    for i in range(5):
        res = d0.delay(16, i + 1)
        print(res.ready())
        # print(res.get(timeout=1, propagate=False))
        # print(res.traceback)
