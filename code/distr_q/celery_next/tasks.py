# -*- coding: utf-8 -*-

__author__ = 'lihe <imanux@sina.com>'
__date__ = '20/12/2017 12:14 PM'
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

from distr_q.celery_next.app import app


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
