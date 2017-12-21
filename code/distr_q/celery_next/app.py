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

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-3])
sys.path.append(app_root)

from celery import Celery

# from distr_q.celery_next import ce_cfg
app = Celery(
    'tasks',
    # broker='amqp://admin:admin@localhost/cc',
    # backend='rpc://admin:admin@localhost/cc',
    include=['distr_q.celery_next.tasks']
)
app.config_from_object('distr_q.celery_next.ce_cfg')

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
