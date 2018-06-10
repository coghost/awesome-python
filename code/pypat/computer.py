# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '05/23/2018 18:24'
__description__ = '''
computer => cpu/mem/monitor
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from logzero import logger as log  # pylint: disable=import-error


if __name__ == '__main__':
    pass
