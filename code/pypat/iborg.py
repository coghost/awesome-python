# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '05/23/2018 11:09'
__description__ = '''
http://code.activestate.com/recipes/66531/
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from logzero import logger as log  # pylint: disable=import-error


class Borg(object):
    """全共享状态, 所有状态均共享, 但可以有多个实例
    """

    __shared_state = {}

    def __init__(self, name="borg", state="run"):
        self.__dict__ = self.__shared_state
        self.name = name
        self.state = state

    def sayhi(self, val=""):
        print("hi", self.name, self.state)


class SemiBorg(object):
    pass


def test_it(the_cls='Borg'):
    """测试
    """
    bcs = globals().get(the_cls)
    cf = bcs()
    cf.sayhi()
    cf2 = bcs("jim", "stop")
    cf.sayhi()
    cf2.sayhi()


if __name__ == '__main__':
    test_it()
