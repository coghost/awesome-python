# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '05/21/2018 14:39'
__description__ = '''
From: https://github.com/faif/python-patterns/blob/master/creational/abstract_factory.py
## Abstract Factory

the Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.

抽象工厂方法用来提供一个接口来创建 `相关/相依赖` 的对象, 而不需要指定具体类
主要用于对于具有相同主题的工厂进行的封装

例如: 生成一台PC机

使用工厂方法模式:
- cpu工厂
- 内存工厂
- 显卡工厂
...

使用抽象工厂模式, 只需要一个PC工厂
只是PC工厂包含了:
- cpu工厂
- 内存工厂
- 显卡工厂
...

另外:
'''

import os
import sys
import random

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

from logzero import logger as log  # pylint: disable=import-error
from pypat import iabs_editor


def create_editor(n):
    if n == 'Vim':
        editor = iabs_editor.VimEditor()
    elif n == 'Emacs':
        editor = iabs_editor.EmacsEditor()
    else:
        raise iabs_editor.EditorNotFound

    ka = editor.create_key('a', 'append')
    code = editor.create_code()
    print(ka.name(), ka.effect())
    print(code.rate())


def test_editor():
    n = 'Emacs'
    if random.randint(1, 10) % 2:
        n = 'Vim'
    try:
        create_editor(n)
    except iabs_editor.EditorNotFound as e:
        print('Not Supported Editor name!')


if __name__ == '__main__':
    test_editor()
