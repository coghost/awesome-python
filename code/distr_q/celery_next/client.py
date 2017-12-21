# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '20/12/2017 1:58 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-3])
sys.path.append(app_root)

from distr_q.celery_next import tasks

if __name__ == '__main__':
    for i in range(10):
        tasks.add.apply_async((2, i), queue='simple_usage', countdown=10)
