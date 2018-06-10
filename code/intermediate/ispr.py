# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/4/9 4:55 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import collections
import os
import sys
from pprint import pprint

from logzero import logger as log  # pylint: disable=import-error

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)


class LoggingDict(dict):
    """
    这个类拥有其父类`dict`的所有功能特性,
    但是它扩展了`dict`的`__setitem__`实现当有 key 更新时触发记录log功能
    在实现了日志记录后, 方法使用了super()来委托实现使用`key/value pair` 更新字典的工作
    在super()引入之前, 我们不得不在程序中硬编码来调用`dict.__setitem__`方法.
    而且, 由于super()是通过计算的非直接引用, 所以是一个更好的实现方式.
    使用间接引用的一个好处在于不需要我们直接使用名字来指定委托类. 
    如果你编辑了源代码来切换到另外基类的映射, super()委托会自动更新. 实际来说你只需要一个简单的源码:
    除了隔离改变之外, 另一个主要收益在于间接计算`动态计算`, 如果是从静态编程语言转换而来, 可能对此不大熟悉. 
    鉴于中间层是在运行时计算, 我们可以自由的影响计算来动态指向其他类.
    动态计算依赖于类的`super`在哪里调用和祖先的实例树. 
    组成第一部分的类的`super`调用由类的程序代码决定.
    在我们例子中,super()被`LoggingDict.__setitem__`方法调用. 这块功能是固定的. 
    第二个但更有意思的部分组成是可变量(我们可以使用一个丰富的祖先树来创建一个子类).
    让我们利用此而不需要修改已有类来构建一个记录有序字典的类.
    """

    def __setitem__(self, key, value):
        log.debug('Setting {} to {}'.format(key, value))
        super().__setitem__(key, value)


'''
class SomeOtherMapping(object):
    pass
class LoggingDict(SomeOtherMapping):    # new base class
    def __setitem__(self, key, value):
        print('Setting %r to %r' % (key, value))
        super().__setitem__(key, value) # no change needed
'''


class LoggingOD(LoggingDict, collections.OrderedDict):
    pass


class Root(object):
    def draw(self):
        assert not hasattr(super(), 'draw')


class Shape(Root):
    def __init__(self, shape_name, **kwargs):
        self.shape_name = shape_name
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing shape... ', self.shape_name)
        super().draw()


class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('Drawing @({}, {})'.format(self.x, self.y))


class MoveableAdapter(Root):
    def __init__(self, x, y, **kwargs):
        self.moveable = Moveable(x, y)
        super().__init__(**kwargs)

    def draw(self):
        self.moveable.draw()
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing color... ', self.color)
        super().draw()


class MoveableColoredShape(ColoredShape, MoveableAdapter):
    pass


def tld():
    fruit = LoggingDict()
    fruit['apple'] = 3
    log.debug(fruit)
    mc = MoveableColoredShape(
        color='red', shape_name='triangle', x=10, y=20
    ).draw()


if __name__ == '__main__':
    pprint(LoggingOD.__mro__)
    # tld()
    # cs = ColoredShape(color='black', shape_name='circle')
    # print(cs.color, cs.shape_name)
    # cs.draw()
    # pprint(ColoredShape.__mro__)
