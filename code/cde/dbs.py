# -*- coding: utf-8 -*-

__author__ = 'lihe <imanux@sina.com>'
__date__ = '14/12/2017 10:40 AM'
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

from cde import cfg

# mongodb 两种连接参数形式
MG_CFG_DICT = {
    'host': cfg.get('mg.host', 'localhost'),
    'port': cfg.get('mg.port', 27027),
    'db': cfg.get('mg.db', 'luoo'),
    'alias': cfg.get('mg.alias', 'luoo_rw'),
    'username': cfg.get('mg.username', ''),
    'password': cfg.get('mg.password', ''),
}

MG_CFG_STR = 'mongodb://{}:{}/{}'.format(
    cfg.get('mg.host', 'localhost'),
    cfg.get('mg.port', 27027),
    cfg.get('mg.db', 'luoo'),
)

# redis 配置参数
REDIS_CONF = {
    'host': cfg.get('rds.host', 'localhost'),
    'port': cfg.get('rds.port', 6379),
    'password': cfg.get('rds.password', '123456'),
    'socket_timeout': cfg.get('rds.socket_timeout'),
    'socket_connect_timeout': cfg.get('rds.socket_connect_timeout'),
    'db': cfg.get('rds.db'),
}
