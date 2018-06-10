# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '04/03/2018 8:50 PM'
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


class Shape(object):
    def __init__(self):
        pass

    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        print('I am a triangle')

    def draw(self):
        print('Drawing triangle')


class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        print('I am a rectangle')

    def draw(self):
        print('Drawing rectangle')


class Trapezoid(Shape):
    def __init__(self):
        Shape.__init__(self)
        print('I am a trapezoid')

    def draw(self):
        print('Drawing trapezoid')


class Diamond(Shape):
    def __init__(self):
        Shape.__init__(self)
        print('I am a diamond')

    def draw(self):
        print('Drawing diamond')


class ShapeFactory(object):
    shapes = {
        'triangle': Triangle,
        'rectangle': Rectangle,
        'trapezoid': Trapezoid,
        'diamond': Diamond,
    }

    def __new__(cls, name):
        print('creating a new shape: {}'.format(name))
        if name in cls.shapes.keys():
            return cls.shapes.get(name)()
        else:
            return Shape()


if __name__ == '__main__':
    ShapeFactory('rectangle').draw()  # pylint: disable=E1101
