# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '03/03/2018 11:40 AM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
- 参考: https://github.com/pytransitions/transitions
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from transitions import Machine


class Matter(object):
    def say_hello(self):
        print('Hello, New state!')

    def say_goodbye(self):
        print('goodbye, old state')

    def on_enter_gas(self):
        print("We've just entered state gas")


def gen_tr(dat):
    _d = dat.split(',')
    return {
        'trigger': _d[0],
        'source': _d[1],
        'dest': _d[2],
    }


states = ['solid', 'liquid', 'gas', 'plasma']

trans = [
    'melt,solid,liquid'.split(','),
    'evaporate,liquid,gas'.split(','),
    'sublimate,solid,gas'.split(','),
    'ionize,gas,plasma'.split(','),
]


def run():
    model = Matter()
    mach = Machine(model=model,
                   states=states,
                   transitions=trans,
                   initial='solid')
    print(model.state)
    model.melt()
    print(model.state)
    model.to_gas()
    print(model.state)
    model.trigger('ionize')
    print(model.state)


if __name__ == '__main__':
    run()
